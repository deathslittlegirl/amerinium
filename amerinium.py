import random
import os
import asyncio
import shelve
from unittest import result

# game files

import amatomic as ama
import amplanets
from time import sleep

from amplanets import Marici, Piscea

class Positioning():
    position = shelve.open('saves/locatio')   
    location = Piscea
    position['planet'] = location
    location_name = Piscea.name
    position['pl_name'] = location_name
    position_up = {'planet': location, 'pl_name': location_name}
    position.update(position_up)
    

    



class economy:

    price_one = Positioning.location.materials_price[0] / ama.Amerinium.flux
    price_two = Positioning.location.materials_price[1] / ama.Amerinium.flux
    price_three = Positioning.location.materials_price[2] / ama.Amerinium.flux

class Shield1:

    # Shield1 (messy name ik) is later imported to 'shield' by PS.
    # The same will go for every other shield.

    name = "TH DOS 20"
    density = 35
    d_up = 32
    surface = "ribbed, transient"


class enemyShield:

    name = "TH DOS 20"
    density = 35
    d_up = 32
    surface = "ribbed, transient"


class wallet:

    name = "Beartech Money Packager"
    
    size = 10 
    process_delay = random.randint(3, 5)
    money = 0 
    bank = 0
    
    if os.path.exists('saves/shmoney'):
        with shelve.open('saves/shmoney') as shmoney:
            size = shmoney['size']
            process_delay = shmoney['process_delay'] 
            money = shmoney['money']
            bank = shmoney['bank'] 
    else:
        with shelve.open('saves/shmoney') as shmoney:
            shmoney['size'] = size
            shmoney['process_delay'] = process_delay
            shmoney['money'] = money
            shmoney['bank'] = bank
    
    if os.path.exists('saves/shmoney'): 
        with shelve.open('saves/shmoney') as shmoney:
            size = 10 + shmoney.get('size')
            process_delay = random.randint(3, 5)
            money = 0 + shmoney.get('money')
            bank = 0 + shmoney.get('bank')
    
       
    async def deposit():
        print('Initiating deposit of +', str(wallet.money))
        await asyncio.sleep(wallet.process_delay)
        wallet.bank = wallet.bank + wallet.money
        print("Æ: +" + str(wallet.money))
        wallet.money = 0
    
    
    def walsave():
         
        with shelve.open('saves/shmoney') as shmoney:
            moneyup = { 'size': wallet.size, 'process_delay': wallet.process_delay,
                   'money': wallet.money, 'bank': wallet.bank }
            shmoney.update(moneyup)    
        
        

class lsCannon:

    name = "AW MK II"


    # Normal Mode
    dmg = random.randrange(2, 20)
    crit = random.randrange(14, 23)
    price = 40


    # Super Mode, needs locked_on = True
    locked_on = False
    super_dmg = random.randrange(18, 30)
    super_crit = random.randrange(18, 48)
    super_price = 60


