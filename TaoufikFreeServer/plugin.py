# -*- coding: utf-8 -*-
# ========================================================================
# TAOUFIK SAT PANEL - Python 3 for Enigma2
# Professional Store Interface with Console Terminal & Modern UI
# ========================================================================

from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.Console import Console
from Components.ActionMap import ActionMap
from Components.Label import Label
from Components.MenuList import MenuList
from Components.Pixmap import Pixmap
from enigma import eConsoleAppContainer
import os

PLUGIN_VERSION = "v3.0-Pro"

# قاعدة بيانات المتجر الشاملة لجميع السكربتات والبلوغينات والأقسام (مع دمج سكربت Free Servers الجديد)
STORE_CATEGORIES = {
    "Panels": {
        "Ajpanel": 'wget -q "--no-check-certificate" http://dreambox4u.com/emilnabil237/plugins/ajpanel/installer.sh -O - | /bin/sh',
        "AjPanel Custom Menu All Panels": "wget https://dreambox4u.com/emilnabil237/plugins/ajpanel/emil-panel-all.sh -O - | /bin/sh",
        "Panel Lite By Emil Nabil": "wget https://dreambox4u.com/emilnabil237/plugins/ajpanel/new/emil-panel-lite.sh -O - | /bin/sh",
        "Ciefp-Panel": "wget https://github.com/ciefp/CiefpsettingsPanel/raw/main/installer.sh -O - | /bin/sh",
        "Ciefp-Panel mod Emil Nabil": "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/Ciefp-Panel/Ciefp-Panel.sh -O - | /bin/sh",
        "dreamosat-downloader": "wget https://dreambox4u.com/emilnabil237/plugins/dreamosat-downloader/installer.sh -O - | /bin/sh",
        "EliesatPanel": "wget https://raw.githubusercontent.com/eliesat/eliesatpanel/main/installer.sh -O - | /bin/sh",
        "EmilPanel": "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/EmilPanel/emilpanel.sh -O - | /bin/sh",
        "Epanel": "wget https://dreambox4u.com/emilnabil237/plugins/epanel/installer.sh -O - | /bin/sh",
        "linuxsat-panel": "wget https://raw.githubusercontent.com/Belfagor2005/LinuxsatPanel/main/installer.sh -O - | /bin/sh",
        "levi45-AddonsManager": "wget https://dreambox4u.com/emilnabil237/plugins/levi45-addonsmanager/installer.sh -O - | /bin/sh",
        "Levi45MulticamManager": "wget https://dreambox4u.com/emilnabil237/plugins/levi45multicammanager/installer.sh -O - | /bin/sh",
        "MagicPanel-HAMDY_AHMED": "wget https://gitlab.com/h-ahmed/Panel/-/raw/main/MagicPanel_install.sh -O - | /bin/sh",
        "SatVenusPanel": "wget https://dreambox4u.com/emilnabil237/plugins/satvenuspanel/installer.sh -O - | /bin/sh",
        "SmartAddonspanel": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/SmartAddonspanel/smart-Panel.sh -O - | /bin/sh",                
        "Tspanel": "wget https://dreambox4u.com/emilnabil237/plugins/tspanel/installer.sh -O - | /bin/sh",
        "TvAddon-Panel": "wget https://dreambox4u.com/emilnabil237/plugins/tvaddon/installer.sh -O - | /bin/sh",
    },
    "Multiboot": {
        "EgamiBoot_10.5": 'wget -q "--no-check-certificate" https://raw.githubusercontent.com/emil237/egamiboot/refs/heads/main/installer.sh -O - | /bin/sh',
        "EgamiBoot_10.6": "wget https://raw.githubusercontent.com/emil237/egamiboot/refs/heads/main/egamiboot-10.6.sh -O - | /bin/sh",
        "Neoboot_9.65": "wget https://dreambox4u.com/emilnabil237/plugins/neoboot-v9.65/iNB.sh -O - | /bin/sh",
        "Neoboot_9.65_Mod-By-ElSafty": "wget https://raw.githubusercontent.com/emil237/neoboot_v9.65/main/iNB_9.65_mod-elsafty.sh -O - | /bin/sh",
        "Neoboot_9.60": "wget https://dreambox4u.com/emilnabil237/plugins/neoboot-v9.60/iNB.sh -O - | /bin/sh",
        "Neoboot_9.58": "wget https://dreambox4u.com/emilnabil237/plugins/neoboot-v9.58/iNB.sh -O - | /bin/sh",
        "Neoboot_9.54": "wget https://raw.githubusercontent.com/emil237/neoboot_9.54/main/installer.sh -O - | /bin/sh",
        "OpenMultiboot_1.3": "wget https://raw.githubusercontent.com/emil237/openmultiboot/main/installer.sh -O - | /bin/sh",
        "OpenMultiboot-E2turk": "wget https://raw.githubusercontent.com/e2TURK/omb-enhanced/main/install.sh -O - | /bin/sh",
        "Multiboot-FlashOnline": "wget https://raw.githubusercontent.com/emil237/download-plugins/main/multiboot-flashonline.sh -O - | /bin/sh",
    },
    "Channels": {
        "Elsafty-Tv-Radio-Steaming": 'wget -q "--no-check-certificate" https://dreambox4u.com/emilnabil237/settings/elsafty/installer.sh -O - | /bin/sh',
        "Khaled Ali": "wget https://raw.githubusercontent.com/emilnabil/channel-khaled/main/installer.sh -O - | /bin/sh",
        "Mohamed Goda": "wget https://raw.githubusercontent.com/emilnabil/channel-mohamed-goda/main/installer.sh -O - | /bin/sh",
        "Emil Nabil": "wget https://raw.githubusercontent.com/emilnabil/channel-emil-nabil/main/installer.sh -O - | /bin/sh",
        "Tarek Ashry": "wget https://raw.githubusercontent.com/emilnabil/channel-tarek-ashry/main/installer.sh -O - | /bin/sh",
    },
    "Plugins": {
        "ArabicSavior": "wget http://dreambox4u.com/emilnabil237/plugins/ArabicSavior/installer.sh -O - | /bin/sh",
        "Acherone": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/acherone/installer.sh -O - | /bin/sh",
        "Advanced-Screen-Shot": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/advancedscreenshot/advancedscreenshot.sh -O - | /bin/sh",
        "Alajre": "wget https://dreambox4u.com/emilnabil237/plugins/alajre/installer.sh -O - | /bin/sh",
        "Ansite": "wget https://raw.githubusercontent.com/emil237/ansite/refs/heads/main/installer.sh -O - | /bin/sh",
        "Apod": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/apod/apod.sh -O - | /bin/sh",
        "Apsattv": "wget https://raw.githubusercontent.com/Belfagor2005/Apsattv/main/installer.sh -O - | /bin/sh",
        "Astronomy": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/astronomy/astronomy.sh -O - | /bin/sh",
        "Athan Times": "wget https://dreambox4u.com/emilnabil237/plugins/athantimes/installer.sh -O - | /bin/sh",
        "Atilehd": "wget https://dreambox4u.com/emilnabil237/plugins/atilehd/installer.sh -O - | /bin/sh",
        "automatic-fullbackup": "wget https://dreambox4u.com/emilnabil237/plugins/automatic-fullbackup/installer.sh -O - | /bin/sh",
        "Auto-Dcw-Key-Add": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/auto-dcw-key-add/auto-dcw-key-add.sh -O - | /bin/sh",
        "Azkar Almuslim": "wget https://dreambox4u.com/emilnabil237/plugins/azkar-almuslim/installer.sh -O - | /bin/sh",
        "BissFeedAutoKey": "wget https://raw.githubusercontent.com/emilnabil/bissfeed-autokey/main/installer.sh -O - | /bin/sh",
        "Bitrate": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/bitrate/bitrate.sh -O - | /bin/sh",
        "Bitrate-mod-ariad": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/bitrate/bitrate-mod-ariad.sh -O - | /bin/sh",
        "Bundesliga-Permanent-Clock": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/bundesliga-permanent-clock/bundesliga-permanent-clock.sh -O - | /bin/sh",
        "CacheFlush": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/cacheflush/cacheflush.sh -O - | /bin/sh",
        "CCcaminfo-py2": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/cccaminfo/cccaminfo_py2.sh -O - | /bin/sh",
        "CCcamininfo-py3": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/cccaminfo/cccaminfo_py3.sh -O - | /bin/sh",
        "CrondManager": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/crondmanager/installer.sh -O - | /bin/sh",
        "CFG_ZOOM_FINAL": "wget https://dreambox4u.com/emilnabil237/plugins/cfg_Zoom_Final_FIX7x/installer.sh -O - | /bin/sh",
        "CiefpBouquetUpdater": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpBouquetUpdater/main/installer.sh -O - | /bin/sh",
        "CiefpChannelManager": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpChannelManager/main/installer.sh -O - | /bin/sh",
        "CiefpE2Converter": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpE2Converter/main/installer.sh -O - | /bin/sh",
        "CiefpEPGshare": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpEPGshare/main/installer.sh -O - | /bin/sh",
        "CiefpIPTVBouquets": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpIPTVBouquets/main/installer.sh -O - | /bin/sh",
        "CiefpMojTvEPG": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpMojTvEPG/main/installer.sh -O - | /bin/sh",
        "CiefpOpenDirectories": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpOpenDirectories/main/installer.sh -O - | /bin/sh",
        "CiefpOscamEditor": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpOscamEditor/main/installer.sh -O - | /bin/sh",
        "CiefpPlugins": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpPlugins/main/installer.sh -O - | /bin/sh",
        "CiefpSatelliteAnalyzer": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpSatelliteAnalyzer/main/installer.sh -O - | /bin/sh",
        "CiefpSatellitesXmlEditor": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpSatelliteXmlEditor/main/installer.sh -O - | /bin/sh",
        "CiefpScreenGrab": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpScreenGrab/main/installer.sh -O - | /bin/sh",
        "CiefpSelectSatellite": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpSelectSatellite/main/installer.sh -O - | /bin/sh",
        "CiefpSettingsDownloader": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpSettingsDownloader/main/installer.sh -O - | /bin/sh",
        "CiefpSettingsPanel": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpsettingsPanel/main/installer.sh -O - | /bin/sh",
        "CiefpSettingsStreamrelay PY2": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpSettingsStreamrelayPY2/main/installer.sh -O - | /bin/sh",
        "CiefpSettingsStreamrelay PY3": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpSettingsStreamrelay/main/installer.sh -O - | /bin/sh",
        "CiefpSettingsT2miAbertis": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpSettingsT2miAbertis/main/installer.sh -O - | /bin/sh",
        "CiefpSettingsT2miAbertisOpenPLi": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpSettingsT2miAbertisOpenPLi/main/installer.sh -O - | /bin/sh",
        "CiefpsettingsMotor": "wget https://raw.githubusercontent.com/ciefp/CiefpsettingsMotor/main/installer.sh -O - | /bin/sh",
        "CiefpTMDBSearch": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpTMDBSearch/main/installer.sh -O - | /bin/sh",
        "CiefpTvProgram": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpTvProgram/main/installer.sh -O - | /bin/sh",
        "CiefpTvProgramA1HR": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpTvProgramA1HR/main/installer.sh -O - | /bin/sh",
        "CiefpTvProgramSBB": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpTvProgramSBB/main/installer.sh -O - | /bin/sh",
        "CiefpTvProgramSK": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpTvProgramSK/main/installer.sh -O - | /bin/sh",
        "CiefpTvTodayDE": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpTvTodayDE/main/installer.sh -O - | /bin/sh",
        "CiefpWhitelistStreamrelay": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/CiefpWhitelistStreamrelay/main/installer.sh -O - | /bin/sh",
        "WebCamE2PrenjSF": "wget -q --no-check-certificate https://raw.githubusercontent.com/ciefp/WebCamE2PrenjSF/main/installer.sh -O - | /bin/sh",
        "chocholousek-picons": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/chocholousek-picons.sh -O - | /bin/sh",
        "CHLogoChanger": "wget https://dreambox4u.com/emilnabil237/plugins/CHLogoChanger/ChLogoChanger.sh -O - | /bin/sh",
        "CrashLogoViewer": "wget https://dreambox4u.com/emilnabil237/plugins/crashlogviewer/install-CrashLogViewer.sh -O - | /bin/sh",
        "Easy-Cccam": "wget https://raw.githubusercontent.com/emil237/plugins/refs/heads/main/easy-cccam/easy-cccam.sh -O - | /bin/sh",
        "enigma2readeradder": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/enigma2readeradder/enigma2readeradder.sh -O - | /bin/sh",
        "Epg Grabber": "wget https://dreambox4u.com/emilnabil237/plugins/Epg-Grabber/installer.sh -O - | /bin/sh",
        "EPGImport": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/epgimport.sh -O - | /bin/sh",
        "EPGImport-99": "wget https://raw.githubusercontent.com/Belfagor2005/EPGImport-99/main/installer.sh -O - | /bin/sh",
        "EPGTranslator": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/epgtranslator.sh -O - | /bin/sh",
        "EvgQuickSignal": "wget https://raw.githubusercontent.com/biko-73/EvgQuickSignal/main/installer.sh -O - | /bin/sh",
        "Estalker": "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/EStalker/EStalker.sh -O - | /bin/sh",
        "EstalkerWebControl": "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/EstalkerWebControl/estalkerwebcontrol.sh -O - | /bin/sh",
        "Feeds-Finder": "wget https://dreambox4u.com/emilnabil237/plugins/feeds-finder/installer.sh -O - | /bin/sh",
        "Filmxy": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/filmxy/filmxy.sh -O - | /bin/sh",
        "Footonsat": "wget https://dreambox4u.com/emilnabil237/plugins/FootOnsat/installer.sh -O - | /bin/sh",
        "Freearhey": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/freearhey/freearhey.sh -O - | /bin/sh",
        "FreeCCcamServer": "wget https://ia803104.us.archive.org/0/items/freecccamserver/installer.sh -O - | /bin/sh",
        "gioppygio": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/gioppygio/gioppygio.sh -O - | /bin/sh",
        "hardwareinfo": "wget https://dreambox4u.com/emilnabil237/plugins/hardwareinfo/installer.sh -O - | /bin/sh",
        "HasBahCa": "wget https://dreambox4u.com/emilnabil237/plugins/HasBahCa/installer.sh -O - | /bin/sh",
        "HistoryZapSelector": "wget https://dreambox4u.com/emilnabil237/plugins/historyzap/installer1.sh -O - | /bin/sh",
        "horoscope": "wget https://raw.githubusercontent.com/emilnabil/horoscope/refs/heads/main/horoscope.sh -O - | /bin/sh",
        "HolidayCountdown": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/HolidayCountdown/installer.sh -O - | /bin/sh",
        "Internet-Speedtest": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/internet-speedtest.sh -O - | /bin/sh",
        "IP_Checker": "wget https://raw.githubusercontent.com/emil237/plugins/refs/heads/main/IP_Checker.sh -O - | /bin/sh",
        "Iptv-Org-Playlists": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/iptv-org-playlists/iptv-org-playlists.sh -O - | /bin/sh",
        "iptvdream": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/main/iptvdream/iptvdream.sh -O - | /bin/sh",
        "IptvPlayer": "wget https://raw.githubusercontent.com/emil237/iptvplayer/main/iptvinstaller.sh -O - | /bin/sh",
        "KeyAdder": "wget https://raw.githubusercontent.com/fairbird/KeyAdder/main/installer.sh -O - | /bin/sh",
        "levi45-freeserver": "wget https://raw.githubusercontent.com/emil237/plugins/refs/heads/main/levi45-freeserver/levi45-freeserver.sh -O - | /bin/sh",
        "levi45-settings": "wget https://dreambox4u.com/emilnabil237/plugins/levi45-settings/levi45-settings.sh -O - | /bin/sh",
        "m3uconverter": "wget https://raw.githubusercontent.com/Belfagor2005/Archimede-M3UConverter/main/installer.sh -O - | /bin/sh",
        "MmPicons": "wget https://raw.githubusercontent.com/Belfagor2005/mmPicons/main/installer.sh -O - | /bin/sh",
        "MoviesManager": "wget http://dreambox4u.com/emilnabil237/plugins/Transmission/MoviesManager.sh -O - | /bin/sh",
        "MyCam-Plugin": "wget https://dreambox4u.com/emilnabil237/plugins/mycam/installer.sh -O - | /bin/sh",
        "MultiCamAdder": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/MultiCamAdder/installer.sh -O - | /bin/sh",
        "Multi-Iptv-Adder": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/MultiIptvAdder/installer.sh -O - | /bin/sh",
        "NewVirtualkeyBoard": "wget https://dreambox4u.com/emilnabil237/plugins/NewVirtualKeyBoard/installer.sh -O - | /bin/sh",
        "ONEupdater": "wget https://raw.githubusercontent.com/Sat-Club/ONEupdaterE2/main/installer.sh -O - | /bin/sh",
        "OrangeAudioPlugin": "wget https://raw.githubusercontent.com/popking159/OrangeAudio/refs/heads/main/installer.sh -O - | /bin/sh",
        "Ozeta-Skins-Setup": "wget https://raw.githubusercontent.com/emil237/skins-enigma2/main/PLUGIN_Skin-ozeta.sh -O - | /bin/sh",
        "Plutotv": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/main/plutotv/plutotv.sh -O - | /bin/sh",
        "Quran-karem": "wget https://dreambox4u.com/emilnabil237/plugins/quran/installer.sh -O - | /bin/sh",
        "Quran-karem_v2.2": "wget https://raw.githubusercontent.com/emil237/quran/main/installer.sh -O - | /bin/sh",
        "Radio-80-s": "wget https://raw.githubusercontent.com/Belfagor2005/Radio-80-s/main/installer.sh -O - | /bin/sh",
        "RadioGit": "wget https://dreambox4u.com/emilnabil237/plugins/radiogit/radiogit.sh -O - | /bin/sh",
        "Radiom": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/main/radiom/radiom.sh -O - | /bin/sh",
        "Rakutentv": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/main/rakutentv/rakutentv.sh -O - | /bin/sh",
        "RaedQuickSignal": "wget https://dreambox4u.com/emilnabil237/plugins/RaedQuickSignal/installer.sh -O - | /bin/sh",
        "PiconsRename": "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/PiconsRename/PiconsRename.sh -O - | /bin/sh",
        "pluginmover": "wget http://dreambox4u.com/emilnabil237/plugins/pluginmover/installer.sh -O - | /bin/sh",
        "pluginskinmover": "wget http://dreambox4u.com/emilnabil237/plugins/pluginskinmover/installer.sh -O - | /bin/sh",
        "ScreenNames": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/screennames/screennames.sh -O - | /bin/sh",
        "Screen-Recorder": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/screenrecorder/installer.sh -O - | /bin/sh",
        "SetPicon": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/setpicon/installer.sh -O - | /bin/sh",
        "scriptexecuter": "wget http://dreambox4u.com/emilnabil237/plugins/scriptexecuter/installer.sh -O - | /bin/sh",
        "showclock": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/showclock/showclock.sh -O - | /bin/sh",
        "Sherlockmod": "wget https://raw.githubusercontent.com/emil237/sherlockmod/main/installer.sh -O - | /bin/sh",
        "Simple-Zoom-Panel": "wget https://dreambox4u.com/emilnabil237/plugins/simple-zoom-panel/installer.sh -O - | /bin/sh",
        "StalkerPortalConverter": "wget https://raw.githubusercontent.com/Belfagor2005/StalkerPortalConverter/main/installer.sh -O - | /bin/sh",
        "SubsSupport_1.5.8-r9": "wget https://dreambox4u.com/emilnabil237/plugins/SubsSupport/installer1.sh -O - | /bin/sh",
        "SubsSupport_by-m.nasr": "wget https://github.com/popking159/ssupport/raw/main/subssupport-install.sh -O - | /bin/sh",
        "SubsSupport_2.1": "wget https://dreambox4u.com/emilnabil237/plugins/SubsSupport/subssupport_2.1.sh -O - | /bin/sh",
        "TMBD": "wget https://raw.githubusercontent.com/biko-73/TMBD/main/installer.sh -O - | /bin/sh",
        "Tmdb": "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/tmdb.sh -O - | /bin/sh",
        "TvDream": "wget https://raw.githubusercontent.com/Belfagor2005/tvDream/main/installer.sh -O - | /bin/sh",
        "TvManager": "wget https://raw.githubusercontent.com/Belfagor2005/tvManager/main/installer.sh -O - | /bin/sh",
        "TvParsa": "wget https://raw.githubusercontent.com/Belfagor2005/tvParsa/main/installer.sh -O - | /bin/sh",
        "TvRaiPreview": "wget https://raw.githubusercontent.com/Belfagor2005/tvRaiPreview/main/installer.sh -O - | /bin/sh",
        "TvSettings": "wget https://raw.githubusercontent.com/Belfagor2005/tvSettings/main/installer.sh -O - | /bin/sh",
        "uninstaller-Plugins": "wget http://dreambox4u.com/emilnabil237/plugins/unstaller-plugins/installer.sh -O - | /bin/sh",
        "vavoo_1.15": "wget https://dreambox4u.com/emilnabil237/plugins/vavoo/installer.sh -O - | /bin/sh",
        "xtraevent_3.3": "wget https://raw.githubusercontent.com/emil237/download-plugins/main/xtraevent_3.3.sh -O - | /bin/sh",
        "xtraevent_4.2": "wget https://raw.githubusercontent.com/emil237/download-plugins/main/xtraEvent_4.2.sh -O - | /bin/sh",
        "xtraevent_4.5": "wget https://raw.githubusercontent.com/emil237/download-plugins/main/xtraEvent_4.5.sh -O - | /bin/sh",
        "Xtraevent_4.6": "wget https://github.com/emil237/download-plugins/raw/main/Xtraevent-v4.6.sh -O - | /bin/sh",
        "xtraevent_6.798": "wget https://dreambox4u.com/emilnabil237/plugins/xtraevent/xtraevent_6.798.sh -O - | /bin/sh",
        "xtraevent_6.805": "wget https://dreambox4u.com/emilnabil237/plugins/xtraevent/xtraevent-6.805.sh -O - | /bin/sh",
        "xtraevent_6.820_All-Python": "wget https://dreambox4u.com/emilnabil237/plugins/xtraevent/xtraevent-6.820.sh -O - | /bin/sh",
        "WorldCam": "wget https://raw.githubusercontent.com/Belfagor2005/WorldCam/main/installer.sh -O - | /bin/sh",
        "Zip2Pkg-Converter": "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/Zip2Pkg/installer.sh -O - | /bin/sh",
        "Zoom_1.1.2-Py3": "wget https://dreambox4u.com/emilnabil237/plugins/zoom/installer.sh -O - | /bin/sh",
    },
    "Media & IPTV": {
        "BouquetMakerXtream": "wget -q --no-check-certificate http://dreambox4u.com/emilnabil237/plugins/BouquetMakerXtream/installer.sh -O - | /bin/sh",
        "E2m3u2Bouquet": "wget -q --no-check-certificate https://dreambox4u.com/emilnabil237/plugins/e2m3u2bouquet/installer.sh -O - | /bin/sh",
        "E2Player-MAXBAMBY": "wget -q --no-check-certificate https://gitlab.com/maxbambi/e2iplayer/-/raw/master/install-e2iplayer.sh -O - | /bin/sh",
        "E2Player-ZADMARIO": "wget -q --no-check-certificate https://gitlab.com/zadmario/e2iplayer/-/raw/master/install-e2iplayer.sh -O - | /bin/sh",
        "IptoSat": "wget -q --no-check-certificate https://dreambox4u.com/emilnabil237/plugins/iptosat/installer.sh -O - | /bin/sh",
        "IpAudio_6.7_py2": "wget -q --no-check-certificate https://dreambox4u.com/emilnabil237/plugins/ipaudio/installer.sh -O - | /bin/sh",
        "IpAudio_7.4_py3": "wget -q --no-check-certificate https://dreambox4u.com/emilnabil237/plugins/ipaudio/ipaudio-7.4-ffmpeg.sh -O - | /bin/sh",
        "IpAudioPro": "wget -q --no-check-certificate https://dreambox4u.com/emilnabil237/plugins/ipaudiopro/installer.sh -O - | /bin/sh",
        "JediEpgExtream": "wget -q --no-check-certificate https://dreambox4u.com/emilnabil237/plugins/jediepgextream/installer.sh -O - | /bin/sh",
        "jedimakerxtream": "wget -q --no-check-certificate https://dreambox4u.com/emilnabil237/plugins/jedimakerxtream/installer.sh -O - | /bin/sh",
        "multistalker": "wget -q --no-check-certificate https://dreambox4u.com/emilnabil237/plugins/multistalker/installer.sh -O - | /bin/sh",
        "MultiStalkerPro": "wget -q --no-check-certificate https://raw.githubusercontent.com/emilnabil/multi-stalkerpro/main/installer.sh -O - | /bin/sh",
        "Quarter pounder": "wget -q --no-check-certificate http://dreambox4u.com/emilnabil237/script/quarterpounder.sh -O - | /bin/sh",
        "Suptv": "wget -q --no-check-certificate https://raw.githubusercontent.com/emil237/suptv/main/installer.sh -O - | /bin/sh",
        "YouTube": "wget -q --no-check-certificate https://dreambox4u.com/emilnabil237/plugins/YouTube/installer.sh -O - | /bin/sh",
        "xklass-iptv": "wget -q --no-check-certificate https://dreambox4u.com/emilnabil237/plugins/xklass/installer.sh -O - | /bin/sh",
        "Xtreamty": "wget -q --no-check-certificate https://dreambox4u.com/emilnabil237/plugins/xtreamity/installer.sh -O - | /bin/sh",
        "Xcpluginforever": "wget -q --no-check-certificate https://raw.githubusercontent.com/Belfagor2005/xc_plugin_forever/main/installer.sh -O - | /bin/sh",
    },
    "Tools": {
        "Wget": "opkg install wget",
        "Curl": "opkg install curl",
        "UPDATE ENIGMA2 ALL PYTHON": "wget https://raw.githubusercontent.com/emil237/updates-enigma/main/update-all-python.sh -O - | /bin/sh",
        "servicescanupdates_1.2": "wget https://dreambox4u.com/emilnabil237/plugins/servicescanupdates/servicescanupdates.sh -O - | /bin/sh",
        "Super Script": "wget https://dreambox4u.com/emilnabil237/script/Super_Script.sh -O - | /bin/sh",
        "OpenATV softcamfeed": "wget -O - -q http://updates.mynonpublic.com/oea/feed | bash",
        "Fix Softcam OpenPli": "wget https://raw.githubusercontent.com/emil237/download-plugins/main/softcam-support-pli.sh -O - | /bin/sh",
        "Update OpenATV Develop feed": "wget -O - -q https://feeds2.mynonpublic.com/devel-feed | bash",
        "Repair-Inodes-From-Hdd": "wget https://raw.githubusercontent.com/emil237/scripts/refs/heads/main/repair-hdd.sh -O - | /bin/sh", 
        "FIX-ipk-Package-Installation": "wget https://dreambox4u.com/emilnabil237/script/fix-ipk-package-installation.sh -O - | /bin/sh",
        "update": "opkg update",
        "astra-sm": "opkg install astra-sm",
        "gstplayer": "opkg install gstplayer",
        "Streamlinksrv": "opkg install streamlinksrv",
        "dabstreamer": "opkg install dabstreamer",
        "eti_tools": "opkg install eti-tools",
        "dvbsnoop": "opkg install dvbsnoop", 
    },
    "Softcams": {
        "Cccam": "wget https://dreambox4u.com/emilnabil237/emu/installer-cccam.sh -O - | /bin/sh",
        "Oscam Mohamed_OS": "wget https://dreambox4u.com/emilnabil237/emu/installer-oscam.sh  -O - | /bin/sh",
        "Ncam fairman": "wget https://dreambox4u.com/emilnabil237/emu/installer-ncam.sh -O - | /bin/sh",
        "Oscam Emu biko-73": "wget https://raw.githubusercontent.com/biko-73/OsCam_EMU/main/installer.sh -O - | /bin/sh",
    },
    "Skins": {
        "BO-HLALA FHD SKIN": "wget https://raw.githubusercontent.com/biko-73/TeamNitro/main/script/installerB.sh -O - | /bin/sh",
        "Aglare-FHD for Atv-Spa-Egami": "wget https://raw.githubusercontent.com/popking159/skins/refs/heads/main/aglareatv/installer.sh -O - | /bin/sh",
        "Aglare-FHD for Pli-OBH-Vix": "wget https://raw.githubusercontent.com/popking159/skins/refs/heads/main/aglarepli/installer.sh -O - | /bin/sh",
        "Red-Dragon-FHD": "wget https://raw.githubusercontent.com/biko-73/TeamNitro/main/script/installerD.sh -O - | /bin/sh",
        "Nitro AdvanceFHD": "wget https://raw.githubusercontent.com/biko-73/NitroAdvanceFHD/main/installer.sh -qO - | /bin/sh",
        "Desert skin": "wget https://raw.githubusercontent.com/biko-73/TeamNitro/main/script/installerDs.sh -O - | /bin/sh",
        "XDreamy-FHD": "wget https://raw.githubusercontent.com/Insprion80/Skins/main/xDreamy/installer.sh -O - | /bin/sh", 
    },
    "Free Servers": {
        "TAOUFIKSAT Panel Free Server": "python3 -c \"import urllib.request, re, os, time; from datetime import datetime, timedelta; print('=== [TAOUFIKSATPANEL v1.0] ==='); print('-> Please wait...'); time.sleep(3); yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'); today = datetime.now().strftime('%Y-%m-%d'); urls = ['https://cccampremium.top/', 'https://cccampremium.biz/', 'https://cccam-premium.pro/free-cccam/', 'https://cccamsate.com/free', 'https://cccamiptv.tv/cccamfree/#page-content', 'https://cccam.net/freecccam', 'https://cccamia.com/cccam-free/', 'https://cccamhub.com/cccamfree/', 'https://cccamgalaxy.com/', 'https://cccamfree48h.yolasite.com/server-2.php', 'https://cccamx.com/free-cccam', 'https://bosscccam.co/Test.php', 'https://iptv-15days.blogspot.com/', f'https://testious.com/old-free-cccam-servers/{yesterday}/', f'https://testious.com/old-free-cccam-servers/{today}/']; ext = set(); \n[ext.add(f'C: {m[0]} {m[1]} {m[2]} {m[3]}') for u in urls for m in re.findall(r'(?i)C:\s*([a-zA-Z0-9.-]+)\s+(\d+)\s+([a-zA-Z0-9.-]+)\s+([a-zA-Z0-9.-]+)', urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=8).read().decode('utf-8', errors='ignore')) if True]; out = []; [out.extend(['[reader]', f'label = TAOUFIKSAT_{l.split()[1]}_{l.split()[2]}', 'enable = 1', 'protocol = cccam', f'device = {l.split()[1]},{l.split()[2]}', f'user = {l.split()[3]}', f'password = {l.split()[4]}', 'group = 1', 'cccversion = 2.1.2', 'ccckeepalive = 1', 'audisabled = 1', 'inactivitytimeout = 1', 'reconnecttimeout = 30', 'disablelog = 1', '']) for l in sorted(ext)]; confs = ['/etc/tuxbox/config/ncam.server', '/etc/tuxbox/config/oscam.server']; \n[open(c, 'w').write(open(c, 'r').read() + '\\n\\n#--- TAOUFIKSATPANEL FREE START ---\\n' + '\\n'.join(out) + '\\n#--- TAOUFIKSATPANEL FREE END ---\\n') for c in confs if os.path.exists(c)]; print('=== Sync Complete! Installed Free Readers Successfully ===')\"",
        "FreeServerCCcam": "wget https://ia803104.us.archive.org/0/items/freecccamserver/installer.sh -qO - | /bin/sh", 
    },
    "Bootlogos": {
        "BootlogoSwapper Atv": "wget http://dreambox4u.com/emilnabil237/script/bootlogoswapper-Atv.sh -O - | /bin/sh",
        "BootlogoSwapper-christmas": "wget http://dreambox4u.com/emilnabil237/script/bootlogoswapper-christmas.sh -O - | /bin/sh",
        "BootlogoSwapper-OpenPli": "wget http://dreambox4u.com/emilnabil237/script/bootlogoswapper-pli.sh -O - | /bin/sh",
        "bootlogoSwapper-OpenBH": "wget http://dreambox4u.com/emilnabil237/script/bootlogoswapper-OpenBH.sh  -O - | /bin/sh",
        "BootlogoSwapper_Egami": "wget http://dreambox4u.com/emilnabil237/script/bootLogoswapper-Egami.sh -O - | /bin/sh",
        "BootlogoSwapper_OpenVix": "wget http://dreambox4u.com/emilnabil237/script/bootlogoswapper-OpenVix.sh -O - | /bin/sh",
        "BootlogoSwapper_PURE2": "wget http://dreambox4u.com/emilnabil237/script/bootLogoswapper-Pure2.sh -O - | /bin/sh",
        "BootlogoSwapper_Kids": "wget http://dreambox4u.com/emilnabil237/script/bootlogoswapper-kids.sh -O - | /bin/sh",
        "BootlogoSwapper_Ramadan": "wget http://dreambox4u.com/emilnabil237/script/bootlogo-swapper-ramadan.sh -O - | /bin/sh",
    },
    "System images": {
        "Image BlackHole-3.1.0": "wget https://dreambox4u.com/emilnabil237/images/BlackHole-3.1.0.sh -O - | /bin/sh",
        "Image-Egami-10.4": "wget https://dreambox4u.com/emilnabil237/images/egami-10.4.sh -O - | /bin/sh",
        "Image-Openatv-6.4": "wget https://dreambox4u.com/emilnabil237/images/openatv-6.4.sh -O - | /bin/sh",
        "Image-Openatv-7.0": "wget https://dreambox4u.com/emilnabil237/images/openatv-7.0.sh  -O - | /bin/sh",
        "Image_Openatv-7.1": "wget https://dreambox4u.com/emilnabil237/images/openatv-7.1.sh -O - | /bin/sh",
        "Image_Openatv-7.2": "wget https://dreambox4u.com/emilnabil237/images/openatv-7.2.sh -O - | /bin/sh",
        "Image_Openatv-7.3": "wget https://dreambox4u.com/emilnabil237/images/openatv-7.3.sh -O - | /bin/sh",
        "Image_Openatv-7.4": "wget https://dreambox4u.com/emilnabil237/images/openatv-7.4.sh -O - | /bin/sh",
        "Image_Openatv-7.5": "wget https://dreambox4u.com/emilnabil237/images/openatv-7.5.sh -O - | /bin/sh",
        "Image_Openatv-7.5.1": "wget https://dreambox4u.com/emilnabil237/images/openatv-7.5.1.sh -O - | /bin/sh",
        "Image_OpenBlackHole-4.4": "wget https://dreambox4u.com/emilnabil237/images/openblackhole-4.4-for-vuplus-only.sh -O - | /bin/sh",
        "Image_OpenBlackHole-5.0": "wget https://dreambox4u.com/emilnabil237/images/openblackhole-5.0.sh -O - | /bin/sh",
        "Image_OpenBlackHole-5.1": "wget https://dreambox4u.com/emilnabil237/images/openblackhole-5.1.sh -O - | /bin/sh",
        "Image_OpenBlackHole-5.2": "wget https://dreambox4u.com/emilnabil237/images/openblackhole-5.2.sh -O - | /bin/sh",
        "Image_OpenBlackHole-5.3": "wget https://dreambox4u.com/emilnabil237/images/openblackhole-5.3.sh -O - | /bin/sh",
        "Image_OpenBlackHole-5.4": "wget https://dreambox4u.com/emilnabil237/images/openblackhole-5.4.sh -O - | /bin/sh",
        "Image_OpenDroid-7.1": "wget https://dreambox4u.com/emilnabil237/images/opendroid-7.1.sh -O - | /bin/sh",
        "Image_OpenDroid-7.3": "wget https://dreambox4u.com/emilnabil237/images/opendroid-7.3.sh -O - | /bin/sh",
        "Image_Openpli-7.3": "wget https://dreambox4u.com/emilnabil237/images/openpli-7.3.sh -O - | /bin/sh",
        "Image_Openpli-8.3": "wget https://dreambox4u.com/emilnabil237/images/openpli-8.3.sh -O - | /bin/sh",
        "Image_OpenPli-8.3-Time-Shift": "wget https://dreambox4u.com/emilnabil237/images/openpli-8.3-py2-TimeShift.sh -O - | /bin/sh",
        "Image_OpenPli-9.0-Time-Shift": "wget https://dreambox4u.com/emilnabil237/images/openpli-9.0-py3-TimeShift.sh -O - | /bin/sh",
        "Image_Openpli-9.0": "wget https://dreambox4u.com/emilnabil237/images/openpli-9.0.sh -O - | /bin/sh",
        "Image_Openpli-9.1": "wget https://dreambox4u.com/emilnabil237/images/openpli-9.1.sh -O - | /bin/sh",
        "Image_OpenPli develop": "wget https://dreambox4u.com/emilnabil237/images/openpli-develop.sh -O - | /bin/sh",
        "Image_openspa-8.4.xxx": "wget https://dreambox4u.com/emilnabil237/images/openspa-8.4.xxx.sh -O - | /bin/sh",
        "Image_Openvix-6.6.004": "wget https://dreambox4u.com/emilnabil237/images/openvix-6.6.004.sh -O - | /bin/sh",
        "Image_OpenVision-py2-10.3-r395": "wget https://dreambox4u.com/emilnabil237/images/openvision/OpenVision-py2-10.3-r395.sh -O - | /bin/sh",
        "Image_Pure2-7.4": "wget https://dreambox4u.com/emilnabil237/images/pure2-7.4.sh -O - | /bin/sh",
        "Image_VTI-15.0.02": "wget https://dreambox4u.com/emilnabil237/images/vti-15.0.02.sh -O - | /bin/sh",
    },
    "Picons": {
        "Picons intelsat_31.5w": "wget https://dreambox4u.com/emilnabil237/picons/intelsat_31.5w/installer.sh -O - | /bin/sh",
        "Picons hispasat_30.0w": "wget https://dreambox4u.com/emilnabil237/picons/hispasat_30.0w/installer.sh -O - | /bin/sh",
        "Picons intelsat_27.5w": "wget https://dreambox4u.com/emilnabil237/picons/intelsat_27.5w/installer.sh -O - | /bin/sh",
        "Picons intelsat_24.5w": "wget https://dreambox4u.com/emilnabil237/picons/intelsat_24.5w/installer.sh -O - | /bin/sh",
        "Picons ses4_22.0w": "wget https://dreambox4u.com/emilnabil237/picons/ses4_22.0w/installer.sh -O - | /bin/sh",
        "Picons nss7_20.0w": "wget https://dreambox4u.com/emilnabil237/picons/nss7_20.0w/installer.sh -O - | /bin/sh",
        "Picons telstar_15.0w": "wget https://dreambox4u.com/emilnabil237/picons/telstar_15.0w/installer.sh -O - | /bin/sh",
        "Picons express_14w": "wget https://dreambox4u.com/emilnabil237/picons/express_14w/installer.sh -O - | /bin/sh",
        "Picons express_11.0w-14.0w": "wget https://dreambox4u.com/emilnabil237/picons/express_11.0w-14.0w/installer.sh -O - | /bin/sh",
        "Picons Nilesat_7W+8W": "wget https://dreambox4u.com/emilnabil237/picons/nilesat/installer.sh -O - | /bin/sh",
        "Picons eutelsat_5.0w": "wget https://dreambox4u.com/emilnabil237/picons/eutelsat_5.0w/installer.sh -O - | /bin/sh",
        "Picons Amos_4.0W": "wget https://dreambox4u.com/emilnabil237/picons/amos_4.0w/installer.sh -O - | /bin/sh",
        "Picons abs_3.0w": "wget https://dreambox4u.com/emilnabil237/picons/abs_3.0w/installer.sh -O - | /bin/sh",
        "Picons thor_0.8w": "wget https://dreambox4u.com/emilnabil237/picons/thor_0.8w/installer.sh -O - | /bin/sh",
        "Picons bulgariasat_1.9e": "wget https://dreambox4u.com/emilnabil237/picons/bulgariasat_1.9e/installer.sh -O - | /bin/sh",
        "Picons eutelsat_3.0e": "wget https://dreambox4u.com/emilnabil237/picons/eutelsat_3.0e/installer.sh -O - | /bin/sh",
        "Picons astra_4.8e": "wget https://dreambox4u.com/emilnabil237/picons/astra_4.8e/installer.sh -O - | /bin/sh",
        "Picons eutelsat_7.0e": "wget https://dreambox4u.com/emilnabil237/picons/eutelsat_7.0e/installer.sh -O - | /bin/sh",
        "Picons eutelsat_9.0e": "wget https://dreambox4u.com/emilnabil237/picons/eutelsat_9.0e/installer.sh -O - | /bin/sh",
        "Picons eutelsat_10.0e": "wget https://dreambox4u.com/emilnabil237/picons/eutelsat_10.0e/installer.sh -O - | /bin/sh",
        "Picons hotbird_13.0e": "wget https://dreambox4u.com/emilnabil237/picons/hotbird_13.0e/installer.sh -O - | /bin/sh",
        "Picons eutelsat_16.0e": "wget https://dreambox4u.com/emilnabil237/picons/eutelsat_16.0e/installer.sh -O - | /bin/sh",
        "Picons astra_19.2e": "wget https://dreambox4u.com/emilnabil237/picons/astra_19.2e/installer.sh -O - | /bin/sh",
        "Picons eutelsat_21.6e": "wget https://dreambox4u.com/emilnabil237/picons/eutelsat_21.6e/installer.sh -O - | /bin/sh",
        "Picons astra_23.5e": "wget https://dreambox4u.com/emilnabil237/picons/astra_23.5e/installer.sh -O - | /bin/sh",
        "Picons eshail_25.5e": "wget https://dreambox4u.com/emilnabil237/picons/eshail_25.5e/installer.sh -O - | /bin/sh",
        "Picons badr_26.0e": "wget https://dreambox4u.com/emilnabil237/picons/badr_26.0e/installer.sh -O - | /bin/sh",
        "Picons astra_28.2e": "wget https://dreambox4u.com/emilnabil237/picons/astra_28.2e/installer.sh -O - | /bin/sh",
        "Picons arabsat_30.5e": "wget https://dreambox4u.com/emilnabil237/picons/arabsat_30.5e/installer.sh -O - | /bin/sh",
        "Picons astra_31.5e": "wget https://dreambox4u.com/emilnabil237/picons/astra_31.5e/installer.sh -O - | /bin/sh",
        "Picons eutelsat-intelsat_33.0e": "wget https://dreambox4u.com/emilnabil237/picons/eutelsat-intelsat_33.0e/installer.sh -O - | /bin/sh",
        "Picons eutelsat_36.0e": "wget https://dreambox4u.com/emilnabil237/picons/eutelsat_36.0e/installer.sh -O - | /bin/sh",
        "Picons hellas-sat_39.0e": "wget https://dreambox4u.com/emilnabil237/picons/hellas-sat_39.0e/installer.sh -O - | /bin/sh",
        "Picons turksat_42.0e": "wget https://dreambox4u.com/emilnabil237/picons/turksat_42.0e/installer.sh -O - | /bin/sh",
        "Picons azerspace_45.0e": "wget https://dreambox4u.com/emilnabil237/picons/azerspace_45.0e/installer.sh -O - | /bin/sh",
        "Picons azerspace_46.0e": "wget https://dreambox4u.com/emilnabil237/picons/azerspace_46.0e/installer.sh -O - | /bin/sh",
        "Picons turksat_50.0e_56.0e_57e": "wget https://dreambox4u.com/emilnabil237/picons/turksat_50.0e_56.0e_57e/installer.sh -O - | /bin/sh",
        "Picons belintersat_51.5e": "wget https://dreambox4u.com/emilnabil237/picons/belintersat_51.5e/installer.sh -O - | /bin/sh",
        "Picons turkmenalem_52.0e": "wget https://dreambox4u.com/emilnabil237/picons/turkmenalem_52.0e/installer.sh -O - | /bin/sh",
        "Picons alyahsat_52.5e": "wget https://dreambox4u.com/emilnabil237/picons/alyahsat_52.5e/installer.sh -O - | /bin/sh",
        "Picons express_53.0e": "wget https://dreambox4u.com/emilnabil237/picons/express_53.0e/installer.sh -O - | /bin/sh",
        "Picons gsat-yamal_54.9e": "wget https://dreambox4u.com/emilnabil237/picons/gsat-yamal_54.9e/installer.sh -O - | /bin/sh",
        "Picons intelsat_60.0e_66.0e_68.0e": "wget https://dreambox4u.com/emilnabil237/picons/intelsat_60.0e_66.0e_68.0e/installer.sh -O - | /bin/sh",
        "Picons intelsat_62.0e": "wget https://dreambox4u.com/emilnabil237/picons/intelsat_62.0e/installer.sh -O - | /bin/sh",
        "Picons eutelsat_70.0e_74.9e_75.0e": "wget https://dreambox4u.com/emilnabil237/picons/eutelsat_70.0e_74.9e_75.0e/installer.sh -O - | /bin/sh",
        "Picons Intelsat_72.1e": "wget https://dreambox4u.com/emilnabil237/picons/Intelsat_72.1e/installer.sh -O - | /bin/sh",
        "Picons abs_75.0e": "wget https://dreambox4u.com/emilnabil237/picons/abs_75.0e/installer.sh -O - | /bin/sh",
    }
}


