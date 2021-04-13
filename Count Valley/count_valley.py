def countingValleys(n, steps):
    altitude = valleys = 0

    for step in steps:
        #print (step)
        altitude += 1 if step == 'U' else -1
        if altitude == 0 and step == 'U':
            valleys += 1
    return valleys
""" 
 altitude += 1 if step == 'U' else -1 
 
 is equal to:
 
 if step == "U":
    
    altitude += 1
 
 else:
    
    altitude += 1
 
 
 
"""



steps = 10
path = "DUDDDUUDUU"

print(countingValleys(steps,path))
