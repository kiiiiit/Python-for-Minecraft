from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = pos = mc.player.getTilePos()
y = 0
print("Position is: ", pos)
blocks = [1,2,3,4,13]
# blocks = [5,14,15,16,17,(17,1),(17,2),(17,3),21,37,38,39,40,56,73,129]
lenght = int(input("Длина: "))
width = int(input("Ширина: "))
y = int(input("Глубина (от 0): "))

for n in range(lenght):
   dx = x+n
   for i in range(width):
      dz = z+i
      y_hi = mc.getHeight(dx,dz)
      print("higest Y: x:{},y:{},z:{}".format(dx,y_hi,dz))
      for j in range(y, y_hi+1):
         boom = dx,j,dz
         print("BOOM: x:{},y:{},z:{}".format(dx,j,dz))
         target = mc.getBlock(boom)
         # if target not in blocks:
         if target in blocks:
            mc.setBlock(boom, 0)