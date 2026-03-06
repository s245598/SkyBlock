import csv
import os 
from datetime import datetime

class DamageCalculator:
    def __init__(self, Bane_value, Sharp_value, Smite_value, Gravity_value, Impaling_value, Cubism_value, Ender_slayer_value):
        self.Bane_value = Bane_value
        self.Sharp_value = Sharp_value
        self.Smite_value = Smite_value
        self.Gravity_value = Gravity_value
        self.Impaling_value = Impaling_value
        self.Cubism_value = Cubism_value
        self.Ender_slayer_value = Ender_slayer_value

    def damage_dealt(player,weapon,armor,pet,thaumaturgist):

        x2_dmg = armor.get("xdmg",1)
        if x2_dmg == 0:
            x2_dmg = 1  # In case xdmg=0 

        Bane = player["Bane_value"].get(weapon.get("bane", 0), 0)
        Sharp = player["Sharp_value"].get(weapon.get("sharpness", 0), 0)
        Smite = player["Smite_value"].get(weapon.get("smite", 0), 0)
        Gravity = player["Gravity_value"].get(weapon.get("gravity",0),0)
        Impaling = player["Impaling_value"].get(weapon.get("impaling",0),0)
        Cubism = player["Cubism_value"].get(weapon.get("cubism",0),0)
        Ender_slayer = player["Ender_slayer_value"].get(weapon.get("ender_slayer",0),0)

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

        for name, value in dmg.items():
            if value < 1000:
                formatted_dmg[name] = round(value, 8)

            elif value > 1000:
                formatted_dmg[name] = str(round(value / 1000, 4)) + "k"
            else:
                print(f"Error in {name}")
                formatted_dmg[name] = None  # hvis du vil have en default


        
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

    # Outputs

    damage_dealt(MatizenDK,Neromancer_sword_M,Tarantula_armor,Tarantula_pet,thaumaturgist_none)

