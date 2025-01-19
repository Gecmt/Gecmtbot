import discord
from discord.ext import commands
import random
import firebase_admin
from firebase_admin import credentials, firestore
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import cooldown, BucketType
from discord import Member
from threading import Thread

# Initialize Firebase Admin SDK
cred = credentials.Certificate("Key.json")  # Replace with your JSON file path
firebase_admin.initialize_app(cred)
db = firestore.client()

client = commands.Bot(command_prefix="", intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Roblox'))
    print("Bot is connected to Discord")

@client.command(aliases=["roblox", "Blox", "ROBLOX", "blox"])
async def Roblox(ctx):
    await ctx.send("I love Roblox!")

@client.command(aliases=["Hello", "Hi", "hello", "Gecmtbot", "gecmtbot", "<@1253751560740016199>", "<@&1254051579670036545>", "HELLO", "HI", "Hİ"])
async def hi(ctx):
    await ctx.send("Hello, what's up!")

@client.command(aliases=["Go", "go", "GO", "Diet", "DİET", "DIET", "AMERİCA", "America", "AMERICA", "america"])
async def diet(ctx):
    await ctx.send("Here is my Roblox game! https://www.roblox.com/games/17408280516/Go-on-a-Diet-in-America")

@client.command(aliases=["Bacon", "BACON", "Steal", "STEAL", "steal"])
async def bacon(ctx):
    await ctx.send("Here is my Roblox game! https://www.roblox.com/games/17190630027/Steal-and-Cook-Bacons")

fruits = [
'Rocket <:Rocket:1204868667368669214>',
'Spin <:Spin:1204841100129341470>',
'Blade <:Blade:1204841000108040232>',
'Spring <:Spring:1204841104697073835>',
'Bomb :Bomb:1204840995334651934>',
'Smoke <:Smoke:1204841094211174530>',
'Spike <:Spike:1204841097793241108>',
'Flame <:Flame:1204841953032806432> ',
'Falcon <:Falcon:1204841015954112522>',
'Ice <:Ice:1204842108486160404>',
'Sand <:Sand:1204841090058813491>',
'Dark <:Dark:1204841004818235432>',
'Diamond <:Diamond:1204841009062748251>',
'Light <:Light:1204841046618546306>',
'Rubber <:Rubber:1204841080047018045>',
'Barrier <:Barrier:1204840990406352936>',
'Ghost <:Ghost:1204869189685215243>',
'Magma <:Magma:1204841051031085168>',
'Quake <:Quake:1204842200039686226>',
'Buddha <:Buddha:1204840998086123611>',
'Love <:Love:1254080989261463563>',
'Spider <:Spider:1204841095947751464>',
'Sound <:Sound:1204868822423699546>',
'Phoenix <:Phoenix:1204841550451056640>',
'Portal <:Portal:1204841064574488576>',
'Rumble <:Rumble:1204841088331030528>',
'Pain <:Pain:1204842110541365358>',
'Blizzard <:Blizzard:1204840993463996457>',
'Gravity <:Gravity:1204841037244141639>',
'Mammoth <:Mammoth:1204868683302961243>',
'T-Rex <:Trex:1204868704794312794>',
'Dough <:Dough:1204841010987802685>',
'Shadow <:Shadow:1204841091313045556>',
'Venom <:Venom:1204842250429792347>',
'Control <:Control:1204841002389479474>',
'Gas <:Gas:1330509321359982622>',
'Spirit <:Spirit:1204841409215987723>',
'Leopard <:Leopard:1204841044802543616>',
'Yeti <:Yeti:1330509369531433005>',
'Kitsune <:Kitsune:1254081916605431828>',
'Dragon East <:Dragon_East:1330509726626091018>',
'Dragon West <:Dragon_West:1330509417929510932>',
]


# Sols Rng died, this is a little old lol

auras = [
'You rolled: [Common](https://static.wikia.nocookie.net/sol-rng/images/e/ef/Common_Aura.gif/revision/latest?cb=20240114221921)',
'You rolled: [Uncommon](https://static.wikia.nocookie.net/sol-rng/images/0/0d/Uncommon_Aura.gif/revision/latest?cb=20240115015355)',
'You rolled: [Good](https://static.wikia.nocookie.net/sol-rng/images/3/3c/GoodAura.gif/revision/latest?cb=20240218214412)',
'You rolled: [Natural](https://static.wikia.nocookie.net/sol-rng/images/9/91/NaturalAura.gif/revision/latest?cb=20240117182459)',
'You rolled: [Rare](https://static.wikia.nocookie.net/sol-rng/images/2/2c/Rare_Aura.gif/revision/latest?cb=20240117215614)',
'You rolled: [Divinus](https://static.wikia.nocookie.net/sol-rng/images/1/10/DivinusAura.gif/revision/latest?cb=20240118185547)',
'You rolled: [Crystallized](https://static.wikia.nocookie.net/sol-rng/images/4/48/CrystalAura.gif/revision/latest?cb=20240118191715)',
'You rolled: [Rage](https://static.wikia.nocookie.net/sol-rng/images/5/5f/RageAura.gif/revision/latest?cb=20240118204702)',
'You rolled: [Topaz](https://static.wikia.nocookie.net/sol-rng/images/3/35/TopazCollection.gif/revision/latest?cb=20240405220031)',
'You rolled: [Ruby](https://static.wikia.nocookie.net/sol-rng/images/0/07/RubyAura.gif/revision/latest?cb=20240218224227)',
'You rolled: [Forbidden](https://static.wikia.nocookie.net/sol-rng/images/a/a3/ForbiddenCollection.gif/revision/latest?cb=20240521221211)',
'You rolled: [Emerald](https://static.wikia.nocookie.net/sol-rng/images/2/25/Emerald_Collection.gif/revision/latest?cb=20240417212653)',
'You rolled: [Gilded](https://static.wikia.nocookie.net/sol-rng/images/7/78/GildedAura.gif/revision/latest?cb=20240218224413)',
'You rolled: [Ink](https://static.wikia.nocookie.net/sol-rng/images/c/cf/InkGif.gif/revision/latest?cb=20240510193613)',
'You rolled: [Jackpot](https://static.wikia.nocookie.net/sol-rng/images/7/74/JackpotAura.gif/revision/latest?cb=20240218224845)',
'You rolled: [Sapphire](https://static.wikia.nocookie.net/sol-rng/images/b/b0/Sapphirecollectiongif.gif/revision/latest?cb=20240405233927)',
'You rolled: [Aquamarine](https://static.wikia.nocookie.net/sol-rng/images/c/c8/Aquamarine_Collection1.gif/revision/latest?cb=20240417213054)',
'You rolled: [Glacier](https://static.wikia.nocookie.net/sol-rng/images/6/60/GlacierAuraNight.gif/revision/latest?cb=20240221190023)',
'You rolled: [Wind](https://static.wikia.nocookie.net/sol-rng/images/f/fa/WindAuraList.gif/revision/latest?cb=20240218215951)',
'You rolled: [Diaboli](https://static.wikia.nocookie.net/sol-rng/images/b/b2/DiaboliAuraNight.gif/revision/latest?cb=20240221185922)',
'You rolled: [Precious](https://static.wikia.nocookie.net/sol-rng/images/0/0f/PreciousAura.gif/revision/latest?cb=20240218224756)',
'You rolled: [Glock](https://static.wikia.nocookie.net/sol-rng/images/7/78/Glock.gif/revision/latest?cb=20240510193744)',
'You rolled: [Magnetic](https://static.wikia.nocookie.net/sol-rng/images/8/8c/MagneticAuraNight.gif/revision/latest?cb=20240221190050)',
'You rolled: [Sidereum](https://static.wikia.nocookie.net/sol-rng/images/2/28/SidereumAura.gif/revision/latest?cb=20240218225013)',
'You rolled: [Bleeding](https://static.wikia.nocookie.net/sol-rng/images/d/d8/BleedingCollectionRework.gif/revision/latest?cb=20240514162454)',
'You rolled: [Solar](https://static.wikia.nocookie.net/sol-rng/images/4/41/SolarAuraNight.gif/revision/latest?cb=20240221190826)',
'You rolled: [Lunar](https://static.wikia.nocookie.net/sol-rng/images/b/b2/LunarAura.gif/revision/latest?cb=20240218222846)',
'You rolled: [Starlight](https://static.wikia.nocookie.net/sol-rng/images/2/22/StarlightCollection.gif/revision/latest?cb=20240406040419)',
'You rolled: [: flushed :](https://static.wikia.nocookie.net/sol-rng/images/4/48/FlushedAuraNight.gif/revision/latest?cb=20240221190158)',
'You rolled: [Hazard](https://static.wikia.nocookie.net/sol-rng/images/a/a9/HazardGif.gif/revision/latest?cb=20240510194924)',
'You rolled: [Quartz](https://static.wikia.nocookie.net/sol-rng/images/e/ec/QuartzGifCollection.gif/revision/latest?cb=20240510194702)',
'You rolled: [Undead](https://static.wikia.nocookie.net/sol-rng/images/e/eb/UndeadAura.gif/revision/latest?cb=20240218090022)',
'You rolled: [Corrosive](https://static.wikia.nocookie.net/sol-rng/images/9/94/Corrosive.gif/revision/latest?cb=20240510194434)',
'You rolled: [Rage:Heated](https://static.wikia.nocookie.net/sol-rng/images/1/14/RageHeatedAura.gif/revision/latest?cb=20240218215325)',
'You rolled: [Leak](https://static.wikia.nocookie.net/sol-rng/images/d/da/LeakGif.gif/revision/latest?cb=20240511090449)',
'You rolled: [Powered](https://static.wikia.nocookie.net/sol-rng/images/9/9a/Powered.gif/revision/latest?cb=20240510195556)',
'You rolled: [Aquatic](https://static.wikia.nocookie.net/sol-rng/images/a/a9/AquaticAura.gif/revision/latest?cb=20240218221908)',
'You rolled: [Flushed:Lobotomy](https://static.wikia.nocookie.net/sol-rng/images/f/f6/FlushedLobotomyAura.gif/revision/latest?cb=20240218220247)',
'You rolled: [Hazard:Rays](https://static.wikia.nocookie.net/sol-rng/images/c/c1/Hazard_Rays.gif/revision/latest?cb=20240510211117)',
'You rolled: [Nautilus](https://static.wikia.nocookie.net/sol-rng/images/e/e2/NautilusAuraNight.gif/revision/latest?cb=20240221190755)',
'You rolled: [Permafrost](https://static.wikia.nocookie.net/sol-rng/images/1/1e/PermafrostAura.gif/revision/latest?cb=20240218215752)',
'You rolled: [Stormal](https://static.wikia.nocookie.net/sol-rng/images/6/65/Stormal_Collection_E7.gif/revision/latest?cb=20240608133437)',
'You rolled: [Exotic](https://static.wikia.nocookie.net/sol-rng/images/7/71/ExoticAura150x150.gif/revision/latest?cb=20240221184239)',
'You rolled: [Diaboli:Void](https://static.wikia.nocookie.net/sol-rng/images/8/89/DiaboliVoidRework-Collection.gif/revision/latest?cb=20240511002535)',
'You rolled: [Undead:Devil](https://static.wikia.nocookie.net/sol-rng/images/f/f9/UndeadDevilAura.gif/revision/latest?cb=20240218223326)',
'You rolled: [Comet](https://static.wikia.nocookie.net/sol-rng/images/2/21/CometAura.gif/revision/latest?cb=20240218222756)',
'You rolled: [Jade](https://static.wikia.nocookie.net/sol-rng/images/0/06/JadeInCollection.gif/revision/latest?cb=20240405174500)',
'You rolled: [Bounded](https://static.wikia.nocookie.net/sol-rng/images/5/52/BoundedAuraNight.gif/revision/latest?cb=20240221191415)',
'You rolled: [Celestial](https://static.wikia.nocookie.net/sol-rng/images/6/60/CelestialAura.gif/revision/latest?cb=20240218223921)',
'You rolled: [Kyawthuite](https://static.wikia.nocookie.net/sol-rng/images/6/67/Kyawthuite_Collection2.gif/revision/latest?cb=20240417210214)',
'You rolled: [Arcane](https://static.wikia.nocookie.net/sol-rng/images/8/86/Arcane_Gif_25Fps.gif/revision/latest?cb=20240218233241)',
'You rolled: [Magnetic:Reverse Polarity](https://static.wikia.nocookie.net/sol-rng/images/c/c2/MagneticReversePolarityCollection.gif/revision/latest?cb=20240405220706)',
'You rolled: [Undefined](https://static.wikia.nocookie.net/sol-rng/images/b/b0/Undefined_Collection1.gif/revision/latest?cb=20240417213730)',
'You rolled: [Astral](https://static.wikia.nocookie.net/sol-rng/images/c/ca/Astral_gif.gif/revision/latest?cb=20240511000517)',
'You rolled: [Gravitational](https://static.wikia.nocookie.net/sol-rng/images/6/62/Gravitationalgif.gif/revision/latest?cb=20240405234317)',
'You rolled: [Unbound](https://static.wikia.nocookie.net/sol-rng/images/6/65/Unbound_E7_Collection2.gif/revision/latest?cb=20240519173345)',
'You rolled: [Virtual](https://static.wikia.nocookie.net/sol-rng/images/2/20/Virtual.gif/revision/latest?cb=20240305083333)',
'You rolled: [Aquatic·Flame](https://static.wikia.nocookie.net/sol-rng/images/7/7f/Aqua_flame_new_gif.gif/revision/latest?cb=20240510210713)',
'You rolled: [Poseidon](https://static.wikia.nocookie.net/sol-rng/images/d/db/PosEra7.gif/revision/latest?cb=20240510224409)',
'You rolled: [Zeus](https://static.wikia.nocookie.net/sol-rng/images/4/41/Zeus_GIF.gif/revision/latest?cb=20240622125824)',
'You rolled: [Solar: Solstice](https://static.wikia.nocookie.net/sol-rng/images/1/1c/SolarSolsticeG.gif/revision/latest?cb=20240510193604)',
'You rolled: [Galaxy](https://static.wikia.nocookie.net/sol-rng/images/f/f8/Galaxy_Aura.gif/revision/latest?cb=20240220022654)',
'You rolled: [Lunar: Full Moon](https://static.wikia.nocookie.net/sol-rng/images/b/b4/LunarFullMoonAura.gif/revision/latest?cb=20240218223736)',
'You rolled: [Twilight](https://static.wikia.nocookie.net/sol-rng/images/b/b4/TwilightInCollection.gif/revision/latest?cb=20240513072650)',
'You rolled: [Hades](https://static.wikia.nocookie.net/sol-rng/images/8/85/HadesCollection.gif/revision/latest?cb=20240406041535)',
'You rolled: [Hyper-Volt](https://static.wikia.nocookie.net/sol-rng/images/d/d4/HpVl.gif/revision/latest?cb=20240220023354)',
'You rolled: [Starscourage](https://static.wikia.nocookie.net/sol-rng/images/6/60/Starscourge_GIF.gif/revision/latest?cb=20240622124540)',
'You rolled: [Sailor](https://static.wikia.nocookie.net/sol-rng/images/e/e2/SailorCollectionEra7.gif/revision/latest?cb=20240510223631)',
'You rolled: [Glitch](https://static.wikia.nocookie.net/sol-rng/images/8/8d/GlitchInCollection.gif/revision/latest?cb=20240405201045)',
'You rolled: [Arcane:Legacy](https://static.wikia.nocookie.net/sol-rng/images/7/72/Arcane_Legacy_Collection_E7.gif/revision/latest?cb=20240620125029)',
'You rolled: [Chromatic](https://static.wikia.nocookie.net/sol-rng/images/d/d6/Chromatic_GIF.gif/revision/latest?cb=20240622185733)',
'You rolled: [Arcane:Dark](https://static.wikia.nocookie.net/sol-rng/images/a/a2/Arcane_-_Dark_GIF.gif/revision/latest?cb=20240622121127)',
'You rolled: [Ethereal](https://static.wikia.nocookie.net/sol-rng/images/b/bc/Etherealpretrans.gif/revision/latest?cb=20240429174550)',
'You rolled: [Exotic·Apex](https://static.wikia.nocookie.net/sol-rng/images/0/09/Exotic_Apex_Collection_E7.gif/revision/latest?cb=20240521232139)',
'You rolled: [Matrix](https://static.wikia.nocookie.net/sol-rng/images/b/b0/MatrixCollections.gif/revision/latest?cb=20240511093006)',
'You rolled: [Chromatic:Genesis](https://static.wikia.nocookie.net/sol-rng/images/7/72/Genesis-Collection.gif/revision/latest?cb=20240513233345)',
'You rolled: [Starscourage:Radiant](https://static.wikia.nocookie.net/sol-rng/images/1/16/Starscourge_Radiant_Gif2.gif/revision/latest?cb=20240519204304)',
'You rolled: [Overture](https://static.wikia.nocookie.net/sol-rng/images/e/e8/Overture_Collection.gif/revision/latest?cb=20240621122629)',
'You rolled: [Impeached](https://static.wikia.nocookie.net/sol-rng/images/e/ee/Image_2024-02-20_191403925.png/revision/latest?cb=20240220181406)',
'You rolled: [Oppression](https://static.wikia.nocookie.net/sol-rng/images/b/bd/OppressionCollection.jpg/revision/latest?cb=20240611043111)',
'You rolled: [Archangel](https://static.wikia.nocookie.net/sol-rng/images/b/bb/Archangel_GIF.gif/revision/latest?cb=20240308035811)',
'You rolled: [Overture:History](https://static.wikia.nocookie.net/sol-rng/images/d/d3/Overture_-_History_GIF.gif/revision/latest?cb=20240622122824)',
'You rolled: [Bloodlust](https://static.wikia.nocookie.net/sol-rng/images/f/f9/BloodlustInCollection.gif/revision/latest?cb=20240512054337)',
'You rolled: [Abyssal Hunter](https://static.wikia.nocookie.net/sol-rng/images/c/ce/Abyssal_Hunter_Collection2.gif/revision/latest?cb=20240511050638)',
'You rolled: [Gargantua](https://static.wikia.nocookie.net/sol-rng/images/d/de/GargantuaCollection.gif/revision/latest?cb=20240510211022)'
]


# Chances are not exactly real but the rarity order is real

aurachance = [10000, 9000, 8000, 7000, 6000, 5000, 4000, 3500, 3000, 2500, 2000, 1500, 1400, 1300, 1200, 1100, 1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 375, 350, 325, 300, 275, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 145, 140, 135, 130, 125, 120, 115, 110, 105, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



fruitchance = [130, 130, 150, 140, 140, 130, 150, 120, 150, 140, 120, 100, 95, 90, 80, 79, 78, 77, 73, 66, 64, 57, 51, 35, 23, 28, 13, 15, 12, 14, 13, 11, 10, 18, 8, 7.5, 7, 3, 3, 1, 0.25, 0.25]




@client.command()
@has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'User {member} has been kicked')





@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permissions to kick people")



@client.command()
@has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'User {member} has been banned')




