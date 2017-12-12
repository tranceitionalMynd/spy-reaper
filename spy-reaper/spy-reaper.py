from __future__ import (absolute_import, division, print_function,)
#                        unicode_literals)

import collections
import sys

if sys.version_info.major == 2:
    sys.stderr.write("Python 2 is not supported.\n")
    sys.exit(1)

try:
    import ibapi.order_condition
except ImportError:
    sys.path.append("/opt/ibapi-beta/pythonclient")
    import ibapi.order_condition
from ibapi.order import (OrderComboLeg, Order)
from ibapi.common import *
from ibapi.tag_value import TagValue
from ibapi import order_condition
from ibapi.order_condition import *


