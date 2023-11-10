import recommender

#Lee los datos de aprendizaje
with open('prices.json') as dataPrices:
    prices = eval(dataPrices.read())

with open('training_data.json') as databaseData:
    database = eval(databaseData.read()) 

recommender = recommender.Recommender().train(prices, database)

#Se crea un carrito de ejemplo y un máximo de recomendaciones
cart = [10,6,2,1,5,7]

max_recommendations = 3 

recommendations = recommender.get_recommendations(cart, max_recommendations)
print('Recomendaciones:', recommendations)