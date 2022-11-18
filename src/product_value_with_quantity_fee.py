
Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Para calcular o valor total que o deve-se levar em consideração o custo de embalagem conforme a tabela abaixo  

Custo de embalagem para frete 

0 <= quantidade < 11 = $30.00 
11 <= quantidade < 101 = $60.00 
101 <= quantidade < 1001 = $120.00 
quantidade >= 1001 = $240.00 

Elabore um programa em Python que: 

Entre com o valor unitário do produto; 
Entre com a quantidade desse produto; 
O programa deve retornar o valor total sem o custo de embalagem para frete; 
O programa deve retornar o valor total após o custo de embalagem para frete; 
Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 1); 
Colocar um exemplo de SAIDA DE CONSOLE de compra de mais de 1000 und.  

##################################################################################################

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