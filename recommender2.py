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

