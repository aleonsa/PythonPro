#union: resultado de combinar con |
#los elementos, (si se repiten se añade solo una vez)

#interseccion: solamente los elementos en comun  con &

#diferencia: resultado de tomar un set y quitar todos los
# elementos que tiene el set 2 que se repiten en s1, con -

#diferencia simetrica: me quedo con los elementos que no se
# comparten en amobs sets con ^

# [1 1 2 2 4] -> [1 2 4]

# def remove_duplicates(some_list):
#     without_duplicates = []
#     for e in some_list:
#         if e not in without_duplicates:
#             without_duplicates.append(e)
#     return without_duplicates

def remove_duplicates(some_list):
    return list(set(some_list))

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()

 