from factory_lcd_azul import FactoryLcdAzul
from factory_plasma_amarillo import FactoryPlasmaAmarillo

factory_led = FactoryLcdAzul()
factory_plasma = FactoryPlasmaAmarillo()

azul = factory_led.createColor()
led = factory_led.createTv()

amarillo = factory_plasma.createColor()
plasma = factory_plasma.createTv()

print(azul)
print(led)
print(amarillo)
print(plasma)