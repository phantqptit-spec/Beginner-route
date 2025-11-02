print("Presentaion:")
print('Hello, i am Phan', 'Im 18 years old', 'How are u today', sep='.', end='.\n')
question = input('What about you? Put the answer here:')
print('I am an introvert', 'I love playing game, i think', sep=' by the way ', end='?\n')
print(question, flush=True)

n = int(input('Enter a number:'))
n += 5
if n % 3 == 0:
    print('congrat u have the lucky number')
else :
    print('Too bad try again')