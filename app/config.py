from pathlib import Path
import traceback
import json
import sys
import os


try:
    port = 8080
except ValueError:
    port = -1
if not 1 <= port <= 65535:
    print("Please make sure the PORT environment variable is an integer between 1 and 65535")
    sys.exit(1)

try:
    api_id = 1064864
    api_hash = "5f3eeab0e6108731551e6a93598b654c"
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    index_settings = {
      "index_all": True,
      "index_private":True,
      "index_group": True,
      "index_channel": True,
      "exclude_chats": [],
      "include_chats": "4A5pMG3S58mBQL",#my index chat
      "otg": {
          "enable": True,
          "include_private": True,
          "include_group": True,
          "include_channel": True
      }
    }
    otg_settings = index_settings['otg']
    enable_otg = otg_settings['enable']
except:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

try:
    session_string = "1BVtsOGYBuwI7Rr9EdRanpfkCgxwBHxwsiM2p0btW4tT48o7K7LH-tkyNkUMwbLZdAUhkmsMZg3jnlZvrj8Du1840GeDU3lgLovy-QiddtehPcSIIMvPqnsDAup2sRmT9bUynp0tlEuLgBecpaytQgcZDYrcVffs_5ipssogOXFJqDNbx6CUWvR44SBMJUvkAJqNC2BNI9PCyQyW4qJIdbqiFVUmoMT0GCI-12EOfuYIzNZ08OVP8paBRZcciIabV2gw_sYoS2IZQMJ2n4sfyedJdi2DQFYjydys8s6QrJ3ZN_Sw2OVLYEYdqy6Iib1pa8PgfOMOy13kEnS_cuaNfUuB9SSdMZ2U="
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

host = "162.241.87.250"
debug = bool(os.environ.get("DEBUG"))
block_downloads = bool(os.environ.get("BLOCK_DOWNLOADS"))
results_per_page = int(os.environ.get("RESULTS_PER_PAGE", "20"))
logo_folder = Path('logo/')
logo_folder.mkdir(exist_ok=True)
