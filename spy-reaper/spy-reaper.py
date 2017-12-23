from __future__ import (absolute_import, division, print_function,)
#                        unicode_literals)

import collections
import sys

# System sanity checks
if sys.version_info.major == 2:
    sys.stderr.write("Python 2 is not supported.\n")
    sys.exit(1)

try:
    import ibapi.order_condition
except ImportError:
    try:
        sys.path.append("/opt/ibapi-beta/pythonclient")
        import ibapi.order_condition
    except ImportError:
        sys.stderr.write("twsapi 973.05 must be installed under a system path or '/opt/ibapi-beta/pythonclient'\n")
        sys.exit(1)

# Import remaining IB API modules
from ibapi.order import (OrderComboLeg, Order)
from ibapi.common import *
from ibapi.tag_value import TagValue
from ibapi import order_condition
from ibapi.order_condition import *

def main():
    pass

if __name__ == "__main__":
    main()
