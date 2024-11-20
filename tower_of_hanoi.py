
# Encoding: utf-8
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system
import time

tower1 = [3, 2, 1]
tower2 = []
tower3 = []

# Checks if tower has pieces correctly placed.
def checkTower(to_tower):
    tower = []
    if to_tower == 'a':
        tower = tower1
    if to_tower == 'b':
        tower = tower2
    if to_tower == 'c':
        tower = tower3
        
    aux = 1
    max_tower = 3
    for i in range(len(tower)):
        try:
            if tower[i] > tower[i+1]:
                aux += 1
            else:
                return -1               # Wrong move
        except IndexError:
            if aux == max_tower:       # Complete sorting. Tower complete.
                return 1                
            if aux != 0:                # Partial sorting. Move allowed.
                return 0

# Switches piece between towers
def switchPiece(from_tower, to_tower):
    piece = 0
    try:
        if from_tower == 'a':
            piece = tower1.pop()
            if to_tower == 'a':
                tower1.append(piece)
            if to_tower == 'b':
                tower2.append(piece)
            if to_tower == 'c':
                tower3.append(piece)
        if from_tower == 'b':
            piece = tower2.pop()
            if to_tower == 'a':
                tower1.append(piece)
            if to_tower == 'b':
                tower2.append(piece)
            if to_tower == 'c':
                tower3.append(piece)
        if from_tower == 'c':
            piece = tower3.pop()
            if to_tower == 'a':
                tower1.append(piece)
            if to_tower == 'b':
                tower2.append(piece)
            if to_tower == 'c':
                tower3.append(piece)
    except IndexError:
        return -1
        
    return 0
    

def showTowers():
    
    system('clear')
    print(f'Tower of Hanoi')
    print(f'A- {tower1}')
    print(f'B- {tower2}')
    print(f'C- {tower3}')
    
def resetAll():
    tower1.clear()
    tower2.clear()
    tower3.clear()

    for i in range(-3, 0): tower1.append(-1*i)

def isInputValid(move_input):

    if len(move_input) > 0:
        valid_labels = ['a', 'b', 'c']
        valid_separator = '-'

        label1_isvalid = move_input[0] in valid_labels
        separator_isvalid = move_input[1] == valid_separator
        label2_isvalid = move_input[2] in valid_labels

        if label1_isvalid and separator_isvalid and label2_isvalid:
            return True

    return False
    
def run():
    while True:
        from_tower = '0'
        to_tower = '0'
        
        while True:
            showTowers()
            action = str(input('From tower? to tower? (t1-t2): ').lower())

            if isInputValid(action):
                break
            else:
                showTowers()
                print(
                '''
Invalid input.
State your move with the formatted string: <from tower>-<to tower>
For example: The string a-c moves top piece from tower A to tower C.
                ''')
                input('Press Any Key to continue...')
            
        
        # Separates inputs from format
        for s in range(len(action)):
            if s == 0:
                from_tower = action[s]
            if s == 2:
                to_tower = action[s]
                
    
        switch = switchPiece(from_tower, to_tower)       # Makes a move
        if switch == -1:
            print(f'Ops! No pieces in current tower. Pick another.')
            time.sleep(3)
        
        if checkTower(to_tower) == -1:          # Validates It. Wrong move
            switchPiece(to_tower, from_tower)   # Unmakes the move
            print('Ops! Wrong move.')                # Warns the user
            time.sleep(3)
        elif checkTower(to_tower) == 0:         # Validates move. Move allowed
            pass                                
        else:                                   # Validates move. 3rd tower complete. Game won.
            if checkTower('c') == 1:
                showTowers()
                print('Congratulations, you made It!')  # User made It
                time.sleep(3)
                
                '''
                Loop for controling input validation at the end of game

                Variable yn controls the loop from outside, not only controling
                the validation flow, but the result after validation.

                In the input validation we have two loops to worry about, the main
                loop of the game, and the input validation loop below. When using
                continue and break keywords we must pay attention to the fact that
                these commands are not being executed in the main loop.
                '''
                yn = None           
                while yn == None:
                    yn = str(input('Would you like to play again? y/n?').lower())

                    if yn == 'y':
                        resetAll()
                        
                    elif yn == 'n':
                        print(f'Nice of you to drop by. Seeya!')
                        
                    else:
                        yn = None
                        showTowers()
                        print('Invalid input. Whether type \"y\" for yes, or \"n\" for no.')
                        time.sleep(3)
                
                if yn == 'y': continue
                if yn == 'n': break

            
run()
        

    
