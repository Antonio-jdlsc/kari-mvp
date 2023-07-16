from pymongo import MongoClient


class MongoDBClient:
    def __init__(self, db_url):
        self.client = MongoClient(db_url)
        self.db = self.client['tu_base_de_datos']

    def get_customer_data(self, customer_id):
        # Implementa la lógica para obtener los datos del cliente de la base de datos
        collection = self.db['customer_data']
        data = collection.find_one({'customer_id': customer_id})
        return data

    def update_sales(self, customer_id, sales_data):
        # Implementa la lógica para actualizar las ventas en la base de datos
        collection = self.db['sales']
        collection.update_one({'customer_id': customer_id}, {'$inc': {'sales': sales_data}})

    def create_order(self, customer_id, order_data):
        # Implementa la lógica para crear un nuevo pedido en la base de datos
        collection = self.db['orders']
        collection.insert_one({'customer_id': customer_id, 'order_data': order_data})

    def update_inventory(self, customer_id, inventory_data):
        # Implementa la lógica para actualizar el inventario en la base de datos
        collection = self.db['inventory']
        collection.update_one({'customer_id': customer_id}, {'$set': {'inventory_data': inventory_data}})

