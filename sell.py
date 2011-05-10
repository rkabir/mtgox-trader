#!/usr/bin/env python

import sys

from mtgox import MTGox
import settings

if len(sys.argv) in (2, 3):
    amount = sys.argv[1]
    ask = sys.argv[2] if len(sys.argv) == 3 else None
else:
    print "Usage: %s <amount> [ask]" % sys.argv[0]
    exit(1)

mtgox = MTGox(user=settings.MTGOX_USER, password=settings.MTGOX_PASSWORD)
status = mtgox.sell_btc(amount=amount, price=ask)
print status
