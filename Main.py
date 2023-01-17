import Cerebros as cb

Ciudad = 'Manila'

PP = cb.CityPopu(Ciudad)
print("---------------------------", PP)
KM = cb.CityDensyKm(Ciudad)
print("---------------------------")
M = cb.CityDensyM(Ciudad)
print("---------------------------")
cb.QuesitosGraph(PP, KM, M)
