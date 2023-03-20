def countString(s):
    counter = 0

    for i in range(len(s)):
        if i == 0:
            counter += 1
            continue
            
        if(1 <= int(s[i]) + int(s[i - 1]) <= 26):
            counter += 1
    return counter

print('Return is', countString('111'))