equation = input('')
last = equation[-1]
print(last)

if type(last) == int:
    print('Last index is a number')
else:
    print('Last index is not a number')
