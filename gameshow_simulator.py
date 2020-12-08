from random import choice
from time import sleep

def play_gameshow(doors, iterations):
    wins = 0
    played = 0
    i = 1
    while i < iterations:
        i += 1
        win_selection = choice(range(1,doors+1))
        player_selection = choice(range(1,doors+1))
        if player_selection == win_selection:
            doors_left = list(range(1,doors+1))
            doors_left.remove(win_selection)
            host_selection = choice(doors_left) 
        else:
            host_selection = win_selection

        if win_selection == host_selection:
            wins+=1

        played+=1

        print("Won " + str(wins) + '/' + str(played) + ' (' + str(round((wins/played)*100)) + '%)')
        
        sleep(0.05)

print("*** Gameshow Problem Simulator ***")
input_doors = input("How many doors to choose from? ")
input_iterations = input("How many games to simulate? ")


try:
    play_gameshow(int(input_doors), int(input_iterations))
except:
    print("Something whent wrong")

