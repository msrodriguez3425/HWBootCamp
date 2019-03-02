print("Welcome to the house of Pies! Here are our quesadillas:")

pies = ["Pecan","Apple Crisp","Bean","Banoffee","Black Bun","Blueberry","Buko","Burek","Tamale","Steak"]
for i in range(3):
    print(" ")

print("-------------------------------------------------")

Line = ""
for i in range(10):
    Line = Line + "(" + str(i+1) + ") " + pies[i] + ", "

print (Line)

pieCount = [0,0,0,0,0,0,0,0,0,0]
more = True
pieList = []
while more == True:
    selected = input("Which would you like (number)? ")
    pieCount[int(selected) -1] += 1
    print(f"Great! we'll have that {pies[int(selected)-1]} right out for you.")
    x = input ("Woul you like to make another purchase? (y)es or (n)o")
    if x == "y":
        continue
        #nothing
    else:
        more = False
        print("Your purchases are the following: ")
        for i in range(len(pieCount)):
            if pieCount[i] == 0:
                continue
            else:
                print(f"{pieCount[i]} {pies[i]}") 

        print("Thankyou for your purchases. Goodbye!")


