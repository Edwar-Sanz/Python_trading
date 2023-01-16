import pandas as pd
import matplotlib.pyplot as plt



if __name__ == "__main__":

    #read
    df = pd.read_csv("results_1.csv")

    #line plot
    plt.plot(df["params"], df["profit"], marker='o', markersize=1)
  
    # promedio
    plt.axhline(y = df["profit"].mean() , color = 'r', linestyle = '--')

    # etiquetas
    plt.title("Grafico 1")
    plt.xlabel("Average")
    plt.ylabel("Profit")
    plt.xticks(df["params"][::20],rotation = 90, fontsize=7)
    
    plt.show()

   


