
# coding: utf-8

# In[2]:

#!/usr/bin/env python

import sys

current_count = 0
spike_count = 0
s1 = 1
current_combo = None
word = None
combo = None

#testl = ["abc.com 1","abc.com 1","abc.com 1","pqr.com 1","pqr.com 1"]

# input comes from STDIN
for line in sys.stdin:
#for line in testl:

    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    speaker, count = line.split()
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    combo = speaker
    if current_combo == combo:
        #current_count_1 = current_count
        current_count += count
        
    else:
        if current_combo:
            
            # write result to STDOUT
            #if current_count > 25000000.0:
            #if spike_count == 2:
            print('%s\t%s' % (current_combo, current_count))
            #spike_count = 0
        current_count = count
        current_combo = combo
# do not forget to output the last word if needed!
if current_combo == combo:
    print('%s\t%s' % (current_combo, current_count))
    


# In[ ]:



