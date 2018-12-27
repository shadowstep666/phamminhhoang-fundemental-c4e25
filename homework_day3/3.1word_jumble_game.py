from random import randint

word ="champion"
letter=list(word)

for i in range(len(letter)):
    b = randint(0,len(letter)-1)
    tu=letter[b]
    print(tu,end=" ")
    letter.pop(b)
print()

answer = input(" your answer: ")
while True :
    if answer != word :
        print(":(")
        answer = input(" your answer: ")
    else :
        print("hura")
        break

