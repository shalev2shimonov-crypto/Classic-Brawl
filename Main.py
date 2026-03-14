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
                    # TODO: Close all connections so that the server gets a bit faster on fixing stuff
                    req = "yes" in input("The server has crashed 2+ times."
                                         " Would you like to check for updates in case there's a fix? ").lower()
                    if req: self.main()

                updaterRollbackRequest: bool = "yes" in input(
                    f"The Updater has detected that the server is in a crashed state (error: {e}).\n"
                    "Would you like to roll-back the update? ").lower()

                if updaterRollbackRequest:
                    self.updater.performRollback()
                    print("The roll-back has been completed successfully!")
                    self.crashCount = 0
                else:
                    print("Request declined. Restarting server...\n")

                self.main()


if __name__ == '__main__':
    Main()
