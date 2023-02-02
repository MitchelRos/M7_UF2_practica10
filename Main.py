import Cerebros as cb

Ciudades = cb.TenRandom()
print(Ciudades)
print("---------------------------")
PPT = cb.CityPopu(Ciudades)[0]
PPV = cb.CityPopu(Ciudades)[1]
print(PPT)
print("---------------------------")
KMT = cb.CityDensyKm(Ciudades)[0]
KMV = cb.CityDensyKm(Ciudades)[1]
print(KMT)
print("---------------------------")
MT = cb.CityDensyM(Ciudades)[0]
MV = cb.CityDensyM(Ciudades)[1]
print(MT)
print("---------------------------")
cb.QuesitosGraph(Ciudades, PPT, PPV)
cb.QuesitosGraph(Ciudades, KMT, KMV)
cb.QuesitosGraph(Ciudades, MT, MV)
