import amatomic as ama
import random as rnd
from time import sleep
import asyncio
import deepinv as di

class Piscea():

    name = "Piscea V"
    materials = [ di.qdb.md[0], di.qdb.ms[0], di.qdb.msp[0] ]
    materials_name = [ di.ndb.mdn[0],  di.ndb.msn[0], di.ndb.mspn[0] ]
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
    materials = [ di.qdb.mmtl[3], di.qdb.mg[4], di.qdb.mg[0] ]
    materials_name = [ di.ndb.mmtln[3], di.ndb.mgn[4], di.ndb.mgn[0] ]
    materials_price = [ ama.Platinum.cost, ama.Sulfur.cost, ama.Ammonia.cost ]
    surface = "Rocky, dark-red hue from carbon-dioxide, argon-filled atmosphere."
    smell = "Fiery, sharp air. Very unwavering, machine-like scent."
    rings = True
    breathable = False
    coordinates = "60, 30" 


    def arrival():
        print("You are now at", Marici.name)