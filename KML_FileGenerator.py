import simplekml
import pandas

df = pandas.read_csv("C:\\Users\\Prajan\\Desktop\\Python Programs\\prajan.csv")

kml=simplekml.Kml()
for nm,lon,lat in zip(df["GeoCode"],df["Longitude"], df["Latitude"]):
    kml.newpoint(name=nm, coords=[(lon,lat)])
kml.save("C:\\Users\\Prajan\\Desktop\\Python Programs\\Positions.kml")