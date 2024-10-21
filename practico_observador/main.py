from alarma_libro import AlarmaLibro
from compras import Compras
from administracion import Administracion
from stock import Stock
from libro import Libro
from biblioteca import Biblioteca

alarma = AlarmaLibro()
compra = Compras()
administracion= Administracion()
stock = Stock()

alarma.attach(compra)
alarma.attach(administracion)
alarma.attach(stock)

libro = Libro()
libro.estado = "MALO"

bibloteca = Biblioteca()
bibloteca.devuelveLibro(libro, alarma)