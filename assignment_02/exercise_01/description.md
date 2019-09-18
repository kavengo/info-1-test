# Task 1: Ice Cream Parlour (4 Points)

In this task, you create a simple price calculator for an ice cream parlour. You will write a program that allows you to calculate the total price of a bowl of ice cream, including any membership discounts.

The goal of this task is for you to get familiar with getting input from the user, variable assignment, doing some simple calculations and printing results.

## Assignment

In Listing 1 you can see a short python program. It contains the variables:

- `price_icecream_ball`

- `price_cream`

- `price_chocolate_sauce`

- `number_of_icecream_balls_ordered`

- `number_of_cream_ordered`

- `number_of_chocolate_sauce_ordered`


These variables indicate the prices of the customisable ice cream bowl components and the the amount of components your next customer purchases. 
Please do not modify this part of the code, else we will not be able to grade your submission. 
Your task is to deﬁne some more variables and print out some results.

```python
if __name__ == '__main__':

    # Please do not modify this part of the code! 
    price_icecream_ball = 2.5 
    price_cream = 1.5 
    price_chocolate_sauce = 1
    
    number_of_icecream_balls_ordered = 3 
    number_of_cream_ordered = 1 
    number_of_chocolate_sauce_ordered = 1
    
    # Your code goes here

```

Consider the following instructions:

* Some customers have a membership card, that grants a discount (0 - 100%). 
The waiter asks to the customer for his membership card. 
Store this input value in a variable called `membership_discount`. 
You can expect the input to be an integer number from 0 to 100.

* Calculate the subtotal price of the ordered ice cream bowl using the predeﬁned variables (see Listing 1) and store the result in a variable named `subtotal_price`.

* Print a message showing the subtotal price of the purchase. 
The message should look as follows: ”The subtotal of your order is x”, where x is the subtotal price you calculated in step 2. 
Don’t worry about number formatting in this step.

* Calculate the amount the customer saves with his membership card using your previous results. 
Store the result in a variable named `savings`. 
Then print a message showing the savings the customer makes. 
The message should look as follows: ”Your savings are y”, where y is the savings you calculated. 
Don’t worry about number formatting in this step.

* Calculate the total price of the purchase and store it in a variable named `total_price`.

* Print a message showing the total price of the purchase. 
The message should look as follows: ”The total price of your purchase is z”, where z is the total price of the purchase you calculated in 6. 
Don’t worry about number formatting in this step.

* Another customer (without any discounts) asks you how many ice cream balls he can order with his 23 CHF. 
Calculate this and store the result in a variable named `number_of_balls` (Hint: You can’t buy 0.2 balls.). 
Then print a message showing the number of balls the customer can buy. 
The message should look as follows: ”The number of ice cream balls are z”, where z is the number of balls you calculated.
