cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}
grep = 'trail'

all_jeeps = ''
for keys, values in cars.items():
    if keys == 'Jeep':
        for i in range(len(values)):
            all_jeeps = all_jeeps + values[i] + ', '
        all_jeeps = all_jeeps[0:len(all_jeeps) -2]
        print(all_jeeps)

cars_array = []
for keys, values in cars.items():
    cars_array.append(values[0])
print(cars_array)


# import pdb;pdb.set_trace()
trail_cars = []
for keys, values in cars.items():
    for car in values:
        if grep.lower() in car.lower():
            print(car)    
            trail_cars.append(car)
            trail_cars.sort()
print(trail_cars)

# sd = sorted(cars.items())
# for keys, values in sd:
#     new_dict = {}
#     values.sort()
#     if keys in new_dict:
#         print('ERROR')
#     else:
#         new_dict.update({keys: values})
#     print(new_dict)

print({manufacturer: sorted(models) for manufacturer, models in cars.items()})