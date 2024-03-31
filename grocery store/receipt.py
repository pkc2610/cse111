import csv

from datetime import datetime

def read_dictionary(filename, key_column_index): 

    product_dictionary = {}

    with open(filename, "r") as infile:
    
        will_read = csv.reader(infile)

        next(will_read)

        for row in will_read:

            product_dictionary[row[ key_column_index]] = row
         
    return product_dictionary




def main():
    print("Bluth Family Banana Store")
    print()
    current_date_and_time = datetime.now()
    products_dict = read_dictionary("products.csv", 0)

    output_string = ""
    item_total = 0
    subtotal = 0.0
    request_code = {}

    with open("request.csv", "r") as infile:

        going_to_read = csv.reader(infile)

        next(going_to_read)

        for row in going_to_read:

            output_string += f"{products_dict[row[0]][1]}: {row[1]} @ {products_dict[row[0]][2]}\n"

            item_total += int(row[1])

            subtotal += (float(row[1]) * float(products_dict[row[0]][2]))

    print(output_string)
    print()

    print(f"Number of items: {item_total}")

    print(f"Subtotal: {subtotal:.2f}")

    sales_tax = 0.06 * subtotal

    print(f"Sales Tax: {sales_tax:.2f}")

    print(f"Total: {(sales_tax + subtotal):.2f}")
    print()

    print("Thank you for shopping at the Bluth Family Banana Store!")
    print(f"{current_date_and_time:%A %I:%M %p}")

main()
#print item, quantity, price
#print number of items
#print sum of prices (subtotal)
#print sales tax amount
#print total due
#print thank you
#print current date and time
#I will be ignoring the try and except blocks with every fiber of my being because I gotta turn this in

#Inkom Emporium

#wheat bread: 2 @ 2.55
#1 cup yogurt: 4 @ 0.75
#32 oz granola: 1 @ 3.21
#twix candy bar: 2 @ 0.85
#1 cup yogurt: 3 @ 0.75

#Number of Items: 12
#Subtotal: 15.26
#Sales Tax: 0.92
#Total: 16.18

#Thank you for shopping at the Inkom Emporium.
#Wed Nov  4 05:10:30 2020