@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permissions to ban people")





@client.command(aliases=["Aura", "AURA", "Sols", "SOLS", "sols", "gamble", "GAMBLE", "Gamble"])
async def aura(ctx):
    await ctx.reply(random.choices(auras, aurachance)[0])







@client.command(aliases=["Roll", "ROLL"])
async def roll(ctx):
    user_id = str(ctx.author.id)
    user_ref = db.collection('users').document(user_id)

    try:
        doc = user_ref.get()
        if doc.exists:
            user_data = doc.to_dict()

            # Ensure 'FruitLimit' field exists and set default value to 1 if not set
            if 'FruitLimit' not in user_data:
                user_data['FruitLimit'] = 1
                user_ref.update({'FruitLimit': 1})

            # Ensure 'fruits' field exists
            if 'fruits' not in user_data:
                user_data['fruits'] = []
                user_ref.update({'fruits': []})

            # Get current fruit counts
            fruits_inventory = user_data.get('fruits', [])
            fruit_limit = user_data.get('FruitLimit', 1)

            # Roll a fruit
            rolled_fruit = random.choices(fruits, fruitchance)[0]

            # Check if the user can add more of this fruit
            current_count = fruits_inventory.count(rolled_fruit)
            if current_count >= fruit_limit:
                await ctx.send(f"You already have the maximum amount of {rolled_fruit}.")
            else:
                await ctx.reply(f"You rolled: {rolled_fruit}")

                # Update firestore: add rolled fruit to the array
                fruits_inventory.append(rolled_fruit)
                user_ref.update({
                    'fruits': fruits_inventory
                })

        else:
            rolled_fruit = random.choices(fruits, fruitchance)[0]
            await ctx.reply(f"You rolled: {rolled_fruit}")
            user_ref.set({
            'fruits': [rolled_fruit],
            'FruitLimit': 1,
            'items': {}  # Initialize items as an empty dictionary
        }, merge=True)



    except Exception as e:
        print(e)
        await ctx.send("An error occurred while rolling for fruits.")







