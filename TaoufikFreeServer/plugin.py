# -*- coding: utf-8 -*-
# DEVELOPED BY TAOUFIK © 2026 - PROFESSIONAL PANEL ENGINE
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.MenuList import MenuList
from Screens.Console import Console
import os

class TaoufikFreeServerPanel(Screen):
	# تصميم الواجهة الرئيسية للبانل بصيغة XML متوافقة مع كافة صور Enigma2
	skin = """
	<screen name="TaoufikFreeServerPanel" position="center,center" size="880,550" title="TAOUFIK FREE SERVER PANEL v2.0" backgroundColor="#0d1b2a">
		<!-- الشريط العلوي -->
		<widget name="header_label" position="0,0" size="880,65" font="Regular;26" halign="center" valign="center" backgroundColor="#1b263b" textColor="#00b4d8" transparent="0" zIndex="1" />
		
		<!-- قائمة الخيارات الرئيسية -->
		<widget name="menu_list" position="40,85" size="800,240" backgroundColor="#1b263b" font="Regular;20" itemHeight="48" scrollbarMode="showOnDemand" zIndex="2" />
		
		<!-- شريط الحالة والوصف -->
		<widget name="status_label" position="40,340" size="800,75" font="Regular;17" halign="center" valign="center" textColor="#ffffff" backgroundColor="#1b263b" transparent="0" zIndex="2" />
		
		<!-- التوقيع والحقوق -->
		<label text="DEVELOPED BY TAOUFIK © 2026" position="40,425" size="800,25" font="Regular;15" halign="center" textColor="#708090" transparent="1" />

		<!-- أزرار التحكم الملونة -->
		<widget name="key_red" position="40,465" size="190,50" backgroundColor="#cf6679" foregroundColor="#000000" zPosition="2" transparent="0" font="Regular;19" halign="center" valign="center" />
		<widget name="key_green" position="243,465" size="190,50" backgroundColor="#3ddc84" foregroundColor="#000000" zPosition="2" transparent="0" font="Regular;19" halign="center" valign="center" />
		<widget name="key_yellow" position="446,465" size="190,50" backgroundColor="#f1c40f" foregroundColor="#000000" zPosition="2" transparent="0" font="Regular;19" halign="center" valign="center" />
		<widget name="key_blue" position="650,465" size="190,50" backgroundColor="#00b4d8" foregroundColor="#000000" zPosition="2" transparent="0" font="Regular;19" halign="center" valign="center" />
	</screen>
	"""

	def __init__(self, session):
		Screen.__init__(self, session)
		self.session = session
		
		self["header_label"] = Label("⚡ TAOUFIK FREE SERVER PANEL v2.0")
		self["status_label"] = Label("حدد الإجراء المطلوب من القائمة أعلاه ثم اضغط OK أو استخدم الأزرار الملونة.")
		
		# قائمة الإضافات والخيارات الاحترافية
		self.menuitems = [
			("🚀 جلب وتحديث السيرفرات المجانية (CCcam & Newcamd)", self.run_embedded_script),
			("🔄 إعادة تشغيل محاكي OSCam / NCam فوراً", self.restart_cam),
			("🔍 فحص الاتصال والتشخيص السريع للبيئة", self.run_manual_check),
			("📂 التحقق من مسارات وأوضاع ملفات Config", self.show_config_info),
			("🧹 تنظيف وحذف السيرفرات المجانية المضافة", self.clean_added_servers),
			("❌ خروج من البانل", self.close)
		]
		
		self["menu_list"] = MenuList([x[0] for x in self.menuitems])
		
		# تسميات الأزرار الملونة
		self["key_red"] = Label("خروج (Red)")
		self["key_green"] = Label("جلب السيرفرات")
		self["key_yellow"] = Label("إعادة الكام")
		self["key_blue"] = Label("فحص النظام")
		
		self["actions"] = ActionMap(["SetupActions", "ColorActions", "DirectionActions"], {
			"red": self.close,
			"green": self.run_embedded_script,
			"yellow": self.restart_cam,
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
# DEVELOPED BY TAOUFIK © 2026 - ADVANCED SCRAPING ENGINE
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
        echo "label = TAOUFIK_${host}_${port}"
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
        echo "label = TAOUFIK_${host}_${port}"
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

rm -f "$TEMP_FILE" "$FINAL_FILE" "$CONVERTED_FILE" "$TEMP_FILE.download" 2>/devnull
"""

		try:
			with open(self.temp_script_path, "w") as f:
				f.write(shell_script_content)
			
			os.system("chmod 755 %s" % self.temp_script_path)
			cmd = "sh %s" % self.temp_script_path
			self.session.open(Console, title="TAOUFIK FREE SERVER - Engine Console", cmdlist=[cmd])
		except Exception as e:
			self["status_label"].setText("خطأ في إنشاء ملف التشغيل المؤقت!")

	def restart_cam(self):
		cmd = "echo 'Restarting Softcam...' && (killall -9 oscam ncam 2>/dev/null; sleep 1; /usr/bin/oscam & /usr/bin/ncam &) && echo 'Done!'"
		self.session.open(Console, title="TAOUFIK FREE SERVER - Softcam Restart", cmdlist=[cmd])

	def clean_added_servers(self):
		cmd = r"""
		START_MARKER="#--- TAOUFIK FREE START ---"
		END_MARKER="#--- TAOUFIK FREE END ---"
		for config_path in "/etc/tuxbox/config/ncam.server" "/etc/tuxbox/config/oscam.server"; do
			if [ -f "$config_path" ]; then
				sed -i "/$START_MARKER/,/$END_MARKER/d" "$config_path"
				sed -i '/^$/N;/^\n$/D' "$config_path"
			fi
		done
		echo "Cleaned all TAOUFIK Free Servers successfully!"
		"""
		self.session.open(Console, title="TAOUFIK FREE SERVER - Clean Configs", cmdlist=[cmd])

	def show_config_info(self):
		ncam_exists = os.path.exists("/etc/tuxbox/config/ncam.server")
		oscam_exists = os.path.exists("/etc/tuxbox/config/oscam.server")
		msg = "حالة مسارات التشكيل:\n- NCam Config: %s | - OSCam Config: %s" % (
			'موجود ✅' if ncam_exists else 'غير متوفر ❌',
			'موجود ✅' if oscam_exists else 'غير متوفر ❌'
		)
		self["status_label"].setText(msg)

	def run_manual_check(self):
		cmd = "echo '=== Diagnostic Check ===' && opkg list-installed | grep -E 'oscam|ncam|wget' && ping -c 2 google.com"
		self.session.open(Console, title="TAOUFIK FREE SERVER - Diagnostics", cmdlist=[cmd])

def main(session, **kwargs):
	session.open(TaoufikFreeServerPanel)

def Plugins(**kwargs):
	return [PluginDescriptor(
		name="TAOUFIK FREE SERVER",
		description="Professional Free Server Scraper Panel for Enigma2",
		where=PluginDescriptor.WHERE_PLUGINMENU,
		icon="plugin.png",
		fnc=main
	)]
