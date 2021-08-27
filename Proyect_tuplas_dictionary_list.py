def catalogacion_audiovisual(inventario: list) -> tuple:



    
    def eliminacion(inventario):
        dvd = [x for x in inventario if x["tipo"] == "DVD"]
        cd =  [x for x in inventario if x["tipo"] == "CD"]
        #identeficamos los dvd a eliminar

        dvd_eliminados = list(filter(lambda x: x['área'] == "Tecnología" and  2021 - x['año'] > 15, dvd))
        dvd_eliminados = list(map(lambda x: x['id'], dvd_eliminados))
        dvd_eliminados.sort()

        cd_eliminados = list(filter(lambda x: x['área'] == "Tecnología" and 2021 - x['año'] > 8, cd))
        cd_eliminados += list(filter(lambda x: x['área'] != "Tecnología" and 2021 - x['año'] > 10, cd ))
        cd_eliminados = list(map(lambda x: x["id"], cd_eliminados))
        cd_eliminados.sort()
        
        if cd_eliminados == [] and dvd_eliminados == []:
            return inventario, dvd_eliminados, cd_eliminados


        ### con esto decimos los dvds a mantener y los cd a mantener

        actualizados  = list(filter(lambda x : x['área'] in ["Administración", 'Matemáticas', 'Física' ],dvd))
        actualizados += list(filter( lambda x: x['área'] == "Tecnología" and 2021 - x["año"] <= 15, dvd))
        actualizados += list(filter(lambda x: x['área'] != "Tecnología" and 2021 - x['año'] <= 10, cd ))
        actualizados += list(filter(lambda x: x['área'] == "Tecnología" and 2021 - x['año'] <= 8, cd ))
        #print(dvd)
        
        
        # organizar a el inventario de mayor a menor.
        actualizados.sort(key = lambda x: x["id"])

        return actualizados, dvd_eliminados, cd_eliminados

    actualizados, dvd_eliminados, cd_eliminados = eliminacion(inventario)
    
    #actualizacion de los nombres.

    def ajuste_nombre(actualizados):
        from functools import reduce
        lista_nombres_autores = actualizados["autor"].split(",")
        nombres = [ x.split()[1] + ','+ x.split()[0] for x in lista_nombres_autores ]
        actualizados["autor"] = reduce(lambda x, y : x + ";" + y, nombres)
        return actualizados
    
    actualizados = list(map(ajuste_nombre,actualizados))
    


    #retonar tupla
    return actualizados ,  dvd_eliminados, cd_eliminados 