from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def my_func(x):
    # blocks = [5,14,15,16,17,(17,1),(17,2),(17,3),21,37,38,39,40,56,73,129]
    # if x not in blocks:
    if x==1: x=152
    print ("fn x: ",x)
    return x

x,y,z = pos = mc.player.getTilePos()

h = 3
now = mc.getBlocks(pos, x+h, y+h, z+h)
new = map(my_func, now)
mc.setBlocks(new)