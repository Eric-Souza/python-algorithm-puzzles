def house_square_meters():
  print('-'*20, 'Menu 1/3 - House Square Meters','-'*20)

  while True:
    try:
      square_meters = int(input('Input the house\'s square meters: '))

      if (square_meters >= 30) and (square_meters <= 300):
        return 60 + 0.3 * square_meters

      elif (square_meters >= 300) and (square_meters <= 700):
        return 120 + 0.5 * square_meters

      else:
        print('We don\'t accept houses with less than 30m² or more than 700m²!')
        continue

    # If user types in floating values or letters
    except ValueError:
      print('!'*20, 'Non integer values are invalid','!'*20)

def cleaning_type():
  print('-'*20, 'Menu 2/3 - Cleaning Type', '-'*20)

  while True:
    clean_type = input(
      'Pick the cleaning type: \n'+
      'B - Basic - For weekly or bi-weekly cleaning \n' +
      'C - Complete - For old dirty spots and/or non-routine cleaning \n' +
      'Input the desired option: '
    )

    clean_type = clean_type.lower()
    clean_type = clean_type.strip()

    if clean_type == 'b':
      return 1.00

    elif clean_type == 'c':
      return 1.30

    else:
      print('!'*30 , 'Invalid Option', '!'*30)
      continue

def cleaning_additional():
  print('-'*20, 'Menu 3/3 - Additional Cleaning', '-'*20)

  counter = 0

  while True:
    clean_additional = input(
      'Do you wish for another additional cleaning? \n' +
      '0 - I don\'t wish for anything else (Finish) \n' +
      '1 - Iron 10 pieces of clothing - $ 10.00 \n' +
      '2 - Furnace/micro-wave cleaning - $ 12.00 \n' +
      '3 - Fridge/freezer cleaning - $ 20.00 \n' +
      'Input the desired option: '
    )

    if clean_additional == '0':
      return counter

    elif clean_additional == '1':
      counter = counter + 10
      continue

    elif clean_additional == '2':
      counter = counter + 12
      continue

    elif clean_additional == '3':
      counter = counter + 20
      continue

    else:
      print('!'*30,'Invalid Option', '!'*30)

# Menu templates
def template_border(s1):
  template_size = len(s1)

  if template_size:
    print('+','-' * template_size, '+')
    print('|', s1, '|')
    print('+','-' * template_size, '+')

template_border('          Welcome to my cleaning service!          ')
print('*'*100)

# Main function
house_size_value = house_square_meters()
print(house_size_value)

cleaning_type_value = cleaning_type()
print(cleaning_type_value)

cleaning_additional_value = cleaning_additional()
print(cleaning_additional_value)

total_value = (house_size_value * cleaning_type_value) + cleaning_additional_value

print('Total value: $ {:.2f} (House size: $ {:.2f} + Cleaning type $ {:.2f} + Additional cleaning $ {:.2f})' .format(total_value, house_size_value, cleaning_type_value, cleaning_additional_value))