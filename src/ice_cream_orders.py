print('Welcome to my ice cream store! \n')

# Table template
print('*********************************** Menu **************************************')
print('|_____________________________________________________________________________|')
print('|   Code   |      Description     |     Size S    |   Size M   |   Size L     |')
print('|          |                      |     500 ML    |   1000 ML  |   2000 ML    |')
print('|   "TR"   | Traditional Flavors  |   $   6,00    |  $  10,00  |  $  18,00    |')
print('|   "SP"   |   Special Flavors    |   $   7,00    |  $  12,00  |  $  21,00    |')
print('|   "PR"   |   Premium Flavors    |   $   8,00    |  $  14,00  |  $  24,00    |')
print('|_____________________________________________________________________________| \n')

available_sizes = ["S", "M", "L"]
available_codes = {"TR": [6.00, 10.00, 18.00], "SP": [7.00, 12.00, 21.00], "PR": [8.00, 14.00, 21.00]}

request_array = []

# Data input
while True:
    chosen_size = input("Select ice cream size ")
    chosen_code = input("Select ice cream code ")

    if chosen_size in available_sizes and chosen_code in available_codes:
        request = available_codes[chosen_code][available_sizes.index(chosen_size)]
        request_array.append(request)

        additional_request = input("Do you wish to order another one? \n" "Type Y for yes or N for no. ")

        if additional_request == "Y":
            continue

        else:
            break

        else:
            print("Invalid ice cream \"Size\" and/or \"Code\"!")
            continue

print ("Total order value:", "$", sum(request_array))