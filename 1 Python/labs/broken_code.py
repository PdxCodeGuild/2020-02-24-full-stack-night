# The following code is broken in at least six ways. It is your job to fix it. 
# The program is supposed to take a user entered temperature value, a user entered 
# temperature unit, and a unit to convert to, then output the appropriate 
# conversion. The conversions should be correct, I checked them quickly, but 
# I'm fairly sure they're right. At any rate, the main point is to figure out 
# how the code is broken, and fix it.

# We'll use this code in another exercise.

def convert_to_c():
  return ((9 / 5) * temp) + 32

convert_to_f(temp):
  return (5 / 9) * (input_temp - 32)

def main():
  float(input('enter a temperature: '))
  input('enter a unit: ')
  input('enter a unit to convert to: ')

  if convert_to_unit in ('c', 'C'):
    converted_temp = convert_to_f(temp_input)
  elif:
    converted_temp = convert_to_c(temp_input)
  else:
    'no temp entered'
  
  print(converted_temp)