@client.command(aliases=["inv", "INV", "Inv", "Inventory", "INVENTORY", "Fruits", "fruits", "FRUITS"])
async def inventory(ctx):
    user_id = str(ctx.author.id)
    user_ref = db.collection('users').document(user_id)

    try:
        doc = user_ref.get()
        if doc.exists:
            user_data = doc.to_dict()
            fruits = user_data.get('fruits', [])
            items = user_data.get('items', [])

            # Count occurrences of each fruit
            fruit_counts = {}
            for fruit in fruits:
                if fruit in fruit_counts:
                    fruit_counts[fruit] += 1
                else:
                    fruit_counts[fruit] = 1

            # Count occurrences of each item
            item_counts = {}
            for item in items:
                if item in item_counts:
                    item_counts[item] += 1
                else:
                    item_counts[item] = 1

            # Prepare inventory message
            inventory_message = "Your inventory:\n"

            if fruits:
                inventory_message += "\n**Fruits**:\n"
                for fruit, count in fruit_counts.items():
                    if count > 1:
                      # I was really stuck at this one
                        inventory_message += f"{fruit} (x{count})\n"
                    else:
                        inventory_message += f"{fruit}\n"

            if items:
                inventory_message += "\n**Items**:\n"
                for item, count in item_counts.items():
                    if count > 1:
                        inventory_message += f"{item} (x{count})\n"
                    else:
                        inventory_message += f"{item}\n"

            await ctx.send(inventory_message.strip())  # strip() removes trailing newline
        else:
            await ctx.send("You have no items in your inventory.")
    except Exception as e:
        print(e)
        await ctx.send("An error occurred while fetching your inventory.")






