"""
In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
"""


def LoadData():
    with open('input.txt', 'r') as choice_data:
        total = 0
        for line in choice_data:

        #X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!

            if line[2] == 'X':
                if line[0] == 'A':
                    total += 3
                if line[0] == 'B':
                    total += 1
                if line[0] == 'C':
                    total += 2

            if line[2] == 'Y':
                if line[0] == 'A':
                    total += 4
                elif line[0] == 'B':
                    total += 5
                elif line[0] == 'C':
                    total += 6

            if line[2] == 'Z':
                if line[0] == 'A':
                    total += 8
                if line[0] == 'B':
                    total += 9
                if line[0] == 'C':
                    total += 7

            #opponent A for Rock, B for Paper, and C for Scissors.
            #player  X for Rock, Y for Paper, and Z for Scissors.
            print(total)


            # (1 point for Rock, 2 for Paper, and 3 for Scissors)
            #(0 if you lost, 3 if the round was a draw, and 6 if you won).

LoadData()
