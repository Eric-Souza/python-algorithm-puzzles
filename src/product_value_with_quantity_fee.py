print('Welcome to my store! \n')

# Input product value
product_value = float(input('Please set individual product value: '))

# Product quantity
product_quantity = int(input('Please set quantity of products: '))  

# Defines additional value based on quantity
additional_value = 0  

if 0 <= product_quantity < 11:
  additional_value = 30

elif 11 <= product_quantity < 101:
  additional_value = 60

elif 101 <= product_quantity < 1001:
  additional_value = 120

else:
  additional_value = 240

# Total value without counting quantity additional
value_without_additional = float(product_value * product_quantity)  

# Total value with quantity additional
total_value = float(value_without_additional + additional_value)  

# Prints formatted values
print('The value without quantity fee is: $ {:.2f}'.format(value_without_additional))  
print('The value with quantity fee is: $ {:.2f} '.format(total_value) + '(quantity fee of $ {:.2f})'.format(additional_value))