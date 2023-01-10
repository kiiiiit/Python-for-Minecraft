import time
from itertools import chain
# import mcpi.block as block
# import mcpi.entity as entity
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# x,y,z = pos = mc.player.getTilePos()
x,y,z = pos = 50,0,50
mult = 5

# Make ZOO
list_a = range( 1, 37)
list_b = range(40, 47)
list_c = range(50, 69)
list_d = range(90, 105)
list_e = (120, 200)
a = chain(list_a, list_b, list_c, list_d, list_e)

i = 0
for j in range(1, 255):#a:
    i+=1
    # Cage
    # mc.setBlocks(x+i*mult,y,z-3, x+7+i*mult, y+7, z+7, 0)
    mc.setBlocks(x+i*mult,y,z, x+mult+i*mult, y+mult, z+mult, 89)
    mc.setBlocks(x+i*mult+1,y+1,z+1, x+mult-1+i*mult, y+mult-1, z+mult-1, j)
    print(j)
    mc.setBlocks(x+i*mult,y,z,x+mult+i*mult, y+mult, z, 20)
    # mc.setBlock (x+3+i*mult,y+mult,z+3,89)
    # mc.setBlock (x+1+i*mult,y+1,z+1,117)

    # Road
    mc.setBlocks(x+i*mult,y-1,z-3, x+mult+i*mult, y-1, z, 152)
    # MOB
    # time.sleep(10)
    # mc.spawnEntity(x+3+i*mult,y+1,z+3,120)

# Move Steve
i = 0
while i < mult:
    i+=1
    # mc.setBlock(x+i,y-1,z-i, 49)
    # mc.setBlock(x+i,y+3,z-i, 89)
    # mc.player.setTilePos(x+i,y+2,z+3)

    mc.setBlocks(x-i, y-1, z-i, x+i, y-1, z+i, 152)
    mc.setBlocks(x-i, y, z-i, x+i, y+i, z+i, 0)
    mc.setBlock (x, y+3, z, 89)
    mc.player.setTilePos(pos)

# x,y,z = pos = mc.player.getTilePos()
# x,y,z = pos = 0,0,0
# for i in range (0, 1000, 1):
#    mc.setBlock(x+2,y+5,z+2, i)
#    time.sleep(0.1)

# x,y,z = pos = mc.player.getTilePos()
# mc.player.setTilePos(x,y+100,z)

# while True:
#     x,y,z = mc.player.getTilePos()
#     print("x="+str(x) + " y="+str(y) + " z="+str(z))
#     time.sleep(1)
