"""
Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of
the numbers. If the user enters anything other than a number, detect their mistake
using try and except and print an error message and skip to the next number.
"""
count = 0
total = 0
avg = None
while True:
    input = raw_input('Enter a number: \n')
    try:
        user_input = int(input)
        count = count + 1
        total = total + user_input
        avg = total/count
    except:
        if input=='done':
            break
        else:
            print 'Error: Invalid Value!'
            continue
print count, total, avg
