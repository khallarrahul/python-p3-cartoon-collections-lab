def roll_call_dwarves(dwarf_names):
    i = 0
    for names in dwarf_names:
        i += 1
        print(f"{i}. {names}")

    return f"{i}. {names}"


roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])


def summon_captain_planet(planeteer_calls):
    new_list = []
    for call in planeteer_calls:
        new_list.append(call.capitalize() + "!")
    print(new_list)
    return new_list


summon_captain_planet(["earth", "wind", "fire", "water", "heart"])


def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            print("True")
            return True

    print("False")
    return False


long_planeteer_calls(["two", "go", "industrious", "bop"])


def find_the_cheese(food_items):
    cheese = ["cheddar", "gouda", "camembert"]

    for item in food_items:
        if item in cheese:
            print(item)
            return item

    print(None)
    return None


find_the_cheese(["garlic", "rosemary", "bread"])
