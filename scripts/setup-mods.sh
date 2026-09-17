#!/usr/bin/env bash
# 下载杀戮尖塔1 modding 三件套到 game-mods/（版本已固定，升级需评审）
set -uo pipefail
cd "$(dirname "$0")/.."
mkdir -p game-mods

dl() { # dl <url> <dest>  带重试与完整性校验
  local url="$1" dest="game-mods/$2" tries=5
  [ -s "$dest" ] && unzip -tq "$dest" >/dev/null 2>&1 && { echo "已有 $2（完整），跳过"; return 0; }
  for i in $(seq 1 $tries); do
    echo "下载 $2 (第 $i 次)..."
    curl -sL --fail --max-time 300 -o "$dest" "$url" || { sleep 3; continue; }
    unzip -tq "$dest" >/dev/null 2>&1 && { echo "$2 ✓"; return 0; }
    sleep 3
  done
  echo "$2 下载失败"; return 1
}

dl "https://github.com/kiooeht/ModTheSpire/releases/download/v3.6.3/ModTheSpire.zip" "ModTheSpire.zip" || exit 1
dl "https://github.com/daviscook477/BaseMod/releases/download/v5.5.0/BaseMod.jar" "BaseMod.jar" || exit 1
dl "https://github.com/ForgottenArbiter/CommunicationMod/releases/download/v1.2.1/CommunicationMod.jar" "CommunicationMod.jar" || exit 1

# MTS 发行的是 zip，解出 ModTheSpire.jar
[ -f game-mods/ModTheSpire.jar ] || (cd game-mods && unzip -o -q ModTheSpire.zip ModTheSpire.jar)
echo "game-mods/ 内容："
ls -la game-mods/
