def grade_qualifier(grade):
  if grade % 10 > 5 or grade == 100:
    return '+'
  elif grade % 10 < 5:
    return '-'
  else:
    return ''


def main():
  while True:
    user_input = input('enter grade: ')

    if user_input.lower() == 'x' or 'q':
      break

    user_input = round(float(user_input))

    if user_input < 60:
      grade = 'F'
    elif 60 <= user_input <= 69:
      grade = 'D'
    elif 70 <= user_input <= 79:
      grade = 'C'
    elif 80 <= user_input <= 89:
      grade = 'B'
    elif 90 <= user_input <= 100:
      grade = 'A'

    grade += grade_qualifier(user_input)

    print(grade)


main()