
# coding: utf-8

# In[9]:




# In[ ]:

#!/usr/bin/env python

import sys
import re
# input comes from STDIN (standard input)
#testl = "199.72.81.55 1995-08-20 05:08:01 1995-08-20 05:11:08"
for line in sys.stdin:
    #remove leading and trailing whitespace
    line = line.strip()
    line = line.strip()
#for i in range(1):
#    line = testl.strip()
#    line = testl.strip()
    ip, sd, st, ed, et = line.split()
    h1 =  st[:2]
    st2 = st[3:]
    m1 = st2[:2]
    st3 = st[6:]
    s1 = st3[:2]
    h2 =  et[:2]
    et2 = et[3:]
    m2 = et2[:2]    
    et3 = et[6:]
    s2 = et3[:2]
    h1i = int(h1)
    m1i = int(m1)
    s1i = int(s1)
    h2i = int(h2)
    m2i = int(m2)
    s2i = int(s2)
    hs = (h2i - h1i) * 60 * 60
    ms = (m2i - m1i) * 60
    ss = (s2i - s1i)
    tots = hs + ms + ss
    print('%s\t%s\t%s' % (ip,sd,tots))
    


# In[ ]:



