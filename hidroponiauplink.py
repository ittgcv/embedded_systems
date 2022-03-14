#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:38:10 2020

@author: nautica
"""

import anvil.server

anvil.server.connect("EYA6TX3VCDONXTVLLD2DIWYT-JPJLTXCWW2KTBATI")

@anvil.server.callable
def say_hello(name):
  print("Hello from the uplink, %s!" % name)

@anvil.server.callable
def leer_sensor():
    humedad=20
    return humedad
anvil.server.wait_forever()