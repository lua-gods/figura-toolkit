#!/usr/bin/env bash
set -e


rm -rf build dist *.egg-info

.venv/bin/python -m PyInstaller \
--onefile \
--collect-submodules ftk.cli.commands \
--name figura-toolkit \
ftk/__main__.py


chmod +x dist/figura-toolkitecho $SHELL