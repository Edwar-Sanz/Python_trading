import pandas as pd
import matplotlib.pyplot as plt
import os

def read_files(path):
    files = [pd.read_csv(os.path.join(path, file)) for file in os.listdir(path) if '.csv' in file]
    return files

path = "C:/Users/jhons/Desktop/resultados"
df = read_files(path)
line = 10000
x = df[1]["params"]



# df_pivot = df[0].pivot_table(index="params", columns="group", values="profit")
# df_pivot.plot(marker='o',markersize=2)

#graficos

plt.subplots()
plt.plot(x, df[1]["profit"], label="100")
plt.plot(x, df[3]["profit"], label="200")
plt.plot(x, df[4]["profit"], label="300")
plt.plot(x, df[5]["profit"], label="400")
plt.plot(x, df[6]["profit"], label="500")
plt.plot(x, df[7]["profit"], label="600")
plt.plot(x, df[8]["profit"], label="700")
plt.plot(x, df[9]["profit"], label="800")
plt.plot(x, df[10]["profit"], label="900")
plt.plot(x, df[2]["profit"], label="1000", marker='o',markersize=1)

# linea horizontal
plt.axhline(y = 10000, color = 'r', linestyle = '-')

plt.legend(loc='center', bbox_to_anchor=(1.01, 0.5))

# etiquetas
plt.title("Grafico 1")
plt.xlabel("Average")
plt.ylabel("Profit")
plt.xticks(x[::20],rotation = 90, fontsize=7)


plt.show()



