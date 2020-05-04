instance = {
        "id": 3,
        "nombre": "Queso Mozzarella",
        "descripcion": "Queso de la mejor calidad"
    }

hamburguesas = [
            {
                "path": "https://iic3103t2.herokuapp.com/ingrediente/1"
            },
            {
                "path": "https://iic3103t2.herokuapp.com/ingrediente/3"
            },
            {
                "path": "https://iic3103t2.herokuapp.com/ingrediente/6"
            },
            {
                "path": "https://iic3103t2.herokuapp.com/ingrediente/7"
            },
            {
                "path": "https://iic3103t2.herokuapp.com/ingrediente/12"
            },
            {
                "path": "https://iic3103t2.herokuapp.com/ingrediente/20"
            }
        ]
aux = list()
for ing in hamburguesas:
    aux2 = ing['path'].split("/")
    aux.append(int(aux2[4]))

print(aux)
