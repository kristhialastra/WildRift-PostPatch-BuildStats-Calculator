class Item:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def update_stats(self):
        print(f"-----------------------\nINPUT STATS: {self.name}\n")
        for stat, values in self.stats.items():
            print(f"+ {stat}")
            try:
                current = int(input("Current: "))
                post_patch = int(input("Post-patch: "))
                percent_diff = ((post_patch - current) / current) * 100
                self.stats[stat] = (current, post_patch, percent_diff)
                print(f"Change: {percent_diff:.2f}%")
            except ValueError:
                print("Please enter a valid integer.")
                raise
            except ZeroDivisionError:
                print("Division by zero is not allowed.")
                raise

    def percent_stats(self):
        total_percent_change = 0
        for stat, values in self.stats.items():
            _, _, percent_diff = values
            total_percent_change += percent_diff
        overall_change = total_percent_change / len(self.stats)
        print(f"\n{self.name} Overall % Change: {overall_change:.2f}%\n-----------------------")
        return overall_change

build_summary = {} 

def print_build_summary():
    print("\n///// SUMMARY /////")
    total_change = 0
    for item_name, percent_change in build_summary.items():
        print(f"{item_name} Overall % Change: {percent_change:.2f}%")
        total_change += percent_change
    if len(build_summary) > 0:  
        overall_build_change = total_change / len(build_summary)
    else:
        overall_build_change = 0
    print(f"OVERALL BUILD % CHANGE POST-PATCH: {overall_build_change:.2f}%\n")


items = {
    "Physical": {
        1: Item("Bloodthirster", {"AD": (None, None), "CRIT%": (None, None)}),
        2: Item("Manamune", {"AD": (None, None), "MAX MANA": (None, None), "ABILITY HASTE": (None, None)}),
        3: Item("Mortal Reminder", {"AD": (None, None), "CRIT%": (None, None)}),
        4: Item("Black Cleaver", {"MAX HEALTH": (None, None), "AD": (None, None), "ABILITY HASTE": (None, None)}),
        5: Item("Trinity Force", {"MAX HEALTH": (None, None), "AD": (None, None), "AS": (None, None), "ABILITY HASTE": (None, None)})
    },
    "Magic": {
        1: Item("Morellonomicon", {"MAX HEALTH": (None, None), "AP": (None, None), "M. PEN": (None, None), "ABILITY HASTE": (None, None)}),
        2: Item("Riftmaker", {"MAX HEALTH": (None, None), "AP": (None, None), "M. PEN": (None, None), "ABILITY HASTE": (None, None)}),
        3: Item("Imperial Mandate", {"MAX HEALTH": (None, None), "AP": (None, None), "ABILITY HASTE": (None, None)}),
        4: Item("Crystalline Reflector", {"MAX HEALTH": (None, None), "AR": (None, None), "AP": (None, None), "M. PEN": (None, None)}),
        5: Item("Luden's Echo", {"AP": (None, None), "M. PEN": (None, None), "MAX MANA": (None, None), "ABILITY HASTE": (None, None)})
    },
    "Defense": {
        1: Item("Thornmail", {"MAX HEALTH": (None, None), "AR": (None, None)}),
        2: Item("Dawnshroud", {"MAX HEALTH": (None, None), "AR": (None, None), "MR": (None, None)}),
        3: Item("Guardian Angel", {"AD": (None, None), "AR": (None, None)}),
        4: Item("Sunfire Aegis", {"MAX HEALTH": (None, None), "ABILITY HASTE": (None, None)}),
        5: Item("Zeke's Convergence", {"MAX HEALTH": (None, None), "AR": (None, None), "MAX MANA": (None, None), "ABILITY HASTE": (None, None)})
    },
}

no_of_items = int(input("Enter no. of items: "))
item_number = 1

for _ in range(no_of_items):
    print(f"\n++++++++ ITEM #{item_number} ++++++++\n")
    item_number += 1
    print(f"-----------------------")
    print("CATEGORY\n[1] Physical\n[2] Magic\n[3] Defense")

    try:
        item_category_input = int(input("Select: "))
        categories = list(items.keys())

        if item_category_input in [1, 2, 3]:  
            category_name = categories[item_category_input - 1]
            item_options = items[category_name]
            print(f"-----------------------\nITEMS: {category_name}")
            for option, item in item_options.items(): 
                print(f"[{option}] {item.name}")
            item_choice = int(input("Select: "))

            if item_choice in item_options:
                selected_item = item_options[item_choice]
                selected_item.update_stats()
                overall_change = selected_item.percent_stats()
                build_summary[selected_item.name] = overall_change
                print_build_summary()  
            else:
                print("Invalid item number.")
        else:
            print("Invalid category.")
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Executing finally block.")
