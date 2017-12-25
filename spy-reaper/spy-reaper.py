# Author Jamiel & Tyler
import sys
import os

# System sanity checks
if sys.version_info.major < 3:
    sys.stderr.write("Python 3 is required.\n")
    sys.exit(1)

alternate_path = "/opt/twsapi/pythonclient"

try:
    import ibapi
except ImportError:
    try:
        sys.path.append(alternate_path)
        import ibapi
    except ImportError:
        sys.stderr.write("twsapi 973.05 must be installed under a system path or '{0}'\n".format(alternate_path))
        sys.exit(1)

# Import our modules
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir + "/../lib/")
from client import App

def main():
    # Connect to the paper account port
    port = 7497

    client_app = App()
    sys.stderr.write("Connecting to TWS on port '{0}'.\n".format(port))
    client_app.connect("127.0.0.1", port, clientId=0)
    if client_app.error:
        sys.exit(1)

if __name__ == "__main__":
    main()
