import sys
#Jamiel & Tyler 3
# System sanity checks
if sys.version_info.major < 3:
    sys.stderr.write("Python 3 is required.\n")
    sys.exit(1)

try:
    import ibapi
except ImportError:
    try:
        sys.path.append("/opt/ibapi-beta/pythonclient")
        import ibapi
    except ImportError:
        sys.stderr.write("twsapi 973.05 must be installed under a system path or '/opt/ibapi-beta/pythonclient'\n")
        sys.exit(1)

def main():
    pass

if __name__ == "__main__":
    main()
