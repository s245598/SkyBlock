import csv
import os 
from datetime import datetime

def damage_dealt(player,weapon,armor,pet,thaumaturgist):

    x2_dmg = armor.get("xdmg",1)
    if x2_dmg == 0:
        x2_dmg = 1  # In case xdmg=0 

    Bane = Bane_value.get(weapon.get("bane", 0), 0)
    Sharp = Sharp_value.get(weapon.get("sharpness", 0), 0)
    Smite = Smite_value.get(weapon.get("smite", 0), 0)
    Gravity = Gravity_value.get(weapon.get("gravity",0),0)
    Impaling = Impaling_value.get(weapon.get("impaling",0),0)
    Cubism = Cubism_value.get(weapon.get("cubism",0),0)
    Ender_slayer = Ender_slayer_value.get(weapon.get("ender_slayer",0),0)

    if weapon.get("bane") > 0:
        Bane_perk = (15/100) # Spider Essence Shop 15% dmg increase to spiders
    else:
        Bane_perk = 0
    # Enchants
    Airborne_enchant = Gravity + Sharp
    Animals_enchant = 0 + Sharp
    Aquatic_enchant = Impaling + Sharp
    Arcane_enchant = 0 + Sharp
    Arthropod_enchant = Bane + Bane_perk + Sharp 
    Construct_enchant = 0 + Sharp
    Cubic_enchant = Cubism + Sharp
    Ender_enchant = Ender_slayer + Sharp
    Elusive_enchant = 0 + Sharp
    Frozen_enchant = 0 + Sharp
    Glacial_enchant = 0 + Sharp
    Humanoid_enchant = 0 + Sharp
    Infernal_enchant = 0 + Sharp
    Magmatic_enchant = 0 + Sharp
    Mysthological_enchant = 0 + Sharp
    Pest_enchant = 0 + Sharp
    Shielded_enchant = 0 + Sharp
    Skeletal_enchant = Smite + Sharp
    Spooky_enchant = 0 + Sharp
    Subterranean_enchant = 0 + Sharp
    Undead_enchant = Smite + Sharp
    Wither_enchant = Smite + Sharp
    Woodland_enchant = 0 + Sharp

    #Perks
    spider_perks= Bane_perk+weapon["spider_dmg"]

    #Shards - Attributes - Base_Dmg increase ==========================================================================================================================================================================
    # Husk dette er mere i base_dmg det betyder at der et nyt element som skal tilføjes til Player og i dmg beregneren - 28-11-25
    #==================================================================================================================================================================================================================

    Additive_Multiplier = player["Combat_level_skill"] #enchant + perks
    
    Multiplicative_Multiplier = (1*(x2_dmg))

    Strength = (weapon["strength"]+player["Strength"]+armor["Strength"]+pet["Extra_weapon_strength"]+thaumaturgist["Strength"])
    Crit_Damage = (weapon["Crit_dmg"]+player["Crit_dmg"]+armor["Crit_dmg"]+pet["Crit_dmg"]+thaumaturgist["Crit_dmg"])
    Base_dmg = weapon["base_damage"]+pet["Extra_weapon_base_dmg"]

    #Old formulars for dmg calcs.
    #Multipliers = Additive_Multiplier*Multiplicative_Multiplier
    #dmg = ((5+Base_dmg)*(1+(Strength/100))*Multipliers)*(1+(Crit_Damage/100)) # Normal dmg
    
    Airborne_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Airborne_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100))

    Animals_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Animals_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Aquatic_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Aquatic_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Arcane_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Arcane_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Arthropod_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Arthropod_enchant+spider_perks))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Construct_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Construct_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Cubic_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Cubic_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Elusive_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Elusive_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Ender_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Ender_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Frozen_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Frozen_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Glacial_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Glacial_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Humanoid_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Humanoid_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Infernal_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Infernal_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Magmatic_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Magmatic_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Mysthological_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Mysthological_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Pest_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Pest_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Shielded_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Shielded_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) # Error, - Mobs that take only one point of damage per hit. Note: Ferocity can be used to calculate

    Skeletal_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Skeletal_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100))

    Spooky_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Spooky_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100))

    Subterranean_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Subterranean_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100))

    Undead_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Undead_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    Wither_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Wither_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100))  

    Woodland_dmg = ((5+Base_dmg)*(1+(Strength/100))*(1+(Additive_Multiplier+Woodland_enchant))*Multiplicative_Multiplier)*(1+(Crit_Damage/100)) 

    dmg = {"Airborne_dmg":Airborne_dmg,
           "Animals_dmg":Animals_dmg,
           "Aquatic_dmg":Aquatic_dmg,
           "Arcane_dmg":Arcane_dmg,
           "Arthropod_dmg":Arthropod_dmg,
           "Construct_dmg":Construct_dmg,
           "Cubic_dmg":Cubic_dmg,
           "Elusive_dmg":Elusive_dmg,
           "Ender_dmg":Ender_dmg,
           "Frozen_dmg":Frozen_dmg,
           "Glacial_dmg":Glacial_dmg,
           "Humanoid_dmg":Humanoid_dmg,
           "Infernal_dmg":Infernal_dmg,
           "Magmatic_dmg":Magmatic_dmg,
           "Mysthological_dmg":Mysthological_dmg,
           "Pest_dmg":Pest_dmg,
           "Shielded_dmg":Shielded_dmg,
           "Skeletal_dmg":Skeletal_dmg,
           "Spooky_dmg":Spooky_dmg,
           "Subterranean_dmg":Subterranean_dmg,
           "Undead_dmg":Undead_dmg,
           "Wither_dmg":Wither_dmg,
           "Woodland_dmg":Woodland_dmg,
    }

    formatted_dmg = {}  # et nyt dictionary til de nye værdier

    for navn, værdi in dmg.items():
        if værdi < 1000:
            formatted_dmg[navn] = round(værdi, 8)
    
        elif værdi > 1000:
            formatted_dmg[navn] = str(round(værdi / 1000, 4)) + "k"
        else:
            print(f"Error in {navn}")
            formatted_dmg[navn] = None  # hvis du vil have en default


    
    # --- Sørg for output-mappe ---
    output_folder = "output_dmg"
    os.makedirs(output_folder, exist_ok=True)  # laver mappen hvis den ikke findes

    # --- Lav filnavn ud fra argumenter + tidsstempel ---
    player_name = player.get("name", "player")
    weapon_name = weapon.get("name", "weapon")
    armor_name = armor.get("name", "armor")
    pet_name = pet.get("name", "pet")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{player_name}_{weapon_name}_{armor_name}_{pet_name}_{timestamp}.csv"
    filepath = os.path.join(output_folder, filename)
    
    # --- Skriv CSV med kolonner for hver mob-type ---
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(formatted_dmg.keys())   # header
        writer.writerow(formatted_dmg.values()) # værdier

    # --- Åbn filen automatisk (Windows) ---
    #     os.startfile(filepath)
    
    return formatted_dmg
    
    #    if dmg < 1000:
    #        return round(dmg,2)
    #    elif dmg > 1000:
    #    dmg_k = dmg/1000
    #    return round(dmg_k,2),"k"
    #    else:
    #        print("Error in function")

