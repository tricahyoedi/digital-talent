temp = eval (input ('Enter a temperature in Celcius: '))
f_temp = 9/5*temp+32
print ('In Fahrentheit, that is ', f_temp)
if f_temp > 212:
    print ('That is above the boiling point.')
if f_temp < 212:
    print ('That is below the boiling point.')
