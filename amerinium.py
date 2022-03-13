import random, os, asyncio, shelve, time
import threading as th



# game files

import amatomic as ama
import amplanets
from time import sleep
import deepinv as di

from amplanets import Piscea

location = Piscea
location = Piscea.name

if os.path.exists('saves/locatio'):
    with shelve.open('saves/locatio') as locatio:
        location = locatio.get('planet')
        location_name = locatio.get('pl_name')

else:
    location = Piscea
    location_name = Piscea.name
    


class economy:

    price_one = location.materials_price[0] / ama.Amerinium.flux
    price_two = location.materials_price[1] / ama.Amerinium.flux
    price_three = location.materials_price[2] / ama.Amerinium.flux

class Shield1:

    # Shield1 (messy name ik) is later imported to 'shield' by PS.
    # The same will go for every other shield.

    name = "TH DOS 20"
    density = 35
    deployed = False
    battery = 3
    surface = "ribbed, transient"
    
    async def recharge():
        
        global battery
        
        print("Recharging shield battery...", end="\n")
        for i in range(3):
            Shield1.battery += 1
            print("Battery:", Shield1.battery, end="\r")
            await asyncio.sleep(1)
        


class enemyShield:

    name = "TH DOS 20"
    density = 35
    deployed = False
    
    surface = "ribbed, transient"
    
    
class wallet:

    name = "Beartech Money Packager"
    
    size = 10 
    process_delay = random.randint(3, 5)
    money = 0 
    bank = 0
        
    with shelve.open('saves/shmoney', 'c') as shmoney:
        shmoney['size'] = size
        shmoney['process_delay'] = process_delay
        shmoney['money'] = money
        shmoney['bank'] = bank
    
    
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
    dmg = random.randrange(2, 10)
    crit = random.randrange(14, 23)
    price = 40
    ammo = 6


    # Super Mode, needs locked_on = True
    locked_on = False
    super_dmg = random.randrange(18, 30)
    super_crit = random.randrange(18, 48)
    super_ammo = 4
    super_price = 60
    
    
    async def recharge():
        
        print("(S)RC Initialized", end="\n")
        await asyncio.sleep(1)
        
        for i in range(4):
            
            lsCannon.super_ammo += 1
            print("PS(s):", lsCannon.super_ammo, end="\r")
            await asyncio.sleep(1)
            
    async def saim():
        
        print("Aiming special cannon...")
        await asyncio.sleep(2)
        
        # If rings around the planet exist, they can damage the ship. and stop the cannon's charge.
        while location.rings == True:
                    
            if random.randint(1, 100) <= 25: # if coin lands on side b or c
                
                if PS.shield.deployed == True: # and the shield is deployed
                    if PS.shield.health > 0: # and the shield health is above zero
                        PS.shield.health -= 8 # remove five health points from the shield
                        
                        print("Debris from the rings of", str(location.name), "have damaged your ship.")
                        await asyncio.sleep(2)
                        print("Ys: -2")
                        await asyncio.sleep(2)
                        print("Cannon not charged...")
                        await asyncio.sleep(2)
                        break
                        
                    elif PS.armor > 0:
                        PS.armor -= 3
                        
                        print("Debris from the rings of", str(location.name), "have damaged your ship.")
                        await asyncio.sleep(2)
                        
                        print("Y+: -2")
                        await asyncio.sleep(2)
                        
                        print("Cannon not charged...")
                        await asyncio.sleep(2)
                        break
                    
                    else:
                    
                        PS.health -= 5
                        
                        print("Debris from the rings of", str(location.name), "have damaged your ship.")
                        await asyncio.sleep(2)
                        
                        print("Y++: -2")
                        await asyncio.sleep(2)
                        
                        print("Cannon not charged...")
                        await asyncio.sleep(2)
                        break
                else:
                    lsCannon.locked_on = True
                    print("Locked on...")
                    await asyncio.sleep(2)
                    break
            
                    
            
                   
        else:
            while location.rings == False:
                
                flip = [ 'a', 'b', 'c' ]
            
            if random.choice(flip) == flip[0]: # if coin lands on side b or c
                
                if PS.shield.deployed == True: # and the shield is deployed
                    if PS.shield.health > 0: # and the shield health is above zero
                        await PS.shield_dmg()

                        print("Cannon not charged...")
                        await asyncio.sleep(2)
                        
                elif PS.armor > 0:
                    PS.attacked() 
                    print("Cannon not charged...")
                    await asyncio.sleep(2)
                    
                else:
                    PS.attacked() 
                    print("Cannon not charged...")
                    await asyncio.sleep(2)
                
            elif random.choice(flip) == flip[2]:
                lsCannon.locked_on = True
                print("Locked on...")
                await asyncio.sleep(2)
                    
                
               
            
                print("Cannon not charged...")
                await asyncio.sleep(2)
                
            else:
                PS.attacked() 
                print("Cannon not charged...")
                await asyncio.sleep(2)
    


