class Product:
    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name},{self.weight},{self.category}'
class Shop:
    def __init__(self, file_name):
        self.__file_name = file_name
        shop = Shop('products.txt')
    def get_products(self):
        try:
            with open(self.__file_name, 'r',encoding='utf-8') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ''
    def add(self,*products):
        existing_products = self._get_existing_products()
        new_products_to_add = []
        for product in products:
            if product.name in existing_products:
                print(f"Продукт{product.name} уже есть в магазине")
            else:
                new_products_to_add.append(str(product))
                if new_products_to_add:
                    with open(self.__file_name,'a',encoding='utf-8') as file:
                        file.write('\n'.join(new_products_to_add) + '\n')
    def _get_existing_products(self):
        existing_products = set()
        try:
            with open(self._file_name,'r',encoding='utf-8') as file:
                for line in file:
                    product_name = line.split(',')[0].strip()
                existing_products.add(product_name)
        except FileNotFoundError:
            pass
        return existing_products

    if __name__=='main__':
        potato = Product('Potato', 50.0, 'Vegetables')
        tomato = Product('tomato', 30.0, 'Vegetables')
        apple = Product('apple', 50.0, 'Fruits')

        shop = Shop()
        shop.add(potato, tomato)
        shop.add(apple)

print(Shop)

