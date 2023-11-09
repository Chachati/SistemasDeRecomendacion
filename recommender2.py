import json

class Recommender:
    def __init__(self):
        self.prices = []
        self.database = []
    def train(self, prices, database) -> None:
        self.prices = prices
        self.database = database
        return self

    def get_recommendations(self, cart: list, max_recommendations: int) -> list:
        # Create a dictionary to count the occurrences of items in the database
        item_counts = {}
        for transaction in self.database:
            for item in transaction:
                item_counts[item] = item_counts.get(item, 0) + 1

        # Sort items by their occurrences in descending order
        sorted_items = sorted(item_counts.keys(), key=lambda x: item_counts[x], reverse=True)

        # Filter out items already in the cart and limit the recommendations to max_recommendations
        recommendations = [item for item in sorted_items if item not in cart][:max_recommendations]

        return recommendations

# Cargar datos desde los archivos JSON
with open('prices.json', 'r') as f:
    prices = json.load(f)

with open('training_data.json', 'r') as f:
    database = json.load(f)

# Crear una instancia de la clase Recommender y entrenar el modelo
recommender = Recommender().train(prices, database)

# Ejemplo de cómo obtener recomendaciones para un carrito de compras y un número máximo de recomendaciones
cart = [1, 3, 5]  # Ejemplo de elementos en el carrito
max_recommendations = 3  # Número máximo de recomendaciones

recommendations = recommender.get_recommendations(cart, max_recommendations)
print('Recomendaciones:', recommendations)
