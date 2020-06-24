import pygame

#Initializes PyGame 
pygame.init()

#Creates a window for game
win = pygame.display.set_mode((850,550))



#Sets the title of window
pygame.display.set_caption('Ultimate Tic-Tac-Toe')

ultimateBoard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

board1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board5 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board6 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board7 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board8 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board9 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


#Draws the game board
first = pygame.draw.rect(win, (255,255,255), (25,25,150,150))

first_first = pygame.draw.rect(win, (100,100,100), (30,30,40,40))
first_second = pygame.draw.rect(win, (100,100,100), (80,30,40,40))
first_third = pygame.draw.rect(win, (100,100,100), (130,30,40,40))

first_fourth = pygame.draw.rect(win, (100,100,100), (30,80,40,40))
first_fifth = pygame.draw.rect(win, (100,100,100), (80,80,40,40))
first_sixth = pygame.draw.rect(win, (100,100,100), (130,80,40,40))

first_seventh = pygame.draw.rect(win, (100,100,100), (30,130,40,40))
first_eighth = pygame.draw.rect(win, (100,100,100), (80,130,40,40))
first_ninth = pygame.draw.rect(win, (100,100,100), (130,130,40,40))

second = pygame.draw.rect(win, (255,255,255), (200,25,150,150))

second_first = pygame.draw.rect(win, (100,100,100), (205,30,40,40))
second_second = pygame.draw.rect(win, (100,100,100), (255,30,40,40))
second_third = pygame.draw.rect(win, (100,100,100), (305,30,40,40))

second_fourth = pygame.draw.rect(win, (100,100,100), (205,80,40,40))
second_fifth = pygame.draw.rect(win, (100,100,100), (255,80,40,40))
second_sixth = pygame.draw.rect(win, (100,100,100), (305,80,40,40))

second_seventh = pygame.draw.rect(win, (100,100,100), (205,130,40,40))
second_eighth = pygame.draw.rect(win, (100,100,100), (255,130,40,40))
second_ninth = pygame.draw.rect(win, (100,100,100), (305,130,40,40))

third = pygame.draw.rect(win, (255,255,255), (375,25,150,150))

third_first = pygame.draw.rect(win, (100,100,100), (380,30,40,40))
third_second = pygame.draw.rect(win, (100,100,100), (430,30,40,40))
third_third = pygame.draw.rect(win, (100,100,100), (480,30,40,40))

third_fourth = pygame.draw.rect(win, (100,100,100), (380,80,40,40))
third_fifth = pygame.draw.rect(win, (100,100,100), (430,80,40,40))
third_sixth = pygame.draw.rect(win, (100,100,100), (480,80,40,40))

third_seventh = pygame.draw.rect(win, (100,100,100), (380,130,40,40))
third_eighth = pygame.draw.rect(win, (100,100,100), (430,130,40,40))
third_ninth = pygame.draw.rect(win, (100,100,100), (480,130,40,40))

fourth = pygame.draw.rect(win, (255,255,255), (25,200,150,150))

fourth_first = pygame.draw.rect(win, (100,100,100), (30,205,40,40))
fourth_second = pygame.draw.rect(win, (100,100,100), (80,205,40,40))
fourth_third = pygame.draw.rect(win, (100,100,100), (130,205,40,40))

fourth_fourth = pygame.draw.rect(win, (100,100,100), (30,255,40,40))
fourth_fifth = pygame.draw.rect(win, (100,100,100), (80,255,40,40))
fourth_sixth = pygame.draw.rect(win, (100,100,100), (130,255,40,40))

fourth_seventh = pygame.draw.rect(win, (100,100,100), (30,305,40,40))
fourth_eighth = pygame.draw.rect(win, (100,100,100), (80,305,40,40))
fourth_ninth = pygame.draw.rect(win, (100,100,100), (130,305,40,40))

fifth = pygame.draw.rect(win, (255,255,255), (200,200,150,150))

fifth_first = pygame.draw.rect(win, (100,100,100), (205,205,40,40))
fifth_second = pygame.draw.rect(win, (100,100,100), (255,205,40,40))
fifth_third = pygame.draw.rect(win, (100,100,100), (305,205,40,40))

fifth_fourth = pygame.draw.rect(win, (100,100,100), (205,255,40,40))
fifth_fifth = pygame.draw.rect(win, (100,100,100), (255,255,40,40))
fifth_sixth = pygame.draw.rect(win, (100,100,100), (305,255,40,40))

fifth_seventh = pygame.draw.rect(win, (100,100,100), (205,305,40,40))
fifth_eighth = pygame.draw.rect(win, (100,100,100), (255,305,40,40))
fifth_ninth = pygame.draw.rect(win, (100,100,100), (305,305,40,40))

sixth = pygame.draw.rect(win, (255,255,255), (375,200,150,150))

sixth_first = pygame.draw.rect(win, (100,100,100), (380,205,40,40))
sixth_second = pygame.draw.rect(win, (100,100,100), (430,205,40,40))
sixth_third = pygame.draw.rect(win, (100,100,100), (480,205,40,40))

sixth_fourth = pygame.draw.rect(win, (100,100,100), (380,255,40,40))
sixth_fifth = pygame.draw.rect(win, (100,100,100), (430,255,40,40))
sixth_sixth = pygame.draw.rect(win, (100,100,100), (480,255,40,40))

sixth_seventh = pygame.draw.rect(win, (100,100,100), (380,305,40,40))
sixth_eighth = pygame.draw.rect(win, (100,100,100), (430,305,40,40))
sixth_ninth = pygame.draw.rect(win, (100,100,100), (480,305,40,40))

seventh = pygame.draw.rect(win, (255,255,255), (25,375,150,150))

seventh_first = pygame.draw.rect(win, (100,100,100), (30,380,40,40))
seventh_second = pygame.draw.rect(win, (100,100,100), (80,380,40,40))
seventh_third = pygame.draw.rect(win, (100,100,100), (130,380,40,40))

seventh_fourth = pygame.draw.rect(win, (100,100,100), (30,430,40,40))
seventh_fifth = pygame.draw.rect(win, (100,100,100), (80,430,40,40))
seventh_sixth = pygame.draw.rect(win, (100,100,100), (130,430,40,40))

seventh_seventh = pygame.draw.rect(win, (100,100,100), (30,480,40,40))
seventh_eighth = pygame.draw.rect(win, (100,100,100), (80,480,40,40))
seventh_ninth = pygame.draw.rect(win, (100,100,100), (130,480,40,40))

eighth = pygame.draw.rect(win, (255,255,255), (200,375,150,150))

eighth_first = pygame.draw.rect(win, (100,100,100), (205,380,40,40))
eighth_second = pygame.draw.rect(win, (100,100,100), (255,380,40,40))
eighth_third = pygame.draw.rect(win, (100,100,100), (305,380,40,40))

eighth_fourth = pygame.draw.rect(win, (100,100,100), (205,430,40,40))
eighth_fifth = pygame.draw.rect(win, (100,100,100), (255,430,40,40))
eighth_sixth = pygame.draw.rect(win, (100,100,100), (305,430,40,40))

eighth_seventh = pygame.draw.rect(win, (100,100,100), (205,480,40,40))
eighth_eighth = pygame.draw.rect(win, (100,100,100), (255,480,40,40))
eighth_ninth = pygame.draw.rect(win, (100,100,100), (305,480,40,40))

ninth = pygame.draw.rect(win, (255,255,255), (375,375,150,150))

