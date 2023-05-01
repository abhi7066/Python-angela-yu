std_heights = [45,75,32,21,43,4,4,76,73,23,23]
tot_sum=0
for x in std_heights:
    tot_sum+=x

print("Average age is ",round(tot_sum/len(std_heights),2))