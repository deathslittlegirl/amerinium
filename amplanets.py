import amatomic as ama
import random as rnd
from time import sleep
import asyncio
import deepinv as di

class Pleroma:

    matter_d = ama.THC, ama.Psycilobin, ama.Dextromethorphan, ama.Diphenhydramine
    matter_g = ama.Ammonia, ama.Helium, ama.Hydrogen, ama.Methane, ama.Sulfur
    matter_m = ama.Meteorite, ama.MR, ama.Junk
    matter_s = ama.Femininium, ama.Angelium
    matter_sp = ama.Silver, ama.Gold, ama.Diamond, ama.Platinum

#def d_select():

       #for i in range(1, 25):
           #drg = rnd.choice(Pleroma.matter_d)

          # if i == 8:
            #   drg = rnd.choice(Pleroma.matter_d)

class Piscea():

    name = "Piscea V"
    materials = [ di.qdb.md[0], di.qdb.ms[0], di.qdb.msp[2] ]
    materials_name = [ di.ndb.mdn[0],  di.ndb.msn[0], di.ndb.mspn[2] ]
    materials_price = [ ama.THC.cost, ama.Femininium.cost, ama.Diamond.cost ]
    surface = "Watery, rainbow hue from multi-shifting, drug-addled atmosphere."
    smell = "Perfume-like, swathed in neptunian breeze, hard candy."
    rings = True
    breathable = True
    coordinates = "34, 77" # coordinates


    def arrival():
        print("You are now at", Piscea.name)

class Marici():

    name = "Marici VII"
    materials = [ di.qdb.msp[3], di.qdb.mg[4], di.qdb.mg[0] ]
    materials_name = [ di.ndb.mspn[3], di.ndb.mgn[4], di.ndb.mgn[0] ]
    materials_price = [ ama.Platinum.cost, ama.Sulfur.cost, ama.Ammonia.cost ]
    surface = "Rocky, dark-red hue from carbon-dioxide, argon-filled atmosphere."
    smell = "Fiery, sharp air. Very unwavering, machine-like scent."
    rings = True
    breathable = False
    coordinates = "60, 30" 


    def arrival():
        print("You are now at", Marici.name)