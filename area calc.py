R = "Rectangle"
C = "Circle"
S = "Square"
Cu = "Cube"
print("Welcome to shape calculator developed by Ankit")
while True:
    li = ["R = Rectangle" , "C = Cricle" , "S = Square" ,"Q = Close calculator"]
    print("Important instructions ! ")
    for i in li:
        print(i)
    while True:
        ans = str(input("Enter a charecter of shape :- "))
        conv1 = ans.lower()
        # code for rectangle
        if (conv1 == "r"):
            
            print("Your selected shape is " , R)
            while True:
                ans1 = str(input("Do you want to proceed 'Yes' or 'No' " ))
                conv2 = ans1.lower()
                if (conv2 == "yes"):
                    try:
                        base = int(input("Enter value of base :- "))
                        height = int(input("Enter value of height :- "))
                        A = base*height
                        print("Area of ",R ,"is :-", A)
                    except:
                        print("Please enter numeric vaue.................!")
                if (conv2 == "no"):
                    print("Do you want to exit?")
                    break

    # code for circle
        elif (conv1 == "c"):
            print("Your selected shape is " , C)
            while True:
                ans2 = str(input("Do you want to proceed 'Yes' or 'No' " ))
                conv3 = ans2.lower()
                if (conv3 == "yes"):
                    try:
                        radius = int(input("Enter value of radius :- "))
                        A = 3.14*(radius**2)
                        print("Area of ",C ,"is :-", A)
                    except:
                        print("Please enter numeric vaue.................!")
                if (conv3 == "no"):
                    print("Do you want to exit?")
                    break
    # code for square
        elif (conv1 == "s"):
            print("Your selected shape is " , S)
            while True:
                ans3 = str(input("Do you want to proceed 'Yes' or 'No' " ))
                conv4 = ans3.lower()
                if (conv4 == "yes"):
                    try:
                        base = int(input("Enter value of base :- "))
                        A = base**2
                        print("Area of ",S ,"is :-", A)
                    except:
                        print("Please enter numeric vaue.................!")
                if (conv4 == "no"):
                    print("Do you want to exit?")
                    break
        if (ans == ""):
            print("!Please enter a value")
        if (ans == "q"):
            print("Good bye.......")
            break
