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