@client.command(aliases=["Eat", "EAT"])
async def eat(ctx, *, fruit_name):
    fruit_name_lower = fruit_name.lower().strip()  # Convert input to lowercase and remove extra spaces

    # Check if the fruit name exists in the inventory
    user_id = str(ctx.author.id)
    user_ref = db.collection('users').document(user_id)

    try:
        doc = user_ref.get()
        if doc.exists:
            user_data = doc.to_dict()
            if 'fruits' in user_data:
                # Check if the exact fruit name is in the inventory
                matching_fruit = None
                for fruit in user_data['fruits']:
                    if fruit.lower().startswith(fruit_name_lower):
                        matching_fruit = fruit
                        break

                if matching_fruit:
                    # Update the "Fruit in usage" field
                    user_ref.update({
                        'FruitInUsage': matching_fruit
                    })

                    # Remove only one instance of the fruit from the inventory
                    updated_fruits = user_data['fruits']
                    updated_fruits.remove(matching_fruit)

                    user_ref.update({
                        'fruits': updated_fruits
                    })

                    await ctx.send(f"You have eaten {matching_fruit.split(' ')[0]}!")
                else:
                    await ctx.send(f"You don't have {fruit_name} in your inventory to eat.")
            else:
                await ctx.send("You have no fruits in your inventory.")
        else:
            await ctx.send("You have no fruits in your inventory.")
    except Exception as e:
        print(e)
        await ctx.send("An error occurred while processing your request.")