class Inv:
    
    name = 'Beartech Organizer'
    max_space = 18


    # Defining

    # Positioning.location.materials[0] = 0
    # Positioning.location.materials[1] = 0
    # Positioning.location.materials[2] = 0
    
    sell_rate = 1
    
    # If the save file already exists, switch the variables to read information from the save file instead of memory.
    # Otherwise, create the save file by storing quantative variables into the database.
    # Then, if the save file exists intact, concatenate the data into memory to display the current amount of materials you're mining.
    
    if os.path.exists('saves/invsave'):
            
        with shelve.open('saves/invsave') as invsh:
            
                Positioning.location.materials[0] = invsh['Material 0 Count']
                Positioning.location.materials[1] = invsh['Material 1 Count']
                Positioning.location.materials[2] = invsh['Material 2 Count']
                sell_rate = invsh['sell_rate']
    else:
        
        with shelve.open('saves/invsave') as invsh:
            
            invsh['Material 0 Count'] = Positioning.location.materials[0]
            invsh['Material 1 Count'] = Positioning.location.materials[1]
            invsh['Material 2 Count'] = Positioning.location.materials[2]
            invsh['sell_rate'] = sell_rate
            
    if os.path.exists('saves/invsave'):
        
        with shelve.open('saves/invsave') as invsh:   
             
            m_one = invsh.get('Material 0 Count')
            m_two = invsh.get('Material 1 Count')
            m_three = invsh.get('Material 2 Count')
            sell_rate = invsh.get('sell_rate')
        
    async def insave():
        
        # Update inventory database with new information.
        
        with shelve.open('saves/invsave') as invsh:
            
            invchange = { 'Material 0 Count':int(Inv.m_one), 
                         'Material 1 Count':int(Inv.m_two), 
                         'Material 2 Count':int(Inv.m_three) }
            
            invsh.update(invchange)

    
    
    async def sell():
       
        while True:
            
            print("Determining ÆFLX...")
            await ama.Amerinium.fluxuation()
            await asyncio.sleep(1)
            print("ÆFLX:", ama.Amerinium.flux)
            
            # For every number of materials that player possesses, that material is sold for its price and depleted by 1.

            for i in Inv.m_one, Inv.m_two, Inv.m_three:
    

                if i == Inv.m_one:
                    
                    # If the material available to be sold totals to zero, passthrough.
                    # Otherwise, sell the material according to the quantity rate and the current price of the material.
                    
                    if Inv.m_one <= 0:
                        pass
                    
                    else:
                        
                        print(Positioning.location.materials_name[0] + ":", "-" + str(Inv.sell_rate), "from", str(Inv.m_one)) # "THC Crystals: -3 from 5"
                        
                        Inv.m_one -= Inv.sell_rate
                        wallet.money += economy.price_one
                        print("財布:", "Æ" + str(wallet.money))

                elif i == Inv.m_two:
                    
                    if Inv.m_two <= 0:
                        pass
                    
                    else:    
                        print(Positioning.location.materials_name[1] + ":", "-" + str(Inv.sell_rate), "from", str(Inv.m_two))
                        Inv.m_two -= Inv.sell_rate
                        wallet.money += economy.price_two
                        print("財布:", "Æ" + str(wallet.money))

                elif i == Inv.m_three:
                    
                    if Inv.m_three <= 0:
                        pass
                    
                    else:  
                        print(Positioning.location.materials_name[2] + ":", "-" + str(Inv.sell_rate), "from", str(Inv.m_three))
                        Inv.m_three -= Inv.sell_rate
                        wallet.money += economy.price_three
                        print("財布:", "Æ" + str(wallet.money))
                
                if Inv.m_one + Inv.m_two + Inv.m_three == 0:
                    print("Inventory empty... Exiting.")
                    sleep(1)
                    break

                await asyncio.sleep(wallet.process_delay)

            if wallet.money == wallet.size:
                
                sleep(wallet.process_delay)
                print("Wallet full, depositing Amerinium to bank.")
                sleep(1)
                await wallet.deposit()
                break

            else:
                break

    
        
class ESP:

    health = 100
    armor = 50
    shield = Shield1()
    weapon = lsCannon()
    detected = False
    engaged = False
    spawned = False

    

    def armor_sw():

        if random.randint(1, 100) == 45:
            ESP.armor -= random.randrange(2, 4)
        else:
            ESP.armor -= random.randrange(4, 10)
    
    def shield_dmg():

        if enemyShield.density < 0:
            ESP.armor_sw()

        else:
            enemyShield.density -= 3.5

    def dmg_esp():

        if ESP.armor == 0:
            ESP.health -= 10

        else:
            ESP.armor_sw()

