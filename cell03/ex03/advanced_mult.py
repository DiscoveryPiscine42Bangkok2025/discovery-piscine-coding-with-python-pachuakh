import sys
if len(sys.argv) > 1:
    print("none")
    sys.exit()
table = 0
while table <= 10:
    line = f"Table de {table}"
    i = 0
    while i <= 10:
        line += f" {table * i}"
        i += 1
    print(line)
    table += 1