class Inv:
    
    name = 'Beartech Organizer'
    max_space = 18


    # Defining
    
    sell_rate = 1
    
    # If the save file already exists, switch the variables to read information from the save file instead of memory.
    # Otherwise, create the save file by storing quantative variables into the database.
    # Then, if the save file exists intact, concatenate the data into memory to display the current amount of materials you're mining.
    
   # if os.path.exists('saves/gems'):
   
    with shelve.open('saves/gems', 'c') as gems:
        
        mtn = [ location.materials_name[0], location.materials_name[1], location.materials[2] ]
        mt = [ location.materials[0], location.materials[1], location.materials[2] ]
        gems[str(mtn[0])] = mt[0]
        gems[str(mtn[1])] = mt[1]
        gems[str(mtn[2])] = mt[2]
        gems['sell_rate'] = sell_rate
   
        m_one = gems.get(str(mtn[0]))
        m_two = gems.get(str(mtn[1]))
        m_three = gems.get(str(mtn[2]))
        sell_rate = gems.get('sell_rate')
    
        
    async def insave():
        
        # Update inventory database with new information.
        
        with shelve.open('saves/gems') as gems:
            
            invchange = { str(Inv.mtn[0]): int(Inv.m_one), 
                        str(Inv.mtn[1]): int(Inv.m_two), 
                         str(Inv.mtn[2]): int(Inv.m_three) }
            
            gems.update(invchange)

    
    
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
                        
                        print(location.materials_name[0] + ":", "-" + str(Inv.sell_rate), "from", str(Inv.m_one)) # "THC Crystals: -3 from 5"
                        Inv.m_one -= Inv.sell_rate
                        wallet.money += economy.price_one
                        print("財布:", "Æ" + str(wallet.money))

                elif i == Inv.m_two:
                    
                    if Inv.m_two <= 0:
                        pass
                    
                    else:    
                        print(location.materials_name[1] + ":", "-" + str(Inv.sell_rate), "from", str(Inv.m_two))
                        Inv.m_two -= Inv.sell_rate
                        wallet.money += economy.price_two
                        print("財布:", "Æ" + str(wallet.money))
                        

                elif i == Inv.m_three:
                    
                    if Inv.m_three <= 0:
                        pass
                    
                    else:  
                        print(location.materials_name[2] + ":", "-" + str(Inv.sell_rate), "from", str(Inv.m_three))
                        Inv.m_three -= Inv.sell_rate
                        wallet.money += economy.price_three
                        print("財布:", "Æ" + str(wallet.money))
                        
                
                if Inv.m_one + Inv.m_two + Inv.m_three == 0:
                    print("Inventory empty... Exiting.")
                    sleep(1)
                    break
                Inv.gems.close()
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

    health = 30
    armor = 20
    shield = Shield1()
    weapon = lsCannon()
    detected = False
    engaged = False
    spawned = False
    armorblock = 38
    
    if health <= 0:
        health = 0

    

    async def armor_sw():
        
        while True:

            if random.randint(1, 100) <= ESP.armorblock:
            
                if ESP.armor - random.randrange(2, 4) <= 0:
                    ESP.armor = 0
                    print('E+: -+', str(ESP.armor - random.randrange(2, 4)))
                    await asyncio.sleep(2)
                    break
                    
                
                else:
                    ESP.armor -= random.randrange(2, 4)
                    
                    print('E+: -+', str(ESP.armor - random.randrange(2, 4)))
                    await asyncio.sleep(2)
                    
                    break
                
            elif ESP.armor - lsCannon.dmg <= 0:
                ESP.armor = 0 
                print('E+: -' + str(lsCannon.dmg))
                await asyncio.sleep(2)
                
                break
                
            
            else:
                ESP.armor -= lsCannon.dmg
                print('E+: -' + str(lsCannon.dmg))
                await asyncio.sleep(2)
                
                break
                             
    
    async def shield_dmg():
        while True:

            if enemyShield.density < 0:
                ESP.armor_sw()
                break
    
            elif enemyShield.density - lsCannon.dmg <= 0:
                    enemyShield.density = 0
                    print("Es: -" + str(lsCannon.dmg))
                    await asyncio.sleep(2)
                    break
                
            else:
                enemyShield.density -= lsCannon.dmg
                print("Es: -" + str(lsCannon.dmg))
                await asyncio.sleep(2)
                break
                
            

    async def dmg_esp():
        while True:

            if ESP.armor == 0:
                
                if ESP.health - lsCannon.dmg <= 0:
                    print('E++: -' + str(lsCannon.dmg))
                    break
                
                else:
                    ESP.health -= lsCannon.dmg
                    print('E++: -' + str(lsCannon.dmg))
                    await()
                    break
    
            else:
                print('E+: +-' + str(lsCannon.dmg))
                await asyncio.sleep(2)
                asyncio.run(ESP.armor_sw())
                
    async def enshipsaving():    
        with shelve.open('saves/enship') as enshipsave:
            enshipsave['health'] = ESP.health
            enshipsave['shield'] = ESP.shield.density
            enshipsave['armor'] = ESP.armor
            upenship = {'health': ESP.health, 'shield': ESP.shield, 'armor': ESP.armor }
            enshipsave.update(upenship)
                

