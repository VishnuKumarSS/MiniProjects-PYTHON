all_scores = input("Input a list of student scores by space: ").split()
for n in range(0, len(all_scores)):
  all_scores[n] = int(all_scores[n])
print(all_scores)

# code for the max() function using for loop
# the below code do the same working of the max() function
maximum=0
for maxx in range(len(all_scores)):
    if all_scores[maxx] > maximum:
        maximum = all_scores[maxx]
print(maximum)