@client.command(aliases=["Equipped", "EQUIPPED", "equipped", "Using", "using", "USING", "EATEN", "Eaten"])
async def eaten(ctx):
    user_id = str(ctx.author.id)
    user_ref = db.collection('users').document(user_id)

    try:
        doc = user_ref.get()
        if doc.exists:
            user_data = doc.to_dict()
            if 'FruitInUsage' in user_data:
                fruit_in_usage = user_data['FruitInUsage']
                await ctx.reply(f"You have {fruit_in_usage.split(' ')[0]} equipped.")
            else:
                await ctx.reply("You have no fruit equipped.")
        else:
            await ctx.reply("You have no fruit equipped.")
    except Exception as e:
        print(e)
        await ctx.reply("An error occurred while fetching your equipped fruit.")









# ------------ Trading ---------------









ongoing_trades = {}

# Function to normalize fruit names
def normalize_fruit_name(fruit):
    return fruit.split()[0].lower()

# Normalize the fruit names dictionary
normalized_fruits = {normalize_fruit_name(fruit): fruit for fruit in fruits}

@client.command(aliases=["Trade", "TRADE"])
async def trade(ctx, member: discord.Member):
    if member == ctx.author:
        await ctx.reply("You cannot trade with yourself.")
        return

    if member.bot:
        await ctx.reply("You cannot trade with a bot.")
        return

    trade_id = f"{ctx.author.id}-{member.id}"
    if trade_id in ongoing_trades:
        await ctx.reply("You already have an ongoing trade with this user.")
        return

    ongoing_trades[trade_id] = {
        'user1': ctx.author,
        'user2': member,
        'user1_offers': {'fruits': [], 'items': []},
        'user2_offers': {'fruits': [], 'items': []},
        'confirmed': []
    }

    await ctx.send(f"{ctx.author.mention} has initiated a trade with {member.mention}. {member.mention}, type `accept` to start trading or `decline` to decline.")

    def check(m):
        return m.author == member and m.content.lower() == "accept"

    try:
        await client.wait_for('message', check=check, timeout=20)
        ongoing_trades[trade_id]['accepted'] = True
        await ctx.send(f"{member.mention} has accepted the trade request. You can now add items using `add <type> <name>` and remove items using `remove <type> <name>`.")
    except asyncio.TimeoutError:
        await decline_trade(ctx, ctx.author, member, trade_id, timeout=True)

