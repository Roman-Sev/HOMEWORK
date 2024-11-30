class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name},{self.weight},{self.category}'
class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ''
    def add(self,*products):
        existing_products = set()
        try:
            with open(self.__file_name, 'r') as file:
                existing_products = {line.split(',')[0] for line in file.readlines()}
        except FileNotFoundError:
            pass
        with open(self.__file_name,'a') as file:
            for product in products:
                if product.name not in existing_products:
                    file.write(f'{product}\n')
                existing_products.add(product.name)
            else:
                    print(f'Продукт{product.name} уже есть в магазине')

product1 = Product('Potato', 50.0, 'Vegetables')
product2 = Product('apple', 30.0, 'Fruits')
product3 = Product('Potato', 50.0, 'Vegetables')

shop = Shop()
shop.add(product1, product2)
shop.add(product3)

print(shop.get_products())

