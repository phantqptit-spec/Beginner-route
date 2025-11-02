S = 'I have 8 friends inside my heart. I have 0 friend in life. '
n = ''
S1 = S.split()
item = ',./<>?;:|~!@$%^&*()_\+-='
for i in S1:
    m = i
    for u in item:
        m = m.replace(u,'')
    n += m + ' '
print(n.replace(' ',''))  