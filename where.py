import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# import mcpi.entity as entity
# import mcpi.block as block

# x = 0
# y = 0
# z = 0
# mc.player.setPos(x,y,z)

while True:
   time.sleep(2)
   pos = mc.player.getTilePos()
   print("pos: x:{},y:{},z:{}".format(pos.x,pos.y,pos.z))
   # rot = mc.player.getRotation()
   # mc.postToChat(rot)