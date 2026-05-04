import os

# The specific list of 29 chip brands
CHIP_BRANDS = [
    # Potato Chips
    "lays", "ruffles", "pringles", "kettle_brand", "cape_cod", 
    "utz", "herrs", "zapps", "popchips", "miss_vickies", "better_made",
    
    # Tortilla & Corn Chips
    "doritos", "tostitos", "fritos", "takis", "sunchips", 
    "popcorners", "santitas", "on_the_border", "late_july",
    
    # Puffed & Extruded Chips
    "cheetos", "funyuns", "bugles", "chesters_puffcorn", "pirates_booty",
    
    # Veggie & Alternative Chips
    "garden_veggie_straws", "terra_chips", "stacys_pita_chips", "quest_protein_chips"
]

def create_directories():
    try:
        base_dir = os.path.join("data", "raw_images")
        
        os.makedirs(base_dir, exist_ok=True)
        print(f"Creating {len(CHIP_BRANDS)} specific chip brand directories in '{base_dir}/'..")

        for brand in CHIP_BRANDS:
            folder_path = os.path.join(base_dir, brand)
            os.makedirs(folder_path, exist_ok=True)

        print("Folders have been generated.")
    except Exception as e:
        print("Something went wrong with creating the directories..")

if __name__ == "__main__":
    create_directories()