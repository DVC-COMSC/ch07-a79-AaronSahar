
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


rnum = len(numbers)
cnum = len(numbers[0])

print ('Sum of rows: ', end=' ')
for i in range(rnum):
	rsum = sum(numbers[i])
	print (rsum, end=' ')
print()

print ('Sum of columns: ', end=' ')
for i in range(cnum):
    csum = 0
    for j in range(rnum):
        csum += numbers[j][i]
    print (csum, end=' ')
print()

print ('The row that has the greatest sum: ', end=' ')
if sum(numbers[0]) > sum(numbers[1]) and sum(numbers[0]) > sum(numbers[2]):
    print('0')
elif sum(numbers[1]) > sum(numbers[0]) and sum(numbers[1]) > sum(numbers[2]):
    print('1')
else:
    print('2')

print ('The greatest number: ', end=' ')
greatest = 0
for i in range(cnum):
    for j in range(rnum):
        if numbers[j][i] > greatest:
            greatest = numbers[j][i]
print(greatest)





# ******************************
# Make your Code
# ******************************