ninth_first = pygame.draw.rect(win, (100,100,100), (380,380,40,40))
ninth_second = pygame.draw.rect(win, (100,100,100), (430,380,40,40))
ninth_third = pygame.draw.rect(win, (100,100,100), (480,380,40,40))

ninth_fourth = pygame.draw.rect(win, (100,100,100), (380,430,40,40))
ninth_fifth = pygame.draw.rect(win, (100,100,100), (430,430,40,40))
ninth_sixth = pygame.draw.rect(win, (100,100,100), (480,430,40,40))

ninth_seventh = pygame.draw.rect(win, (100,100,100), (380,480,40,40))
ninth_eighth = pygame.draw.rect(win, (100,100,100), (430,480,40,40))
ninth_ninth = pygame.draw.rect(win, (100,100,100), (480,480,40,40))

def draw():
    first = pygame.draw.rect(win, (255,255,255), (25,25,150,150))

    first_first = pygame.draw.rect(win, (100,100,100), (30,30,40,40))
    first_second = pygame.draw.rect(win, (100,100,100), (80,30,40,40))
    first_third = pygame.draw.rect(win, (100,100,100), (130,30,40,40))

    first_fourth = pygame.draw.rect(win, (100,100,100), (30,80,40,40))
    first_fifth = pygame.draw.rect(win, (100,100,100), (80,80,40,40))
    first_sixth = pygame.draw.rect(win, (100,100,100), (130,80,40,40))

    first_seventh = pygame.draw.rect(win, (100,100,100), (30,130,40,40))
    first_eighth = pygame.draw.rect(win, (100,100,100), (80,130,40,40))
    first_ninth = pygame.draw.rect(win, (100,100,100), (130,130,40,40))

    second = pygame.draw.rect(win, (255,255,255), (200,25,150,150))

    second_first = pygame.draw.rect(win, (100,100,100), (205,30,40,40))
    second_second = pygame.draw.rect(win, (100,100,100), (255,30,40,40))
    second_third = pygame.draw.rect(win, (100,100,100), (305,30,40,40))

    second_fourth = pygame.draw.rect(win, (100,100,100), (205,80,40,40))
    second_fifth = pygame.draw.rect(win, (100,100,100), (255,80,40,40))
    second_sixth = pygame.draw.rect(win, (100,100,100), (305,80,40,40))

    second_seventh = pygame.draw.rect(win, (100,100,100), (205,130,40,40))
    second_eighth = pygame.draw.rect(win, (100,100,100), (255,130,40,40))
    second_ninth = pygame.draw.rect(win, (100,100,100), (305,130,40,40))

    third = pygame.draw.rect(win, (255,255,255), (375,25,150,150))

    third_first = pygame.draw.rect(win, (100,100,100), (380,30,40,40))
    third_second = pygame.draw.rect(win, (100,100,100), (430,30,40,40))
    third_third = pygame.draw.rect(win, (100,100,100), (480,30,40,40))

    third_fourth = pygame.draw.rect(win, (100,100,100), (380,80,40,40))
    third_fifth = pygame.draw.rect(win, (100,100,100), (430,80,40,40))
    third_sixth = pygame.draw.rect(win, (100,100,100), (480,80,40,40))

    third_seventh = pygame.draw.rect(win, (100,100,100), (380,130,40,40))
    third_eighth = pygame.draw.rect(win, (100,100,100), (430,130,40,40))
    third_ninth = pygame.draw.rect(win, (100,100,100), (480,130,40,40))

    fourth = pygame.draw.rect(win, (255,255,255), (25,200,150,150))

    fourth_first = pygame.draw.rect(win, (100,100,100), (30,205,40,40))
    fourth_second = pygame.draw.rect(win, (100,100,100), (80,205,40,40))
    fourth_third = pygame.draw.rect(win, (100,100,100), (130,205,40,40))

    fourth_fourth = pygame.draw.rect(win, (100,100,100), (30,255,40,40))
    fourth_fifth = pygame.draw.rect(win, (100,100,100), (80,255,40,40))
    fourth_sixth = pygame.draw.rect(win, (100,100,100), (130,255,40,40))

    fourth_seventh = pygame.draw.rect(win, (100,100,100), (30,305,40,40))
    fourth_eighth = pygame.draw.rect(win, (100,100,100), (80,305,40,40))
    fourth_ninth = pygame.draw.rect(win, (100,100,100), (130,305,40,40))

    fifth = pygame.draw.rect(win, (255,255,255), (200,200,150,150))

    fifth_first = pygame.draw.rect(win, (100,100,100), (205,205,40,40))
    fifth_second = pygame.draw.rect(win, (100,100,100), (255,205,40,40))
    fifth_third = pygame.draw.rect(win, (100,100,100), (305,205,40,40))

    fifth_fourth = pygame.draw.rect(win, (100,100,100), (205,255,40,40))
    fifth_fifth = pygame.draw.rect(win, (100,100,100), (255,255,40,40))
    fifth_sixth = pygame.draw.rect(win, (100,100,100), (305,255,40,40))

    fifth_seventh = pygame.draw.rect(win, (100,100,100), (205,305,40,40))
    fifth_eighth = pygame.draw.rect(win, (100,100,100), (255,305,40,40))
    fifth_ninth = pygame.draw.rect(win, (100,100,100), (305,305,40,40))

    sixth = pygame.draw.rect(win, (255,255,255), (375,200,150,150))

    sixth_first = pygame.draw.rect(win, (100,100,100), (380,205,40,40))
    sixth_second = pygame.draw.rect(win, (100,100,100), (430,205,40,40))
    sixth_third = pygame.draw.rect(win, (100,100,100), (480,205,40,40))

    sixth_fourth = pygame.draw.rect(win, (100,100,100), (380,255,40,40))
    sixth_fifth = pygame.draw.rect(win, (100,100,100), (430,255,40,40))
    sixth_sixth = pygame.draw.rect(win, (100,100,100), (480,255,40,40))

    sixth_seventh = pygame.draw.rect(win, (100,100,100), (380,305,40,40))
    sixth_eighth = pygame.draw.rect(win, (100,100,100), (430,305,40,40))
    sixth_ninth = pygame.draw.rect(win, (100,100,100), (480,305,40,40))

    seventh = pygame.draw.rect(win, (255,255,255), (25,375,150,150))

    seventh_first = pygame.draw.rect(win, (100,100,100), (30,380,40,40))
    seventh_second = pygame.draw.rect(win, (100,100,100), (80,380,40,40))
    seventh_third = pygame.draw.rect(win, (100,100,100), (130,380,40,40))

    seventh_fourth = pygame.draw.rect(win, (100,100,100), (30,430,40,40))
    seventh_fifth = pygame.draw.rect(win, (100,100,100), (80,430,40,40))
    seventh_sixth = pygame.draw.rect(win, (100,100,100), (130,430,40,40))

    seventh_seventh = pygame.draw.rect(win, (100,100,100), (30,480,40,40))
    seventh_eighth = pygame.draw.rect(win, (100,100,100), (80,480,40,40))
    seventh_ninth = pygame.draw.rect(win, (100,100,100), (130,480,40,40))

    eighth = pygame.draw.rect(win, (255,255,255), (200,375,150,150))

    eighth_first = pygame.draw.rect(win, (100,100,100), (205,380,40,40))
    eighth_second = pygame.draw.rect(win, (100,100,100), (255,380,40,40))
    eighth_third = pygame.draw.rect(win, (100,100,100), (305,380,40,40))

    eighth_fourth = pygame.draw.rect(win, (100,100,100), (205,430,40,40))
    eighth_fifth = pygame.draw.rect(win, (100,100,100), (255,430,40,40))
    eighth_sixth = pygame.draw.rect(win, (100,100,100), (305,430,40,40))

    eighth_seventh = pygame.draw.rect(win, (100,100,100), (205,480,40,40))
    eighth_eighth = pygame.draw.rect(win, (100,100,100), (255,480,40,40))
    eighth_ninth = pygame.draw.rect(win, (100,100,100), (305,480,40,40))

    ninth = pygame.draw.rect(win, (255,255,255), (375,375,150,150))

    ninth_first = pygame.draw.rect(win, (100,100,100), (380,380,40,40))
    ninth_second = pygame.draw.rect(win, (100,100,100), (430,380,40,40))
    ninth_third = pygame.draw.rect(win, (100,100,100), (480,380,40,40))

    ninth_fourth = pygame.draw.rect(win, (100,100,100), (380,430,40,40))
    ninth_fifth = pygame.draw.rect(win, (100,100,100), (430,430,40,40))
    ninth_sixth = pygame.draw.rect(win, (100,100,100), (480,430,40,40))

    ninth_seventh = pygame.draw.rect(win, (100,100,100), (380,480,40,40))
    ninth_eighth = pygame.draw.rect(win, (100,100,100), (430,480,40,40))
    ninth_ninth = pygame.draw.rect(win, (100,100,100), (480,480,40,40))

