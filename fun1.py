##total = 0
##for number in range(1, 10 + 1):
##    print(number)
##    total = total + number
##print(total)


def add_number():
    total = 0
    for number in range(1, 10 + 1):
        print(number)
        total = total + number
        return(total)
    new_answer=total+10

answer=add_number()
new_answer=answer+8
print(new_answer)
#print(answer)
