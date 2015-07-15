'''
Rewrite your pay computation to give the employee 1.5 times the
hourly rate for hours worked above 40 hours.
'''
inputHour = raw_input('Enter Hours: \n')
inputRate = raw_input('Enter Rate: \n')
try:
  Hour = int(inputHour)
  Rate = float(inputRate)
  if Hour <= 40:
    Pay = Hour*Rate
  else:
    Pay = (Hour-40) * Rate * 1.5 + 40 * Rate
  print Pay
except:
  print 'Error. Please enter a number.'
