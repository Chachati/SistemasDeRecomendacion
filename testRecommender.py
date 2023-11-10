import recommender

#Lee los datos de aprendizaje
with open('prices.json') as dataPrices:
    prices = eval(dataPrices.read())

with open('training_data.json') as databaseData:
    database = eval(databaseData.read()) 

recommender = recommender.Recommender().train(prices, database)

#Se crea un carrito de ejemplo y un máximo de recomendaciones
cart = [15,42,1,2,4,6,7,9,9,6,5,3,2,4,5,6,3,5,78,1,2,6,8,4,2]

max_recommendations = 3 

recommendations = recommender.get_recommendations(cart, max_recommendations)
print('Recomendaciones:', recommendations)