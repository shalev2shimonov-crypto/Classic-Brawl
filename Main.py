import os
import json
from Core.Networking.Server import Server
from Utils.Updater import Updater

class Main:
    def __init__(self):
        self.crashCount = 0
        try:
            with open("config.json", "r") as f:
                self.configuration = json.loads(f.read())
        except:
            self.configuration = {}
        self.useUpdater = self.configuration.get("UpgradesEnabled", False)
        self.updater = None

    def main(self):
        port = int(os.environ.get("PORT", 9339))
        try:
            print(f"Server starting on port {port}...")
            Server("0.0.0.0", port).start()
        except Exception as e:
            print(f"Encountered exception: {e}")
            if self.crashCount < 2:
                self.crashCount += 1
                self.main()
            else:
                print("Too many crashes, exiting.")
                exit()

if __name__ == '__main__':
    Main().main()
