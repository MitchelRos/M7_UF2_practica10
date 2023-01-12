import matplotlib.pyplot as plt
import pandas as pd


def CityPopu():
        cd_pp = pd.read_csv("List_B.csv", usecols=['City', 'Population'], low_memory=True)
        result = cd_pp[(cd_pp['City'] == 'Manila')]
        print(result.keys[1])
        return result[1]

def CityDensyKm():
        cd_dk = pd.read_csv("List_B.csv", usecols=['City', 'Density KM2'], low_memory=True)
        print(cd_dk[(cd_dk['City']=='Manila')])

def CityDensyM():
        cd_dm = pd.read_csv("List_B.csv", usecols=['City', 'Density  M2'], low_memory=True)
        print(cd_dm[(cd_dm['City']=='Manila')])

def QuesitosGraph():
        labels = ["Population", "Density KM2", "Density  M2"]
        sizes = [15323, 332320, 2323245]
        """Esto siguiente hace qie el quesito sobresalga un 0.1"""
        explode = (0, 0.1, 0)
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        """Esto enseñara el quesito apartir de lo anterior"""
        plt.show()

QuesitosGraph()
CityPopu()
CityDensyKm()
CityDensyM()