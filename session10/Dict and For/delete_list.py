print('We Never Learn')
film = {
    'Name': 'We Never Learn(Bokutachi wa Benkyō ga Dekinai)',
    'Released Year': '2019',
    'Director':['Taishi Tsutsui']
}
print(film)
film["Director"].append("Shigeo Tokuda")
print(film["Director"])
film['Director'].remove('Taishi Tsutsui')
print(film)