#!/bin/sh
# =========================================================
# INSTALLER SCRIPT FOR TAOUFIK FREE SERVER ENIGMA2 PLUGIN
# DEVELOPED BY KHALED © 2026
# =========================================================

PLUGIN_DIR="/usr/lib/enigma2/python/Plugins/Extensions/TaoufikFreeServer"
TMP_DIR="/tmp/taoufik_install"

echo "================================================="
echo "   🚀 Starting TAOUFIK FREE SERVER Installation   "
echo "================================================="

# 1. Vérification et création des dossiers nécessaires
mkdir -p "$PLUGIN_DIR"
mkdir -p "$TMP_DIR"
mkdir -p /etc/tuxbox/config

# 2. Vérification des dépendances (wget et python)
echo "[+] Checking system dependencies..."
if ! command -v wget >/dev/null 2>&1; then
    echo "[!] Wget is missing. Installing wget..."
    opkg update && opkg install wget
fi

# 3. Écriture directe du plugin.py dans le répertoire d'extension
echo "[+] Creating plugin structure..."

cat << 'EOF' > "$PLUGIN_DIR/plugin.py"
# -*- coding: utf-8 -*-
# DEVELOPED BY KHALED © 2026
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.MenuList import MenuList
from Screens.Console import Console
import os

class TaoufikFreeServerPanel(Screen):
	skin = """
	<screen name="TaoufikFreeServerPanel" position="center,center" size="850,520" title="TAOUFIK FREE SERVER" backgroundColor="#0d1b2a">
		<widget name="header_label" position="0,0" size="850,60" font="Regular;24" halign="center" valign="center" backgroundColor="#1b263b" textColor="#00b4d8" transparent="0" zIndex="1" />
		<widget name="menu_list" position="40,80" size="770,220" backgroundColor="#1b263b" font="Regular;20" itemHeight="45" scrollbarMode="showOnDemand" zIndex="2" />
		<widget name="status_label" position="40,315" size="770,70" font="Regular;16" halign="center" valign="center" textColor="#ffffff" backgroundColor="#1b263b" transparent="0" zIndex="2" />
		<widget name="key_red" position="40,430" size="185,45" backgroundColor="#cf6679" foregroundColor="#000000" zPosition="2" transparent="0" font="Regular;19" halign="center" valign="center" />
		<widget name="key_green" position="235,430" size="185,45" backgroundColor="#3ddc84" foregroundColor="#000000" zPosition="2" transparent="0" font="Regular;19" halign="center" valign="center" />
		<widget name="key_yellow" position="430,430" size="185,45" backgroundColor="#f1c40f" foregroundColor="#000000" zPosition="2" transparent="0" font="Regular;19" halign="center" valign="center" />
		<widget name="key_blue" position="625,430" size="185,45" backgroundColor="#00b4d8" foregroundColor="#000000" zPosition="2" transparent="0" font="Regular;19" halign="center" valign="center" />
	</screen>
	"""

	def __init__(self, session):
		Screen.__init__(self, session)
		self.session = session
		
		self["header_label"] = Label("⚡ TAOUFIK FREE SERVER")
		self["status_label"] = Label("اختر العملية من القائمة أعلاه أو اضغط مباشرة على الأزرار الملونة بالأسفل.")
		
		self.menuitems = [
			("🚀 جلب وتحديث السيرفرات المجانية (CCcam & Newcamd)", self.run_embedded_script),
			("🔍 فحص الاتصال والتشخيص السريع للبيئة", self.run_manual_check),
			("📂 التحقق من حالة مسارات ملفات التشكيل (Config)", self.show_config_info),
			("❌ خروج من البانل", self.close)
		]
		
		self["menu_list"] = MenuList([x[0] for x in self.menuitems])
		
		self["key_red"] = Label("خروج (Red)")
		self["key_green"] = Label("تنفيذ (Green)")
		self["key_yellow"] = Label("الملفات (Yellow)")
		self["key_blue"] = Label("فحص (Blue)")
		
		self["actions"] = ActionMap(["SetupActions", "ColorActions", "DirectionActions"], {
			"red": self.close,
			"green": self.okClicked,
			"yellow": self.show_config_info,
			"blue": self.run_manual_check,
			"ok": self.okClicked,
			"cancel": self.close
		}, -2)

		self.temp_script_path = "/tmp/Taoufik_Free_Server.sh"

	def okClicked(self):
		selected_index = self["menu_list"].getSelectedIndex()
		if selected_index is not None and selected_index < len(self.menuitems):
			self.menuitems[selected_index][1]()

	def run_embedded_script(self):
		shell_script_content = r"""#!/bin/sh
# DEVELOPED BY KHALED © 2026 - WGET BACKBONE ENGINE FOR UNIVERSAL COMPATIBILITY
LOG_FILE="/tmp/downloader.log"

OUTPUT_FILE="/etc/tuxbox/config/ncam.server"
[ ! -f "$OUTPUT_FILE" ] && OUTPUT_FILE="/etc/tuxbox/config/oscam.server"

URLS=(
    "https://cccam-premium.pro/free-cccam/"
    "https://cccamsate.com/free"
    "https://cccamiptv.tv/cccamfree/#page-content"
    "https://cccam.net/freecccam"
    "https://cccamia.com/cccam-free/"
    "https://cccamhub.com/cccamfree/"
    "https://cccamgalaxy.com/"
    "https://cccamfree48h.yolasite.com/server-2.php"
    "https://raw.githubusercontent.com/levi-45/free-cccam/main/servers.txt"
)

YESTERDAY=$(python -c "from datetime import datetime, timedelta; print((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))")
TODAY=$(python -c "from datetime import datetime; print(datetime.now().strftime('%Y-%m-%d'))")

URLS+=("https://testious.com/old-free-cccam-servers/$YESTERDAY/")
URLS+=("https://testious.com/old-free-cccam-servers/$TODAY/")

TEMP_FILE="/tmp/servers_temp.txt"
FINAL_FILE="/tmp/servers_final.txt"
CONVERTED_FILE="/tmp/servers_converted.txt"

> "$FINAL_FILE"
> "$TEMP_FILE"
> "$CONVERTED_FILE"

echo "=== Panel Engine: Scraping Live Feeds ==="

parse_servers() {
    local content="$1"
    local clean_content=$(echo "$content" | sed 's/<[^>]*>//g' | tr -d '\r' | sed 's/&nbsp;/ /g' | sed 's/&amp;/\&/g')
    
    echo "$clean_content" | grep -oE 'C:[[:space:]]*[[:alnum:].-]+[[:space:]]+[0-9]+[[:space:]]+[[:alnum:].-]+[[:space:]]+[[:alnum:].-]+' >> "$TEMP_FILE"
    echo "$clean_content" | grep -oE 'C:[[:space:]]*[[:alnum:].-]+[[:space:]]+[0-9]+[[:space:]]+[[:alnum:].-]+[[:space:]]+[[:alnum:].-]+' | sed 's/$/ #/' >> "$TEMP_FILE"
    echo "$clean_content" | grep -oE 'N:[[:space:]]*[[:alnum:].-]+[[:space:]]+[0-9]+[[:space:]]+[[:alnum:].-]+[[:space:]]+[[:alnum:].-]+[[:space:]]+[0-9a-fA-F]+' >> "$TEMP_FILE"
}

for URL in "${URLS[@]}"; do
    echo "Downloading & Processing: $URL"
    
    if wget -q --no-check-certificate --timeout=6 --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "$URL" -O "$TEMP_FILE".download; then
        if [ -s "$TEMP_FILE".download ]; then
            CONTENT=$(cat "$TEMP_FILE".download)
            parse_servers "$CONTENT" "$URL"
        fi
        rm -f "$TEMP_FILE".download
    else
        echo "--> Timeout or Host Down: Skipping $URL safely..."
    fi
done

convert_to_oscam() {
    local line="$1"
    local parts=($line)
    if [ "${#parts[@]}" -lt 5 ]; then return; fi
    
    local protocol_type=$(echo "${parts[0]}" | tr -d ':')
    local host="${parts[1]}"
    local port="${parts[2]}"
    local user="${parts[3]}"
    local password="${parts[4]}"
    
    if [ "$protocol_type" = "C" ] || [ "$protocol_type" = "c" ]; then
        echo "[reader]"
        echo "label = ${host}_${port}"
        echo "protocol = cccam"
        echo "device = ${host},${port}"
        echo "user = ${user}"
        echo "password = ${password}"
        echo "group = 1"
        echo "cccversion = 2.1.2"
        echo "inactivitytimeout = 1"
        echo "reconnecttimeout = 30"
        echo "disablelog = 1"
        echo ""
    elif [ "$protocol_type" = "N" ] || [ "$protocol_type" = "n" ] && [ "${#parts[@]}" -ge 6 ]; then
        local key="${parts[5]}"
        echo "[reader]"
        echo "label = ${host}_${port}"
        echo "enable = 1"
        echo "protocol = newcamd"
        echo "key = ${key}"
        echo "device = ${host},${port}"
        echo "user = ${user}"
        echo "password = ${password}"
        echo "group = 1"
        echo "inactivitytimeout = 1"
        echo "reconnecttimeout = 30"
        echo "ccckeepalive = 1"
        echo ""
    fi
}

if [ -s "$TEMP_FILE" ]; then
    grep -E '^[CN]:' "$TEMP_FILE" | sed 's/#.*//' | sed 's/[[:space:]]*$//' | sort | uniq > "$FINAL_FILE"
    FINAL_COUNT=$(wc -l < "$FINAL_FILE")
    
    if [ "$FINAL_COUNT" -gt 0 ]; then
        START_MARKER="#--- TAOUFIK FREE SERVER START ---"
        END_MARKER="#--- TAOUFIK FREE SERVER END ---"
        
        while IFS= read -r line; do
            convert_to_oscam "$line" >> "$CONVERTED_FILE"
        done < "$FINAL_FILE"
        
        TARGET_CONFIGS=(
            "/etc/tuxbox/config/ncam.server"
            "/etc/tuxbox/config/oscam.server"
        )
        
        for config_path in "${TARGET_CONFIGS[@]}"; do
            if [ -f "$config_path" ]; then
                cp "$config_path" "${config_path}.bak"
                sed -i "/$START_MARKER/,/$END_MARKER/d" "$config_path"
                sed -i '/^$/N;/^\n$/D' "$config_path"
                echo "$START_MARKER" >> "$config_path"
                cat "$CONVERTED_FILE" >> "$config_path"
                echo "$END_MARKER" >> "$config_path"
            fi
        done
        echo "=== Sync Complete! Total Active Readers Installed: $FINAL_COUNT ==="
    fi
else
    echo "--> No servers found from any active source."
fi

rm -f "$TEMP_FILE" "$FINAL_FILE" "$CONVERTED_FILE" "$TEMP_FILE.download" 2>/dev/null
"""

		try:
			with open(self.temp_script_path, "w") as f:
				f.write(shell_script_content)
			
			os.system("chmod 755 %s" % self.temp_script_path)
			cmd = "sh %s" % self.temp_script_path
			self.session.open(Console, title="TAOUFIK FREE SERVER - Live Panel Console", cmdlist=[cmd])
		except Exception as e:
			self["status_label"].setText("خطأ في إنشاء ملف التشغيل المؤقت!")

	def show_config_info(self):
		ncam_exists = os.path.exists("/etc/tuxbox/config/ncam.server")
		oscam_exists = os.path.exists("/etc/tuxbox/config/oscam.server")
		msg = "حالة مسارات التشكيل:\n- NCam Config: %s | - OSCam Config: %s" % (
			'موجود' if ncam_exists else 'غير متوفر',
			'موجود' if oscam_exists else 'غير متوفر'
		)
		self["status_label"].setText(msg)

	def run_manual_check(self):
		cmd = "echo '=== Diagnostic & Environment Check ===' && opkg list-installed | grep -E 'oscam|ncam|wget'"
		self.session.open(Console, title="TAOUFIK FREE SERVER - Diagnostics", cmdlist=[cmd])

def main(session, **kwargs):
	session.open(TaoufikFreeServerPanel)

def Plugins(**kwargs):
	return [PluginDescriptor(
		name="TAOUFIK FREE SERVER",
		description="Free Server Panel Menu for Enigma2",
		where=PluginDescriptor.WHERE_PLUGINMENU,
		icon="plugin.png",
		fnc=main
	)]
EOF

# 4. Création du fichier __init__.py obligatoire
touch "$PLUGIN_DIR/__init__.py"

# 5. Définition des permissions
chmod -R 755 "$PLUGIN_DIR"

# 6. Nettoyage des fichiers temporaires
rm -rf "$TMP_DIR"

echo "================================================="
echo "   ✅ TAOUFIK FREE SERVER Installed Successfully! "
echo "   🔄 Restarting Enigma2 GUI...                  "
echo "================================================="

# Redémarrage de l'interface Enigma2
killall -9 enigma2