async def decline_trade(ctx, user1, user2, trade_id, timeout=False):
    if trade_id in ongoing_trades:
        del ongoing_trades[trade_id]
        if timeout:
            await ctx.send(f"{user2.mention} did not respond in time. Trade request has been canceled.")
        else:
            await ctx.send(f"{user1.mention} has declined the trade.")

# I love trading!

@client.command(aliases=["Accept", "ACCEPT"])
async def accept(ctx):
    trade = None
    for trade_id, details in ongoing_trades.items():
        if details['user2'] == ctx.author:
            trade = trade_id
            break

    if not trade:
        await ctx.reply("You have no pending trade requests.")
        return

    ongoing_trades[trade]['accepted'] = True
    await ctx.send(f"{ctx.author.mention} has accepted the trade request. You can now add items using `add <type> <name>` and remove items using `remove <type> <name>`.")

@client.command(aliases=["Decline", "DECLINE"])
async def decline(ctx):
    trade = None
    for trade_id, details in ongoing_trades.items():
        if details['user2'] == ctx.author or details['user1'] == ctx.author:
            trade = trade_id
            break

    if not trade:
        await ctx.reply("You are not part of any ongoing trade.")
        return

    user1 = details['user1']
    user2 = details['user2']
    await decline_trade(ctx, user1, user2, trade)

@client.command(aliases=["Add", "ADD"])
async def add(ctx, type: str, *, name: str):
    type = type.lower()
    normalized_name = normalize_fruit_name(name) if type == 'fruit' else name.lower()

    if type == 'fruit':
        if normalized_name not in normalized_fruits:
            await ctx.reply(f"{name} is not a valid fruit.")
            return
        name = normalized_fruits[normalized_name]
    elif type != 'item':
        await ctx.reply("Invalid type. Use 'fruit' or 'item'.")
        return

    trade = None
    for trade_id, details in ongoing_trades.items():
        if details['user1'] == ctx.author or details['user2'] == ctx.author:
            trade = trade_id
            break

    if not trade:
        await ctx.reply("You are not part of any ongoing trade.")
        return

    details = ongoing_trades[trade]
    if ctx.author == details['user1']:
        details['user1_offers'][f'{type}s'].append(name)
    else:
        details['user2_offers'][f'{type}s'].append(name)

    await ctx.send(f"{ctx.author.mention} has added {name} to their trade offer.")

@client.command(aliases=["Remove", "REMOVE"])
async def remove(ctx, type: str, *, name: str):
    type = type.lower()
    normalized_name = normalize_fruit_name(name) if type == 'fruit' else name.lower()

    if type == 'fruit':
        if normalized_name not in normalized_fruits:
            await ctx.reply(f"{name} is not a valid fruit.")
            return
        name = normalized_fruits[normalized_name]
    elif type != 'item':
        await ctx.reply("Invalid type. Use 'fruit' or 'item'.")
        return

    trade = None
    for trade_id, details in ongoing_trades.items():
        if details['user1'] == ctx.author or details['user2'] == ctx.author:
            trade = trade_id
            break

    if not trade:
        await ctx.reply("You are not part of any ongoing trade.")
        return

    details = ongoing_trades[trade]
    if ctx.author == details['user1']:
        try:
            details['user1_offers'][f'{type}s'].remove(name)
        except ValueError:
            await ctx.reply(f"You do not have {name} in your trade offer.")
            return
    else:
        try:
            details['user2_offers'][f'{type}s'].remove(name)
        except ValueError:
            await ctx.reply(f"You do not have {name} in your trade offer.")
            return

    await ctx.send(f"{ctx.author.mention} has removed {name} from their trade offer.")

