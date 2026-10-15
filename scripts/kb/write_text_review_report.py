"""Publish the exact-pair review outcomes without changing canonical data."""
import json,sqlite3
from bootstrap_sample import ROOT,DB_PATH
from build_wiki import entity_path

def main():
    data=json.loads((ROOT/'data/decisions/xiao-text-review.json').read_text(encoding='utf-8'))
    c=sqlite3.connect(DB_PATH);c.row_factory=sqlite3.Row
    def label(d):
        r=c.execute("SELECT name FROM names WHERE entity_id=? AND language='zh-CN' ORDER BY is_preferred DESC LIMIT 1",(d['entity_id'],)).fetchone()
        kind=c.execute('SELECT kind FROM entities WHERE id=?',(d['entity_id'],)).fetchone()[0]
        path=entity_path(kind,d['entity_id']).relative_to(ROOT).as_posix()
        return f"[{r[0] if r else d['entity_id']}](../{path}) · {d['field_path']}"
    headings={'equivalent_notation':'数字/标点写法等价','equivalent_wording':'措辞/非规则文案等价',
              'source_editorial_error':'来源错字、重复或编辑残留','resolved_source_difference':'已有采用依据的来源差异',
              'source_annotation':'来源附加注释，分开审核','renderer_corrected':'本库图标渲染错误，已修正','rule_difference_pending':'尚需规则核验'}
    lines=['# 文本差异自审结果','','重新逐对审阅此前96项数值或文字差异及139项文字差异，共235项。此前直接把文本差异交给人工审核，包含大量误报；本次已更正分类。',
    '','| 自审分类 | 数量 |','|---|---:|']
    for status,title in headings.items():lines.append(f"| {title} | {data['counts'].get(status,0)} |")
    lines += ['','“1个／一个”“两点／2点”等数量写法不再算数值冲突。对措辞差异逐对判断，而不是粗暴删除“不”“所有”“每回合”等词，或仅按数字相同判定等价。',
    '','发现并修正回收基础/升级和双重存在基础描述的能量单位误渲染，中英文共6段：`与其耗能相等的1点能量`改为`与其耗能相等的能量`；`X 1点能量`改为`X点能量`。',
    '','逐项决定见 [审核决定JSON](../data/decisions/xiao-text-review.json)，保存原值、新值、来源值和理由。判定只对完全相同的值对生效，数据更新后不会沿用旧判定。原始来源文字保留。',
    '','22项附加注释并非全部已验证：包括关键词解释、卡牌生成限制、时间吞噬者技巧等；它们与卡面固定描述分开。1项规则待核验也只针对这235项文本差异，并非全库只剩1项工作。',
    '','怪物条件/概率、事件条件、特殊卡动态数值、99篇历史快照等原有缺口仍在，未以本次文字等价判定代替规则审核。','']
    for status in headings:
        lines += [f'## {headings[status]}','']
        for d in data['decisions']:
            if d['status']!=status:continue
            lines += [f"- {label(d)}：{d['reason']}"]
        lines.append('')
    (ROOT/'reports/文本差异自审.md').write_text('\n'.join(lines),encoding='utf-8')
    from manual_review_prompts import write_checklist
    write_checklist(ROOT,data,label)
    path=ROOT/'reports/xiaoheihe-full-review.md';text=path.read_text(encoding='utf-8')
    start=text.index('自动对照状态统计') if '自动对照状态统计' in text else text.index('文本差异已逐对自审')
    end=text.index('## 使用与复核',start)
    report=json.loads((ROOT/'reports/xiaoheihe-full-review.json').read_text(encoding='utf-8'))
    table='文本差异已逐对自审，详见[自审结果](文本差异自审.md)。数字写法、同义措辞和已解释的来源差异不再作为待用户判断的数值冲突。以下统计含候选与废弃实体；状态只表示对应字段的审核层次。\n\n| 状态 | 条数 |\n|---|---:|\n'
    table+=''.join(f'| {s} | {n} |\n' for s,n in report['field_status'].items())+'\n'
    text=text[:start]+table+text[end:]
    text=text.replace('9项回归测试通过','11项回归测试通过')
    path.write_text(text,encoding='utf-8');c.close()

if __name__=='__main__':main()
