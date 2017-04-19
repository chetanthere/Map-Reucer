
import sys

current_count = 0
spike_count = 0
s1 = 1
current_combo = None
word = None
combo = None

#testl = ["abc.com 1995-08-20 2","abc.com 1995-08-21 3","abc.com 1995-08-22 7","abc.com 1995-08-23 15","pqr.com 1995-08-23 55",
#        "pqr.com 1995-08-23 120","pqr.com 1995-08-23 550"]


for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    speaker, word, count = line.split()
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently discard this line        
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    combo = speaker
    if current_combo == combo:
        current_count_1 = current_count
        current_count = count
        #current_count_2 += count_1   
        if current_count >= (2 * current_count_1) :
            spike_count += 1            
        else:
            spike_count = 0            
        if spike_count == 2:
                print('%s\t%s' % (current_combo, s1))
                spike_count = 0
    else:
        if current_combo:
            # write result to STDOUT
            #if current_count > 25000000.0:
            #if spike_count == 2:
            #    print('%s\t%s' % (current_combo, s1))
            spike_count = 0
        current_count = count
        current_combo = combo
# the last word if needed!
if current_combo == combo:    
    if spike_count == 2:
        print('%s\t%s' % (current_combo, s1))
    

