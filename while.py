# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:00:31 2020

@author: user
"""
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True: 
    x,y,z=mc.player.getTilePos()
    mc.postToChat("我正在看著你x:"+str(x)+"y"str(y)+"z:"+str(z))
    time.sleep(0.5)