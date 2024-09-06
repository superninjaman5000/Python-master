print('''
       88                                          
            ""                         ,d               
                                       88               
8b,dPPYba,  88 8b,dPPYba, ,adPPYYba, MM88MMM ,adPPYba,  
88P'    "8a 88 88P'   "Y8 ""     `Y8   88   a8P_____88  
88       d8 88 88         ,adPPPPP88   88   8PP"""""""  
88b,   ,a8" 88 88         88,    ,88   88,  "8b,   ,aa  
88`YbbdP"'  88 88         `"8bbdP"Y8   "Y888 `"Ybbd8"'  
88                                                      
88   
             .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''')


print("Welcome to Pirate Island")
print("Your mission is to survive")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "Left" or "right". ').lower()

if choice1 == "left":
    #continue in game
    choice2 = input("You have come to a island in the middle of the ocean, type 'wait' to wait for a boat or 'swim' to swim to the island. ").lower()

    if choice2 == "wait":
        choice3 = input("You arive at a house with 3 doors, "
                        "which colour do you choose to open. "
                         "  red, blue, or yellow ").lower()
        if choice3 == "red":
            print("oh no you fell into a volcano, game over!")
        elif choice3 == "yellow":
            print("you found the room full of treasure, you win!")
        elif choice3 == "blue":
            print("You fell into the ocean, swim back")
            
        else:
            print("You made the wrong choice, game over!")



    else:
        print("You encounter a group of pirates and you are attacked.")
else: 
    print("You have encountered a pirate, you are now captured.")
