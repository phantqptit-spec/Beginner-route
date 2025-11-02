song_line = 'Im on your ark. Answer me, my sinking ship. Where is our tomorrow? Where does our future go?'
u = 0
big = ""
for i in song_line.split():
    if u > len(i):
        continue
    u = len(i)
    big = i
print(big)

