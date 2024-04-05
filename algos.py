#function to get the min max and average of a given list
def MinMaxAvg(lst):
    min = None
    max = None
    sum = 0
    tmp = []
    for i in lst:
        if min == None or i < min:
            min = i
        if max == None or i > max:
            max = i
        sum += i
    avg = sum / len(lst)
    tmp.append(min)
    tmp.append(max)
    tmp.append(int(avg))
    return(tmp)

print(MinMaxAvg([1,2,3,4,5]))
print(MinMaxAvg([1,6,3,0,9,22,5,6]))

#function that tells you if the length of your list is odd or even
def oddOrEvenList(oddevenlst):
    if len(oddevenlst) % 2 != 0:
        return "odd"
    elif len(oddevenlst) %2 == 0:
        return "even"
    else:
        print("you messed something up")
print(oddOrEvenList([1,2,3,4]))
print(oddOrEvenList([1,2,3]))

#function that returns true if a users birthday is passed, false if not. Also prints how old user is
def is_past(birthday, today):
    if (int(birthday[:2]) < int(today[:2])):
        print("user is currently",int(today[6:]) - int(birthday[6:]), "years old")
        return True
    elif(int(birthday[:2]) > int(today[:2])):
        print("user is currently",int(today[6:]) - int(birthday[6:]) - 1, "years old")
        return False
    elif(int(birthday[3:5]) > int(today[3:5])):
        print("user is currently",int(today[6:]) - int(birthday[6:]) - 1, "years old")
        return False
    else:
        print("user is currently",int(today[6:]) - int(birthday[6:]), "years old")
        return True


print(is_past("10/26/1993", "12/07/2022"))
print(is_past("12/26/1993", "12/07/2022"))
print(is_past("12/05/1991", "12/07/2022"))