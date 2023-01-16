from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

def sand_to_air(x):
    if x in blocks:
        x = 0
    return x

blocks = [1,2,3,4,8,9,12,13,24]
x,y,z = pos = mc.player.getTilePos()
# x,y,z = pos = 0,0,0
print("Position is: ", pos)
y=0
lenght = int(input("Длина: "))
width  = int(input("Ширина: "))
depth  = int(input("Высота: "))

delta_x = x+lenght
delta_y = y+depth
delta_z = z+width
block = 0
m = 0

now = list(mc.getBlocks(pos, delta_x-1, delta_y-1, delta_z-1))
# print(now)
new = list(map(sand_to_air, now))
# print(new)
time.sleep(5)
for dy in range(y,delta_y):
    for dx in range(x,delta_x):
         for dz in range(z,delta_z):
            boom = dx,dy,dz
            target = new[m]
            mc.setBlock(boom, target)
            m += 1