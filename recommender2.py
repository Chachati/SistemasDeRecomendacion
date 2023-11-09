class Recommender:
    def train(self, prices, database) -> None:
        self.prices = prices
        self.database = database
        return self

    def get_recommendations(self, cart: list, max_recommendations: int) -> list:
        # Conteo de las ocurrencias de los productos en las transacciones
        item_counts = {}
        for transaction in self.database:
            for item in transaction:
                item_counts[item] = item_counts.get(item, 0) + 1

        # Ordenamiento de los productos por ocurrencias en orden descendente
        sorted_items = sorted(item_counts.keys(), key=lambda x: item_counts[x], reverse=True)

        # Filtrado de productos ya presentes en el carrito y limitación a `max_recommendations`
        recommendations = [item for item in sorted_items if item not in cart][:max_recommendations]

        return recommendations

# Cargar datos desde los archivos directamente como listas de Python
# Suponiendo que los datos están en "prices.json" y "training_data.json"
with open('prices.json', 'r') as f:
    prices = eval(f.read())  # Evaluar el contenido del archivo como una lista de Python

with open('training_data.json', 'r') as f:
    database = eval(f.read())  # Evaluar el contenido del archivo como una lista de Python

# Crear una instancia de la clase Recommender y entrenar el modelo
recommender = Recommender().train(prices, database)

# Ejemplo de cómo obtener recomendaciones para un carrito de compras y un número máximo de recomendaciones
cart = [1, 3, 5]  # Ejemplo de elementos en el carrito
max_recommendations = 3  # Número máximo de recomendaciones

recommendations = recommender.get_recommendations(cart, max_recommendations)
print('Recomendaciones:', recommendations)
