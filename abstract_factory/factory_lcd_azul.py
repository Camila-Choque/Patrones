from azul import Azul
from lcd import LCD
from abstractfactory_tv import TvAbstractFactory

class FactoryLcdAzul(TvAbstractFactory):

    def createColor(self):
        return Azul()
    
    def createTv(self):
        return LCD()