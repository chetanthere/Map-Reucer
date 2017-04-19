
import sys
import re
# input comes from STDIN (standard input)
#testl = ["abc.com 1","abc.com 1","pqr.com 1"]
for line in sys.stdin:
    #remove leading and trailing whitespace
    line = line.strip()
    ip, tots = line.split()
    print('%s\t%s' % (ip,tots))
    



