""" 
Write a program to keep adding a stream of number inputted by useres. 
The adding stops as soon as user presses q key on the keyboard
""" 
#Solve
sum=0
while True:
    userInput=input("Enter the price of item or press q:")
    if userInput!="q":
        sum=sum+int(userInput)
        print(f"Your sum total is {sum}")
    else: 
        print(f"Your sum total is {sum}\n!!THANK YOU!!")    