import random

class concurso:
    puertas = ["A", "B", "C"]
    gana_sin_cambio = 0
    gana_con_cambio = 0
    pierde_sin_cambio = 0
    pierde_con_cambio = 0
    iteraciones = 0

    def __init__(self):
        pass

    def concursar(self, iteraciones):
        self.iteraciones = iteraciones
        for i in range(0, iteraciones):
            eleccion_jugador = random.choice(self.puertas)
            puerta_premio = random.choice(self.puertas)

            if eleccion_jugador == puerta_premio:
                fase_final = []
                fase_final.append(eleccion_jugador)
                self.puertas.remove(eleccion_jugador)
                fase_final.append(random.choice(self.puertas))
            else:
                fase_final = []
                fase_final.append(eleccion_jugador)
                fase_final.append(puerta_premio)
            
            cambio = random.radint(0,1)

            if cambio == 0:
                fase_final.remove(eleccion_jugador)
                if fase_final == puerta_premio:
                    self.pierde_sin_cambio += 1
                elif fase_final != puerta_premio:
                    self.gana_sin_cambio += 1
            else:
                fase_final.remove(eleccion_jugador)
                if fase_final == puerta_premio:
                    self.gana_con_cambio += 1
                elif fase_final != puerta_premio:
                    self.pierde_con_cambio += 1
    
    def informe(self):
        print(f"Cambiando la caja el jugador ha:  \n    -Ganado el {(self.gana_con_cambio/self.iteraciones)*100}% de las veces. \n    -Perdido el {(self.pierde_con_cambio/self.iteraciones)*100}% de las veces. \n No cambiando:\n -Ganado el {(self.gana_sin_cambio/self.iteraciones)*100}\n   -Perdido el {(self.pierde_con_cambio/self.iteraciones)*100}% de las veces.")           

concurso1 = concurso()
concurso1.concursar(100)



