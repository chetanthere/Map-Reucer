
# coding: utf-8

# In[2]:




# In[ ]:

#!/usr/bin/env python

import sys
import re
# input comes from STDIN (standard input)
#testl = ["abc.com 1","abc.com 1","pqr.com 1"]
for line in sys.stdin:
#for line in testl:
    #remove leading and trailing whitespace
    line = line.strip()
#for i in range(1):
#    line = testl.strip()
    ip, tots = line.split()
    print('%s\t%s' % (ip,tots))
    


# In[ ]:



