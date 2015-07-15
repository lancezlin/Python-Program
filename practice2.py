count = 0
total = 0
while True:
    input = raw_input('Enter a number: \n')
    try:
        user_input = int(input)
        count = count + 1
        total = total + user_input
    except:
        if input=='done':
            break
        else:
            print 'Error: Invalid Value!'
            continue
print count, total
