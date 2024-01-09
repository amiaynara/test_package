

def get_inputs():
  '''Method to get inputs from the user'''
  answer = ['yes', 'y']
  wants_to_continue = 'yes' 
  inputs = []
  while wants_to_continue in answer:
    try:
      user_input = int(input('Enter an integer: '))
      inputs.append(user_input) 
    except Exception as error:
      print('Try again. The input is not acceptable, please feed a valid number.')
      print(error)
      continue
    wants_to_continue = input('Do you want to enter more integers? (y/n):')
  return inputs

def show_results(result):
  '''Method to show the result to the user'''
  print('The answer is: ', result)

def pretty_print(result):
  '''Method to show the result in a fancy way'''
  print('*' * 80)
  print('The result of the operation is: ', result)
  print('*' * 80)
