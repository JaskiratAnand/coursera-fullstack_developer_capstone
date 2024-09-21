from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
        ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description']
            )
        )

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2018,
         "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "Pickup", "year": 2020,
         "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2017,
         "car_make": car_make_instances[0]},
        {"name": "A-Class", "type": "Hatchback", "year": 2015,
         "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "Sedan", "year": 2024,
         "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "Coupe", "year": 2019,
         "car_make": car_make_instances[1]},
        {"name": "A4", "type": "Sedan", "year": 2018,
         "car_make": car_make_instances[2]},
        {"name": "A5", "type": "Coupe", "year": 2021,
         "car_make": car_make_instances[2]},
        {"name": "A6", "type": "Wagon", "year": 2022,
         "car_make": car_make_instances[2]},
        {"name": "Sorrento", "type": "SUV", "year": 2024,
         "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "SUV", "year": 2020,
         "car_make": car_make_instances[3]},
        {"name": "Cerato", "type": "Sedan", "year": 2019,
         "car_make": car_make_instances[3]},
        {"name": "Corolla", "type": "Sedan", "year": 2011,
         "car_make": car_make_instances[4]},
        {"name": "Camry", "type": "Sedan", "year": 2016,
         "car_make": car_make_instances[4]},
        {"name": "Kluger", "type": "SUV", "year": 2015,
         "car_make":car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year']
            )
