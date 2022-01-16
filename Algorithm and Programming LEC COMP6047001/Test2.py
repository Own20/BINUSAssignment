items = {'apple': 2, 'banana': 4, 'orange': 6}
for item_name in items:
    print('--------------------------------------------------')
    print('Each ' + item_name + ' costs ' + str(items[item_name]) + ' dollars')
    
    # Receive a value by using input(), and assign it to the input_count variable
    input_count = input("How many " + item_name + "s do you want?: ")
    # Print 'You will buy ____ ____s' by using input_count and item_name
    # print("You will buy " + str(input_count) + " " + str(item_name) + "s")
    print(f"You will buy {str(input_count)} {str(item_name)}s")

    # Convert input_count to an integer and assign it to the count variable
    count_variable = int(input_count)
    # Multiply the price of each item and the count variable, and assign it to the total_price variable
    total_price = items[item_name] * count_variable
    # By using total_price and type conversion, print 'The total price is ____ dollars'
    print("The total price is " + str(total_price) + " dollars")