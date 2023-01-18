# import time
# import mcpi.block as block
# import mcpi.entity as entity
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# mc = Minecraft.create("192.168.50.11", 4711)

# x,y,z = pos = mc.player.getTilePos()
# x,y,z = pos = -300,-30,-450 # Здесь много лута и и гавно плавает!
# pos: x:-134,y:-75,z:81 # Красивый поздемный биом
# pos: x:-402,y:-1,z:91 - дерево на острове
# pos: x:-685,y:4,z:-133 - пчелы и рядом деревня

# x,y,z = pos = 0,0,0
x = int(input("x: "))
# y = int(input("y: "))
z = int(input("z: "))

# width = 3
y = mc.getHeight(x,z)
# mc.setBlocks(x-width, y, z-width, x+width, y+width, z+width, 0)
# mc.setBlocks(x-width, y-1, z-width, x+width, y-1, z+width, 152)
mc.setBlock (x, y, z, 89)
mc.player.setTilePos(x,y+1,z)

# flower = 38
# flowerColor = 3
# mc.setBlock(x, y+2, z, flower, flowerColor)

# x,y,z = pos = mc.player.getTilePos()
# mc.player.setTilePos(x,y+100,z)

#while True:
#   pos = mc.player.getTilePos()
#   mc.postToChat("x="+str(pos.x) + " y="+str(pos.y) + " z="+str(pos.z))
#   time.sleep(5)
