#imports
import pygame
import pygame_menu
import sys
import time
from random import randint

pygame.init()
#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (128,128,129)
RED = (255,0,0)

#Variables
WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Tic Tac Toe")
ico = pygame.image.load('ico.ico')
pygame.display.set_icon(ico)
FONT = pygame.font.SysFont(None, 45)
COMPUTER=False


def make_board():
    board=[[None,None,None],[None,None,None],[None,None,None]]
    return board

def draw_board(win,width):
    win.fill(WHITE)
    gap=width//3
    for i in range(gap,width,gap):
        pygame.draw.line(win,BLACK,(0,i),(width,i))
        pygame.draw.line(win,BLACK,(i,0),(i,width))
    pygame.display.update()

def get_pos(pos,gap):
    x, y = pos
    row=y//gap
    col=x//gap
    return row, col

def draw_o(win,gap,row,col):
    half_gap=gap//2
    pygame.draw.circle(win,BLACK,(half_gap+gap*col,half_gap+gap*row),half_gap//2,3)
    pygame.display.update()

def draw_x(win,gap,row,col):
    quarter_gap=gap//4
    pygame.draw.line(win,BLACK,(quarter_gap+gap*col,quarter_gap+gap*row),(3*quarter_gap+gap*col,3*quarter_gap+gap*row),3)
    pygame.draw.line(win,BLACK,(3*quarter_gap+gap*col,quarter_gap+gap*row),(quarter_gap+gap*col,3*quarter_gap+gap*row),3)
    pygame.display.update()

def update_board(board,col,row,turn):
    board[row][col]=turn
    return board

def check_row(board):
    for row in board:
        if all( map(lambda x: x == row[0], row)) and None not in row:
            return True
    return False

def check_col(board):
    check=False
    temp_col=[]
    i=0
    while i<3 and not check:
        for j in range(0,3):
            temp_col.append(board[j][i])
        i+=1
        check=all( map(lambda x: x == temp_col[0], temp_col)) and None not in temp_col
        temp_col=[]
    return check

def check_diag(board):
    check=False
    middle=board[1][1]
    temp_diag1=[board[0][0],board[1][1],board[2][2]]
    temp_diag2=[board[2][0],board[1][1],board[0][2]]
    check=all( map(lambda x: x == temp_diag1[0], temp_diag1)) and None not in temp_diag1
    if not check:
        check=all( map(lambda x: x == temp_diag2[0], temp_diag2)) and None not in temp_diag2
    return check

def check_draw(board):
    check1= not None in board[0]
    check2= not None in board[1]
    check3=not None in board[2]
    return check1 and check2 and check3

def show_winner(win,width,winner,font):
    quart=width//4
    pygame.draw.rect(win,GREY,((quart,quart),(2*quart,2*quart)))
    text = font.render(f'The winner is: {winner}!', True, BLACK, GREY)
    textRect = text.get_rect()
    textRect.center = (width // 2, width // 2)
    win.blit(text, textRect)
    pygame.display.update()

def show_draw(win,width,font):
    quart=width//4
    pygame.draw.rect(win,GREY,((quart,quart),(2*quart,2*quart)))
    text = font.render("It's draw!", True, BLACK, GREY)
    textRect = text.get_rect()
    textRect.center = (width // 2, width // 2)
    win.blit(text, textRect)
    pygame.display.update()

def get_free_spaces(board):
    free_spaces=[]
    i=0
    j=0
    for row in board:
        for col in row:
            if col==None:
                free_spaces.append([i,j])
            j+=1
        j=0
        i+=1
    return free_spaces

def random_move(free_spaces):
    random=randint(0,len(free_spaces))
    return free_spaces[random]


def main(win,width,font,computer):
    run=True
    ended=False
    gap=width//3
    draw_board(win,width)
    board=make_board()
    player1=True
    player2=False
    pygame.display.set_caption("Tic Tac Toe (turn: x)")
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:      
                run = False

            if pygame.mouse.get_pressed()[0] and not ended : # LEFT mouse event
                pos = pygame.mouse.get_pos()
                row, col = get_pos(pos, gap)
                if board[row][col]==None:
                    if player1:
                        pygame.display.set_caption("Tic Tac Toe (turn: o)")
                        draw_x(win,gap,row,col)
                        board=update_board(board,col,row,'x')

                    elif player2 and not computer:
                        pygame.display.set_caption("Tic Tac Toe (turn: x)")
                        draw_o(win,gap,row,col)
                        board=update_board(board,col,row,'o')
                        

                    if check_row(board) or check_col(board) or check_diag(board):
                        if player1:
                            #print('The winner is X')
                            show_winner(win,width,'X',font)
                            ended=True
                            pygame.display.set_caption("Tic Tac Toe (press 'R' to restart)")
                        elif player2:
                           #print('The winner is O')
                            show_winner(win,width,'O',font)
                            ended=True
                            pygame.display.set_caption("Tic Tac Toe (press 'R' to restart)")
                    elif check_draw(board):
                        #print("Draw")
                        show_draw(win,width,font)
                        ended=True
                        pygame.display.set_caption("Tic Tac Toe (press 'R' to restart)")
                    
                    player1, player2=player2,player1

                    #if computer and player2:
                    #    free_spaces=get_free_spaces(board)
                    #    move=random_move(free_spaces)
                    #    print(move[0],move[1])
                    #    draw_o(win,gap,move[0],move[1])
                    #    board=update_board(board,move[0],move[1],'o')
                    #    player1, player2=player2,player1

            #Keys events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:     #k key
                    main(win,width,font,computer)
                if event.key == pygame.K_q:     #q key
                    run=False
                #if event.key == pygame.K_c:     #c key
                #    computer=not computer


                        
    pygame.quit()


try:
    main(WIN,WIDTH,FONT,COMPUTER)
except Exception:
    pass