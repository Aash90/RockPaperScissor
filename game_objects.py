from enum import Enum


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

class Choices(Enum):

    Rock = 'I beat Scissor and Lizard'
    Paper = 'Paper'
    Scissor = 'Scissor'
    Lizard = 'Lizard'
    Spock = 'Spock'

    def beats(self, other_choice):
        beats_map = { self.Rock: other_choice in [self.Scissor, self.Lizard] }

        return beats_map.get(self)



