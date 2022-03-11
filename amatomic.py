from argparse import MetavarTypeHelpFormatter
import random
from time import sleep
import asyncio
import shelve

class Amerinium:

    name = "Amerinium"
    flux = random.randrange(4, 42)
    transfer_rate = random.randrange(1, 4)

    async def fluxuation():
        Amerinium.flux = 0
        await asyncio.sleep(1)
        Amerinium.flux = Amerinium.flux + random.randrange(4, 42)
        

    def fluxflip():

        fluxflip = [ 'a', 'b', 'c', 'd' ]

        sleep(1)

        if random.choice(fluxflip) == fluxflip[0]:
            Amerinium.fluxuation()
            sleep(2)

        if random.choice(fluxflip) == fluxflip[1]:
            Amerinium.fluxuation()
            sleep(2)

        if random.choice(fluxflip) == fluxflip[2]:
            pass

        if random.choice(fluxflip) == fluxflip[3]:
            pass


class THC:

    name = "THC Crystals"
    cost = 35
    quantity = 0

class Iron:

    name = "Iron"
    cost = 15
    quantity = 0

class Gold:

    name = "Gold"
    cost = 70
    quantity = 0

class Sulfur:

    name = "Sulfur"
    cost = 10
    quantity = 0

class Hydrogen:

    name = "Hydrogen"
    cost = 25
    quantity = 0

class Helium:

    name = "Helium"
    cost = 25
    quantity = 0

class Diamond:

    name = "Diamonds"
    cost = 60
    quantity = 0


class Psycilobin:

    name = "Psycilobin"
    cost = 35
    quantity = 0


class Dextromethorphan:

    name = "dxm.crystl"
    cost = 25
    quantity = 0


class Diphenhydramine:

    name = "dph.crystl"
    cost = 10
    quantity = 0

class Angelium:

    name = "Angelium"
    cost = 222
    quantity = 0

class Femininium:

    name = "Femininium Crystals"
    cost = 40
    quantity = 0

class Ammonia:

    name = "Ammonia"
    cost = 20
    quantity = 0

class Methane:

    name = "Methane"
    cost = 15
    quantity = 0

class Silver:

    name = "Silver"
    cost = 60
    quantity = 0

class Platinum:

    name = "Platinum"
    cost = 90
    quantity = 0

class Meteorite:

    name = "Meteorite"
    cost = 10
    quantity = 0

class MR:

    name = "Moon Rock"
    cost = 8
    quantity = 0

class Junk:

    name = "Space Junk"
    cost = 5
    quantity = 0


    