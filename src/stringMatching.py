#contents = []
import re
#i = 0
with open('gene.txt') as f:
    lines = f.readlines()
    i = 1
    sizeOflines = len(lines)
    while i < sizeOflines:
        # print(lines[i])
        fullString = lines[i]
        i += 1
        sub = lines[i]
        print(fullString)
        print(sub)
        i += 1
        for match in re.finditer('sub','fullString'):
            print(match.start())
        #[m.start() for m in re.finditer('sub', 'fullString')]
                                                                        
