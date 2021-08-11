import csv


with open("data.csv",newline="") as f:
    reader= csv.reader(f)
    file_data= list(reader)

numbers = 0
numberofnumbers = len(file_data)
for sum in file_data:
    numbers = numbers+ float(sum[1])

mean= numbers / numberofnumbers
print("mean is: "+ str(mean))

import math 

diffrence= 0
for dif in file_data:
    diffrence =  (diffrence - mean) 

diffrence_squared= diffrence ** 2
print("difference of each number by the mean and squared is: " + str(diffrence_squared))


standard_deviation= math.sqrt(diffrence_squared/ (file_data - 1))
print("standard deviation is: " + str(standard_deviation))










