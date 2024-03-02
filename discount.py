#gets a customer’s subtotal as input and gets the current day of the week from your computer’s 
#operating system. Your program must not ask the user to enter the day of the week. Instead, 
#it must get the day of the week from your computer’s operating system.
#If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 
#10% from the subtotal. Your program must then compute the total amount due by adding sales tax 
#of 6% to the subtotal. Your program must print the discount amount if applicable, the sales tax 
#amount, and the total amount due.
#Your program asks the user for the subtotal but does not ask the user for the day of the week. 
#Your program gets the day of the week from your computer’s operating system.
#Your program correctly computes and prints the discount amount if applicable.
#Your program correctly computes and prints the sales tax amount and the total amount due.

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()

discount = net_total*.1

if day_of_week == 1: 
    print(discount)