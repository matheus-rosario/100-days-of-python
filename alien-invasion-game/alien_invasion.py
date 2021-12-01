print('''
.     .       .  .   . .   .   . .    +  .
  .     .  :     .    .. :. .___---------___.
       .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
    .  :       .  .  .:../:            . .^  :.:\.
        .   . :: +. :.:/: .   .    .        . . .:\
 .  :    .     . _ :::/:               .  ^ .  . .:\
  .. . .   . - : :.:./.                        .  .:\
  .      .     . :..|:                    .  .  ^. .:|
    .       . : : ..||        .                . . !:|
  .     . . . ::. ::\(                           . :)/
 .   .     : . : .:.|. ######              .#######::|
  :.. .  :-  : .:  ::|.#######           ..########:|
 .  .  .  ..  .  .. :\ ########          :######## :/
  .        .+ :: : -.:\ ########       . ########.:/
    .  .+   . . . . :.:\. #######       #######..:/
      :: . . . . ::.:..:.\           .   .   ..:/
   .   .   .  .. :  -::::.\.       | |     . .:/
      .  :  .  .  .-:.":.::.\             ..:/
 .      -.   . . . .: .:::.:.\.           .:/
.   .   .  :      : ....::_:..:\   ___.  :/
   .   .  .   .:. .. .  .: :.:.:\       :/
     +   .   .   : . ::. :.:. .:.|\  .:/|
     .         +   .  .  ...:: ..|  --.:|
.      . . .   .  .  . ... :..:.."(  ..)"
 .   .       .      :  .   .: ::/  .  .::\
''')
print("Welcome to Alien Invasion.")
print("Your mission is to escape from the planet.") 


decision = input("You see the Aliens arriving. Where do you want to go? Type 'left' or 'right'\n").lower()
if decision == "left":

  decision = input("You found a group of people who are trying to get to the extraction area together. Will you join the group or go alone? type 'join' or 'alone'\n").lower()

  if decision == "join":

    decision = input("With the help from the group, you were able to reach the extraction area alive, but there are only three spaceships remaining. Which one will you choose? Type 'left', 'middle' or 'right'\n").lower()

    if decision == "left":
      print("The spaceship you chose got exploded before leaving the planet. GAME OVER")
    
    elif decision == "middle":
      print("The spaceship you chose leaves the planet and reaches the lunar base safely. YOU WON")
    
    else:
      print("There were too many people trying to reach the spaceship and you weren't able to enter before it leaves. GAME OVER.")

  else:
    print("You got attacked by the Aliens. GAME OVER")

else:
  print("You got abducted by the UFO. GAME OVER.")