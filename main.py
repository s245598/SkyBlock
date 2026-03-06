from Skyblock_dmg import DamageCalculator
import json

def load_json(filename):
    """Load and return JSON data from file."""
    with open(filename, 'r') as file:
        return json.load(file)

def find_by_name(items, name):
    """Find an item in a list by its 'name' field."""
    for item in items:
        if item.get('name') == name:
            return item
    raise ValueError(f"Item '{name}' not found")

def main(name, weapon_name, armor_name, pet_name, thaumaturgist_name):
    # Load all JSON files
    enchantments = load_json('Json/enchantmens.json')
    players = load_json('Json/player.json')
    weapons_and_armor = load_json('Json/weapons.json')
    pets = load_json('Json/pets.json')
    thaumaturgists = load_json('Json/thaumaturgist.json')

    # Initialize calculator with enchantment configuration
    calc = DamageCalculator(enchantments)

    # Select specific items by name
    player = find_by_name(players, name)
    weapon = find_by_name(weapons_and_armor, weapon_name)
    armor = find_by_name(weapons_and_armor, armor_name)
    pet = find_by_name(pets, pet_name)
    thaumaturgist = find_by_name(thaumaturgists, thaumaturgist_name)

    # Calculate damage
    output = calc.damage_dealt(player, weapon, armor, pet, thaumaturgist)
    
    # Print results
    print(f"Damage results for {player['name']}:")
    for mob_type, damage in output.items():
        print(f"  {mob_type}: {damage}")

if __name__ == "__main__":
    name = "MatizenDK"
    weapon_name = "Neromancer_sword_M"
    armor_name = "Tarantula_armor"
    pet_name = "Tarantula_pet"
    thaumaturgist_name = "thaumaturgist_none"

    main(name, weapon_name, armor_name, pet_name, thaumaturgist_name)