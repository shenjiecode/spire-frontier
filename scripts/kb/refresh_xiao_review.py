"""Save current public directory/articles separately from historical evidence."""
import concurrent.futures
import hashlib
import json
import random
import sys
import time
from datetime import datetime, timezone
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError

from bootstrap_sample import ROOT, decode_xiao
from discover_inventory import xiao_signature

OUT = ROOT / 'data/raw/xiaoheihe-review/2026-09-18'


def request(url):
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Referer': 'https://web.xiaoheihe.cn/'}), timeout=25) as response:
                return response.read()
        except Exception as exc:
            if isinstance(exc, HTTPError) and exc.code in (401,403,429):
                raise
            if attempt == 2:
                raise
            time.sleep(2 + attempt)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    directory = OUT / 'directory.json'
    if not directory.exists():
        timestamp = int(time.time())
        nonce = hashlib.md5(f'{timestamp}{random.random()}'.encode()).hexdigest().upper()
        params = dict(os_type='web', app='heybox', client_type='mobile', version='999.0.4',
                      x_client_type='web', x_os_type='Windows', x_app='heybox', heybox_id='-1',
                      wiki_id='646570', verison='', is_share='1', _time=str(timestamp), nonce=nonce,
                      hkey=xiao_signature('/wiki/get_homepage_content/', timestamp, nonce))
        raw = request('https://api.xiaoheihe.cn/wiki/get_homepage_content/?' + urlencode(params))
        payload = json.loads(raw.decode('utf-8'))
        if not payload.get('result', {}).get('chunk'):
            raise ValueError('Directory response is not a Wiki directory')
        directory.write_bytes(raw)
    payload = json.loads(directory.read_text(encoding='utf-8'))
    entries = {}
    for chunk in payload['result']['chunk']:
        for block in chunk.get('block', []):
            for tag in block.get('tag_list', []):
                for entry in tag.get('block_entries') or []:
                    aid = entry.get('article_id')
                    if aid:
                        entries[str(aid)] = entry
    manifest_path = OUT / 'manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else {}
    pending = [aid for aid in sorted(entries) if aid not in manifest or manifest[aid].get('error')]

    def fetch(aid):
        url = f'https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id={aid}&wiki_id=646570'
        try:
            raw = request(url)
            text = decode_xiao(raw)
            if 'article-content' not in text:
                raise ValueError('No article-content in response')
            content = text.encode('utf-8')
            digest = hashlib.sha256(content).hexdigest()
            path = OUT / f'{aid}-{digest[:12]}.html'
            path.write_bytes(content)
            return aid, dict(url=url, path=path.relative_to(ROOT).as_posix(), sha256=digest,
                             fetched_at=datetime.now(timezone.utc).isoformat())
        except Exception as exc:
            return aid, dict(url=url, error=str(exc))
        finally:
            time.sleep(.25)

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for n, (aid, result) in enumerate(executor.map(fetch, pending), 1):
            manifest[aid] = result
            if n % 40 == 0 or n == len(pending):
                manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
                print(f'{n}/{len(pending)} articles; errors={sum(bool(v.get("error")) for v in manifest.values())}', flush=True)
    print(json.dumps(dict(directory_articles=len(entries),saved=len(manifest), errors={k:v for k,v in manifest.items() if v.get('error')}), ensure_ascii=False))


if __name__ == '__main__':
    main()