class Miner:

    name = "LSP-1000"

    strength = random.randint(2, 3)
    speed = random.randint(3, 7)

    async def mining():
        print("Mining", location_name + "...")
        sleep(2)
        
        
        # If any of the materials collected are at zero or below zero, make sure they are zero.
        
        if Inv.m_one <= 0:
            Inv.m_one = 0
            pass
            
        if Inv.m_two <= 0:
            Inv.m_two = 0
            pass
            
        if Inv.m_three <= 0:
            Inv.m_three = 0
            pass

        for n in range(8):
            
            # Flips a coin to decide randomly which material is mined from the current planet. 
            # a is material one, b is material two, c is material three, and so on.

            flip = [ 'a', 'b', 'c' ]
            
            

            if random.choice(flip) == 'a':
                
                if Inv.m_one == Inv.max_space:
                    return
                
                else:
                    Inv.m_one += Miner.strength
                    
                print(Inv.m_one, location.materials_name[0], "collected.")

                await asyncio.sleep(Miner.speed)


            elif random.choice(flip) == 'b':

                if Inv.m_two == Inv.max_space:
                    return

                else:
                    Inv.m_two += Miner.strength

                print(Inv.m_two, location.materials_name[1], "collected.")

                await asyncio.sleep(Miner.speed)


            elif random.choice(flip) == 'c':

                if Inv.m_three == Inv.max_space:
                    return

                else:
                    Inv.m_three += Miner.strength

                print(Inv.m_three, location.materials_name[2], "collected.")
            
                await asyncio.sleep(Miner.speed)
    
    
    #with shelve.open('minersh') as minersh: 
        # minersh['minerstrength'] = strength
       #  minersh['minerspeed'] = speed
       # mineup = {'minerstrength':strength, 
                 # 'minerspeed':speed }
        # minersh.update(mineup)
        

