import re
file=open("regex_sum_634688.txt")
nums=[]
temp=[]
for line in file:
    y=re.findall("[0-9]+",line)
    nums.append(y)
for i in nums:
    for j in i:
        temp.append(int(j))
sum=0
for k in temp:
    sum+=k
print(sum)


