#!/bin/bash
git clone https://github.com/sc0tfree/mentalist.git "$HOME/tools/information/mentalist"
python3 "$HOME/tools/information/mentalist/setup.py" install
rm -rf "$HOME/tools/information/mentalist"