class PS:

    name = "Calcula I"
    health = 30
    armor = 20
    shield = Shield1()
    shield_deptime = 10
    inventory = Inv()
    weapon = lsCannon()
    in_combat = False
    armorblock = 45
    
    

    async def shield_dmg():
        
            while PS.shield.deployed == True:
                
                if Shield1.density <= 0:
                    print("Ys(v)")
                    PS.shield.deployed = False
                    await asyncio.sleep(2)
                    await PS.armor_sw()
        
                else:
                    if Shield1.density - lsCannon.dmg <= 0:
                        Shield1.density = 0
                        print("Ys: -" + str(lsCannon.dmg))
                        await asyncio.sleep(2)
                        break
                    
                    elif Shield1.battery > 0:
                        Shield1.density -= lsCannon.dmg
                        Shield1.battery -= 1
                        print("Ys: -" + str(lsCannon.dmg))
                        await asyncio.sleep(2)
                        break
                    
                    else:
                        PS.shield.deployed = False
                        break

    async def armor_sw():
        
        while True:
            
            # 45% chance to mitigate some damage with armor. 
        
            if random.randint(1, 100) <= PS.armorblock:
                
                if PS.armor - random.randrange(2, 3) <= 0:
                    PS.armor = 0
                    print('Y+: +-' + str(PS.armor - random.randrange(2, 3)))
                    await asyncio.sleep(2)
                    break
            
                else:
                    PS.armor -= random.randrange(2, 3)
                    print('Y+: +-' + str(PS.armor - random.randrange(2, 3)))
                    await asyncio.sleep(2)
                    break
                
            elif PS.armor - lsCannon.dmg <= 0:
                PS.armor = 0
                break
                
            else:
                PS.armor -= lsCannon.dmg
                
                print("Y+: -" + str(lsCannon.dmg))
                await asyncio.sleep(2)
                break

    async def dmg_ps():
        
        while True:
        
            if random.randint(1, 100) <= 70:
                
                if ESP.armor == 0: # If enemy armor is zero...
                    
                    if ESP.health - lsCannon.dmg <= 0: ## Check for death hit...
                        ESP.health = 0
                        break
                    
                    else:
                        ESP.health -= lsCannon.dmg # Or issue damage.
                        print("E++: -" + str(lsCannon.dmg))
                        await asyncio.sleep(2)
                        break
        
                else:
                    if PS.shield.deployed == True:
                        await PS.shield_dmg()
                        break
                    else:
                        await ESP.armor_sw()
                        break
                    
                    
            else:
                print("Y:::MISFIRE:::Y")
                sleep(2)
                break
            
    async def powershot():
        
        if lsCannon.super_ammo > 0:
            
            if lsCannon.locked_on == True:
                
                lsCannon.super_ammo -= 1
                
                print("Deploying super-charged round...")
                await asyncio.sleep(2)
                
                if ESP.armor - lsCannon.super_dmg == 0:
                    ESP.armor = 0
                    print("E++: -" +  str(lsCannon.super_dmg))
                    await asyncio.sleep(2)
                    
                elif ESP.armor <= 0: 
                    ESP.armor = 0
                    ESP.health -= lsCannon.super_dmg
                    print("E++: -" +  str(lsCannon.super_dmg))
                    await asyncio.sleep(2)
                
                if ESP.health - lsCannon.super_dmg == 0:
                    ESP.health = 0
                    print("E++: -" +  str(lsCannon.super_dmg))
                    await asyncio.sleep(2)
                    
                else:
                    print("E+: -" +  str(lsCannon.super_dmg))
                    ESP.armor -= lsCannon.super_dmg
                    await asyncio.sleep(2)
                
                lsCannon.locked_on = False
                
                pass
            
            else:
                
                print("PS: OFFLINE")
                await asyncio.sleep(2)
                pass
            
        else:
            
            print("Out of ammo...")
            await asyncio.sleep(2)
            pass
        
    async def attacked():
        
        while True:
            
            if random.randint(1, 100) <= 70:
                
                if PS.armor == 0:
                    
                    if PS.health - lsCannon.dmg <= 0:
                        PS.health = 0
                        print("Y++: -" + lsCannon.dmg)
                        await asyncio.sleep(2)
                        break
                    
                    else:
                        PS.health -= lsCannon.dmg
                        print("Y++: -" + str(lsCannon.dmg))
                        await asyncio.sleep(2)
                        break

                else:
                    await PS.armor_sw()
                    break
            
            else:
                print('E:::MISFIRE:::E')
                await asyncio.sleep(2)
                break
    
    async def shipsaving():    
        with shelve.open('saves/ship') as shipsave:
            shipsave['health'] = PS.health
            shipsave['shield'] = PS.shield.density
            shipsave['armor'] = PS.armor
            shipsave['incombat'] = PS.in_combat
            upship = {'health': PS.health, 'shield': PS.shield, 'armor': PS.armor, 'incombat': PS.in_combat }
            shipsave.update(upship)

    def saveloc():
        
        global location
        global location_name
        
        

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
            PS.shipsaving()
            break

    def inv_upgrade():

        while wallet.bank > Shop.inv_up:
            wallet.bank -= Shop.inv_up
            sleep(2)
            PS.inventory.max_space = PS.inventory.max_space * 2
            print("INV:", str(PS.inventory.max_space))
            Inv.insave()
            wallet.walsave()
            PS.shipsaving()
            break

    def health_upgrade():

        while wallet.bank >= Shop.health_up:
            wallet.bank -= Shop.health_up
            sleep(2)
            PS.health = PS.health * 1.5
            print('+::', str(PS.health))
            wallet.walsave()
            PS.shipsaving()
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
    
    # Combat interface.

    offense = [ 'attack', 'scan', 'ff', 'ps' ]
    off_sp = [ 'sp.a', 'cat',  'aim' ] # cat = capture
    defense = [ 'sh', 'rcs', 'rcps' ]  
    
    
    async def edeath():
        
        print('e:kill + 15AME')
        PS.in_combat = False
        ESP.health = 30
        ESP.armor = 20
        await ESP.enshipsaving()
        PS.health = 30
        PS.armor = 20
        PS.shield.battery = 3
        await PS.shipsaving()
            
    async def ydeath():
        
        print('y:kill +- 15AME')
        PS.in_combat = False
        ESP.health = 30
        ESP.armor = 20
        await ESP.enshipsaving()
        PS.health = 30
        PS.armor = 20
        PS.shield.battery = 3
        await PS.shipsaving()
        
    async def attacking():
        
        while PS.in_combat == True:
            
                if ESP.health <= 0:
                    await CIT.edeath()
                    break
                
                if PS.health <= 0:
                    await CIT.ydeath()
                    break
                
                print('E+:', ESP.armor)
                print('E++:', ESP.health)
                print('Es:', ESP.shield.density)
                print('Y+:', PS.armor)
                print('Y++:', PS.health)
                print('Ys:', PS.shield.density)
                
                CITF = input("CIT: ")
                
                if CITF == CIT.offense[0]:
                    await PS.dmg_ps()
                    await PS.attacked()
                
                elif CITF == CIT.offense[2]:
                    break
                
                elif CITF == CIT.off_sp[2]:
                    await lsCannon.saim()
                    
                elif CITF == CIT.offense[3]:
                    await PS.powershot()
                    
                elif CITF == CIT.defense[0]:
                    print('Deploying shield...')
                    await asyncio.sleep(2)
                    if PS.shield.battery > 0:
                        PS.shield.battery -= 1
                        PS.shield.deployed = True
                        pass
                    
                    else:
                        print('Shield battery depleted...')
                        pass
                
                elif CITF == CIT.defense[1]:
                    await Shield1.recharge()
                    await PS.attacked()
                
                elif CITF == 'clear':
                    os.system('clear')
                    pass
                                
                       
    async def spawn():
        if random.randrange(1, 100) <= 45:
            ESP.engaged = True
            PS.in_combat = True
            await PS.shipsaving()
                
        if ESP.engaged == True:
            await CIT.attacking()
        
        else:
            pass

