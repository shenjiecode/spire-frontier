"""Read JVM field constants and constructor/upgrade instructions, without running game code."""
import hashlib,json,struct,zipfile
from pathlib import Path
from bootstrap_sample import ROOT


def inspect(raw):
    pos=8
    def take(n):
        nonlocal pos
        value=raw[pos:pos+n];pos+=n;return value
    def u2():return int.from_bytes(take(2),'big')
    def u4():return int.from_bytes(take(4),'big')
    cp=[None]*u2();i=1
    while i<len(cp):
        tag=take(1)[0]
        if tag==1:cp[i]=take(u2()).decode('utf-8',errors='replace')
        elif tag==3:cp[i]=int.from_bytes(take(4),'big',signed=True)
        elif tag==4:cp[i]=struct.unpack('>f',take(4))[0]
        elif tag in (5,6):cp[i]=take(8).hex();i+=1
        elif tag in (7,8,16,19,20):cp[i]=(tag,u2())
        elif tag in (9,10,11,12,18,17):cp[i]=(tag,u2(),u2())
        elif tag==15:cp[i]=(tag,take(1)[0],u2())
        else:raise ValueError(tag)
        i+=1
    def resolve(i):
        value=cp[i]
        if isinstance(value,tuple):return ':'.join(str(resolve(x)) for x in value[1:])
        return value
    take(6);take(2*u2())
    fields={}
    for _ in range(u2()):
        access=u2();name=resolve(u2());desc=resolve(u2())
        for _ in range(u2()):
            attr=resolve(u2());size=u4();payload=take(size)
            if attr=='ConstantValue':fields[name]=resolve(int.from_bytes(payload,'big'))
    methods={}
    for _ in range(u2()):
        access=u2();name=resolve(u2());desc=resolve(u2())
        for _ in range(u2()):
            attr=resolve(u2());payload=take(u4())
            if attr!='Code' or name not in ('<init>','upgrade','onRest','getUpdatedDescription'):continue
            code=payload[8:8+int.from_bytes(payload[4:8],'big')];pc=0;instructions=[]
            # Operand sizes for ordinary JVM instructions. Switch/wide are
            # decoded explicitly, so byte values are never treated as opcodes.
            one={0x10,0x12,*range(0x15,0x1a),*range(0x36,0x3b),0xa9,0xbc}
            two={0x11,0x13,0x14,0x84,*range(0x99,0xa9),*range(0xb2,0xb9),0xbb,0xbd,0xc0,0xc1,0xc6,0xc7}
            while pc<len(code):
                at=pc;op=code[pc];pc+=1
                if op in (0xaa,0xab):
                    pc+=(4-pc%4)%4
                    if op==0xaa:
                        low=int.from_bytes(code[pc+4:pc+8],'big',signed=True);high=int.from_bytes(code[pc+8:pc+12],'big',signed=True);pc+=12+4*(high-low+1)
                    else:pc+=8+8*int.from_bytes(code[pc+4:pc+8],'big')
                    continue
                if op==0xc4:
                    pc+=5 if code[pc]==0x84 else 3;continue
                size=1 if op in one else 2 if op in two else 4 if op in (0xb9,0xba,0xc8,0xc9) else 3 if op==0xc5 else 0
                operand=code[pc:pc+size];pc+=size
                if 0x02<=op<=0x08:instructions.append([at,'int',op-3])
                elif op in (0x10,0x11):instructions.append([at,'int',int.from_bytes(operand,'big',signed=True)])
                elif op in (0x12,0x13,0x14):instructions.append([at,'ldc',resolve(int.from_bytes(operand,'big'))])
                elif 0xb2<=op<=0xb9:instructions.append([at,hex(op),resolve(int.from_bytes(operand[:2],'big'))])
            methods[name+desc]=instructions
    return dict(sha256=hashlib.sha256(raw).hexdigest(),constant_fields=fields,methods=methods)


def main():
    jar=Path(r'C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\desktop-1.0.jar')
    result={}
    with zipfile.ZipFile(jar) as z:
        for name in z.namelist():
            if name.endswith('.class') and ((name.startswith('com/megacrit/cardcrawl/cards/') and '$' not in name) or name.rsplit('/',1)[-1] in ('RegalPillow.class','Boot.class')):
                result[name]=inspect(z.read(name))
    out=ROOT/'data/raw/game_local/cfad868ac8d65a88/review-class-evidence.json'
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'classes':len(result),'path':out.relative_to(ROOT).as_posix()}))


if __name__=='__main__':main()
