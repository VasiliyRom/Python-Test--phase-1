class Person():

    def first_name(self, *args, **kwargs):
        pass
    
    def last_name():
        pass
    def age():
        pass

class Teacher(Person):
    def salary():



class Student(Person):


#Task2
class Test:
    
    def square_nums(self, x):
        print([i**2 for i in x]) 
        
    def remove_positives(self, x):
        neg = []
        for i in x:
            if i < 0:
                neg.append(i)
        print(neg)

    def filter_leaps(self, year):
        leaps = []
        for y in year:
            if y % 4 == 0 or (y % 100 != 0 and y % 400 == 0):
                leaps.append(y)
        print(leaps)


class Mathematician(Test):
    pass


mat = Mathematician()

mat.square_nums([7, 11, 5, 4])  #== [49, 121, 25, 16]
mat.remove_positives ([26, -11, -8, 13, -90]) #== [-11, -8, -90]
mat.filter_leaps([2001, 1884, 1995, 2003, 2020]) #== [1884, 2020]


#Task3
class Product:
    
    prod_type = ""
    name = ""
    price = 0

    def __init__(self, prod_type, name, price):
        if type(price) != str:
            self.prod_type = prod_type
        else:
            raise TypeError('Prod_typeError')
        
        if type(price) != str:
            self.name = name
        else:
            raise TypeError('NameError')

        if type(price) != int or type(price) != float and price > 0:
            self.price = price
        else:
            raise TypeError('PriceError')

    def __str__(self):
       return f'{self.name} = {self.price}'

    def __repr__(self):
       return f'{self.name} = {self.price}'


class ProductStore:
    
    prod_store = []
    amount = 0
    profit = 0

    def add(self, product, amount):
        prod = {}
        prod["product"] = product
        prod["amount"] = amount
        product.price *= 1.3
        self.prod_store.append(prod)

    def set_discount(self, identifier, percent):
        if type(percent) == int or type(percent) == float:
            for i in self.prod_store:
                if i["product"].prod_type == identifier or i["product"].name == identifier:
                    i["product"].price = i["product"].price * (1 - (percent / 100))
        else:
            raise Exception("Відсотки мають бути числом")
        
    def sell_product(self, product_name, amount):
        for i in self.prod_store:
            if i['product'].name == product_name:
                try:
                    if amount <= i['amount']:
                        i['amount'] -= amount
                        self.profit = amount * i['product'].price
                    else:
                        raise Exception('Невистачає товару!')

                except Exception as e:
                    print(e)

    def get_income(self):
        print(f"{self.profit} UAH")

    def get_all_products(self):
        print(self.prod_store)

    def get_product_info(self, product_name):
        for i in self.prod_store:
            if i['product'].name == product_name:
                print(product_name, i['amount'])


try:
    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 1.5)

    s = ProductStore()

    s.add(p, 10)
    s.add(p2, 300)
    s.add(p, 100000)
    s.sell_product('Ramen', 10)
    s.get_income()
    s.get_all_products()
    s.get_product_info('Ramen')
    s.set_discount('Ramen', 10)
    s.get_all_products()

except ValueError as e:
    print(e)


#Task4
class CustomException(Exception):
    def __init__(self, msg, *args):
        self.msg = msg

    def __str__(self):
        return ''.join(self.msg)


error = CustomException('Custom error')

try:
    name = 'aaaa'
    if len(name) < 5:
        raise CustomException(f'{name} - має містити 5 символів')
except CustomException as e:
    print(type(e))
    print(str(e))
    log = []
    log.append(str(e))
    new_file = open('logs.txt', 'a')
    new_file.writelines(log)
    new_file.close()
    