class IT:

    global location 
    global location_name
    
    # Various commands


    async def command_deck():
        
        utility = [ 'mine', 'scan', 'travel', 'automine', 'sell' ]
        shop = [ 'shop', '++', 'shi+', 'inv+', '$$$+', '$R' ]
        diag = [ 'health', 'shield', 'inventory' ]
        money = [ 'wallet', 'deposit' ]
        
        command = ""

        while command != "kill":

            command = input("""\n司令官: """)

            while command == utility[0]: # Mining
                await di.qdb.gemstones()
                await asyncio.sleep(1)
                await Miner.mining()
                await Inv.insave()
                await di.qdb.gemstones()
                await CIT.spawn()           
                command = ""

            
            while command == utility[2]: # Travel
                zyX = input("X, Y: ")

                if zyX == str(amplanets.Piscea.coordinates):
                    location = Piscea
                    location_name = Piscea.name
                    amplanets.Piscea.arrival()
                    
                    # Quickly save the location and location name into the database file.
                    
                    with shelve.open('saves/locatio') as position:
                        
                        position_up = {'planet': location, 'pl_name': location_name}
                        position.update(position_up)
                        
                    await CIT.spawn()
                    command = ""

                else:
                    command = ""
                
                if zyX == (amplanets.Marici.coordinates):
                    location = amplanets.Marici
                    location_name = amplanets.Marici.name
                    amplanets.Marici.arrival()
                    with shelve.open('saves/locatio') as position:
                        position_up = { 'planet': location, 'pl_name': location_name }
                        position.update(position_up)
                    await CIT.spawn()
                    command = ""
                
                else:
                    await CIT.spawn()
                    command = ""

            while command == utility[4]: # Selling
                await Inv.sell()
                wallet.walsave()
                await Inv.insave()
                di.qdb.gemstones()
                await CIT.spawn()  
                command = ""

            while command == diag[0]: # Print health information.
                
                print("Health:", PS.health)
                command = ""

            while command == diag[1]: # Print shield information.
                
                print("Shield:", PS.shield.density)
                command = ""

            while command == diag[2]: # Print inventory
                await di.ndb.displayinv()
                command = ""
            
            while command == money[1]:
                await wallet.deposit()
                wallet.walsave()
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

asyncio.run(IT.command_deck())




        