class PanelStore(Screen):
    skin = """
    <screen name="PanelStore" position="center,center" size="1280,720" title="TAOUFIK SAT PANEL">
        <!-- الهيدر المدمج: TAOUFIK SAT PANEL بخط كبير وواضح -->
        <widget name="header_main" position="20,15" size="320,45" font="Bold;20" halign="center" valign="center" backgroundColor="#b30000" foregroundColor="#ffffff" />
        <widget name="header_right" position="350,15" size="200,45" font="Bold;20" halign="center" valign="center" backgroundColor="#3b3b6d" foregroundColor="#00ffcc" />
        
        <!-- معلومات الجهاز بخط مكبر -->
        <widget name="box_info" position="560,15" size="220,45" font="Regular;17" valign="center" backgroundColor="#111118" foregroundColor="#ffffff" />
        <widget name="cpu_temp_info" position="790,15" size="220,45" font="Regular;17" valign="center" backgroundColor="#111118" foregroundColor="#ffffff" />
        <widget name="ram_flash_info" position="1020,15" size="240,45" font="Regular;16" valign="center" backgroundColor="#111118" foregroundColor="#ffffff" />

        <!-- القائمة الأولى: Categories بخط كبير ومريح للعناوين -->
        <widget name="categories_title" position="20,75" size="360,35" font="Bold;20" foregroundColor="#ff007f" backgroundColor="#111118" />
        <widget name="categories_menu" position="20,115" size="360,500" scrollbarMode="showOnDemand" itemHeight="55" font="Regular;22" backgroundColor="#111118" foregroundColor="#ffffff" foregroundColorSelected="#ffff00" backgroundColorSelected="#2a1b3d" />

        <!-- القائمة الثانية: PACKAGES -->
        <widget name="packages_title" position="400,75" size="520,35" font="Bold;20" foregroundColor="#ff007f" backgroundColor="#111118" />
        <widget name="packages_menu" position="400,115" size="520,500" scrollbarMode="showOnDemand" itemHeight="55" font="Regular;22" backgroundColor="#111118" foregroundColor="#ffffff" foregroundColorSelected="#ffff00" backgroundColorSelected="#005577" />

        <!-- لوحة المعلومات: Information -->
        <widget name="info_title" position="940,75" size="320,35" font="Bold;20" foregroundColor="#ff007f" backgroundColor="#111118" />
        <widget name="info_box" position="940,115" size="320,375" font="Regular;18" backgroundColor="#111118" foregroundColor="#cccccc" />
        <widget name="preview_image" position="940,500" size="320,115" backgroundColor="#1e1e2f" />

        <!-- الأزرار السفلية -->
        <widget name="btn_red" position="20,635" size="180,45" font="Bold;20" halign="center" valign="center" backgroundColor="#b30000" foregroundColor="#ffffff" />
        <widget name="btn_green" position="350,635" size="250,45" font="Bold;20" halign="center" valign="center" backgroundColor="#1b4d3e" foregroundColor="#ffffff" />
        <widget name="btn_yellow" position="680,635" size="250,45" font="Bold;20" halign="center" valign="center" backgroundColor="#b38f00" foregroundColor="#ffffff" />
        <widget name="btn_blue" position="950,635" size="310,45" font="Bold;20" halign="center" valign="center" backgroundColor="#005580" foregroundColor="#ffffff" />
    </screen>
    """

    def __init__(self, session):
        self.session = session
        Screen.__init__(self, session)

        self["header_main"] = Label(f"TAOUFIK SAT {PLUGIN_VERSION}")
        self["header_right"] = Label("TAOUFIK SAT")

        self["box_info"] = Label("Box: DM8000\nOS: ZERO4K")
        self["cpu_temp_info"] = Label("CPU Load: 0.27\nTemp: 65 C")
        self["ram_flash_info"] = Label("RAM: 20% (1029M Free)\nFlash: 8.2 GB Free")

        self["categories_title"] = Label("CATEGORIES")
        self["packages_title"] = Label("PACKAGES")
        self["info_title"] = Label("INFORMATION")

        self.categories = list(STORE_CATEGORIES.keys())
        self["categories_menu"] = MenuList(self.categories)
        self["packages_menu"] = MenuList([])

        self["info_box"] = Label("Section: Plugins\nName: -\nVersion: -\n\nDescription:\nمتجر TAOUFIK SAT PANEL احترافي لإنغما 2 مع شاشة ترمنال مباشرة.")
        self["preview_image"] = Pixmap()

        self["btn_red"] = Label("Exit")
        self["btn_green"] = Label("Install")
        self["btn_yellow"] = Label("Refresh Store")
        self["btn_blue"] = Label("Update Store")

        self["actions"] = ActionMap(
            ["ColorActions", "SetupActions", "OkCancelActions", "DirectionActions"],
            {
                "red": self.close,
                "cancel": self.close,
                "green": self.install_package,
                "ok": self.install_package,
                "yellow": self.refresh_store,
                "blue": self.update_store,
                "up": self.go_up,
                "down": self.go_down,
                "left": self.go_left,
                "right": self.go_right,
            },
            -1
        )

        self.current_focus = "categories"
        self.update_packages()

    def go_up(self):
        if self.current_focus == "categories":
            self["categories_menu"].up()
            self.update_packages()
        else:
            self["packages_menu"].up()
            self.update_info()

    def go_down(self):
        if self.current_focus == "categories":
            self["categories_menu"].down()
            self.update_packages()
        else:
            self["packages_menu"].down()
            self.update_info()

    def go_left(self):
        self.current_focus = "categories"
        self.update_info()

    def go_right(self):
        self.current_focus = "packages"
        self.update_info()

    def update_packages(self):
        cat = self["categories_menu"].getCurrent()
        if cat in STORE_CATEGORIES:
            items = list(STORE_CATEGORIES[cat].keys())
            self["packages_menu"].setList(items)
            self.update_info()

    def update_info(self):
        cat = self["categories_menu"].getCurrent()
        pkg = self["packages_menu"].getCurrent()
        if cat and pkg:
            self["info_box"].setText(f"Section: {cat}\nName: {pkg}\nVersion: Latest\n\nDescription:\nاضغط زر Install أو OK لفتح شاشة التثبيت (Terminal).")

    def install_package(self):
        cat = self["categories_menu"].getCurrent()
        pkg = self["packages_menu"].getCurrent()
        if cat and pkg:
            cmd = STORE_CATEGORIES[cat].get(pkg, "")
            if cmd:
                self.session.open(Console, title=f"Installing: {pkg}", cmdlist=[cmd])

    def refresh_store(self):
        self.session.open(MessageBox, "تم تحديث قوائم المتجر بنجاح!", MessageBox.TYPE_INFO)

    def update_store(self):
        cmd = "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/Ciefp-Panel/Ciefp-Panel.sh -O - | /bin/sh"
        self.session.open(Console, title="Update Panel Store", cmdlist=[cmd])


def Plugins(**kwargs):
    return [
        PluginDescriptor(
            name="TaoufikSatPanel",
            description="TAOUFIK SAT PANEL - Professional Addon Downloader with Terminal",
            where=PluginDescriptor.WHERE_PLUGINMENU,
            icon="icon.png",
            fnc=lambda session, **kwargs: session.open(PanelStore),
        )
    ]
