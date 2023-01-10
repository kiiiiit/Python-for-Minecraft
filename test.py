import time
# import mcpi.block as block
import mcpi.entity as entity
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = pos = mc.player.getTilePos()
mult = 5
for i in range(1,105):
    if i not in [38,39,48,49,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89]:
        mc.setBlocks(x+i*mult,y-1,z-3, x+7+i*mult, y+7, z+7, 0)
        mc.setBlocks(x+i*mult,y,z, x+5+i*mult, y+5, z+5, 166)
        mc.setBlocks(x+i*mult,y-1,z-3, x+5+i*mult, y, z, 152)
        mc.setBlocks(x+1+i*mult,y+1,z+1, x+4+i*mult, y+4, z+4, 0)
        # mc.setBlock(x,y-1,z,41)
        mc.setBlock(   x+3+i*mult,y-1,z+3,89)
        mc.spawnEntity(x+3+i*mult,y+3,z+3,i)

# x,y,z = pos = mc.player.getTilePos()
# x,y,z = pos = 0,0,0
# mc.setBlock(x,y-1,z, 152)
# mc.setBlock(x, y+3, z, block.GLOWSTONE_BLOCK.id)
# mc.player.setTilePos(pos)
# for i in range (0, 1000, 1):
#    mc.setBlock(x+2,y+5,z+2, i)
#    time.sleep(0.1)

# x,y,z = pos = mc.player.getTilePos()
# mc.player.setTilePos(x,y+100,z)

# while True:
#     x,y,z = mc.player.getTilePos()
#     print("x="+str(x) + " y="+str(y) + " z="+str(z))
#     time.sleep(1)
