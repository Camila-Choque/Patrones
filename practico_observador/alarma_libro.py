from subject import Subject

class AlarmaLibro(Subject):

    def __init__(self):
        self.observador = []

    def attach(self, o1):
        self.observador.append(o1)
    
    def dettach(self, o1):
        self.observador.remove(o1)
    
    def notifyObservers(self):
        for i in self.observador:
            i.update()