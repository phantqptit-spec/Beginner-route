colour = input('What is your favourite colour? Write the answer here: ')
def answer():
    print ("So your favourite colour is", colour)
repeattime = int(input("The number of time u want to repeat the answer:"))
for a in range(repeattime):
    answer()
if colour.lower() == "yellow":
    print ("That is also my favourite colour")
