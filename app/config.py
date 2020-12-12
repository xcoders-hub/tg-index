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
    session_string = "1BVtsOMQBuysvXwTKTYlsi4OnkWR7a5_CLDHUzbX4ZbdocDGCzOevstpsrTBGrDERO_SxHIyPqAjdbRx5ACz1XKOpzhKCaO8iJMgdidcut7oRIXHJ-gR4uLOK79FToWvklBEgNuni2YD8ffU2rgJe54z0Z77RBygrRifHXhHJm77_Pcct2eeoxow-XercU2k6CuJedn6DZ722GOsG-o6zifcN5dIq40Url01eEuw8uRqn-v9gzyHXAUrjiErwTKZbWuz-e9Izxde4xZOZbTmpWI3okqdaAYBIC1dwaBN6nFN5GGswqCMuc0yN7rTla-5OEGtYAvRnqrQq1iz_Bz5epV6KHna-HJU="
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
