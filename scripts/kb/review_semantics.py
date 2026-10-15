"""Conservative number notation matching and exact-pair semantic decisions.

Do not remove negation, sort effects, or equate different numeric values.
Manual decisions only apply to the exact reviewed source/current pair.
"""
import hashlib,json,re,unicodedata
from pathlib import Path

DECISIONS=Path(__file__).resolve().parents[2]/'data/decisions/xiao-text-review.json'

def pair_key(entity,article,field,current,source):
    return hashlib.sha256(json.dumps([entity,article,field,current,source],ensure_ascii=False,separators=(',',':')).encode()).hexdigest()

def chinese_integer(text):
    digits={'零':0,'〇':0,'一':1,'二':2,'两':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9}
    total=0;number=0
    for ch in text:
        if ch in digits:number=digits[ch]
        else:total+=(number or 1)*{'十':10,'百':100,'千':1000}[ch];number=0
    return str(total+number)

def notation(text):
    text=unicodedata.normalize('NFKC',str(text)).casefold()
    # Only number+unit contexts; preserve names such as 一切 and 两者择一.
    text=re.sub(r'[零〇一二两三四五六七八九十百千]+(?=\s*(?:个|张|点|层|次|回合|金币|瓶|名|件|伤害))',lambda m:chinese_integer(m[0]),text)
    text=re.sub(r'(?<=变为)零(?=[。.!！\s]|$)','0',text)
    return re.sub(r'[\s。，、；：！？,.!?:;“”"（）()\[\]【】]','',text)

def load_decisions():
    if not DECISIONS.exists():return {}
    return {r['pair_key']:r for r in json.loads(DECISIONS.read_text(encoding='utf-8'))['decisions']}

def decision_for(decisions,entity,article,field,current,source):
    return decisions.get(pair_key(entity,article,field,current,source))
