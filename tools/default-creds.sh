#!/bin/bash
git clone https://github.com/ihebski/DefaultCreds-cheat-sheet "$HOME/tools/information/DefaultCreds-cheat-sheet"
pip3 install -r "$HOME/tools/information/DefaultCreds-cheat-sheet/requirements.txt"
cp creds /usr/bin/ && chmod +x /usr/bin/creds
rm -rf "$HOME/tools/information/DefaultCreds-cheat-sheet"