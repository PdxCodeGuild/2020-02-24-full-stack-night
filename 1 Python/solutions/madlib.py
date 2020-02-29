from random import choice


def choose(a_list):
  '''
  chooses a random element from a list, removes the element from the list, then returns the random element
  input: takes in a list from which a random element is chosen
  returns: a random element from the list
  depends on: random.choice
'''
  rand_item = choice(a_list)
  a_list.remove(rand_item)
  return rand_item


def main():
  user_input = []

  prompts = [
    '\nGive me an antonym for \'data\': ',
    'Give me a noun: ',
    'Tell me an adjective: ',
    'Give me a sciency buzzword: ',
    'A type of animal (plural): ',
    'Some Sciency thing: ',
    'Another sciency thing: ',
    'Sciency adjective: ',
  ]
  
  while True:
    for prompt in prompts:
      user_input.append(input(prompt))

    madlib = f'\n{choose(user_input)} scientist Job Description: \
      \nSeeking a {choose(user_input)} engineer, able to work on {choose(user_input)} projects with a team of {choose(user_input)}.\
      \nKey responsibilities: \
      \n - Extract patterns from {choose(user_input)} \
      \n - Optimize {choose(user_input)} \
      \n - Transform {choose(user_input)} into {choose(user_input)} material.'

    print(madlib)

    if(input('\nWould you like to make another? (y/n): ').lower() != 'y'):
      print('i don\'t blame you, madlibs are lame.\n')

      break

main()