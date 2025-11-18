
import geopandas as gpd
import matplotlib.pyplot as plt
import os
import sys

print(os.getcwd())

#sys.exit()

shapefile_path = 'Downloads/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'

world = gpd.read_file(shapefile_path)

europe = world[world['CONTINENT'] == 'Europe']

europe['color'] = ['red' if country == 'Slovenia' else 'lightgray' for country in europe['NAME']]

fig, ax = plt.subplots(figsize=(10, 8))
europe.plot(ax=ax, color=europe['color'], edgecolor='black')

plt.title("Zemljevid Evrope (Slovenija obarvana rdeče)", fontsize=14)

plt.axis('off')
plt.show()