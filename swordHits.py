from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

time.sleep(10)

blockHits = mc.events.pollBlockHits()

print(str(blockHits))

blockHitsLength = len(blockHits)
mc.postToChat("Your Score is " + str(blockHitsLength))
