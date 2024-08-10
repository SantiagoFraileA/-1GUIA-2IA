import random

class AgenteIA:
    def __init__(self):
        self.temperatura_objetivo = 22 
        self.temperatura_actual = random.uniform(15, 30)
        self.humedad = random.uniform(30, 70)

        self.sensor_temperatura = None
        self.sensor_humedad = None

        self.calefaccion = False
        self.aire_acondicionado = False

        self.tiempo_total = 0
        self.ajustes_realizados = 0

    def sensor_leer_temperatura(self):
        self.sensor_temperatura = round(self.temperatura_actual + random.uniform(-0.5, 0.5), 1)
        return self.sensor_temperatura

    def sensor_leer_humedad(self):
        self.sensor_humedad = round(self.humedad + random.uniform(-2, 2), 1)
        return self.sensor_humedad

    def actuador_ajustar_temperatura(self):
        if self.sensor_temperatura < self.temperatura_objetivo - 0.5:
            self.calefaccion = True
            self.aire_acondicionado = False
            self.temperatura_actual += 0.5
        elif self.sensor_temperatura > self.temperatura_objetivo + 0.5:
            self.calefaccion = False
            self.aire_acondicionado = True
            self.temperatura_actual -= 0.5
        else:
            self.calefaccion = False
            self.aire_acondicionado = False
        
        self.ajustes_realizados += 1

    def ejecutar(self, ciclos):
        for _ in range(ciclos):
            temp = self.sensor_leer_temperatura()
            hum = self.sensor_leer_humedad()
            print(f"Temperatura: {temp}°C, Humedad: {hum}%")
            
            self.actuador_ajustar_temperatura()
            
            if self.calefaccion:
                print("Calefacción encendida")
            elif self.aire_acondicionado:
                print("Aire acondicionado encendido")
            else:
                print("Sistemas apagados")
            
            self.tiempo_total += 1
            print(f"Ciclo {self.tiempo_total} completado\n")

    def mostrar_rendimiento(self):
        print(f"Tiempo total de operación: {self.tiempo_total} ciclos")
        print(f"Ajustes de temperatura realizados: {self.ajustes_realizados}")
        print(f"Eficiencia: {self.ajustes_realizados / self.tiempo_total:.2f} ajustes por ciclo")


agente = AgenteIA()
agente.ejecutar(10)
agente.mostrar_rendimiento()