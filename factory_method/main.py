from triangulo_factory import *

triangulo = TrianguloFactory()

equilatero = triangulo.createTriangulo(10,10,10)
escaleno = triangulo.createTriangulo(8,9,10)
isosceles = triangulo.createTriangulo(10,10,9)


equilatero.getDescripcion()
print(equilatero.ladoA)
escaleno.getDescripcion()
print(escaleno.ladoA)
isosceles.getDescripcion()
print(isosceles.ladoC)