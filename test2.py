line = input()
n = len(line)

curChar = line[0]
curCount = 1

maxChar = ''
maxCount = 0
maxChar2 = ''
maxCount2 = 0

i = 1

while i < n:
    if curChar != line[i]:
        if curCount > maxCount:
            maxChar2 = maxChar
            maxCount2 = maxCount
            maxChar = curChar
            maxCount = curCount
        elif curCount > maxCount2:
            maxChar2 = curChar
            maxCount2 = curCount
        curChar = line[i]
        curCount = 1
    else:
        curCount += 1

    i = i + 1


print(maxChar2 * maxCount2)
