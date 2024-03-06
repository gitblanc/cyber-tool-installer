#!/bin/bash
mkdir -p "$HOME/tools/peass"
wget "https://github.com/carlospolop/PEASS-ng/releases/download/20240303-ce06043c/linpeas.sh" -O "$HOME/tools/peass/linpeas.sh"
wget "https://github.com/carlospolop/PEASS-ng/releases/download/20240303-ce06043c/winPEAS.bat" -O "$HOME/tools/peass/winpeas.bat"