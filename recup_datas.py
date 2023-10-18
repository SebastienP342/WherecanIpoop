import pandas as pd

def datas_display():
    # Index(['type', 'statut', 'adresse', 'arrondissement', 'horaire', 'acces_pmr',
    #        'relais_bebe', 'url_fiche_equipement', 'geo_shape', 'geo_point_2d_lat',
    #        'geo_point_2d_long'],
    #       dtype='object')
    datas = pd.read_csv('sanisettesparis.csv', sep=';')
    print(datas.columns)

    dataframe = datas[['adresse','geo_point_2d_lat','geo_point_2d_long']]

    return dataframe



