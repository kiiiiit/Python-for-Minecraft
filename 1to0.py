# Расчистка поверхности от инертных блоков (земля, гравий, камень и т.п.)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = pos = mc.player.getTilePos() #Получаем позицию игрока
y = 0 # Выставляем уровень в 0
print("Position is: ", pos)

blocks = [1,2,3,4,8,9,13] # Перечень типов блоков, что нужно убирать
# blocks = [5,14,15,16,17,(17,1),(17,2),(17,3),21,37,38,39,40,56,73,129]

lenght = int(input("Длина: "))
width = int(input("Ширина: "))
y = int(input("Глубина начала ниже 0: "))

for n in range(lenght):
   dx = x+n # Высчитываем Х
   for i in range(width):
      dz = z+i # Высчитываем Z
      y_hi = mc.getHeight(dx,dz) # Находим максимальную высоту в данной точке
      # print("higest Y: x:{},y:{},z:{}".format(dx,y_hi,dz))
      for dy in range(y, y_hi+1):
         boom = dx,dy,dz # Вычисляем блок для анализа
         # print("BOOM: x:{},y:{},z:{}".format(dx,dy,dz))
         target = mc.getBlock(boom) # Получаем тип блока
         # if target not in blocks:
         if target in blocks:
            mc.setBlock(boom, 0) # Заполняем ненужные блоки "воздухом"