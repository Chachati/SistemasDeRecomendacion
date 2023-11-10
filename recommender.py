class Recommender:
    
    def train(self, prices, database) -> None:
        self.prices = prices
        self.database = database
        return self

    def get_recommendations(self, cart: list, max_recommendations: int) -> list:
        
        itemCounts = {}

        #Cuando los items del carrito son demasiados (Mayor que el conjunto máximo de datos de entrenamiento) se limita a los tres primeros datos
        if (len(cart) >= 9):
             cart = cart[:3]

        #Lee las y suma las transacciones útiles de acuerdo al carrito
        for transaction in self.database:
            for item in transaction:
                if all(item in transaction for item in cart):
                    itemCounts[item] = itemCounts.get(item, 0) + 1
                #Aumenta tiempos, buscaba solucionar ausencia de subsets pero no sirve
                """else:
                    cart = cart[:2]
                    if all(item in transaction for item in cart):
                        itemCounts[item] = itemCounts.get(item, 0) + 1"""

        sortedItems = sorted(itemCounts.keys(), key=lambda x: itemCounts[x], reverse=True)

        recommendations = [item for item in sortedItems if item not in cart][:max_recommendations]

        return recommendations