@client.command(aliases=["Confirm", "CONFIRM"])
async def confirm(ctx):
    trade = None
    for trade_id, details in ongoing_trades.items():
        if details['user1'] == ctx.author or details['user2'] == ctx.author:
            trade = trade_id
            break

    if not trade:
        await ctx.reply("You are not part of any ongoing trade.")
        return

    details = ongoing_trades[trade]
    if ctx.author in details['confirmed']:
        await ctx.reply("You have already confirmed your offer.")
        return

    details['confirmed'].append(ctx.author)

    if len(details['confirmed']) == 2:
        await ctx.send(f"Both users have confirmed their offers. Here are the final offers:\n\n{details['user1'].mention} offers: {', '.join(details['user1_offers']['fruits'] + details['user1_offers']['items'])}\n{details['user2'].mention} offers: {', '.join(details['user2_offers']['fruits'] + details['user2_offers']['items'])}\n\nBoth users type `finalconfirm` to complete the trade.")
    else:
        await ctx.send(f"{ctx.author.mention} has confirmed their offer. Waiting for the other user to confirm.")

@client.command(aliases=["Finalconfirm", "FINALCONFIRM", "FinalConfirm", "Final", "final", "FINAL"])
async def finalconfirm(ctx):
    trade = None
    for trade_id, details in ongoing_trades.items():
        if details['user1'] == ctx.author or details['user2'] == ctx.author:
            trade = trade_id
            break

    if not trade:
        await ctx.reply("You are not part of any ongoing trade.")
        return

    details = ongoing_trades[trade]
    if 'final_confirmed' not in details:
        details['final_confirmed'] = []

    if ctx.author in details['final_confirmed']:
        await ctx.reply("You have already confirmed the trade.")
        return

    details['final_confirmed'].append(ctx.author)

    if len(details['final_confirmed']) == 2:
        # Finalize the trade by updating the inventories in the database
        user1_ref = db.collection('users').document(str(details['user1'].id))
        user2_ref = db.collection('users').document(str(details['user2'].id))

        try:
            user1_doc = user1_ref.get()
            user2_doc = user2_ref.get()

            if not user1_doc.exists or not user2_doc.exists:
                await ctx.send("One of the users does not have an inventory.")
                del ongoing_trades[trade]
                return

            user1_data = user1_doc.to_dict()
            user2_data = user2_doc.to_dict()

            for fruit in details['user1_offers']['fruits']:
                if fruit not in user1_data['fruits']:
                    await ctx.send(f"{details['user1'].mention} does not have {fruit} in their inventory.")
                    del ongoing_trades[trade]
                    return
                user1_data['fruits'].remove(fruit)
                user2_data['fruits'].append(fruit)

            for fruit in details['user2_offers']['fruits']:
                if fruit not in user2_data['fruits']:
                    await ctx.send(f"{details['user2'].mention} does not have {fruit} in their inventory.")
                    del ongoing_trades[trade]
                    return
                user2_data['fruits'].remove(fruit)
                user1_data['fruits'].append(fruit)

            for item in details['user1_offers']['items']:
                if item not in user1_data['items']:
                    await ctx.send(f"{details['user1'].mention} does not have {item} in their inventory.")
                    del ongoing_trades[trade]
                    return
                user1_data['items'].remove(item)
                user2_data['items'].append(item)

            for item in details['user2_offers']['items']:
                if item not in user2_data['items']:
                    await ctx.send(f"{details['user2'].mention} does not have {item} in their inventory.")
                    del ongoing_trades[trade]
                    return
                user2_data['items'].remove(item)
                user1_data['items'].append(item)

            user1_ref.set(user1_data)
            user2_ref.set(user2_data)

            await ctx.send(f"Trade completed successfully between {details['user1'].mention} and {details['user2'].mention}!")
        except Exception as e:
            print(e)
            await ctx.send("An error occurred while processing the trade.")
        finally:
            del ongoing_trades[trade]
    else:
        await ctx.send(f"{ctx.author.mention} has confirmed the trade. Waiting for the other user to confirm.")






# --------- Trading Finish -----------









