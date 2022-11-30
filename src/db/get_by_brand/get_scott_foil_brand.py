from src.db.get_bicycles import get_bicycles

def get_brand_scott_foil():

    #  Cogemos la conexion a las bicis
    bikes_collection = get_bicycles()
    # Creamos la query para sacar el tipo racing
    query_results = bikes_collection.find({"bicycle brand": "SCOTT FOIL"})


    data_scott_foil = []
    for document in query_results:
        #  Creamos el tipo de archivo que queremos que nos saque para el link a la página de detalles
        file_name = document['model'].replace(' ', '-') + str(document['_id'])
        #  Añadimos los datos que vamos a queres sacar de la coleccion bicicletas
        data_scott_foil.append(
            {
                "id": str(document['_id']),
                "model": document['model'],
                "bicycle brand": document['bicycle brand'],
                "image": "/assets/images/bicicleta.webp",
                "details_link": "details/" + file_name + ".html",
                "description": document["description"],
                "specifications": document["specifications"],
                "bicycle type": document["bicycle type"]
            }
        )

    return data_scott_foil
