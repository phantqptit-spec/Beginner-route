S = 'Hello world. Hello everyone, I am Phan'
S1 = 'Hello'
print(S[:S.find(S1)] + S[(S.find(S1) + len(S1)):])
