#!/usr/bin/env bash
# CommunicationMod SpireConfig 的 command 指向本文件。
# 注意：CommunicationMod 以游戏目录为 cwd 启动外部进程，所以这里必须先 cd 回仓库。
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"
exec "$REPO/.venv/bin/python" -m bridge.main "$@"
