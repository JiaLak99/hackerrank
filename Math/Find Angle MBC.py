from math import *

leg1 = input()
leg2 = input()

print str(int(round(degrees(atan2(leg1, leg2))))) + u"\u00b0"
