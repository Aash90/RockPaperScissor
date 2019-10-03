"""
This file is responsible creating/removing Objects and their associated Rules for the game.

For e.g

"Rock":{
                "beats_to" : ["Scissor", "Lizard"],
                "lose_to"  : ["Paper", "Spock"]
        }
In the above example the rule is defined for the "Rock" object.

The "beats_to" value is a list of Objects which are defeated by Rock(i.e lose againts Rock)
The "lose_to" value is a list of Objects which defeat the Rock(i.e beats Rock)
So in order to extend the game for more and more objects. User is required to add these rules
and an entry in the GAME_RULES object as shown in above sample.

"""

GAME_RULES = {
             "Rock":{
                "beats_to" : ["Scissor", "Lizard"],
                "lose_to"  : ["Paper", "Spock"]
                },

             "Paper":{
                "beats_to" : ["Rock", "Spock"],
                "lose_to"  : ["Scissor", "Lizard"]
                },

             "Scissor":{
                "beats_to" : ["Paper","Lizard"],
                "lose_to"  : ["Rock", "Spock"]
                },

            "Lizard": {
                "beats_to": ["Paper", "Spock"],
                "lose_to": ["Rock", "Scissor"]
            },
            "Spock": {
                "beats_to": ["Rock", "Scissor"],
                "lose_to": ["Lizard", "Paper"]
            },

}
