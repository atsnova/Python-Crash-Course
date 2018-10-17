Mens = {'Jack':'Hindu', 'Kphn':'Jewish','Shaun':'Ateiast','Pop':'Christian'}
Ladies = {'Selina':'Hindu','Aliya':'Muslim','Sunny':'Hindu'}

for k,v in Mens.items():
    print('Name of the individual is : ' + k)
    print('\t and he is :' + v)

for lady in Ladies:
    print('Hey ' + lady)
    print('want to teach me about ' + Ladies[lady])

fav_place = {'Atish':['morroco', 'SA', 'bag']}

for fav in fav_place:
    print(fav)
    for place in fav_place[fav]:
        print(place)