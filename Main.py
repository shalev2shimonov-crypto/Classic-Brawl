import os
import json

# Try to import the server logic, if it fails it will show in the logs
try:
    from Core.Networking.Server import Server
except ImportError:
    print("Error: Could not find Core.Networking.Server. Make sure your files are uploaded correctly.")

class Main:
    def __init__(self):
        # This tells the server which port to use for Render
        self.port = int(os.environ.get("PORT", 9339))

    def start(self):
        print(f"Server is starting on port {self.port}...")
        try:
            # Starting the Brawl Stars server
            server = Server("0.0.0.0", self.port)
            server.start()
        except Exception as e:
            print(f"Server Error: {e}")

if __name__ == "__main__":
    Main().start()
    