#   Variabler
#   
#   Weapons
Hand = {
    "name":"Hand",
    "base_damage": 0,
    "strength": 0,
    "Crit_dmg": 0,
    "Crit_chance":0,
    "sharpness": 0,
    "smite":0,
    "bane": 0,
    "cubism":0,
    "spider_dmg":0,
    "zombie_dmg":0,
    "Defense":0,
}
Silk_Edge = {
    "name":"Silk_Edge",
    "base_damage": 222.5,
    "strength": 179.5,
    "Crit_dmg": 177.5,
    "Crit_chance":1,
    "sharpness": 5,
    "bane": 0,
    "cubism":5,
    "gravity":0,
    "impaling":3,
    "ender_slayer":5,
    "spider_dmg":0,
    "zombie_dmg":0,
}
Scorpion = {
    "name":"Scorpion",
    "base_damage": 128,
    "strength": 78,
    "Crit_dmg": 160,
    "Crit_chance":1,
    "sharpness": 0,
    "bane": 6,
    "cubism":0,
    "spider_dmg":250/100,
    "zombie_dmg":0,
}
Tarantula_Fang = {
    "name":"Tarantula_Fang",
    "base_damage": 110,
    "strength": 72,
    "Crit_dmg": 130,
    "Crit_chance":1,
    "sharpness": 0,
    "bane": 6,
    "cubism":0,
    "spider_dmg":200/100,
    "zombie_dmg":0,
}
Reaper_Falchion_M = {
    "name":"Reaper_Falchion_M",
    "base_damage": 138,
    "strength": 118,
    "Crit_dmg": 115,
    "Crit_chance":5,
    "sharpness": 0,
    "smite":6,
    "bane": 0,
    "cubism":0,
    "spider_dmg":0,
    "zombie_dmg":200/100,
}
Reaper_Falchion_R = {
    "name":"Reaper_Falchion_R",
    "base_damage": 140,
    "strength": 120,
    "Crit_dmg": 105,
    "Crit_chance":15,
    "sharpness": 0,
    "smite":6,
    "bane": 0,
    "cubism":0,
    "spider_dmg":0,
    "zombie_dmg":200/100,
}
AD_blade = {
    "name":"AD_blade",
    "base_damage":198.29,
    "strength":160.44,
    "Crit_dmg":137.76,
    "sharpness":5,
    "bane":0,
    "spider_dmg":0,
    "zombie_dmg":0,
}
Livid_dagger = {
    "name":"Livid_dagger",
    "base_damage": 231.8,
    "strength": 90.8,
    "Crit_dmg": 221,
    "Crit_chance":103,
    "sharpness": 6,
    "smite":0,
    "bane": 0,
    "cubism":5,
    "gravity":5,
    "impaling":5,
    "ender_slayer":5,
    "spider_dmg":0,
    "zombie_dmg":0,
}
Neromancer_sword_R = {
    "name":"Neromancer_sword_R",
    "base_damage": 267.6,
    "strength": 142.6,
    "Crit_dmg": 0,
    "Crit_chance":0,
    "sharpness": 0,
    "smite":0,
    "bane": 0,
    "cubism":0,
    "spider_dmg":0,
    "zombie_dmg":0,
    "Defense":125,
}
Neromancer_sword_M = {
    "name":"Neromancer_sword_M",
    "base_damage": 295,
    "strength": 174.5,
    "Crit_dmg": 170,
    "Crit_chance":1,
    "sharpness": 6,
    "smite":0,
    "bane": 0,
    "cubism":5,
    "gravity":5,
    "impaling":3,
    "ender_slayer":5,
    "spider_dmg":0,
    "zombie_dmg":0,
    "Defense":132.5,
}

