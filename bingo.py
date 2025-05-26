from random import shuffle,choice

shuffle(cpu:=[*range(1,26)])

user = []

bingo_sublist_user = []

bingo_sublist_cpu = []

def user_inp(user_lst,auto = 0):
    if auto == 0:
        x = 1
        while len(user_lst) < 25:
            try:
                temp = int(input(f"Enter number {x}: "))
                if temp in user or 0 >= int(temp) or int(temp) > 25:raise Exception
                user_lst.append(temp)
                x += 1
            except:
                print("Invalid input, try again\n")
        return user_lst
    elif auto:
        user_lst=[*range(1,26)]
        shuffle(user_lst)
        return user_lst
    
def show(lst):
    for x,i in enumerate(lst,start=1):
        if x % 5 == 0:
            print(f"{i}".zfill(4),end="")
            print("")
        else:print(f"{i}".zfill(4),end=" | ")

def cross(num,lst):
    place = lst.index(num)
    lst[place] = f"-{num}-".zfill(4)
    return lst

def check(lst):
    count = 0 
    for i in lst:
        if isinstance(i,str):count += 1
    if count == 5:return True
    return False

def check_bingo(lst,times,sublist):
    if times > 2:
        for j in range(5):
            x , y , xy , yx = [] , [] , [] , []

            for i in range(5):
                x += [lst[5 * j + i]]
                y += [lst[5 * i + j]]
            
            if check(x) and x not in sublist : sublist += [x]
            if check(y) and y not in sublist : sublist += [y]

            xy += [lst[5 * j + j]]
            yx += [lst[5 * j + (4-j)]]

        if check(xy) and xy not in sublist : sublist += [xy]
        if check(yx) and yx not in sublist : sublist += [yx]

def cpu_inp(lst1=cpu):
    while 1:
        inp = choice(lst1)
        if isinstance(inp,int):break
    print(f"Cpu: {inp}")
    cross(inp,lst1)
    cross(inp,user)

def show_bingo(x,y):
    print(f"User: {len(x)} bingos")
    print(f"Cpu: {len(y)} bingos")

def first_bingo(x):
    if len(x) >= 5:
        print("\nBingo Stop")
        return True

def special_inp():
    try:
        temp = int(input("Enter number (1-25) and not already marked: "))
        if temp not in user:raise Exception
        return temp
    except:
        print("Invalid Input, try again")
        return special_inp()

auto = input("Want to use random value?(y/n): ").lower()
if auto in ["yes","y"] : auto = 1
else : auto = 0

user = user_inp(user,auto)

for i in range(1,26) : 

    print("\nYours: ")
    show(user)

    temp = special_inp()

    cross(temp,user)
    cross(temp,cpu)

    check_bingo(user,i,bingo_sublist_user)
    if first_bingo(bingo_sublist_user):
        show(user)
        break

    cpu_inp()
    print()

    check_bingo(cpu,i,bingo_sublist_cpu)
    if first_bingo(bingo_sublist_cpu):
        show(user)
        break

    show_bingo(bingo_sublist_user,bingo_sublist_cpu)
    
show_bingo(bingo_sublist_user,bingo_sublist_cpu)

print("User Won") if len(bingo_sublist_user) > len(bingo_sublist_cpu) else print("CPU Won")

print("\nWant to see CPU's side? (y/n): ",end="")
user = input().lower()
if user in ["yes","y"]:
    show(cpu)
    print("\nSee ya mate!")
else:print("\nSee ya mate!")