
import sys
import re
# input comes from STDIN (standard input)
#testl = "abc.com 1995-08-20 187"
for line in sys.stdin:
    #remove leading and trailing whitespace
    line = line.strip()
    ip, sd, tots = line.split()
    print('%s\t%s\t%s' % (ip,sd,tots))
    
