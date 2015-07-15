inputHour = raw_input('Enter Hours: \n')
inputRate = raw_input('Enter Rate: \n')
try:
  Hour = int(inputHour)
  Rate = float(inputRate)
  if Hour <= 40:
    Pay = Hour*Rate
  else:
    Pay = Hour * Rate * 1.5
  print Pay
except:
  print 'Please enter a number.'
