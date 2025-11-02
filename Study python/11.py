S = 'Number 1 is better than 2. Why? Cause who would want to be number 2?'
sum = 0
if '1' in S:
    sum += 1 * S.count('1')
    for i in range(S.count('1')):
        print("1")
if '2' in S:
    sum += 2 * S.count('2')
    for i in range(S.count('2')):
        print("2")
if '3' in S:
    sum += 3 * S.count('3')
    for i in range(S.count('3')):
        print("3")
if '4' in S:
    sum += 4 * S.count('4')
    for i in range(S.count('4')):
        print("4")
if '5' in S:
    sum += 5 * S.count('5')
    for i in range(S.count('5')):
        print("5")
if '6' in S:
    sum += 6 * S.count('6')
    for i in range(S.count('6')):
        print("6")
if '7' in S:
    sum += 7 * S.count('7')
    for i in range(S.count('7')):
        print("7")
if '8' in S:
    sum += 8 * S.count('8')
    for i in range(S.count('8')):
        print("8")
if '9' in S:
    sum += 9 * S.count('9')
    for i in range(S.count('9')):
        print("9")
if '0' in S:
    for i in range(S.count('0')):
        print('0')
for i in range(10):
    if str(i) in S:
        print(sum)
        break
else:
    print("Come on, I'm so tired!")