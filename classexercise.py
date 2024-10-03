#Question one
#The volume of a sphere with radius r is (4/3)*pie*r**2. what is the volume of the sphere with radius 5.
# make sure the program enters the radius from the keyboard and provide  the answer in 2 decimal places.
pie = (22/7)
r = int(input("Enter the radius of the sphere: "))
volume = (4/3)*pie*r**2
print(f"The volume of the sphere is {volume}")


#Question two
#create a program to calculates the area of a triangle (1/2*base*height). 
#base and height should be entered using the keyboard.
base = int(input("Enter the base_value: "))
height = int(input("Enter the height_value: "))
area_of_a_triangle = (1/2*base*height)
print(f"The area of the triangle is {area_of_a_triangle}")


#Question three
#Witi has tasked you to automate a simple grading system. As a python student, write a program used to 
# display the grades that the students will be receiving based on the marks scored in a subject.
#The grades are:
# 90% - 100% Grade is A
# 80% - 89% Grade is B
# 70% - 79% Grade is C
# 60% - 69% Grade is D
# 50% - 59% Grade is E
# < 50% Fail
subject_mark = int(input("Enter your subject mark: "))
if subject_mark >= 90 and subject_mark <= 100:
    print(f"The student grade is A") 
elif subject_mark >= 80 and subject_mark <= 89:
    print(f"The student grade is B")
elif subject_mark >= 70 and subject_mark <=79:
    print(f"The student grade is C")
elif subject_mark >= 60 and subject_mark <= 69:
    print(f"The student grade is D")
elif subject_mark >= 50 and subject_mark <= 59:
    print(f"The student grade is E")
else:
    print("Fail")
    
    
#Question four
#WITI Academy is proposing a Sacco to help students save their money.
# Design a platform that will do the following.
# Welcome to, WITIAcademy Sacco.
# 1. Deposit Money
# 2. Withdraw Money
# 3. Check Balance
# Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
# If the student selects 2, money should be withdrawn and a minimum withdraw is 500.
# If the student selects 3, the account balance should be displayed.
def sacco_transactions():
    
    account_balance = 0
    run = 1
    
    while run == 1:
        print("\n Welcome to, WITIAcademy Sacco.")
        
        #options
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        
        student_choice = int(input("Enter your selected option (1, 2 or 3): "))
        
        #performing a transaction based on the student`s selected option
        
        if student_choice == 1:
            print("\n...processing a deposit transaction...")
            deposit_ammount = int(input("Enter amount to be deposited: "))
            
            #check if deposit amount is less than 1000
            if deposit_ammount < 1000:
                print("\nMinimum deposit is 1000")
                
            else:
                account_balance += deposit_ammount
                
                print(f"deposition of {deposit_ammount:,} confirmed and the current account balance is {account_balance:,}")
            
        
        elif student_choice == 2:
            print("\n...processing a withdraw transaction...")
            withdraw_ammount = int(input("Enter amount to be withdrawn: "))
            
            if account_balance == 0:
                print("Your account balance is 0")
                
            elif withdraw_ammount < 500:
                    print("\n Minimum withdraw amount is 500")
            elif withdraw_ammount > account_balance:
                print(f"Withdraw failed, insuficient funds")
                
            else:
                account_balance =  account_balance -   withdraw_ammount
                print(f"withdraw of {withdraw_ammount:,} confirmed and your current account balance is {account_balance} ")
                    
                    
                
        
        elif student_choice == 3:
            print(f"Your account balance is {account_balance:,}")
        
        else:
            print("You entered a wrong choice, please select 1, 2 or 3\n")
            
            
            
        run = int(input("Enter 1 to continue or any number to exit: "))
        
        if run != 1:
            print("Thank you for using our sacco")
            break
        
sacco_transactions()
        
        
