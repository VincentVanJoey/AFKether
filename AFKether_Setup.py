import wx
import os
import sys
import json
import subprocess

def get_config_path():
    # Get user's Documents folder
    if sys.platform == "win32":
        documents_folder = os.path.join(os.environ["USERPROFILE"], "Documents")
    else:
        documents_folder = os.path.join(os.path.expanduser("~"), "Documents")

    # Create AFKether folder inside Documents
    afkether_folder = os.path.join(documents_folder, "AFKether")
    if not os.path.exists(afkether_folder):
        os.makedirs(afkether_folder)

    # Define the config file path
    return os.path.join(afkether_folder, "config.json")

def open_config(config_path):
    if os.name == 'nt':  # Windows
        os.system("start " + config_path)
    elif os.name == 'posix':  # macOS or Linux
        os.system("open " + shlex.quote(config_path))

def write_to_config(config_path, key, value):
    config = {}
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                config = json.load(f)
        except Exception:
            config = {}
    config[key] = value
    with open(config_path, "w") as f:
        json.dump(config, f)

def read_from_config(config_path, key):
    if not os.path.exists(config_path):
        return None
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        return config.get(key, None)
    except Exception:
        return None

#region vigem related methods

def check_vigem_installed():
        config_path = get_config_path()
        if read_from_config(config_path, "vigem_installed"):
            return  # Already installed, do nothing

        dlg = wx.MessageBox("Do you need to install the ViGEm Driver?"
                            "\n(You need it for the program to work, may have to restart machine if installing for the first time)"
                            ,"Install Needed Driver?", wx.YES_NO | wx.CANCEL | wx.ICON_INFORMATION)
        if dlg == wx.YES:
            install_vigem()
            write_to_config(config_path, "vigem_installed", True)
        elif dlg == wx.NO:
            # moves on to the app
            write_to_config(config_path, "vigem_installed", True)
        else:
            sys.exit(1)

def install_vigem():
    if getattr(sys, 'frozen', False):
        # Running as a PyInstaller EXE
        installer_path = os.path.join(sys._MEIPASS, "ViGEmBus_1.22.0_x64_x86_arm64.exe")
    else:
        # Running as a script
        installer_path = os.path.join(os.path.dirname(__file__), "ViGEmBus_1.22.0_x64_x86_arm64.exe")
    subprocess.call([installer_path])

#endregion