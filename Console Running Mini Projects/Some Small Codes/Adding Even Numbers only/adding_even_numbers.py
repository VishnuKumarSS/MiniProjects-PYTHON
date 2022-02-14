# adding even numbers from 1 to 100

total1 = 0
n = int(input("Enter the number until you want to calculate: "))
for i in range(1,n+1):
    if i % 2 == 0:
        total1+=i
        print(i,end=" ") # to know whats happening
print()
print("TOTAL1 : ",total1)
print("\n")
# or 
# total2=0
# for i in range(2,100+1,2):
#     total2+=i
#     print(i,end=" ")
# print()
# print("TOTAL2 : ",total1)