@client.command(aliases=["Quest", "QUEST"])
@cooldown(1, 30, BucketType.user)  # 30 seconds cooldown
async def quest(ctx):
    user_id = str(ctx.author.id)
    user_ref = db.collection('users').document(user_id)
    user_doc = user_ref.get()

    level = 1
    exp = 0
    money = 0

    if user_doc.exists:
        user_data = user_doc.to_dict()
        level = user_data.get('level', 1)
        exp = user_data.get('exp', 0)
        money = user_data.get('money', 0)

    exp_gain = 125 * level  # Example EXP gain range
    exp_to_level_up = 100 * level

    if level < 2600:
        exp += exp_gain

        if exp >= exp_to_level_up:
            level += 1
            exp -= exp_to_level_up

        coins_earned = level * 10
        money += coins_earned

        user_ref.set({
            'level': level,
            'exp': exp,
            'money': money
        }, merge=True)  # Merge ensures existing data is not overwritten

        await ctx.reply(f"Quest completed! You earned {coins_earned} coins.\nYour current level is {level}.\nCurrent EXP: {exp}/{exp_to_level_up}\nYour current money is {money}.")
    else:
        coins_earned = level * 10
        money += coins_earned
        await ctx.reply(f"Quest completed! You earned {coins_earned} coins.\nYou have reached the maximum level.\nYour current money is {money}.")




@quest.error
async def quest_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        await ctx.send(f"This command is on cooldown. Please try again in {round(error.retry_after)} seconds.")





@client.command(aliases=["Level", "LEVEL"])
async def level(ctx):
    user_id = str(ctx.author.id)
    user_ref = db.collection('users').document(user_id)
    user_doc = user_ref.get()

    if user_doc.exists:
        user_data = user_doc.to_dict()
        level = user_data.get('level', 1)
        exp = user_data.get('exp', 0)
        exp_to_level_up = 100 * level
        await ctx.reply(f"Your current level is {level}.\nCurrent EXP: {exp}/{exp_to_level_up}")
    else:
        await ctx.reply("You have not started your journey yet. Use the quest command to begin.")





@client.command(aliases=["MONEY", "Money", "Beli", "BELI", "beli"])
async def money(ctx):
    user_id = str(ctx.author.id)
    user_ref = db.collection('users').document(user_id)
    user_doc = user_ref.get()

    if user_doc.exists:
        user_data = user_doc.to_dict()
        money = user_data.get('money', 0)
        await ctx.reply(f"Your current money is {money}.")
    else:
        await ctx.reply("You have not started your journey yet. Use the quest command to begin.")









@client.command(aliases=["SHOP", "Shop"])
async def shop(ctx):
    shop_items = {
        '+1 Fruit Storage': {
            'price': 1000000,
            'description': 'Use this to store 1 more fruit of all types'
        }
    }

    shop_message = "Welcome to the shop!\n\n"
    for item, details in shop_items.items():
        shop_message += f"**{item}**: {details['description']} - Price: {details['price']} coins\n"

    await ctx.send(shop_message)





@client.command(aliases=["BUY", "Buy"])
async def buy(ctx, *, item_name):
    user_id = str(ctx.author.id)
    user_ref = db.collection('users').document(user_id)
    user_doc = user_ref.get()

    if user_doc.exists:
        user_data = user_doc.to_dict()
        money = user_data.get('money', 0)
        inventory = user_data.get('items', [])  # Initialize items as empty list if not exists
    else:
        await ctx.send("Error: User data not found.")
        return

    shop_items = {
        '+1 Fruit Storage': {
            'price': 1000000,
            'description': 'Use this to store 1 more fruit of all types'
        }
    }

    if item_name in shop_items:
        item_price = shop_items[item_name]['price']
        item_description = shop_items[item_name]['description']

        if money >= item_price:
            # Deduct the price from user's money
            money -= item_price

            # Add the item to user's inventory
            if 'items' not in user_data:
                user_data['items'] = []
            user_data['items'].append(item_name)

            # Update user's money and inventory in Firestore
            user_ref.update({
                'money': money,
                'items': user_data['items']
            })

            await ctx.send(f"You have successfully bought {item_name} for {item_price} coins!")

        else:
            await ctx.send("You don't have enough money to buy this item.")
    else:
        await ctx.send("Item not found in the shop.")





@client.command(aliases=["USE", "Use"])
async def use(ctx, *, item_name):
    if item_name == "+1 Fruit Storage":
        user_id = str(ctx.author.id)
        user_ref = db.collection('users').document(user_id)
        user_doc = user_ref.get()

        if user_doc.exists:
            user_data = user_doc.to_dict()
            items = user_data.get('items', [])

            if item_name in items:
                # Remove the used item from inventory
                items.remove(item_name)

                # Update user's inventory in Firestore
                user_ref.update({
                    'items': items
                })

                # Increase the fruit limit by 1
                fruit_limit = user_data.get('FruitLimit', 1)
                fruit_limit += 1

                # Update user's fruit limit in Firestore
                user_ref.update({
                    'FruitLimit': fruit_limit
                })

                await ctx.send(f"You have successfully used {item_name}. Your fruit limit is now {fruit_limit}.")
            else:
                await ctx.send(f"You don't have {item_name} in your inventory.")
        else:
            await ctx.send("Error: User data not found.")
    else:
        await ctx.send("Item usage not supported.")


client.run("token")
