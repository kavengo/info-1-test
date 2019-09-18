# Please do not modify this part of the code!
price_icecream_ball = 2.5
price_cream = 1.5
price_chocolate_sauce = 1

number_of_icecream_balls_ordered = 3
number_of_cream_ordered = 1
number_of_chocolate_sauce_ordered = 1


# Your code goes here

# instruction 1:
membership_discount = int(input("Membership Discount (0-100): "))

# instruction 2: (subtotal of the order)
subtotal_price = price_icecream_ball * number_of_icecream_balls_ordered + price_cream * number_of_cream_ordered + price_chocolate_sauce * number_of_chocolate_sauce_ordered

# instruction 3: (print the subtotal)
print("The subtotal of your order is", subtotal_price)

# instruction 4: (savings)
savings = subtotal_price * (membership_discount / 100)
print("Your savings are ", savings)

# instruction 5:
total_price = subtotal_price - savings

# instruction 6:
print("The total price of your purchase is ", total_price)

# instruction 7:
number_of_balls = 23 // price_icecream_ball
print("The number of ice cream balls are ", savings)