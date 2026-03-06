import csv
import os 
from datetime import datetime
import json

class DamageCalculator:
    def __init__(self, enchantments_config):
        """Initialize with enchantment configuration from JSON."""
        self.Bane_value = enchantments_config['Bane_value']
        self.Sharp_value = enchantments_config['Sharp_value']
        self.Smite_value = enchantments_config['Smite_value']
        self.Gravity_value = enchantments_config['Gravity_value']
        self.Impaling_value = enchantments_config['Impaling_value']
        self.Cubism_value = enchantments_config['Cubism_value']
        self.Ender_slayer_value = enchantments_config['Ender_slayer_value']
        self.mob_enchants = enchantments_config['mob_enchants']

    def dmg_calculator(self, player, weapon, armor, pet, thaumaturgist, 
                   Base_dmg, Strength, Crit_Damage, Additive_Multiplier, 
                   Multiplicative_Multiplier, enchants):
        """
        Calculate damage for all mob types using a single formula.
        
        enchants: dictionary mapping mob types to their enchant bonus values
        """
        damage_results = {}
        
        for mob_type, enchant_value in enchants.items():
            dmg = ((5 + Base_dmg) * (1 + (Strength / 100)) * 
                   (1 + (Additive_Multiplier + enchant_value)) * 
                   Multiplicative_Multiplier) * (1 + (Crit_Damage / 100))
            damage_results[f"{mob_type}_dmg"] = dmg
        
        return damage_results

    def damage_dealt(self, player, weapon, armor, pet, thaumaturgist):
        # Get enchant values from weapon
        Bane = self.Bane_value.get(str(weapon.get("bane", 0)), 0)
        Sharp = self.Sharp_value.get(str(weapon.get("sharpness", 0)), 0)
        Smite = self.Smite_value.get(str(weapon.get("smite", 0)), 0)
        Gravity = self.Gravity_value.get(str(weapon.get("gravity", 0)), 0)
        Impaling = self.Impaling_value.get(str(weapon.get("impaling", 0)), 0)
        Cubism = self.Cubism_value.get(str(weapon.get("cubism", 0)), 0)
        Ender_slayer = self.Ender_slayer_value.get(str(weapon.get("ender_slayer", 0)), 0)

        x2_dmg = armor.get("xdmg",1)
        if x2_dmg == 0:
            x2_dmg = 1  # In case xdmg=0 

        if weapon.get("bane") > 0:
            Bane_perk = (15/100) # Spider Essence Shop 15% dmg increase to spiders
        else:
            Bane_perk = 0

        # Perks
        spider_perks = Bane_perk + weapon["spider_dmg"]

        # Calculate stats
        Additive_Multiplier = player["Combat_level_skill"]
        Multiplicative_Multiplier = (1 * (x2_dmg))
        Strength = (weapon["strength"] + player["Strength"] + armor["Strength"] + 
                   pet["Extra_weapon_strength"] + thaumaturgist["Strength"])
        Crit_Damage = (weapon["Crit_dmg"] + player["Crit_dmg"] + armor["Crit_dmg"] + 
                      pet["Crit_dmg"] + thaumaturgist["Crit_dmg"])
        Base_dmg = weapon["base_damage"] + pet["Extra_weapon_base_dmg"]

        # Build enchant values dictionary
        enchant_values = {
            "Gravity": Gravity,
            "Sharp": Sharp,
            "Impaling": Impaling,
            "Bane": Bane,
            "Bane_perk": Bane_perk,
            "Cubism": Cubism,
            "Ender_slayer": Ender_slayer,
            "Smite": Smite
        }

        # Calculate enchants dynamically from config
        enchants = {}
        for mob_type, components in self.mob_enchants.items():
            enchant_total = sum(enchant_values.get(comp, 0) for comp in components)
            # Special case for Arthropod which includes spider_perks
            if mob_type == "Arthropod":
                enchant_total += weapon["spider_dmg"]
            enchants[mob_type] = enchant_total

        dmg_results = self.dmg_calculator(player, weapon, armor, pet, thaumaturgist,
                   Base_dmg, Strength, Crit_Damage, Additive_Multiplier, 
                   Multiplicative_Multiplier, enchants)


        dmg = dmg_results

        formatted_dmg = {}

        for name, value in dmg.items():
            if value < 1000:
                formatted_dmg[name] = round(value, 8)

            elif value > 1000:
                formatted_dmg[name] = str(round(value / 1000, 4)) + "k"
            else:
                print(f"Error in {name}")
                formatted_dmg[name] = None 


        
        output_folder = "output_dmg"
        os.makedirs(output_folder, exist_ok=True)

        player_name = player.get("name", "player")
        weapon_name = weapon.get("name", "weapon")
        armor_name = armor.get("name", "armor")
        pet_name = pet.get("name", "pet")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{player_name}_{weapon_name}_{armor_name}_{pet_name}_{timestamp}.csv"
        filepath = os.path.join(output_folder, filename)
        
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(formatted_dmg.keys()) 
            writer.writerow(formatted_dmg.values())

        
        return formatted_dmg
        