FoT = {
    "name":"FoT",
    "base_damage": 180,
    "strength": 332,
    "Crit_dmg": 150,
    "Crit_chance":1,
    "sharpness": 6,
    "smite":0,
    "bane": 0,
    "cubism":0,
    "spider_dmg":0,
    "zombie_dmg":0,
    "Defense":0,
}
# Armor

no_armor = {
    "name":"no_armor",
    "xdmg":1,
    "Health":0,
    "Defense":0,
    "True_def":0,
    "Strength":0,
    "Crit_Chance":0,
    "Crit_dmg":0,
    "Health_regen":0,
    "Speed":0,
    "Undead_def":0,
    "Arachnal_def":0,
    }

Tarantula_armor = {
    "name":"Tarantula_armor",
    "xdmg":2,
    "Health":225+247+230.5+192,
    "Defense":128+150+139+117,
    "Strength":8+8+8+8,
    "Crit_Chance":5+5+5+5,
    "Crit_dmg":14+14+14+14,
    "Health_regen":10+10+10+10,
    "Speed":0+0+0+5.5,
    "Undead_def":0,
    "Arachnal_def":215+215+215+215,
    }  

Perfect_armor = {
    "name":"Perfect_armor",
    "xdmg":1,
    "Health":233+295+295+115,
    "Defense":143.5+510+488+529,
    "True_def":0+5+0+0,
    "Strength":0,
    "Crit_Chance":0,
    "Crit_dmg":0,
    "Health_regen":10+10+10+10,
    "Speed":6,
    "Undead_def":0,
    "Arachnal_def":0,
    }
Rampart_armor = {
    "name":"Rampart_armor",
    "xdmg":1,
    "Health":0,
    "Defense":0,
    "Strength":0,
    "Crit_Chance":0,
    "Crit_dmg":0,
    }
Shadow_Assassin_Armor = {
    "name":"Shadow_Assassin_Armor",
    "xdmg":1,
    "Health":291+319+348.4+247.5,
    "Defense":117+137+138.8+98.3,
    "Strength":35.5+33+34+34.5,
    "Crit_Chance":5+5+5+5,
    "Crit_dmg":41.5+39+40+40.4,
    "Health_regen":10+10+10+10,
    "Speed":7.7+7+7.28+13.42,
    "Undead_def":0,
    "Arachnal_def":0,
}
Revenant_armor_M = {
    "name":"Revenant_armor_M",
    "xdmg":1,
    "Health":187+261+201+181,
    "Defense":61+96+76+56,
    "Strength":6+6+6+6,
    "Crit_Chance":8+8+8+8,
    "Crit_dmg":6+6+6+6,
    "Health_regen":10+10+0+0,
    "Speed":1+1+1+7,
    "Undead_def":0+200+220+220+(100),
    "Arachnal_def":0,
}
Revenant_armor_R = {
    "name":"Revenant_armor_R",
    "xdmg":1,
    "Health":233+295+235+215,
    "Defense":143.5+110+90+70,
    "True_def":0,
    "Strength":0+8+8+8,
    "Crit_Chance":0+5+5+5,
    "Crit_dmg":0+14+14+14,
    "Health_regen":10+0+0+0,
    "Speed":0,
    "Undead_def":0+200+200+200+(100),
    "Arachnal_def":0,
    }

