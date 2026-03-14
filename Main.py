from Core.Networking.Server import Server
import json  # meh

from Utils.Updater import Updater


class Main:
    def __init__(self):
        self.crashCount: int = 0
        self.configuration = json.loads(open("config.json", "r").read())
        self.useUpdater = self.configuration.get("UpgradesEnabled", False)
        self.main()
        self.updater: Updater = None

def main(self):
import os
        port = int(os.environ.get("PORT", 9339))
        try:
            print("Server starting...")
            Server("0.0.0.0", port).start()
        except Exception as e:
            print(f"Encountered exception: {e}")
            if self.crashCount >= 2:
                exit()
            self.crashCount += 1
            self.main()

if __name__ == '__main__':
    Main().main()
                
