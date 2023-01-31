import matplotlib.pyplot as plt
import pandas as pd
import random


def TenNumRandom():
    Ciudades = []
    for x in range(10):
        num = int(random.uniform(1, 78))
        txt = CambiameDelux(num)
        Ciudades.append(txt)
    return Ciudades

def CambiameDelux(num):
    cd = pd.read_csv("List_B.csv", usecols=['Rank', 'City'], low_memory=True)
    result = cd[(cd['Rank'] == num)]
    result = result['City']
    return ''.join(result)


print(TenNumRandom())


def CityPopu():
    cd_pp = pd.read_csv("List_B.csv", usecols=['City', 'Population'], low_memory=True)
    result = cd_pp[(cd_pp['City'] == City)]
    print(result)
    return result['Population'].sum().replace(",", "")


def CityDensyKm(City):
    cd_dk = pd.read_csv("List_B.csv", usecols=['City', 'Density KM2'], low_memory=True)
    result = cd_dk[(cd_dk['City'] == City)]
    print(result)
    return result['Density KM2'].sum().replace(",", "")


def CityDensyM(City):
    cd_dm = pd.read_csv("List_B.csv", usecols=['City', 'Density  M2'], low_memory=True)
    result = cd_dm[(cd_dm['City'] == City)]
    print(result)
    return result['Density  M2'].sum().replace(",", "")


def QuesitosGraph(val1, val2, val3):
    labels = ["Population", "Density KM2", "Density  M2"]
    sizes = [int(val1), int(val2), int(val3)]
    """Esto siguiente hace qie el quesito sobresalga un 0.1"""
    explode = (0, 0.1, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    """Esto enseñara el quesito apartir de lo anterior"""
    plt.show()
