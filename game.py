
import random, os, time

from game_objects import GAME_RULES


class Player(object):
    """
    The Player class is responsible for creating player objects in the game play.
    It uses parameters Name and Throw as properties of each Player object.

    For e.g: player1 = Player('P1')  player2 = Player('P2')
            player1.throw = 'Rock'   player2.throw = 'Paper'

     As shown above the choice of player in the game is set by the the throw parameter.
    """
    def __init__(self, name):
        """
        Takes player name as param for creating Player objects
        :param name: string value for the Player Name
        """
        self.name = name
        self.throw = None



class Game(object):
    """
    The Game class is responsible for the interactions and game play.
    It uses Player Class for creating entities for the game.
    """

    def __init__(self, user1, user2):
        """
        Accepts player names for the Game. Initializes params for the respective game.
        Game Map and Score variables are used in the game for co-ordination and decision making.
        Game map is created using the Rules of the Game

        :param user1: string value for the Player1 Name
        :param user2: string value for the Player2 Name
        """

        self.player1 = Player(user1)
        self.player2 = Player(user2)
        self.score = {self.player1: 0, self.player2: 0}
        self.game_map = dict((i + 1, v) for i, v in enumerate(GAME_RULES.keys()))


    def __player_comp_menu(self):
        """
        This method display menu items for the game of type Player v/s Computer

                ============== Player v/s Computer(SkyNet-X) : Game Started ============
                         Object List
                ----------------------------------------
                1 . Rock
                2 . Paper
                3 . Scissor
                S . Get Play Score
                X . Exit Play
                Player enter a choice to Throw:

        :return: None
        """
        print('\n ============== %s v/s Computer(SkyNet-X) : Game Started ============\n'%self.player2.name)

        print("\n \t Object List")
        print("--------" * 5)

        for k, v in self.game_map.items():
            print("%s . %s \n" % (k, v))
        print("%s . %s \n" % ('S', 'Get Play Score'))
        print("%s . %s \n" % ('X', 'Exit Play'))

    def __comp_comp_menu(self):
        """
        This method display menu items for the game of type Computer v/s Computer

            ============== Jarvis v/s SkyNet-X : Game Started ============
                     Option List
            ----------------------------------------
            P . Throw
            S . Check Score
            X . Exit Play

            Enter Option to play:

        :return: None
        """

        print('\n ============== Jarvis v/s SkyNet-X : Game Started ============\n')

        print("\n \t Option List")
        print("--------" * 5)

        print("%s . %s \n" % ('P', 'Throw'))
        print("%s . %s \n" % ('S', 'Check Score'))
        print("%s . %s \n" % ('X', 'Exit Play'))

    def __reset_screen(self):
        """
        This method is to reset(clear) screen.
        For Windows : 'cls'
        For Unix    : 'clear
        :return: None
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def __score_board(self):
        """
        This method is to display score of the current game on the screen.

              =============== Score Board ============
                    Jarvis: 1,     SkyNet-X: 1
              ========================================
        :return: None
        """

        (player1_name, player1_score, player2_name, player2_score) = self.get_game_score()

        print("\n ", "===" * 5, "Score Board", "===" * 5)
        print("  %s: %s, \t %s: %s" % (player1_name, player1_score,
                                       player2_name, player2_score))
        print(" ", "==" * 20, "\n")


    def __display_result(self):
        """
        This method is to display result for the current/recent match.
        It reads the details(score attribute of Game class) for the winner and displays on screen.

        ************************* Result ******************************************************
            Jarvis throws: Lizard       SkyNet-X throws: Paper      -----> Jarvis Wins <-----
        ***************************************************************************************

        :return: None
        """

        print("\n", "*********" * 5, "Result", "*********" * 5)
        print("\n %s throws: %s \t %s throws: %s" % (self.player1.name, self.player1.throw,
                                                  self.player2.name, self.player2.throw), end= "\t")
        winner = self.get_winner()

        if winner:
            print("\t -----> %s Wins <----- "%winner.name)
        else:
            print("\t -----> Its a TIE!!!, play again ! <-----")

        print("\n","**********" * 10)

    def __parse_input(self, msg):
        """
        This method is to read input from user and perform cleaning/simplification operations required for the game.
        For e.g  String Strip and String Lower

        :param msg, :type: String :
            message to be displayed to user while asking for inputs
        :return user_input: String value of the processed user inputs
        """
        user_input = input(msg).strip().lower()
        return user_input

    def get_game_score(self):
        """
        This method is used to fetch score of the Game play.
        :return Player and Player Score :type Tuple
        """
        (player1_name, player1_score,player2_name, player2_score) = (self.player1.name, self.score[self.player1],
                                                                     self.player2.name, self.score[self.player2])

        return (player1_name, player1_score,player2_name, player2_score)

    def get_winner(self):
        """
        This method is used to get the winner of the Game play.
        :return Player Object :type Player
        """
        if self.player2.throw in GAME_RULES[self.player1.throw].get('beats_to'):
            self.score[self.player1] += 1
            return self.player1

        elif self.player2.throw in GAME_RULES[self.player1.throw].get('lose_to'):
            self.score[self.player2] += 1
            return self.player2
        else:
            return None

    def run(self, game_type):
        """
        This method is used to trigger the game play.
        It uses param game type to decide the play to be executed
        :param game_type, :type String
            It decides the type of game to be executed
            1. Player v/s Computer
            2. Computer v/s Computer

        :return: None
        """
        # works for Windows screen clear
        self.__reset_screen()

        run_map = { 'user': self.comp_vs_ply, 'comp': self.comp_vs_comp }
        module = run_map.get(game_type)
        module()

        return

    def comp_vs_ply(self):
        """
        This method is used to trigger the game play of type Player v/s Computer.
        :return: None
        """
        self.__player_comp_menu()

        while True:

            # Player 1 is computer 1
            self.player1.throw = random.choice(list(GAME_RULES.keys()))

            # Player 2 is User
            player_input = self.__parse_input("\n%s enter a choice to Throw: "%self.player2.name)
            print("", end="\r")

            # to reset page
            self.__reset_screen()
            self.__player_comp_menu()

            try:
                if player_input == 's':
                    self.__score_board()
                elif player_input == 'x':
                    self.__reset_screen()
                    break

                elif int(player_input) not in self.game_map.keys():
                    print("xx" * 5, "Wrong IP..!", "xx" * 5, "\n")
                    continue
                else:
                    self.player2.throw = self.game_map.get(int(player_input))
                    self.__display_result()
            except ValueError as e:
                print(" XxxxxX Input Error: Please enter game options")
                continue

    def comp_vs_comp(self):
        """
        This method is used to trigger the game play of type Computer v/s Computer.
        :return: None
        """

        self.__comp_comp_menu()

        while True:
            user_input = self.__parse_input("Enter Option to play: ")
            self.__reset_screen()
            self.__comp_comp_menu()

            if user_input == 'p':
                for i in range(3):
                    print(" Waiting for Throw...: %s"%(i+1), end="\r")
                    time.sleep(1)
                print(".... %s" % (" !! Throw !! "))
                time.sleep(1)

                # Player 1 is computer 1
                self.player1.throw = random.choice(list(GAME_RULES.keys()))

                # Player 2 is computer 2
                self.player2.throw = random.choice(list(GAME_RULES.keys()))

                self.__display_result()

            elif user_input == 's':
                self.__score_board()

            elif user_input == 'x':
                 self.__reset_screen()
                 break
            else:
                print("xxxxxxxxxxxx Wrong Input, Try Again xxxxxxxxxxxx")


def main():
    """
    This method is the main program that is responsible to drive the Game.
    This module is responsble to present the initial Game Menu.

                      Game Menu
    ========================================
     1. Player v/s Computer
     2. Computer v/s Computer
     X. Exit Game

     Choose game option:

    :return: None
    """

    while True:

        print("\n","\t"*2," Game Menu ", "\t"*2)
        print("========"*5)

        print(" 1. Player v/s Computer \n 2. Computer v/s Computer \n X. Exit Game")
        try:
            choice = input("\n Choose game option: ").strip()

            if choice == '1':
                player_name = input("\n Enter Player name: ").strip()
                g = Game('SkyNet-X', player_name)
                g.run('user')

            elif choice == '2':
                g = Game('Jarvis', 'SkyNet-X')
                g.run('comp')
            elif choice.lower() == 'x':
                print("\n", "***" * 5, "Happy Gaming :)", "***" * 5)
                time.sleep(2)
                break

            else:
                print(" XxxxxX Input Error: Please enter game options")
        except Exception:
            print(" XxxxxX Input Error: Please enter game options")
            continue




if __name__ == "__main__":
    main()