#Sets first player's shape
draw_object = 'circle'

#Used to see if space is taken
#test
first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True
    #1
first_first_open = True
first_second_open = True
first_third_open = True
first_fourth_open = True
first_fifth_open = True
first_sixth_open = True
first_seventh_open = True
first_eighth_open = True
first_ninth_open = True
    #2
second_first_open = True
second_second_open = True
second_third_open = True
second_fourth_open = True
second_fifth_open = True
second_sixth_open = True
second_seventh_open = True
second_eighth_open = True
second_ninth_open = True
    #3
third_first_open = True
third_second_open = True
third_third_open = True
third_fourth_open = True
third_fifth_open = True
third_sixth_open = True
third_seventh_open = True
third_eighth_open = True
third_ninth_open = True
    #4
fourth_first_open = True
fourth_second_open = True
fourth_third_open = True
fourth_fourth_open = True
fourth_fifth_open = True
fourth_sixth_open = True
fourth_seventh_open = True
fourth_eighth_open = True
fourth_ninth_open = True
 #5
fifth_first_open = True
fifth_second_open = True
fifth_third_open = True
fifth_fourth_open = True
fifth_fifth_open = True
fifth_sixth_open = True
fifth_seventh_open = True
fifth_eighth_open = True
fifth_ninth_open = True
    #6
sixth_first_open = True
sixth_second_open = True
sixth_third_open = True
sixth_fourth_open = True
sixth_fifth_open = True
sixth_sixth_open = True
sixth_seventh_open = True
sixth_eighth_open = True
sixth_ninth_open = True
    #7
seventh_first_open = True
seventh_second_open = True
seventh_third_open = True
seventh_fourth_open = True
seventh_fifth_open = True
seventh_sixth_open = True
seventh_seventh_open = True
seventh_eighth_open = True
seventh_ninth_open = True
    #8
eighth_first_open = True
eighth_second_open = True
eighth_third_open = True
eighth_fourth_open = True
eighth_fifth_open = True
eighth_sixth_open = True
eighth_seventh_open = True
eighth_eighth_open = True
eighth_ninth_open = True
    #9
ninth_first_open = True
ninth_second_open = True
ninth_third_open = True
ninth_fourth_open = True
ninth_fifth_open = True
ninth_sixth_open = True
ninth_seventh_open = True
ninth_eighth_open = True
ninth_ninth_open = True

red = (235, 3, 0) 
green = (0, 255, 0) 
black = (0, 0, 0)  
white = (255, 250, 250)
  
font = pygame.font.Font('freesansbold.ttf', 32) 
  
text1 = font.render("    Red's Round         ", True, red, black) 

text2 = font.render("    Green's Round         ", True, green, black)

text3 = font.render("    Red won               ", True, red, black)

text4 = font.render("    Green won                  ", True, green, black)

text5 = font.render(" Restart ", True, green, white)

textRect = text1.get_rect()  

textRect1 = text5.get_rect()

