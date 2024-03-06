#!/bin/bash
latest_release_tag=$(curl -s https://api.github.com/repos/carlospolop/PEASS-ng/releases/latest | jq -r '.tag_name')
download_url_lin="https://github.com/carlospolop/PEASS-ng/releases/download/${latest_release_tag}/linpeas.sh"
mkdir -p "$HOME/tools/peass"
wget "$download_url_lin" -O "$HOME/tools/peass/linpeas.sh"
download_url_win="https://github.com/carlospolop/PEASS-ng/releases/download/${latest_release_tag}/winpeas.bat"
wget "$download_url_win" -O "$HOME/tools/peass/winpeas.bat"