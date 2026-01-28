print('''
                 __..--.                                   _.._
    _..--''_______|-._____  ______________________|``  __``--.._
   '-.-..---..---..---..--''.---..---..---..---..---..---..---.-'
     |_::___::___::___::___::___::___::___::___::___::___::___|
     |________________________________________________________|
     '.--.':'.--.' '.--.'  '.--.'  '.--.'  '.--.' '.--.' '.--.'
      |''|.|.|''|-. |''|    |''|    |''|    |''|   |''|.|.|''|
      |''|.| |''| | |''|    |''|    |''|    |''|   |''| |.|''|
      |''|.|.|''| | |''|    |''|    |''|    |''| _,|''|.|.|''|
      |''|.| |''|.| |''|    |''|    |''|    |''|/ .|''| |.|''|
      |''|.|.|''| |_|''|`.__|''|,--'|''|``-.|''|   |''|.|.|''|
      |''|.| |''| |.|''| |  |''|  __|''|   ||''|.  |''| |.|''|
      |''|.|.|''| | |''| |  |''| |  |''|   ||''|   |''|.|.|''|
      |''|.| |''|.| |''| |  |''| |  |''|   ||''|  .|''| |.|''|
      |''|.|.|''| | |''| |__|''|_|__|''|___||''|   |''|.|.|''|
      |''|_|_|__| |.|''|'   |''|    |''|    |''|-._|''| |.|''|
      |'/  )| | ||  |''|    |''|    |''|    |''|   |''|'|.|''|
    .-'|`-' | | ||--''''----''''----''''----''''---''''---''''-.
  .'---|| | | |,''--.,-------------------.----------------------'.
 '-----|| | | /  - - - - - - - - ,---. -  \-----------------------'
       || | | : _ _,---._ _ _ _ _`._.'_ _ :    TREASURE                 
       ||_|_|_\  _ `---' _ _ _ ,._ _ _ _  /       HUNT
               `--------------'--`-------'          GAME
''')
print('''Welcome to the Realm of Shadows.
Your mission is to claim the Crystal of Eternity.
There are two paths ahead, which one do you choose to follow?
Path of Darkness or Path of Light? Type 'light' or 'dark'
''')
first = input()
if first == "dark":
    print('''Up ahead is the Blood River!
    Do you want to cross it or wait for a Valkyrie?
    Type 'cross' or 'wait'
    ''')
    second = input()
    if second == "wait":
        print('''Three doors are open to you, which one do you step into?
        Gate of Flames?(red) Gate of Shadows?(blue) Gate of Dawn?(gold)
        ''')
        third = input()
        if third == "red":
            print("Consumed by hellfire. Game Over.")
        elif third == "blue":
            print("Devoured by shadow beasts. Game Over.")
        elif third == "gold":
            print("You claim the Crystal of Eternity. YOU WIN!")
        else:
            print("Lost in eternal darkness. Game Over.")
    else:
        print("Dragged under by river wraiths. Game Over.")
else:
    print("Ambushed by vampires. Game Over.")