# Player
MatizenDK={
    "name":"MatizenDK",
    "Combat_level_skill": 164/100,
    "Health":1278,
    "Defense":73,
    "Strength":342.72,
    "Crit_Chance":49.5,
    "Crit_dmg":246.72,
    "ferocity":0,
    "Magic_find":11.5,
    "Pet_luck":37,
    "Speed":144,
    }
Redlom3n ={
    "name":"Redlom3n",
    "Combat_level_skill": 160/100,
    "Health":1879.5,
    "Defense":115,
    "Strength":187,
    "Crit_Chance":49.5,
    "Crit_dmg":62,
    "ferocity":0,
    "Magic_find":15,
    "Pet_luck":52,
    "Speed":121,
    }
# Enchantmens
Bane_value = {
    1:0.1,
    2:0.2,
    3:0.3,
    4:0.4,
    5:0.6,
    6:0.8,}
Sharp_value = {
    1:0.05,
    2:0.1,
    3:0.15,
    4:0.2,
    5:0.3,
    6:0.45,
    7:0.65,}
Smite_value = {
    1:0.1,
    2:0.2,
    3:0.3,
    4:0.4,
    5:0.6,
    6:0.8,}
Gravity_value = {
    1:0.1,
    2:0.2,
    3:0.3,
    4:0.4,
    5:0.6,}
Impaling_value = {
    1:0.1,
    2:0.2,
    3:0.3,
    4:0.4,
    5:0.6,}
Cubism_value = {
    1:0.1,
    2:0.2,
    3:0.3,
    4:0.4,
    5:0.6,}
Ender_slayer_value = {
    1:0.15,
    2:0.3,
    3:0.45,
    4:0.6,
    5:0.8,}

# Pets
Test_pet = {
    "name":"Test_pet",
    "Health":0,
    "Defense":0,
    "True_def":0,
    "Strength":0,
    "Crit_Chance":0,
    "Crit_dmg":0,
    "Health_regen":0,
    "Speed":0,
    "ferocity":0,
    "Magic_find":0,
    "Pet_luck":0,
    "Extra_weapon_base_dmg":0,
    "Extra_weapon_strength":0,
}
Tarantula_pet = {
    "name":"Tarantula_pet",
    "Health":0,
    "Defense":0,
    "True_def":0,
    "Strength":9.3,
    "Crit_Chance":13.02,
    "Crit_dmg":39.06,
    "Health_regen":0,
    "Speed":0,
    "ferocity":0,
    "Magic_find":0,
    "Pet_luck":0,
    "Extra_weapon_base_dmg":0,
    "Extra_weapon_strength":0,
}
Lion_pet = {
    "name":"Lion_pet",
    "Health":0,
    "Defense":0,
    "True_def":0,
    "Strength":43,
    "Crit_Chance":5,
    "Crit_dmg":0,
    "Health_regen":0,
    "Speed":0,
    "ferocity":4.3,
    "Magic_find":21.5,
    "Pet_luck":0,
    "Extra_weapon_base_dmg":17.2,
    "Extra_weapon_strength":17.2,
}

# Thaumaturgist
Adept = {
    "Health":456,
    "Defense":253,
    "Strength":0,
    "Crit_Chance":0,
    "Crit_dmg":0,
    "Vitality":0,
    "Intelligence":76,
    "ferocity":0,
    "Magic_find":0,
    "Pet_luck":0,
    "Speed":0,
}
Silky = {
    "Health":0,
    "Defense":0,
    "Strength":0,
    "Crit_Chance":0,
    "Crit_dmg":483,
    "Vitality":0,
    "Intelligence":0,
    "ferocity":0,
    "Magic_find":0,
    "Pet_luck":0,
    "Speed":13,
    "Attackt_speed":5
}
Sanguisuge = {
    "Health":107,
    "Defense":0,
    "Strength":254,
    "Crit_dmg":102,
    "Crit_Chance":0,
    "Vitality":25,
    "Intelligence":76,
    "Vitality":0,
    "Intelligence":0,
    "ferocity":0,
    "Magic_find":0,
    "Pet_luck":0,
    "Speed":0,
}
thaumaturgist_none = {
    "Health":0,
    "Defense":0,
    "Strength":0,
    "Crit_Chance":0,
    "Crit_dmg":0,
    "Vitality":0,
    "Intelligence":0,
    "ferocity":0,
    "Magic_find":0,
    "Pet_luck":0,
    "Speed":0,
}

Accessory_powers = {
    "none":0,
}
# Outputs

damage_dealt(MatizenDK,Neromancer_sword_M,Tarantula_armor,Tarantula_pet,thaumaturgist_none)

