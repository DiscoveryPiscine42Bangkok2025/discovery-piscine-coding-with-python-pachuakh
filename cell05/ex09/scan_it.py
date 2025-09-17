import sys
import re
if len(sys.argv) == 3:
    word = sys.argv[1]
    search_in = sys.argv[2]
    found = re.findall(word,search_in)
    print(len(found))
else:
    print("none")