class Miner:

    name = "LSP-1000"

    strength = random.randint(2, 3)
    speed = random.randint(3, 7)

    async def mining():
        print("Mining", Positioning.location_name + "...")
        sleep(2)
        
        
        # If any of the materials collected are at zero or below zero, make sure they are zero.
        
        if Inv.m_one <= 0:
            Inv.m_one = 0
            
        if Inv.m_two <= 0:
            Inv.m_two = 0
            
        if Inv.m_three <= 0:
            Inv.m_three = 0

        for n in range(8):
            
            # Flips a coin to decide randomly which material is mined from the current planet. 
            # a is material one, b is material two, c is material three, and so on.

            flip = [ 'a', 'b', 'c' ]
            
            

            if random.choice(flip) == 'a':
                
                if Inv.m_one == Inv.max_space:
                    return
                
                else:
                    Inv.m_one += Miner.strength
                    
                print(Inv.m_one, Positioning.location.materials_name[0], "collected.")

                await asyncio.sleep(Miner.speed)


            elif random.choice(flip) == 'b':

                if Inv.m_two == Inv.max_space:
                    return

                else:
                    Inv.m_two += Miner.strength

                print(Inv.m_two, Positioning.location.materials_name[1], "collected.")

                await asyncio.sleep(Miner.speed)


            elif random.choice(flip) == 'c':

                if Inv.m_three == Inv.max_space:
                    return

                else:
                    Inv.m_three += Miner.strength

                print(Inv.m_three, Positioning.location.materials_name[2], "collected.")
            
                await asyncio.sleep(Miner.speed)
    
    
    #with shelve.open('minersh') as minersh: 
        # minersh['minerstrength'] = strength
       #  minersh['minerspeed'] = speed
       # mineup = {'minerstrength':strength, 
                 # 'minerspeed':speed }
        # minersh.update(mineup)
        

class PS:

    name = "Calcula I"
    health = 100
    armor = 50
    shield = Shield1()
    inventory = Inv()
    weapon = lsCannon()
    in_combat = False

    def shield_dmg():

        if Shield1.density <= 0:
            PS.armor_sw()

        else:
            Shield1.density -= 3.5

    def armor_sw():
        
        # 45% to mitigate some damage with armor. 

        if random.randint(1, 100) == 45:
            PS.armor -= random.randrange(2, 3)
        else:
            PS.armor -= random.randrange(4, 10)

    def dmg_esp():

        if ESP.armor == 0:
            ESP.health -= 10

        else:
            ESP.armor_sw()
            
    with shelve.open('saves/ship') as shipsave:
        shipsave['health'] = health
        shipsave['shield'] = shield.density
        shipsave['armor'] = armor
        shipsave['incombat'] = in_combat
        upship = {'health': health, 'shield': shield, 'armor': armor, 'incombat': in_combat }
        shipsave.update(upship)


class Shop:

    name = "The Midnight Bliss™️ E-Shop"
    comfort_msg = "Welcome to " + name + "."

    # Upgrade Prices

    health_up = 100
    shield_up = 100
    inv_up = 42
    wallet_up = 60
    sell_price = 15
    
    with shelve.open('saves/gucci') as gucci:
        gucci['health_up'] = health_up
        gucci['shield_up'] = shield_up
        gucci['inv_up'] = inv_up
        gucci['wallet_up'] = wallet_up
        gucci['sell_price'] = sell_price

    # Functions

    def online():
        print(Shop.comfort_msg)
        sleep(3)
        print("Æ", wallet.bank)
        sleep(2)


    def listing():
        print('++:', Shop.health_up) # Print health price
        sleep(2)
        print('shi+:', Shop.shield_up)
        sleep(2)
        print('inv+:', Shop.inv_up)
        sleep(2)
        print('$$$+:', Shop.wallet_up)
        sleep(2)
        print('$R:', Shop.sell_price)

    def shield_upgrade():

        while wallet.bank >= Shop.shield_up:
            wallet.bank -= Shop.shield_up
            sleep(2)
            PS.shield.density = PS.shield.density * 2
            print("SHI:", str(PS.shield.density))
            PS.shipsave.update(PS.upship)
            wallet.walsave()
            break

    def inv_upgrade():

        while wallet.bank > Shop.inv_up:
            wallet.bank -= Shop.inv_up
            sleep(2)
            PS.inventory.max_space = PS.inventory.max_space * 2
            print("INV:", str(PS.inventory.max_space))
            Inv.insave()
            wallet.walsave()
            break

    def health_upgrade():

        while wallet.bank >= Shop.health_up:
            wallet.bank -= Shop.health_up
            sleep(2)
            PS.health = PS.health * 1.5
            print('+::', str(PS.health))
            wallet.walsave()
            break

    def money_upgrade():

        while wallet.bank >= Shop.wallet_up:
            wallet.bank -= Shop.wallet_up
            sleep(2)
            wallet.size = wallet.size * 1.3
            print("$$$: Expanded to Æ", str(wallet.size))
            wallet.walsave()
            break
    
    def sell_up():
        
        while wallet.bank >= Shop.sell_price:
            wallet.bank -= Shop.sell_price
            sleep(2)
            Inv.sell_rate = Inv.sell_rate + 2
            print("$R: +" + str(Inv.sell_rate))
            wallet.walsave()
            break
        
        
