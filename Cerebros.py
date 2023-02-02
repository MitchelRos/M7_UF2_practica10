import matplotlib.pyplot as plt
import pandas as pd
import random


def TenRandom():
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


def CityPopu(city):
    ltctpp = []
    cd_pp = pd.read_csv("List_B.csv", usecols=['City', 'Population'], low_memory=True)
    for x in city:
        result = cd_pp[(cd_pp['City'] == x)]
        ltctpp.append(int(result['Population'].sum().replace(",", "")))
        """df["size"].replace(",", "", regex=True)"""
    return ltctpp, 'Population'


def CityDensyKm(city):
    ltctdk = []
    cd_dk = pd.read_csv("List_B.csv", usecols=['City', 'Density KM2'], low_memory=True)
    for x in city:
        result = cd_dk[(cd_dk['City'] == x)]
        ltctdk.append(int(result['Density KM2'].sum().replace(",", "")))
    return ltctdk, 'Density KM2'


def CityDensyM(city):
    ltctdm = []
    cd_dm = pd.read_csv("List_B.csv", usecols=['City', 'Density  M2'], low_memory=True)
    for x in city:
        result = cd_dm[(cd_dm['City'] == x)]
        ltctdm.append(int(result['Density  M2'].sum().replace(",", "")))
    return ltctdm, 'Density  M2'


def QuesitosGraph(txt, val, title):
    labels = txt
    sizes = val
    """Esto siguiente hace qie el quesito sobresalga un 0.1"""
    explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    """Esto enseñara el quesito apartir de lo anterior"""
    plt.title(title , b)
    plt.legend()
    plt.show()
