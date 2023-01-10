import time
from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()

# mc.player.setDirection(1,1,1)
while True:
   time.sleep(1)

   ## ## ## Детектор того, что под ногами ## ## ##
   pos = mc.player.getTilePos()
   x,y,z = pos.x,pos.y,pos.z

   for i in range(0,30):
      blocks = (15, 16, 21, 56, 73, 129)
      target = mc.getBlock(x,y-i,z)
      if target in blocks:
         print("Block: " + str(target), " x=" + str(x), " y=" + str(y-i), " z=" + str(z))
         mc.setBlock( x, y+2, z, 89)
         mc.setBlock( x, y+5, z, 9)
         mc.setBlocks(x, y, z, x, y-i+1, z, 0)
         mc.setBlock( x, y-i+3, z, 89)
         mc.setBlock( x, y-i+4, z, 165)


         # mc.postToChat(i)
         # mc.postToChat(target)


   # pos = mc.player.getDirection()
   # mc.postToChat("x="+str(pos.x) + " y="+str(pos.y) + " z="+str(pos.z))

   # pos = mc.player.getPitch()
   # mc.postToChat(pos)

