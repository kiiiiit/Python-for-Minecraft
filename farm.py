# import mcpi.block
import time
from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
mc = Minecraft.create("192.168.50.11", 4711)

wall = 155
air = 0
farmland = 60
water = 9
torch = 50
index_seed = 0

def farmzone(x, y, z, height, sed):
	delta = 4
	mc.setBlocks(x-delta, y, z-delta, x+delta, height, 	z+delta, air)
	mc.setBlocks(x-delta, y, z-delta, x+delta, y, 		z+delta, wall)
	for i in range(3):
		for j in range(3):
			mc.setBlock(x - delta + delta*i, y+1, z - delta + delta * j, torch)
	mc.setBlocks(x-delta+1, y,   z-delta+1, x+delta-1, y,   z+delta-1, farmland)
	mc.setBlocks(x-delta+1, y+1, z-delta+1, x+delta-1, y+1, z+delta-1, sed)
	mc.setBlock(x, y, z, water)

qual_lands = int(input("Введите количество требуемых полей: "))
qual_levels = int(input("Введите количество требуемых этажей: "))
lenght = qual_lands * 9 - 1
mc.postToChat(f"Get in the center. ({lenght}x{lenght})")
time.sleep(5)
mc.postToChat("Time is over.")
x, y, z = pos = mc.player.getTilePos()

height = []
for i in range(x-lenght//2+1, x+lenght//2+1):
	for j in range(z-lenght//2+1, z+lenght//2+1):
		height.append(mc.getHeight(i,j))

min_height = min(height)
if not(min_height > y):
	y = min_height

max_height = max(height)
x0 = x - lenght//2+1
z0 = z - lenght//2+1
ylevel = y
print(qual_levels-1)
for level in range(qual_levels):
	ylevel += 4
	xi = x0
	for i in range(qual_lands):
		xi += 9-1
		zj = z0
		for j in range(qual_lands):
			zj += 9-1
			seed = [59, 142, 141, 104, 105]
			farmzone(xi, ylevel, zj, max_height, seed[index_seed])
			if (index_seed < 4):
				index_seed += 1
			else:
				index_seed = 0