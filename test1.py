line = input()
n = len(line)
newLine = ''

curChar = line[0]
curCount = 1

i = 1

while i < n:
    if curChar != line[i]:
        newLine += curChar + str(curCount)
        curChar = line[i]
        curCount = 1
    else:
        curCount += 1

    i = i + 1
newLine += curChar + str(curCount)

print(newLine)
