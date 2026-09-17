#!/usr/bin/env bash
# CommunicationMod SpireConfig 的 command 指向本文件。
# 注意：CommunicationMod 以游戏目录为 cwd 启动外部进程，所以这里必须先 cd 回仓库。
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"
# Steam 沙盒内 LANG 可能未设：强制 Python 侧 UTF-8，与游戏端 stdin 编码对齐
export PYTHONIOENCODING=utf-8
export LANG=C.UTF-8 LC_ALL=C.UTF-8
exec "$REPO/.venv/bin/python" -m bridge.main "$@"
