from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

while True:
    x += random.uniform(-0.2, 0.2)
    z += random.uniform(-0.4, 0.4)
    y = mc.getHeight(x, z)

    mc.player.setPos(x, y, z)
    time.sleep(0.1)
                    
