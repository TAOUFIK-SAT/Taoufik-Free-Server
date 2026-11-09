#!/bin/sh
# ==========================================
# Installer Script for TAOUFIK SAT PANEL
# ==========================================

PLUGIN_PATH="/usr/lib/enigma2/python/Plugins/Extensions/TaoufikFreeServer"

echo ">>> Creating PanelStore directory..."
mkdir -p "$PLUGIN_PATH" > /dev/null 2>&1

echo ">>> Downloading TAOUFIK SAT PANEL..."
wget -q -O "$PLUGIN_PATH/__init__.py" "https://raw.githubusercontent.com/TAOUFIK-SAT/Taoufik-Free-Server/main/TaoufikFreeServer/__init__.py"
wget -q -O "$PLUGIN_PATH/plugin.py" "https://raw.githubusercontent.com/TAOUFIK-SAT/Taoufik-Free-Server/main/TaoufikFreeServer/plugin.py"
wget -q -O "$PLUGIN_PATH/icon.png" "https://raw.githubusercontent.com/TAOUFIK-SAT/Taoufik-Free-Server/main/TaoufikFreeServer/plugin.png"

if [ $? -eq 0 ]; then
    chmod 755 "$PLUGIN_PATH/"*.py > /dev/null 2>&1
    echo "------------------------------------------"
    echo ">>> SUCCESS: TAOUFIK SAT PANEL installed!"
    echo ">>> Please restart Enigma2 GUI now."
    echo "------------------------------------------"
else
    echo ">>> Error: Download failed. Please check your internet connection."
fi
exit 0
