
import sys

current_count = 0
current_combo = None
word = None
combo = None

#testl = ["abc.com 1995-08-20 2","abc.com 1995-08-20 3","abc.com 1995-08-20 7","abc.com 1995-08-23 15","pqr.com 1995-08-23 55",
#        "pqr.com 1995-08-23 120","pqr.com 1995-08-23 550"]

# input comes from STDIN
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
    combo = speaker + word
    if current_combo == combo:
        current_count += count
    else:
        if current_combo:
            # write result to STDOUT                      
            print('%s\t%s\t%s' % (current_ip, current_dt,current_count))
            current_ip = speaker
            current_dt = word
        current_count = count
        current_combo = combo
        current_ip = speaker
        current_dt = word
        
# the last word if needed!
if current_combo == combo:    
    print('%s\t%s\t%s' % (current_ip, current_dt,current_count))




