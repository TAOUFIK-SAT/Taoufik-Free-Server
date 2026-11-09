# -*- coding: utf-8 -*-
# DEVELOPED BY TAOUFIK © 2026 - ALL IN ONE ENGINE
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.Label import Label
from Screens.Console import Console
import os

class TaoufikFreeServerLauncher(Screen):
	skin = """
	<screen name="TaoufikFreeServerLauncher" position="center,center" size="750,260" title="TAOUFIK FREE SERVER (All-In-One)" backgroundColor="#151515">
		<widget name="status_label" position="30,60" size="690,50" font="Regular;24" halign="center" valign="center" textColor="#ffffff" transparent="1" />
		<label text="DEVELOPED BY TAOUFIK © 2026" position="30,130" size="690,40" font="Regular;18" halign="center" textColor="#00ff8000" transparent="1" />
		<widget name="key_red" position="50,190" size="200,45" backgroundColor="#ff0000" zPosition="1" transparent="0" font="Regular;20" halign="center" valign="center" textColor="#ffffff" />
		<widget name="key_green" position="500,190" size="200,45" backgroundColor="#00ff00" zPosition="1" transparent="0" font="Regular;20" halign="center" valign="center" textColor="#ffffff" />
	</screen>
	"""

	def __init__(self, session):
		Screen.__init__(self, session)
		self.session = session
		
		self["status_label"] = Label("اضغط الزر الأخضر لتشغيل جلب وتحديث السيرفرات")
		self["key_red"] = Label("خروج")
		self["key_green"] = Label("بدء العملية")
		
		self["actions"] = ActionMap(["SetupActions", "ColorActions"], {
			"red": self.close,
			"green": self.run_embedded_script,
			"cancel": self.close
		}, -2)

		self.temp_script_path = "/tmp/Taoufik_Free_Server.sh"

	def run_embedded_script(self):
		shell_script_content = r"""#!/bin/sh
# DEVELOPED BY TAOUFIK © 2026 - WGET BACKBONE ENGINE FOR UNIVERSAL COMPATIBILITY
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

echo "=== Scraping Live Feeds (Wget Universal Engine) ==="

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
        START_MARKER="#--- TAOUFIK FREE START ---"
        END_MARKER="#--- TAOUFIK FREE END ---"
        
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
			self.session.open(Console, title="Taoufik Free Server Live Engine", cmdlist=[cmd])
		except Exception as e:
			self["status_label"].setText("خطأ في إنشاء ملف التشغيل المؤقت!")

def main(session, **kwargs):
	session.open(TaoufikFreeServerLauncher)

def Plugins(**kwargs):
	return [PluginDescriptor(
		name="TAOUFIK FREE SERVER",
		description="All-In-One Free Server Scraper Engine for Enigma2",
		where=PluginDescriptor.WHERE_PLUGINMENU,
		icon="plugin.png",
		fnc=main
	)]