textRect1.center = (1350 // 2, 1000 // 2)

# set the center of the rectangular object. 
textRect.center = (1400 // 2, 100 // 2) 

#board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


#board1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def win_check1(num):
    for row in board1:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            first_open = False
            return True

    for column in range(3):
        for row in board1:
            if row[column] == num:
                continue
            else:
                break
        else:
            first_open = False
            return True
    

    for tile in range(3):
        if board1[tile][tile] == num:
            continue
        else:
            break
    else:
        first_open = False
        return True
    
    
    for tile in range(3):
        if board1[tile][2-tile] == num:
            continue
        else:
            break
    else:
        first_open = False
        return True

#board2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def win_check2(num):
    for row in board2:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            second_open = False
            return True

    for column in range(3):
        for row in board2:
            if row[column] == num:
                continue
            else:
                break
        else:
            second_open = False
            return True
    

    for tile in range(3):
        if board2[tile][tile] == num:
            continue
        else:
            break
    else:
        second_open = False
        return True
    
    
    for tile in range(3):
        if board2[tile][2-tile] == num:
            continue
        else:
            break
    else:
        second_open = False
        return True


#board3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def win_check3(num):
    for row in board3:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            third_open = False
            return True

    for column in range(3):
        for row in board3:
            if row[column] == num:
                continue
            else:
                break
        else:
            third_open = False
            return True
    

    for tile in range(3):
        if board3[tile][tile] == num:
            continue
        else:
            break
    else:
        third_open = False
        return True
    
    
    for tile in range(3):
        if board3[tile][2-tile] == num:
            continue
        else:
            break
    else:
        third_open = False
        return True

#board4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def win_check4(num):
    for row in board4:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            fourth_open = False
            return True

    for column in range(3):
        for row in board4:
            if row[column] == num:
                continue
            else:
                break
        else:
            fourth_open = False
            return True
    

    for tile in range(3):
        if board4[tile][tile] == num:
            continue
        else:
            break
    else:
        fourth_open = False
        return True
    
    
    for tile in range(3):
        if board4[tile][2-tile] == num:
            continue
        else:
            break
    else:
        fourth_open = False
        return True

#board5 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def win_check5(num):
    for row in board5:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            fifth_open = False
            return True

    for column in range(3):
        for row in board5:
            if row[column] == num:
                continue
            else:
                break
        else:
            fifth_open = False
            return True
    

    for tile in range(3):
        if board5[tile][tile] == num:
            continue
        else:
            break
    else:
        fifth_open = False
        return True
    
    
    for tile in range(3):
        if board5[tile][2-tile] == num:
            continue
        else:
            break
    else:
        fifth_open = False
        return True

#board6 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def win_check6(num):
    for row in board6:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            sixth_open = False
            return True

    for column in range(3):
        for row in board6:
            if row[column] == num:
                continue
            else:
                break
        else:
            sixth_open = False
            return True
    

    for tile in range(3):
        if board6[tile][tile] == num:
            continue
        else:
            break
    else:
        sixth_open = False
        return True
    
    
    for tile in range(3):
        if board6[tile][2-tile] == num:
            continue
        else:
            break
    else:
        sixth_open = False
        return True

#board7 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def win_check7(num):
    for row in board7:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            seventh_open = False
            return True

    for column in range(3):
        for row in board7:
            if row[column] == num:
                continue
            else:
                break
        else:
            seventh_open = False
            return True
    

    for tile in range(3):
        if board7[tile][tile] == num:
            continue
        else:
            break
    else:
        seventh_open = False
        return True
    
    
    for tile in range(3):
        if board7[tile][2-tile] == num:
            continue
        else:
            break
    else:
        seventh_open = False
        return True

#board8 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def win_check8(num):
    for row in board8:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            eighth_open = False
            return True

    for column in range(3):
        for row in board8:
            if row[column] == num:
                continue
            else:
                break
        else:
            eighth_open = False
            return True
    

    for tile in range(3):
        if board8[tile][tile] == num:
            continue
        else:
            break
    else:
        eighth_open = False
        return True
    
    
    for tile in range(3):
        if board8[tile][2-tile] == num:
            continue
        else:
            break
    else:
        eighth_open = False
        return True

#board9 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def win_check9(num):
    for row in board9:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            ninth_open = False
            return True
            

    for column in range(3):
        for row in board9:
            if row[column] == num:
                continue
            else:
                break
        else:
            ninth_open = False
            return True
    

    for tile in range(3):
        if board9[tile][tile] == num:
            continue
        else:
            break
    else:
        ninth_open = False
        return True

    
    
    for tile in range(3):
        if board9[tile][2-tile] == num:
            continue
        else:
            break
    else:
        ninth_open = False
        return True
        
def ultimateWin(num):
    for row in ultimateBoard:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            first_open = False
            return True

    for column in range(3):
        for row in ultimateBoard:
            if row[column] == num:
                continue
            else:
                break
        else:
            first_open = False
            return True
    

    for tile in range(3):
        if ultimateBoard[tile][tile] == num:
            continue
        else:
            break
    else:
        first_open = False
        return True
    
    
    for tile in range(3):
        if ultimateBoard[tile][2-tile] == num:
            continue
        else:
            break
    else:
        first_open = False
        return True

#Main Loop
run = True

ultmateWon = False

won1 = False
won2 = False
won3 = False
won4 = False
won5 = False
won6 = False
won7 = False
won8 = False
won9 = False


    


while run:

    
    # copying the text surface object 
    # to the display surface object  


    #Pygame Events
    for event in pygame.event.get():

        if draw_object == 'circle':
            win.blit(text1, textRect) 
        if draw_object == 'rect':
            win.blit(text2, textRect) 

        #Quit Event
        if event.type == pygame.QUIT:
            run = False

        pos = pygame.mouse.get_pos()

        #Space bar to reset
        win.blit(text5, textRect1) 
        if event.type == pygame.MOUSEBUTTONUP and (not ultmateWon):
            if textRect1.collidepoint(pos):

                if ultmateWon:
                    pygame.draw.rect(win, (255,250,250), (0,0,550,550))
                draw()
                first_open = True
                second_open = True
                third_open = True
                fourth_open = True
                fifth_open = True
                sixth_open = True
                seventh_open = True
                eighth_open = True
                ninth_open = True
                    #1
                first_first_open = True
                first_second_open = True
                first_third_open = True
                first_fourth_open = True
                first_fifth_open = True
                first_sixth_open = True
                first_seventh_open = True
                first_eighth_open = True
                first_ninth_open = True
                    #2
                second_first_open = True
                second_second_open = True
                second_third_open = True
                second_fourth_open = True
                second_fifth_open = True
                second_sixth_open = True
                second_seventh_open = True
                second_eighth_open = True
                second_ninth_open = True
                    #3
                third_first_open = True
                third_second_open = True
                third_third_open = True
                third_fourth_open = True
                third_fifth_open = True
                third_sixth_open = True
                third_seventh_open = True
                third_eighth_open = True
                third_ninth_open = True
                    #4
                fourth_first_open = True
                fourth_second_open = True
                fourth_third_open = True
                fourth_fourth_open = True
                fourth_fifth_open = True
                fourth_sixth_open = True
                fourth_seventh_open = True
                fourth_eighth_open = True
                fourth_ninth_open = True
                #5
                fifth_first_open = True
                fifth_second_open = True
                fifth_third_open = True
                fifth_fourth_open = True
                fifth_fifth_open = True
                fifth_sixth_open = True
                fifth_seventh_open = True
                fifth_eighth_open = True
                fifth_ninth_open = True
                    #6
                sixth_first_open = True
                sixth_second_open = True
                sixth_third_open = True
                sixth_fourth_open = True
                sixth_fifth_open = True
                sixth_sixth_open = True
                sixth_seventh_open = True
                sixth_eighth_open = True
                sixth_ninth_open = True
                    #7
                seventh_first_open = True
                seventh_second_open = True
                seventh_third_open = True
                seventh_fourth_open = True
                seventh_fifth_open = True
                seventh_sixth_open = True
                seventh_seventh_open = True
                seventh_eighth_open = True
                seventh_ninth_open = True
                    #8
                eighth_first_open = True
                eighth_second_open = True
                eighth_third_open = True
                eighth_fourth_open = True
                eighth_fifth_open = True
                eighth_sixth_open = True
                eighth_seventh_open = True
                eighth_eighth_open = True
                eighth_ninth_open = True
                    #9
                ninth_first_open = True
                ninth_second_open = True
                ninth_third_open = True
                ninth_fourth_open = True
                ninth_fifth_open = True
                ninth_sixth_open = True
                ninth_seventh_open = True
                ninth_eighth_open = True
                ninth_ninth_open = True

                won1 = False
                won2 = False
                won3 = False
                won4 = False
                won5 = False
                won6 = False
                won7 = False
                won8 = False
                won9 = False
                ultmateWon = False

                ultimateBoard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                board1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                board2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                board3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                board4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                board5 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                board6 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                board7 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                board8 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                board9 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


        #Used to see which space is clicked
        if event.type == pygame.MOUSEBUTTONUP and (not ultmateWon):
            pos = pygame.mouse.get_pos()
            print(pos)
            #Checks if mouse position is in a space and if space is available
            if first_first.collidepoint(pos) and (first_open and first_first_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (50,50),19)
                    draw_object = 'rect'
                    board1[0][0] = 1
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True

                else:
                    pygame.draw.circle(win,(0,255,0), (50,50),19)
                    draw_object = 'circle'
                    board1[0][0] = 2
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                first_first_open = False
                    
            if first_second.collidepoint(pos) and (first_open and first_second_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (100,50),19)
                    draw_object = 'rect'
                    board1[0][1] = 1
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (100,50),19)
                    draw_object = 'circle'
                    board1[0][1] = 2
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                first_second_open = False
                    
            if first_third.collidepoint(pos) and (first_open and first_third_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (150,50),19)
                    draw_object = 'rect'
                    board1[0][2] = 1
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (150,50),19)
                    draw_object = 'circle'
                    board1[0][2] = 2
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                first_third_open = False
                    
            if first_fourth.collidepoint(pos) and (first_open and first_fourth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (50,100),19)
                    draw_object = 'rect'
                    board1[1][0] = 1
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (50,100),19)
                    draw_object = 'circle'
                    board[1][0] = 2
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                first_fourth_open = False
                    
            if first_fifth.collidepoint(pos) and (first_open and first_fifth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (100,100),19)
                    draw_object = 'rect'
                    board1[1][1] = 1
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (100,100),19)
                    draw_object = 'circle'
                    board1[1][1] = 2
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                first_fifth_open = False
                    
            if first_sixth.collidepoint(pos) and (first_open and first_sixth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (150,100),19)
                    draw_object = 'rect'
                    board1[1][2] = 1
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (150,100),19)
                    draw_object = 'circle'
                    board1[1][2] = 2
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                first_sixth_open = False
                    
            if first_seventh.collidepoint(pos) and (first_seventh_open and first_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (50,150),19)
                    draw_object = 'rect'
                    board1[2][0] = 1
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (50,150),19)
                    draw_object = 'circle'
                    board1[2][0] = 2
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                first_seventh_open = False
                    
            if first_eighth.collidepoint(pos) and (first_open and first_eighth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (100,150),19)
                    draw_object = 'rect'
                    board1[2][1] = 1
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (100,150),19)
                    draw_object = 'circle'
                    board1[2][1] = 2
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                first_eighth_open = False
                    
            if first_ninth.collidepoint(pos) and (first_open and first_ninth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (150,150),19)
                    draw_object = 'rect'
                    board1[2][2] = 1
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
        
                else:
                    pygame.draw.circle(win,(0,255,0), (150,150),19)
                    draw_object = 'circle'
                    board1[2][2] = 2
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                first_ninth_open = False

            if second_first.collidepoint(pos) and (second_open and second_first_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (225,50),19)
                    draw_object = 'rect'
                    board2[0][0] = 1
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (225,50),19)
                    draw_object = 'circle'
                    board2[0][0] = 2
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                second_first_open = False

            if second_second.collidepoint(pos) and (second_open and second_second_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (275,50),19)
                    draw_object = 'rect'
                    board2[0][1] = 1
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (275,50),19)
                    draw_object = 'circle'
                    board2[0][1] = 2
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                second_second_open = False
                    
            if second_third.collidepoint(pos) and (second_open and second_third_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (325,50),19)
                    draw_object = 'rect'
                    board2[0][2] = 1
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (325,50),19)
                    draw_object = 'circle'
                    board2[0][2] = 2
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                second_third_open = False
                    
            if second_fourth.collidepoint(pos) and (second_open and second_fourth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (225,100),19)
                    draw_object = 'rect'
                    board2[1][0] = 1
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (225,100),19)
                    draw_object = 'circle'
                    board2[1][0] = 2
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                second_fourth_open = False
                    
            if second_fifth.collidepoint(pos) and (second_open and second_fifth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (275,100),19)
                    draw_object = 'rect'
                    board2[1][1] = 1
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (275,100),19)
                    draw_object = 'circle'
                    board2[1][1] = 2
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                second_fifth_open = False
                    
            if second_sixth.collidepoint(pos) and (second_open and second_sixth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (325,100),19)
                    draw_object = 'rect'
                    board2[1][2] = 1
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (325,100),19)
                    draw_object = 'circle'
                    board2[1][2] = 2
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                second_sixth_open = False
                    
            if second_seventh.collidepoint(pos) and (second_seventh_open and second_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (225,150),19)
                    draw_object = 'rect'
                    board2[2][0] = 1
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (225,150),19)
                    draw_object = 'circle'
                    board2[2][0] = 2
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                second_seventh_open = False
                    
            if second_eighth.collidepoint(pos) and (second_open and second_eighth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (275,150),19)
                    draw_object = 'rect'
                    board2[2][1] = 1
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (275,150),19)
                    draw_object = 'circle'
                    board2[2][1] = 2
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                second_eighth_open = False
                    
            if second_ninth.collidepoint(pos) and (second_open and second_ninth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (325,150),19)
                    draw_object = 'rect'
                    board2[2][2] = 1
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (325,150),19)
                    draw_object = 'circle'
                    board2[2][2] = 2
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                second_ninth_open = False
            
            if third_first.collidepoint(pos) and (third_open and third_first_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (400,50),19)
                    draw_object = 'rect'
                    board3[0][0] = 1
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (400,50),19)
                    draw_object = 'circle'
                    board3[0][0] = 2
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                third_first_open = False
                    
            if third_second.collidepoint(pos) and (third_open and third_second_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (450,50),19)
                    draw_object = 'rect'
                    board3[0][1] = 1
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (450,50),19)
                    draw_object = 'circle'
                    board3[0][1] = 2
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                third_second_open = False
                    
            if third_third.collidepoint(pos) and (third_open and third_third_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (500,50),19)
                    draw_object = 'rect'
                    board3[0][2] = 1
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (500,50),19)
                    draw_object = 'circle'
                    board3[0][2] = 2
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                third_third_open = False
                    
            if third_fourth.collidepoint(pos) and (third_open and third_fourth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (400,100),19)
                    draw_object = 'rect'
                    board3[1][0] = 1
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (400,100),19)
                    draw_object = 'circle'
                    board3[1][0] = 2
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                third_fourth_open = False
                    
            if third_fifth.collidepoint(pos) and (third_open and third_fifth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (450,100),19)
                    draw_object = 'rect'
                    board3[1][1] = 1
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                    
                else:
                    pygame.draw.circle(win,(0,255,0), (450,100),19)
                    draw_object = 'circle'
                    board3[1][1] = 2
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                third_fifth_open = False
                    
            if third_sixth.collidepoint(pos) and (third_open and third_sixth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (500,100),19)
                    draw_object = 'rect'
                    board3[1][2] = 1
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (500,100),19)
                    draw_object = 'circle'
                    board3[1][2] = 2
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                third_sixth_open = False
                    
            if third_seventh.collidepoint(pos) and (third_seventh_open and third_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (400,150),19)
                    draw_object = 'rect'
                    board3[2][0] = 1
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (400,150),19)
                    draw_object = 'circle'
                    board3[2][0] = 2
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                third_seventh_open = False
                    
            if third_eighth.collidepoint(pos) and (third_open and third_eighth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (450,150),19)
                    draw_object = 'rect'
                    board3[2][1] = 1
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (450,150),19)
                    draw_object = 'circle'
                    board3[2][1] = 2
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                third_eighth_open = False
                    
            if third_ninth.collidepoint(pos) and (third_open and third_ninth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (500,150),19)
                    draw_object = 'rect'
                    board3[2][2] = 1
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (500,150),19)
                    draw_object = 'circle'
                    board3[2][2] = 2
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                third_ninth_open = False

            if fourth_first.collidepoint(pos) and (fourth_open and fourth_first_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (50,225),19)
                    draw_object = 'rect'
                    board4[0][0] = 1
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (50,225),19)
                    draw_object = 'circle'
                    board4[0][0] = 2
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                fourth_first_open = False
                    
            if fourth_second.collidepoint(pos) and (fourth_open and fourth_second_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (100,225),19)
                    draw_object = 'rect'
                    board4[0][1] = 1
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (100,225),19)
                    draw_object = 'circle'
                    board4[0][1] = 2
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                fourth_second_open = False
                    
            if fourth_third.collidepoint(pos) and (fourth_open and fourth_third_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (150,225),19)
                    draw_object = 'rect'
                    board4[0][2] = 1
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (150,225),19)
                    draw_object = 'circle'
                    board4[0][2] = 2
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fourth_third_open = False
                    
            if fourth_fourth.collidepoint(pos) and (fourth_open and fourth_fourth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (50,275),19)
                    draw_object = 'rect'
                    board4[1][0] = 1
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (50,275),19)
                    draw_object = 'circle'
                    board4[1][0] = 2
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fourth_fourth_open = False
                    
            if fourth_fifth.collidepoint(pos) and (fourth_open and fourth_fifth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (100,275),19)
                    draw_object = 'rect'
                    board4[1][1] = 1
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (100,275),19)
                    draw_object = 'circle'
                    board4[1][1] = 2
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fourth_fifth_open = False
                    
            if fourth_sixth.collidepoint(pos) and (fourth_open and fourth_sixth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (150,275),19)
                    draw_object = 'rect'
                    board4[1][2] = 1
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (150,275),19)
                    draw_object = 'circle'
                    board4[1][2] = 2
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fourth_sixth_open = False
                    
            if fourth_seventh.collidepoint(pos) and (fourth_seventh_open and fourth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (50,325),19)
                    draw_object = 'rect'
                    board4[2][0] = 1
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (50,325),19)
                    draw_object = 'circle'
                    board4[2][0] = 2
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fourth_seventh_open = False
                    
            if fourth_eighth.collidepoint(pos) and (fourth_open and fourth_eighth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (100,325),19)
                    draw_object = 'rect'
                    board4[2][1] = 1
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (100,325),19)
                    draw_object = 'circle'
                    board4[2][1] = 2
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fourth_eighth_open = False
                    
            if fourth_ninth.collidepoint(pos) and (fourth_open and fourth_ninth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (150,325),19)
                    draw_object = 'rect'
                    board4[2][2] = 1
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (150,325),19)
                    draw_object = 'circle'
                    board4[2][2] = 2
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fourth_ninth_open = False

            if fifth_first.collidepoint(pos) and (fifth_open and fifth_first_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (225,225),19)
                    draw_object = 'rect'
                    board5[0][0] = 1
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (225,225),19)
                    draw_object = 'circle'
                    board5[0][0] = 2
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                fifth_first_open = False
                    
            if fifth_second.collidepoint(pos) and (fifth_open and fifth_second_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (275,225),19)
                    draw_object = 'rect'
                    board5[0][1] = 1
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True

                else:
                    pygame.draw.circle(win,(0,255,0), (275,225),19)
                    draw_object = 'circle'
                    board5[0][1] = 2
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                fifth_second_open = False
                    
            if fifth_third.collidepoint(pos) and (fifth_open and fifth_third_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (325,225),19)
                    draw_object = 'rect'
                    board5[0][2] = 1
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (325,225),19)
                    draw_object = 'circle'
                    board5[0][2] = 2
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fifth_third_open = False
                    
            if fifth_fourth.collidepoint(pos) and (fifth_open and fifth_fourth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (225,275),19)
                    draw_object = 'rect'
                    board5[1][0] = 1
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (225,275),19)
                    draw_object = 'circle'
                    board5[1][0] = 2
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fifth_fourth_open = False
                    
            if fifth_fifth.collidepoint(pos) and (fifth_open and fifth_fifth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (275,275),19)
                    draw_object = 'rect'
                    board5[1][1] = 1
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (275,275),19)
                    draw_object = 'circle'
                    board5[1][1] = 2
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fifth_fifth_open = False
                    
            if fifth_sixth.collidepoint(pos) and (fifth_open and fifth_sixth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (325,275),19)
                    draw_object = 'rect'
                    board5[1][2] = 1
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (325,275),19)
                    draw_object = 'circle'
                    board5[1][2] = 2
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fifth_sixth_open = False
                    
            if fifth_seventh.collidepoint(pos) and (fifth_seventh_open and fifth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (225,325),19)
                    draw_object = 'rect'
                    board5[2][0] = 1
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (225,325),19)
                    draw_object = 'circle'
                    board5[2][0] = 2
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fifth_seventh_open = False
                    
            if fifth_eighth.collidepoint(pos) and (fifth_open and fifth_eighth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (275,325),19)
                    draw_object = 'rect'
                    board5[2][1] = 1
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (275,325),19)
                    draw_object = 'circle'
                    board5[2][1] = 2
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fifth_eighth_open = False
                    
            if fifth_ninth.collidepoint(pos) and (fifth_open and fifth_ninth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (325,325),19)
                    draw_object = 'rect'
                    board5[2][2] = 1
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (325,325),19)
                    draw_object = 'circle'
                    board5[2][2] = 2
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                fifth_ninth_open = False

            if sixth_first.collidepoint(pos) and (sixth_open and sixth_first_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (400,225),19)
                    draw_object = 'rect'
                    board6[0][0] = 1
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (400,225),19)
                    draw_object = 'circle'
                    board6[0][0] = 2
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                sixth_first_open = False
                    
            if sixth_second.collidepoint(pos) and (sixth_open and sixth_second_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (450,225),19)
                    draw_object = 'rect'
                    board6[0][1] = 1
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (450,225),19)
                    draw_object = 'circle'
                    board6[0][1] = 2
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                sixth_second_open = False
                    
            if sixth_third.collidepoint(pos) and (sixth_open and sixth_third_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (500,225),19)
                    draw_object = 'rect'
                    board6[0][2] = 1
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (500,225),19)
                    draw_object = 'circle'
                    board6[0][2] = 2
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                sixth_third_open = False
                    
            if sixth_fourth.collidepoint(pos) and (sixth_open and sixth_fourth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (400,275),19)
                    draw_object = 'rect'
                    board6[1][0] = 1
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (400,275),19)
                    draw_object = 'circle'
                    board6[1][0] = 2
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                sixth_fourth_open = False
                    
            if sixth_fifth.collidepoint(pos) and (sixth_open and sixth_fifth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (450,275),19)
                    draw_object = 'rect'
                    board6[1][1] = 1
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (450,275),19)
                    draw_object = 'circle'
                    board6[1][1] = 2
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                sixth_fifth_open = False
                    
            if sixth_sixth.collidepoint(pos) and (sixth_open and sixth_sixth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (500,275),19)
                    draw_object = 'rect'
                    board6[1][2] = 1
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (500,275),19)
                    draw_object = 'circle'
                    board6[1][2] = 2
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                sixth_sixth_open = False
                    
            if sixth_seventh.collidepoint(pos) and (sixth_seventh_open and sixth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (400,325),19)
                    draw_object = 'rect'
                    board6[2][0] = 1
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (400,325),19)
                    draw_object = 'circle'
                    board6[2][0] = 2
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                sixth_seventh_open = False
                    
            if sixth_eighth.collidepoint(pos) and (sixth_open and sixth_eighth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (450,325),19)
                    draw_object = 'rect'
                    board6[2][1] = 1
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (450,325),19)
                    draw_object = 'circle'
                    board6[2][1] = 2
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                sixth_eighth_open = False
                    
            if sixth_ninth.collidepoint(pos) and (sixth_open and sixth_ninth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (500,325),19)
                    draw_object = 'rect'
                    board6[2][2] = 1
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (500,325),19)
                    draw_object = 'circle'
                    board6[2][2] = 2
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                sixth_ninth_open = False

            if seventh_first.collidepoint(pos) and (seventh_open and seventh_first_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (50,400),19)
                    draw_object = 'rect'
                    board7[0][0] = 1
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (50,400),19)
                    draw_object = 'circle'
                    board7[0][0] = 2
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                seventh_first_open = False
                    
            if seventh_second.collidepoint(pos) and (seventh_open and seventh_second_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (100,400),19)
                    draw_object = 'rect'
                    board7[0][1] = 1
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (100,400),19)
                    draw_object = 'circle'
                    board7[0][1] = 2
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                seventh_second_open = False
                    
            if seventh_third.collidepoint(pos) and (seventh_open and seventh_third_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (150,400),19)
                    draw_object = 'rect'
                    board7[0][2] = 1
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (150,400),19)
                    draw_object = 'circle'
                    board7[0][2] = 2
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                seventh_third_open = False
                    
            if seventh_fourth.collidepoint(pos) and (seventh_open and seventh_fourth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (50,450),19)
                    draw_object = 'rect'
                    board7[1][0] = 1
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (50,450),19)
                    draw_object = 'circle'
                    board7[1][0] = 2
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                seventh_fourth_open = False
                    
            if seventh_fifth.collidepoint(pos) and (seventh_open and seventh_fifth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (100,450),19)
                    draw_object = 'rect'
                    board7[1][1] = 1
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (100,450),19)
                    draw_object = 'circle'
                    board7[1][1] = 2
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                seventh_fifth_open = False
                    
            if seventh_sixth.collidepoint(pos) and (seventh_open and seventh_sixth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (150,450),19)
                    draw_object = 'rect'
                    board7[1][2] = 1
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (150,450),19)
                    draw_object = 'circle'
                    board7[1][2] = 2
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                seventh_sixth_open = False
                    
            if seventh_seventh.collidepoint(pos) and (seventh_seventh_open and seventh_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (50,500),19)
                    draw_object = 'rect'
                    board7[2][0] = 1
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (50,500),19)
                    draw_object = 'circle'
                    board7[2][0] = 2
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                seventh_seventh_open = False
                    
            if seventh_eighth.collidepoint(pos) and (seventh_open and seventh_eighth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (100,500),19)
                    draw_object = 'rect'
                    board7[2][1] = 1
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (100,500),19)
                    draw_object = 'circle'
                    board7[2][1] = 2
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                seventh_eighth_open = False
                
                    
            if seventh_ninth.collidepoint(pos) and (seventh_open and seventh_ninth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (150,500),19)
                    draw_object = 'rect'
                    board7[2][2] = 1
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (150,500),19)
                    draw_object = 'circle'
                    board7[2][2] = 2
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                seventh_ninth_open = False

            if eighth_first.collidepoint(pos) and (eighth_open and eighth_first_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (225,400),19)
                    draw_object = 'rect'
                    board8[0][0] = 1
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (225,400),19)
                    draw_object = 'circle'
                    board8[0][0] = 2
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                eighth_first_open = False
                    
            if eighth_second.collidepoint(pos) and (eighth_open and eighth_second_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (275,400),19)
                    draw_object = 'rect'
                    board8[0][1] = 1
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (275,400),19)
                    draw_object = 'circle'
                    board8[0][1] = 2
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                eighth_second_open = False
                    
            if eighth_third.collidepoint(pos) and (eighth_open and eighth_third_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (325,400),19)
                    draw_object = 'rect'
                    board8[0][2] = 1
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (325,400),19)
                    draw_object = 'circle'
                    board8[0][2] = 2
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                eighth_third_open = False
                    
            if eighth_fourth.collidepoint(pos) and (eighth_open and eighth_fourth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (225,450),19)
                    draw_object = 'rect'
                    board8[1][0] = 1
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (225,450),19)
                    draw_object = 'circle'
                    board8[1][0] = 2
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                eighth_fourth_open = False
                    
            if eighth_fifth.collidepoint(pos) and (eighth_open and eighth_fifth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (275,450),19)
                    draw_object = 'rect'
                    board8[1][1] = 1
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (275,450),19)
                    draw_object = 'circle'
                    board8[1][1] = 2
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                eighth_fifth_open = False
                    
            if eighth_sixth.collidepoint(pos) and (eighth_open and eighth_sixth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (325,450),19)
                    draw_object = 'rect'
                    board8[1][2] = 1
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (325,450),19)
                    draw_object = 'circle'
                    board8[1][2] = 2
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                eighth_sixth_open = False
                    
            if eighth_seventh.collidepoint(pos) and (eighth_seventh_open and eighth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (225,500),19)
                    draw_object = 'rect'
                    board8[2][0] = 1
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (225,500),19)
                    draw_object = 'circle'
                    board8[2][0] = 2
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                eighth_seventh_open = False
                    
            if eighth_eighth.collidepoint(pos) and (eighth_open and eighth_eighth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (275,500),19)
                    draw_object = 'rect'
                    board8[2][1] = 1
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (275,500),19)
                    draw_object = 'circle'
                    board8[2][1] = 2
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                eighth_eighth_open = False
                    
            if eighth_ninth.collidepoint(pos) and (eighth_open and eighth_ninth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (325,500),19)
                    draw_object = 'rect'
                    board8[2][2] = 1
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (325,500),19)
                    draw_object = 'circle'
                    board8[2][2] = 2
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                    
                eighth_ninth_open = False

            if ninth_first.collidepoint(pos) and (ninth_open and ninth_first_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (400,400),19)
                    draw_object = 'rect'
                    board9[0][0] = 1
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (400,400),19)
                    draw_object = 'circle'
                    board9[0][0] = 2
                    if not won1:
                        first_open = True
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won1:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                ninth_first_open = False
                    
            if ninth_second.collidepoint(pos) and (ninth_open and ninth_second_open):
                #Draws a shapes based on whose turn it is
                if draw_object == 'circle':
                    #pygame.draw.circle(surface, (color), (centerx, centery),radius)                   
                    pygame.draw.circle(win,(255,0,0), (450,400),19)
                    draw_object = 'rect'
                    board9[0][1] = 1
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (450,400),19)
                    draw_object = 'circle'
                    board9[0][1] = 2
                    if not won2:
                        first_open = False
                        second_open = True
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won2:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                #Marks this space as taken
                ninth_second_open = False
                    
            if ninth_third.collidepoint(pos) and (ninth_open and ninth_third_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (500,400),19)
                    draw_object = 'rect'
                    board9[0][2] = 1
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (500,400),19)
                    draw_object = 'circle'
                    board9[0][2] = 2
                    if not won3:
                        first_open = False
                        second_open = False
                        third_open = True
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won3:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                ninth_third_open = False
                    
            if ninth_fourth.collidepoint(pos) and (ninth_open and ninth_fourth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (400,450),19)
                    draw_object = 'rect'
                    board9[1][0] = 1
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (400,450),19)
                    draw_object = 'circle'
                    board9[1][0] = 2
                    if not won4:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = True
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won4:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                ninth_fourth_open = False
                    
            if ninth_fifth.collidepoint(pos) and (ninth_open and ninth_fifth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (450,450),19)
                    draw_object = 'rect'
                    board9[1][1] = 1
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (450,450),19)
                    draw_object = 'circle'
                    board9[1][1] = 2
                    if not won5:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = True
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won5:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                ninth_fifth_open = False
                    
            if ninth_sixth.collidepoint(pos) and (ninth_open and ninth_sixth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (500,450),19)
                    draw_object = 'rect'
                    board9[1][2] = 1
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (500,450),19)
                    draw_object = 'circle'
                    board9[1][2] = 2
                    if not won6:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = True
                        seventh_open = False
                        eighth_open = False
                        ninth_open = False
                    if won6:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                ninth_sixth_open = False
                    
            if ninth_seventh.collidepoint(pos) and (ninth_seventh_open and ninth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (400,500),19)
                    draw_object = 'rect'
                    board9[2][0] = 1
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (400,500),19)
                    draw_object = 'circle'
                    board9[2][0] = 2
                    if not won7:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = True
                        eighth_open = False
                        ninth_open = False
                    if won7:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                ninth_seventh_open = False
                    
            if ninth_eighth.collidepoint(pos) and (ninth_open and ninth_eighth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (450,500),19)
                    draw_object = 'rect'
                    board9[2][1] = 1
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (450,500),19)
                    draw_object = 'circle'
                    board9[2][1] = 2
                    if not won8:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = True
                        ninth_open = False
                    if won8:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                ninth_eighth_open = False
                    
            if ninth_ninth.collidepoint(pos) and (ninth_open and ninth_ninth_open):
                if draw_object == 'circle':
                    pygame.draw.circle(win,(255,0,0), (500,500),19)
                    draw_object = 'rect'
                    board9[2][2] = 1
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                else:
                    pygame.draw.circle(win,(0,255,0), (500,500),19)
                    draw_object = 'circle'
                    board9[2][2] = 2
                    if not won9:
                        first_open = False
                        second_open = False
                        third_open = False
                        fourth_open = False
                        fifth_open = False
                        sixth_open = False
                        seventh_open = False
                        eighth_open = False
                        ninth_open = True
                    if won9:
                        first_open = True
                        second_open = True
                        third_open = True
                        fourth_open = True
                        fifth_open = True
                        sixth_open = True
                        seventh_open = True
                        eighth_open = True
                        ninth_open = True
                ninth_ninth_open = False
                



  

    if win_check1(1) and (not won1):
        ultimateBoard[0][0] = 1
        won1 = True
        first_open = False
        pygame.draw.rect(win, red, (25,25,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True

    if win_check1(2) and (not won1):
        ultimateBoard[0][0] = 2
        first_open = False
        won1 = True
        pygame.draw.rect(win, green, (25,25,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True

    if win_check2(1) and (not won2):
        ultimateBoard[0][1] = 1
        won2 = True
        second_open = False
        pygame.draw.rect(win, red, (200,25,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True
    if win_check2(2) and (not won2):
        ultimateBoard[0][1] = 2
        second_open = False
        won2 = True
        pygame.draw.rect(win, green, (200,25,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True

    if win_check3(1) and (not won3):
        ultimateBoard[0][2] = 1
        won3 = True
        third_open = False
        pygame.draw.rect(win, red, (375,25,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True
    if win_check3(2)  and (not won3):
        ultimateBoard[0][2] = 2
        third_open = False
        won4 = True
        pygame.draw.rect(win, green, (375,25,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True

    if win_check4(1) and (not won4):
        ultimateBoard[1][0] = 1
        won4 = True
        fourth_open = False
        pygame.draw.rect(win, red, (25,200,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True
    if win_check4(2) and (not won4):
        ultimateBoard[1][0] = 2
        fourth_open = False
        won4 = True
        pygame.draw.rect(win, green, (25,200,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True
    
    if win_check5(1) and (not won5):
        ultimateBoard[1][1] = 1
        won5 = True
        fifth_open = False
        pygame.draw.rect(win, red, (200,200,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True
    if win_check5(2) and (not won5):
        ultimateBoard[1][1] = 2
        fifth_open = False
        won5 = True
        pygame.draw.rect(win, green, (200,200,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True
    
    if win_check6(1) and (not won6):
        ultimateBoard[1][2] = 1
        won6 = True
        sixth_open = False
        pygame.draw.rect(win, red, (375,200,150,150))
        if won6:
            first_open = True
            second_open = True
            third_open = True
            fourth_open = True
            fifth_open = True
            sixth_open = True
            seventh_open = True
            eighth_open = True
            ninth_open = True

    if win_check6(2) and (not won6):
        ultimateBoard[1][2] = 2
        sixth_open = False
        won6 = True
        pygame.draw.rect(win, green, (375,200,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True

    if win_check7(1) and (not won7):
        ultimateBoard[2][0] = 1
        won7 = True
        seventh_open = False
        pygame.draw.rect(win, red, (25,375,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True
    if win_check7(2) and (not won7):
        ultimateBoard[2][0] = 2
        seventh_open = False
        won7 = True
        pygame.draw.rect(win, green, (25,375,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True

    if win_check8(1) and (not won8):
        ultimateBoard[2][1] = 1
        won8 = True
        eighth_open = False
        pygame.draw.rect(win, red, (200,375,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True
    if win_check8(2) and (not won8):
        ultimateBoard[2][1] = 2
        eighth_open = False
        won8 = True
        pygame.draw.rect(win, green, (200,375,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True

    if win_check9(1) and (not won9):
        ultimateBoard[2][2] = 1
        ninth_open = False
        won9 = True
        pygame.draw.rect(win, green, (375,375,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True
    if win_check9(2) and (not won9):
        ultimateBoard[2][2] = 2
        ninth_open = False
        won9 = True
        pygame.draw.rect(win, green, (375,375,150,150))
        first_open = True
        second_open = True
        third_open = True
        fourth_open = True
        fifth_open = True
        sixth_open = True
        seventh_open = True
        eighth_open = True
        ninth_open = True
    
    if ultimateWin(1):
        ultmateWon = True
        win.blit(text3, textRect) 
        pygame.draw.rect(win, red, (0,0,550,550))
    if ultimateWin(2):
        ultmateWon = True
        win.blit(text4, textRect)
        pygame.draw.rect(win, green, (0,0,550,550))
    #Updates screen with new shapes



    if first_open:
        pygame.draw.rect(win, (255, 255, 0), (25,25,150,150), 3)  # width = 3
    else:
        pygame.draw.rect(win, (255, 250, 250), (25,25,150,150), 3)  # width = 3


    if second_open:
        pygame.draw.rect(win, (255, 255, 0), (200,25,150,150), 3)  # width = 3
    else:
        pygame.draw.rect(win, (255, 250, 250), (200,25,150,150), 3)  # width = 3


    if third_open:
        pygame.draw.rect(win, (255, 255, 0), (375,25,150,150), 3)  # width = 3
    else:
        pygame.draw.rect(win, (255, 250, 250), (375,25,150,150), 3)  # width = 3


    if fourth_open:
        pygame.draw.rect(win, (255, 255, 0), (25,200,150,150), 3)  # width = 3
    else:
        pygame.draw.rect(win, (255, 250, 250), (25,200,150,150), 3)  # width = 3


    if fifth_open:
        pygame.draw.rect(win, (255, 255, 0), (200,200,150,150), 3)  # width = 3
    else:
        pygame.draw.rect(win, (255, 250, 250), (200,200,150,150), 3)  # width = 3


    if sixth_open:
        pygame.draw.rect(win, (255, 255, 0), (375,200,150,150), 3)  # width = 3
    else:
        pygame.draw.rect(win, (255, 250, 250), (375,200,150,150), 3)  # width = 3


    if seventh_open:
        pygame.draw.rect(win, (255, 255, 0), (25,375,150,150), 3)  # width = 3
    else:
        pygame.draw.rect(win, (255, 250, 250), (25,375,150,150), 3)  # width = 3


    if eighth_open:
        pygame.draw.rect(win, (255, 255, 0), (200,375,150,150), 3)  # width = 3
    else:
        pygame.draw.rect(win, (255, 250, 250), (200,375,150,150), 3)  # width = 3


    if ninth_open:
        pygame.draw.rect(win, (255, 255, 0), (375,375,150,150), 3)  # width = 3
    else:
        pygame.draw.rect(win, (255, 250, 250), (375,375,150,150), 3)  # width = 3


    pygame.display.update()



#Closes game once loop is broken
pygame.quit()
