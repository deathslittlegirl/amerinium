import os
import random
import amatomic as ama
import amplanets as amp
import asyncio


class qdb():
    
    # Quantative Database
    
    md = [ ama.THC.quantity, ama.Psycilobin.quantity, ama.Dextromethorphan.quantity, ama.Diphenhydramine.quantity ] # (matter) Drugs
    mg = [ ama.Ammonia.quantity, ama.Helium.quantity, ama.Hydrogen.quantity, ama.Methane.quantity, ama.Sulfur.quantity ] # Gases
    mm = [ ama.Meteorite.quantity, ama.MR.quantity, ama.Junk.quantity ] # Misc
    ms = [ ama.Femininium.quantity, ama.Angelium.quantity ] # Special
    msp = [ ama.Silver.quantity, ama.Gold.quantity, ama.Diamond.quantity, ama.Platinum.quantity ] # Special+

class ndb():
   
   # Name Database
   
    mdn = [ ama.THC.name, ama.Psycilobin.name, ama.Dextromethorphan.name, ama.Diphenhydramine.name ] # (matter) Drug names
    mgn = [ ama.Ammonia.name, ama.Helium.name, ama.Hydrogen.name, ama.Methane.name, ama.Sulfur.name ] # Gas names
    mmn = [ ama.Meteorite.name, ama.MR.name, ama.Junk.name ] # Miscellaneous names
    msn = [ ama.Femininium.name, ama.Angelium.name ] # Special names 
    mspn = [ ama.Silver.name, ama.Gold.name, ama.Diamond.name, ama.Platinum.name ] # Special+ names

