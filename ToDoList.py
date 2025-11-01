#TO DO LIST APPLICATION
print("-----TO DO LIST APPLICATION-----")
ml=[]

while True:
    print("1.New\t2.Open\t3.Update\n4.View\t5.Exit")
    ch=int(input("Enter your choice(1-5):"))
    match ch:
        case 1:
            l=[]
            H=input("Heading:")
            n=int(input("No of items:"))
            for i in range(n):
                item=input(f"{i+1}.")
                l.append(item)
            ml.append(l)    
        case 2:
            for i in range(len(ml)):
                print(i+1,".",ml[i])
            ln=int(input("Enter List No: "))
            for x in range(len(ml)):
                if x == ln-1:
                    print("---LIST ITEMS---")
                    for item in ml[x]:
                        print(item)
                    print("------------------------")
                    print("1.Add\n2.Remove")
                    oc=int(input("Enter your choice(1-2):"))
                    match oc:
                        case 1:
                            n=int(input("No of items:"))
                            for i in range(n):
                                item=input(f"{i+1}.")
                                ml[x].append(item)
                        case 2:
                            item=input("Enter remove Item Name:")
                            ml[x].remove(item)
                        case _:
                            print("Wrong input")
                else:
                    print("List not found")
        case 3:
            print("1.Add\n2.Remove\n3.Replace")
            oc=int(input("Enter your choice(1-3):"))
            match oc:
                case 1:
                    n=int(input("No of items:"))
                    for i in range(n):
                        tem=input(f"{i+1}.")
                        l.append(item)
                case 2:
                    item=input("Enter remove Item Name:")
                    l.remove(item)
                case 3:
                    old=input("Enter old value:")
                    New=input("Enter new value:")
                    l.insert(l.index(old),New)
                    l.remove(old)
                case _:
                    print("Wrong input")
        case 4:
            print("---LIST ITEMS---")
            print("------------------------\n",H.upper(),"\n------------------------")
            for item in l:
                print(item)
            print("------------------------")
        case 5:
            break
        case _:
            print("Wrong input")
            break