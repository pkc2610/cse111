from datetime import datetime

d = datetime.now()

subtotal = float(input("Please enter your subtotal: "))
discount=subtotal*.9
rabat=subtotal*.1
tax=discount*.06

salestax=subtotal*.06

if d == (2, 3) and subtotal >= 50:
    print("Your discount is 10%!")
    print(f"Your subtotal is: ${discount:.2f}")
    print(f"Your discount amount is: ${rabat:.2f}")
    print(f"Sales Tax: ${tax:.2f}")
    print(f"Your total is: ${discount+tax:.2f}")
elif d !=(2, 3):
    print(f"Sales Tax: ${salestax:.2f}")
    print(f"Your total is: ${salestax+subtotal:.2f}")