#!/bin/bash
git clone https://github.com/sc0tfree/mentalist.git "$HOME/tools/information/mentalist"
apt-get update && apt-get install python3.6 -y
python3.6 "$HOME/tools/information/mentalist/setup.py" install
rm -rf "$HOME/tools/information/mentalist"