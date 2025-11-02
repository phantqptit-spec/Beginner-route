print(5+5)
x = 4
y = 5
sum = x + y + x * y * 8
print(sum)
fnumber = (1, 4, 18, 19, 3)
for i in fnumber:
    print(i * i)
pet1 = ('dog', 'cat')
for m in pet1:
    for n in m:
        print(n)
N = 89 ** 4.0
print(N)
M = 'Big' + ' dog'
print(M)
print(len('Phạm '))
mumber = "-10"
print('Hi I am', str(abs(int(mumber)-8)), '.Nice to meet you.') # im using int to make -10 a number then -10-8 for -18. After that using abs to make it 18 and str to make it a word and done
letter = 'Well look like I will do this until 12:45'
print(letter[-7:5:-1])
truth = input("What is one thing that I want than all, love than all but further than all? Answer here:").strip().lower()
if truth == "friendship":
    print("U are right. Thanks for understand.")
else:
    print("Wrong. But I can understand why no one will find out.")