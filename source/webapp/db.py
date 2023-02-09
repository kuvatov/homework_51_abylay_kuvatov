from random import randint


class Database:
    cats = [
        {
            "name": '',
            "age": randint(1, 15),
            "happiness": randint(0, 100),
            "satiety": randint(0, 100),
            "image": '/media/normal.jpeg',
            "state": ''
        }
    ]
