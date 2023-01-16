import pandas as pd
import numpy as np
import random


def n_tick(rango_i, rango_f, redondear_x):
    nuevo_tick = random.random() + random.randrange(rango_i, rango_f)
    return round(nuevo_tick, redondear_x)

def entrada(precio, profit, stop, spread):
    return [precio+spread, precio+spread+profit, precio-stop+spread]
       

d = {"in": [], "out": [], "tipo": []}
spread = 1

ri, rf, rx = -4, 4, 1   #generar los ticks desde ri hasta rf, redondeando el numero a rx decimales
pf, st = 1, 3          #profit y stop 

precio_actual = 1000
numero_simulaciones = 10



for i in range(numero_simulaciones):
    compra = entrada(precio_actual, pf, st, spread)   
    d["in"].append(compra[0])

    print(f"precio_actual actual:{precio_actual}  entrada:{compra[0]}  tp:{compra[1]}  sl:{compra[2]} ")
    

    while True:       
        if compra[1] <= precio_actual:
            d["out"].append(precio_actual)
            d["tipo"].append("win")
            print(f"profit{compra[0]} - precio_actual {precio_actual} - gana")
            break
        elif compra[2] >= precio_actual:
            d["out"].append(precio_actual)
            d["tipo"].append("lose")
            print(f"stop {compra[2]} - precio_actual {precio_actual} - pierde")
            break
        precio_actual = precio_actual + n_tick(ri, rf, rx)

        print(f"precio_actual actual:{precio_actual}")
        input()
        
d = pd.DataFrame(d)
print((d["tipo"].value_counts()/numero_simulaciones)*100)




