import rpg

kitchen = rpg.Room("Kitchen")

kitchen.set_description("a cute white room where\nount Nilda cooks for my"
                        " family!")


dinning_room = rpg.Room("Dinning Room")
dinning_room.set_description("an illuminated room,\nwith a cristal "
                             "chandelier and a square glass table"
                             "with two wood cupboards\nthat serve as "
                             "wine cellars :p")


living_room = rpg.Room("Living Room")
living_room.set_description("a big room, field with\npompous furniture "
                            "and glass doors to the inside"
                            "garden and the pool :)")

dinning_room.link_to_room(kitchen, "north")
dinning_room.link_to_room(living_room, "east")
kitchen.link_to_room(dinning_room, "south")
living_room.link_to_room(dinning_room, "west")

dave = rpg.Enemy("Dave", "A smelly zombie")
dave.set_conversation("Me want brainnnnnsss >:(")
dave.set_weakness("dog")
dave.set_stolen_item("nothing")

catrina = rpg.Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Why hello there!")
catrina.set_greetings("Hi, my name is Catrina, it's nice to meet you!")

cheese = rpg.Item("cheese")
cheese.set_desc_item("a large and smelly block of cheese")

dog = rpg.Item("dog")
dog.set_desc_item("a protective dog, cute with you,"
                     "\nmercilessly against your enemies")

dinning_room.set_character(dave)
living_room.set_character(catrina)
kitchen.set_item(cheese)
living_room.set_item(dog)


current_room = kitchen
backpack = []
ready_to_fight = None
fight_mode = not None
dead = False
victory = not None
defeats = 0


while dead == False:
    print("\n")
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    current_character = isinstance(inhabitant, rpg.Friend)
    current_room.get_details()

    if item is not None:
        print("\n")
        item.describe_item()

    if inhabitant is not None:
        print("\n")
        inhabitant_name = inhabitant.name
        inhabitant.describe()

    command = input("\n> ")

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            if victory is not None:
                inhabitant.talk()

            else:
                print("\nThere's no one here...")

        else:
            print("\nThere's no one here...")

    elif command == "defeats":
        if defeats == 0:
            print("\nYou didn't defeat any enemies yet! Look around," \
                  "\nperhaps you will find one..,")

        else:
            print("\nDefeated enemies: " + inhabitant.number_of_defeats())

    elif command == "fight":
        if inhabitant == None:
            print("\nThere's no one here...")

        else:
            if current_character == True:
                print("\nYou can't fight " + inhabitant.name +
                      ", he(she)'s a harmless character!")

            else:
                if fight_mode == None:
                    print("\nYou don't have items to fight this enemy, "
                          "\nlook around to see if you can find something...")

                else:
                    if  victory is not None:
                        if current_character == False:
                            print("\nWhat will you fight with?")
                            fight_with = input("\n> ")

                            if fight_with in backpack:
                                ready_to_fight = inhabitant.fight(fight_with)
                                if ready_to_fight == True:
                                    dead = False
                                    print("\nDo you wish to steal from " + inhabitant.name + "?")
                                    response = input("> ")

                                    if response == "steal":
                                        result = inhabitant.steal()

                                        if result == True:
                                            print(inhabitant.get_stolen_item())

                                    elif response == "no":
                                        print("\nLet's continue our adventure then!")

                                    victory = inhabitant.defeated()
                                    defeats = inhabitant.number_of_defeats()


                                elif ready_to_fight == None:
                                    print("")

                                elif ready_to_fight == False:
                                    dead = True

                            else:
                                print("\nYou don't have this item!"
                                      "\nlook around to see if you can find something...")
                                print("\n")
                                ready_to_fight = None
                                fight_mode = None

                    else:
                        print("\nThere's no one here...")


    elif command == "steal":
        if inhabitant is not None:
            if inhabitant_name is not None:
                if current_character == False:
                    print("\nYou can only steal from " + inhabitant.name + " if you\ndefeat your enemy!")

                else:
                    print("\nYou can't steal from " + inhabitant.name +
                          ", he(she)'s a good character!")

            else:
                print("\nThere's no one here...")
        else:
            print("\nThere's no one here...")

    elif command == "greet":
        if inhabitant is not None:
            if inhabitant_name is not None:
                if current_character == True:
                    inhabitant.greets()

                else:
                    print("\nThis character doesn't look so friendly...")

            else:
                print("\nThere's no one here...")

        else:
            print("\nThere's no one here...")

    elif command == "take":
        if item is not None:
            backpack.append(item.name_item)
            current_room.item_was_taken()

        elif item == None:
            print("\nThere's no item here for you to take...")

    else:
        print("\nInvalid command...")




