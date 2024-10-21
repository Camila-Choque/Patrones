from amarillo import Amarillo
from plasma import Plasma
from abstractfactory_tv import TvAbstractFactory

class FactoryPlasmaAmarillo(TvAbstractFactory):

    def createColor(self):
        return Amarillo()
    
    def createTv(self):
        return Plasma()