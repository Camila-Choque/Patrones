from alarma_libro import AlarmaLibro

class Biblioteca():
    def devuelveLibro(self,libro, alarma):
        if libro.estado == "MALO":
            alarma.notifyObservers()