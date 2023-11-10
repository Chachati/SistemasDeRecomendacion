import recommender2 

# Cargar datos desde los archivos directamente como listas de Python
# Suponiendo que los datos están en "prices.json" y "training_data.json"
with open('prices.json', 'r') as f:
    prices = eval(f.read())  # Evaluar el contenido del archivo como una lista de Python

with open('training_data.json', 'r') as f:
    database = eval(f.read())  # Evaluar el contenido del archivo como una lista de Python

# Crear una instancia de la clase Recommender y entrenar el modelo
recommender = recommender2.Recommender().train(prices, database)

# Ejemplo de cómo obtener recomendaciones para un carrito de compras y un número máximo de recomendaciones
cart = [1, 3, 5]  # Ejemplo de elementos en el carrito
max_recommendations = 3  # Número máximo de recomendaciones

recommendations = recommender.get_recommendations(cart, max_recommendations)
print('Recomendaciones:', recommendations)
