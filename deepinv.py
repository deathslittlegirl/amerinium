import os, shelve, asyncio
import amatomic as ama
import amplanets as amp

class qdb():
    
    # Quantative Database
    
    md = [ ama.THC.quantity, ama.Psycilobin.quantity, ama.Dextromethorphan.quantity, ama.Diphenhydramine.quantity ] # (matter) Drugs
    mg = [ ama.Ammonia.quantity, ama.Helium.quantity, ama.Hydrogen.quantity, ama.Methane.quantity, ama.Sulfur.quantity ] # Gases
    mm = [ ama.Meteorite.quantity, ama.MR.quantity, ama.Junk.quantity ] # Misc
    ms = [ ama.Femininium.quantity, ama.Angelium.quantity ] # Special
    msp = [ ama.Diamond.quantity  ] # Special+
    mmtl = [ ama.Iron.quantity, ama.Gold.quantity, ama.Silver.quantity,  ama.Platinum.quantity ] # (matter) Metal
    
    async def gemstones():
        
        with shelve.open('saves/gems') as gemmy:
        
            gemmy['THC Crystals'] = qdb.md[0]
            gemmy['Psycilobin'] = qdb.md[1]
            gemmy['Dextromethorphan'] = qdb.md[2]
            gemmy['Diphenhydramine'] = qdb.md[3]
            
            gemmy['Iron'] = qdb.mmtl[0]
            gemmy['Gold'] = qdb.mmtl[1]
            gemmy['Silver'] = qdb.mmtl[2]
            gemmy['Platinum'] = qdb.mmtl[3]
            
            gemmy['Ammonia'] = qdb.mg[0]
            gemmy['Helium'] = qdb.mg[1]
            gemmy['Hydrogen'] = qdb.mg[2]
            gemmy['Methane'] = qdb.mg[3]
            gemmy['Sulfur'] = qdb.mg[4]
            
            gemmy['Diamond'] = qdb.msp[0]
            
            gemmy['Femininium'] = qdb.ms[0]
            gemmy['Angelium'] = qdb.ms[1]
        
            gemmy['Meteorite'] = qdb.mm[0]
            gemmy['Moon Rocks'] = qdb.mm[1]
            gemmy['Junk'] = qdb.mm[2]
    
    
            

class ndb():
   
   # Name Database
   
    mdn = [ ama.THC.name, ama.Psycilobin.name, ama.Dextromethorphan.name, ama.Diphenhydramine.name ] # (matter) Drug names
    mgn = [ ama.Ammonia.name, ama.Helium.name, ama.Hydrogen.name, ama.Methane.name, ama.Sulfur.name ] # Gas names
    mmn = [ ama.Meteorite.name, ama.MR.name, ama.Junk.name ] # Miscellaneous names
    msn = [ ama.Femininium.name, ama.Angelium.name ] # Special names 
    mspn = [ ama.Diamond.name ] # Special+ names
    mmtln = [ ama.Iron.name, ama.Gold.name, ama.Silver.name,  ama.Platinum.name ] # (matter) Metal names


    async def displayinv():

        with shelve.open('saves/gems') as gems:
            
            debase = {'THC Crystals': qdb.md[0],
                      'Psycilobin': qdb.md[1],
                      'Dextromethorphan': qdb.md[2],
                      'Diphenhydramine': qdb.md[3],
                      
                      'Iron': qdb.mmtl[0],
                      'Gold': qdb.mmtl[1],
                      'Silver': qdb.mmtl[2],
                      'Platnium': qdb.mmtl[3],
                      
                      'Ammonia': qdb.mg[0],
                      'Helium': qdb.mg[1],
                      'Hydrogen': qdb.mg[2],
                      'Methane': qdb.mg[3],
                      'Sulfur': qdb.mg[4],
                      
                      'Diamond': qdb.msp[0],
                      
                      'Femininium': qdb.ms[0],
                      'Angelium': qdb.ms[1],
                      
                      'Meteorite': qdb.mm[0],
                      'Moon Rocks': qdb.mm[1],
                      'Junk': qdb.mm[2] }
            
            gems.update(debase)
            print('Updating contents...')
            
            await asyncio.sleep(2) 
                   
            drg0 = "THC Crystals: {}\n \bPsycilobin: {}\n \bDXM Crystals: {}\n \bDPH Crystals: {}\n"
            
            print(drg0.format(str(gems.get('THC Crystals')), str(gems.get('Psycilobin')), str(gems.get('Dextromethorphan')), str(gems.get('Diphenhydramine'))))
            
         