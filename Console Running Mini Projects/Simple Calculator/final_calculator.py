from calc_logo import logo

import sys
sys.path.append("C:\VScode_workspace\python_vscode") # these two lines is to add the temporary directory to import the clear module from another folder or outside folder.

from clear import clear


# defining functions
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
operations={
    "+":addition,
    "-":subtraction,
    "*":multiplication,
    "/":division,
}
print(logo)
def main():
    a=float(input("Enter the first number: "))
    for i in operations: # to print all the operators
        print(i)

    action=input("Enter an operator to perform: ")
    b=float(input("Enter the second number: "))

    calc_function=operations[action]
    answer = calc_function(a,b) # this function acts depending upon the corresponding operations.

    print(f"{a} {action} {b} = {answer}")


    end_flag = True # this method is called as Flag
    while end_flag:
        end=input("""Enter 
'y' to continue 'n' to start the new calculation
'exit' to exit the calculator:  """).lower()
        if end =="n":
            clear()
            print(logo)
            print(f"The TOTAL of last calculation is: {answer}")
            print()
            print("New Calculation: ")
            main()
            break
        elif end=="exit":
            clear()
            print(logo)
            print(f"The TOTAL of last calculation is: {answer}")
            print()
            print("Exited.")
            end_flag = False
            break
        elif end!="y":
            print("Invalid Input.")
            continue
            # end_flag=False
            # break
        if end_flag == True:
            action=input("Enter an operator to perform: ")
            calc_function=operations[action]
            c=float(input("Enter the next number: "))
            old_answer=answer
            answer=calc_function(answer,c) # here we should use first argument as ----- first_answer
                                                        # we should not use the calc_function in the place of first_answer....it will make the code to execute wrong.
            print(f"{old_answer} {action} {c} = {answer}")

main()