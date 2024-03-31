import csv

product_dictionary = {}

def read_dictionary(filename, key_column_index): 

    with open("products.csv", "r") as infile:
    
      will_read = csv.reader(infile)

      next(will_read)

      for row in will_read:
            code = row[0]
            product = row[1]
            price = row[2]

            product_dictionary[code] = {code, product, price}
         
            print(product_dictionary)


def main():
    read_dictionary()
    products_dict = read_dictionary()

    request_dictionary = {}

    with open("request.csv", "r") as infile:

      going_to_read = csv.reader(infile)

      next(going_to_read)

      for row in going_to_read:
            code_ = row[0]
            quantity = row[1]
     
    request_dictionary[code_] = {code_, quantity}

    print(request_dictionary)