class CIT:

    offense = [ 'attack', 'scan', 'ff', 'ps' ]
    off_sp = [ 'sp.a', 'cat',  'aim' ] # cat = capture
    defense = ['sh']
    
    def attacking():
        while True:
            
            CITF = input("CIT: ")
            
            if CITF == CIT.offense[0]:
                ESP.dmg_esp()
            
            if CITF == CIT.offense[2]:
                break
            
            if CITF == CIT.off_sp[2]:
                lsCannon.locked_on = True
                
            if CITF == CIT.offense[3]:
                if lsCannon.locked_on == True:
                    ESP.health -= 30
                else: 
                    pass
    
                
    async def spawn():
        if random.randrange(1, 100) == 45:
            ESP.engaged = True
            
        if ESP.engaged == True:
            CIT.attacking()
        
        else:
            pass

class IT:

    # Various commands

    utility = [ 'mine', 'scan', 'travel', 'automine', 'sell' ]
    shop = [ 'shop', '++', 'shi+', 'inv+', '$$$+', '$R' ]
    diag = [ 'health', 'shield', 'inventory' ]
    money = [ 'wallet', 'deposit' ]

    command = ""

    while command != "kill":

        command = input("""司令官: """)

        while command == utility[0]:
            asyncio.run(Miner.mining())
            asyncio.run(Inv.insave())
            asyncio.run(CIT.spawn())            
            command = ""


        while command == utility[2]:
            zyX = input("X, Y: ")

            if zyX == str(amplanets.Piscea.coordinates):
                Positioning.location = Piscea
                Positioning.location_name = Piscea.name
                amplanets.Piscea.arrival()
                Positioning.position.update(Positioning.position_up)
                CIT.spawn()
                command = ""

            else:
                command = ""
            
            if zyX == (amplanets.Marici.coordinates):
                Positioning.location = amplanets.Marici
                Positioning.location_name = amplanets.Marici.name
                amplanets.Marici.arrival()
                Positioning.position.update(Positioning.position_up)
                asyncio.run(CIT.spawn())  
                command = ""
            
            else:
                CIT.spawn()
                command = ""

        while command == utility[4]:
            asyncio.run(Inv.sell())
            wallet.walsave()
            asyncio.run(Inv.insave())
            asyncio.run(CIT.spawn())  
            command = ""

        while command == diag[0]:
            print("Health:", PS.health)
            asyncio.run(CIT.spawn())  
            command = ""

        while command == diag[1]:
            print("Shield:", PS.shield.density)
            asyncio.run(CIT.spawn())  
            command = ""

        while command == money[1]:
            asyncio.run(wallet.deposit())
            wallet.walsave()
            asyncio.run(CIT.spawn())  
            command = ""


        # Shop Commands

        while command == shop[0]:
            print('Logging on...')
            sleep(2)
            Shop.online()
            Shop.listing()
            
            command = ""


        while command == shop[1]:
            print("Upgrading", PS.name + "'s", 'health')
            Shop.health_upgrade()
            
            command = ""

        while command == shop[2]:
            print("Upgrading", Shield1.name)
            Shop.shield_upgrade()
            
            command = ""

        while command == shop[3]:
            print("Upgrading inventory...")
            Shop.inv_upgrade()
            
            command = ""

        while command == shop[4]:
            print("Upgrading", wallet.name)
            Shop.money_upgrade()
            
            command = ""
            
        while command == shop[5]:
            print("Upgrading", Inv.name, "sell rate.")
            Shop.sell_up()
            
            command = ""

        while command == "clear":
            os.system('clear')
            
            command = ""
            
        else:
            pass





        
