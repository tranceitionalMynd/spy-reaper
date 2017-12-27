# Author Jamiel, Tyler, and Michael.
import sys
import os

# System sanity checks
if sys.version_info.major < 3:
    sys.stderr.write("Python 3 is required.\n")
    sys.exit(1)
if os.name == "nt":
    alternate_path = "C:\\TWS API\\source\\pythonclient"
else:
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
        
#TWS API version check, please see if this works.    
tws_api_ver = ibapi.get_version_string()
tws_req_ver = "9.73.2"

if tws_api_ver != tws_req_ver:
    sys.stderr.write("twsapi version '{0}' required, version installed is '{1}'\n".format(tws_req_ver, tws_api_ver))
    sys.exit(1)
                
# Import our modules
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir + "/../lib/")
from client import ClientApp

def main():
    # Connect to the paper account port
    port = 7497

    client_app = ClientApp()
    sys.stderr.write("Connecting to TWS on port '{0}'.\n".format(port))
    client_app.connect("127.0.0.1", port, clientId=0)
    sys.stderr.write("serverVersion:{0}\nconnectionTime:{1}\n".format(client_app.serverVersion(), client_app.twsConnectionTime()))
    sys.stderr.write("Handling incoming messages.\n")
    client_app.run()

if __name__ == "__main__":
    main()
