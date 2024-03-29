import pygame
import random
import time
pygame.init()

# Setting few properties
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("DICE GAME")
bg = pygame.image.load("resources/background1.jpg")
bg2 = pygame.image.load("resources/background2.jpg")
clock = pygame.time.Clock()
player_area = (110,230)
comp_area = (640,230)
score_list=[1,2,3,4,5,6]
bat_ball=["batting","balling"]
sound = pygame.mixer.Sound("resources/crowd.wav")

# Loading images
proposal = pygame.image.load("resources/slides/proposal.jpg")
great = pygame.image.load("resources/slides/great.jpg")
proposal2 = pygame.image.load("resources/slides/proposal2.jpg")
ooe = pygame.image.load("resources/slides/ooe.jpg")
bat_dots = pygame.image.load("resources/slides/bat_dots.jpg")
ball_dots = pygame.image.load("resources/slides/ball_dots.jpg")
ball_first = pygame.image.load("resources/slides/ball_first.jpg")
bat_first = pygame.image.load("resources/slides/bat_first.jpg")
bob = pygame.image.load("resources/slides/bob.jpg")
won_game = pygame.image.load("resources/slides/won_game.jpg")
lost_game = pygame.image.load("resources/slides/lost_game.jpg")
draw_game = pygame.image.load("resources/slides/draw_game.jpg")
won_toss = pygame.image.load("resources/slides/won_toss.jpg")
lost_toss = pygame.image.load("resources/slides/lost_toss.jpg")
now_balling = pygame.image.load("resources/slides/now_balling.jpg")
now_batting = pygame.image.load("resources/slides/now_batting.jpg")
out = pygame.image.load("resources/slides/out.jpg")


# Some useful outsider functions
# display an image for centain time in the screen.
def screen_timer(win,time,slide):
    i = 0
    while i < time+1:
        clock.tick(60)
        win.blit(slide, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        i += 1
        pygame.display.update()

# write a string and display it.
def write(win,string,size,pos):
    font = pygame.font.SysFont("comicsans",size)
    text = font.render(string, 1, (0,0,0))
    win.blit(text, pos)
    pygame.display.update()


# Creating player class
class Player:
    shot_1 = [pygame.image.load("resources/1_0.png")]
    shot_2 = [pygame.image.load("resources/2_0.png")]
    shot_3 = [pygame.image.load("resources/3_0.png")]
    shot_4 = [pygame.image.load("resources/4_0.png")]
    shot_5 = [pygame.image.load("resources/5_0.png")]
    shot_6 = [pygame.image.load("resources/6_0.png")]

    def __init__(self,area):
        self.area = area

    def one(self):
        shot = random.choice(Player.shot_1)
        return shot
    def two(self):
        shot = random.choice(Player.shot_2)
        return shot
    def three(self):
        shot = random.choice(Player.shot_3)
        return shot
    def four(self):
        shot = random.choice(Player.shot_4)
        return shot
    def five(self):
        shot = random.choice(Player.shot_5)
        return shot
    def six(self):
        shot = random.choice(Player.shot_6)
        return shot

# Creating few properties for main_loop
counter = 0 # GAME-CHANGER
player1 = Player(player_area)
comp = Player(comp_area)
player1.total=0
player1.dot_count=0
comp.dot_count=0
comp.total = 0
counter_7 = False # Proof that player bat
counter_9 = False # Proof that player ball
counter_4 = False # Ensure credits display 1 time

# main loop
while True:
    clock.tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    # counter 0 is for introduction
    if counter == 0:
        counter += 1

    # counter 1 is for proposal for play
    if counter == 1:
        win.blit(proposal, (0,0))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_y]:
            screen_timer(win,50,great)
            counter += 1
        elif keys[pygame.K_n]:
            counter = -1  
    
    # counter 2 is for toss setup
    if counter == 2:
        win.blit(ooe, (0,0))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_o]:
            player1.toss = "odd"
            counter += 1
        elif keys[pygame.K_e]:
            player1.toss = "even"
            counter += 1   
        
    # counter 3 is for player toss selection
    if counter == 3:
        win.blit(bg, (0,0))
        write(win,"TOSS",45,(360,20))
        pygame.display.update()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            player_num = 1
            player_pic = player1.one()
            counter += 1
        elif keys[pygame.K_2]:
            player_num = 2
            player_pic = player1.two()
            counter += 1
        elif keys[pygame.K_3]:
            player_num = 3
            player_pic = player1.three()
            counter += 1
        elif keys[pygame.K_4]:
            player_num = 4
            player_pic = player1.four()
            counter += 1
        elif keys[pygame.K_5]:
            player_num = 5
            player_pic = player1.five()
            counter += 1
        elif keys[pygame.K_6]:
            player_num = 6
            player_pic = player1.six()
            counter += 1
    
    # counter 4 is for computer toss and toss results
    if counter == 4:
        comp_num = random.choice(score_list)
        if comp_num == 1:
            comp_pic = comp.one()
        elif comp_num == 2:
            comp_pic = comp.two()
        elif comp_num == 3:
            comp_pic = comp.three()
        elif comp_num == 4:
            comp_pic = comp.four()
        elif comp_num == 5:
            comp_pic = comp.five()
        elif comp_num == 6:
            comp_pic = comp.six()

        win.blit(player_pic, player1.area)
        win.blit(comp_pic, comp.area)
        pygame.display.update()
        time.sleep(1)

        if (player_num+comp_num)%2==0:
            real_toss="even"
        else:
            real_toss="odd"
        
        if player1.toss==real_toss:
            toss_winner = True
            screen_timer(win,150,won_toss)
        else:
            toss_winner = False
            screen_timer(win,150,lost_toss)

        counter += 1
    
    
    # counter 5 is for 'first' batting or balling question part
    if counter == 5:
        if toss_winner:
            win.blit(bob,  (0,0))
            pygame.display.update()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_y]:
                section = "batting"
                counter += 1
            elif keys[pygame.K_n]:
                section = "balling"
                counter += 1
        
        else:
            section = random.choice(bat_ball)
            counter += 1
    
    # counter 6 is for 'first' batting or balling selection part 
    if counter == 6:
        if section=="batting":
            screen_timer(win,150,bat_first)
            section = None
            old_section = "batting"
            counter += 1
        elif section == "balling":
            screen_timer(win,150,ball_first)
            section = None
            old_section = "balling"
            counter = 9

    # counter 7 is for batting part of player [connected to counter 8]
    if counter == 7:
        if not counter_7:
            player1.total=0
            player1.dot_count=0
            comp.dot_count=0

        counter_7 = True
        win.blit(bg, (0,0))
        write(win,"Player run: " + str(player1.total), 40, (30,20))
        if counter_9:
            write(win,"Target: " + str(comp.total), 40, (600,20))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            run = 1
            run_pic = player1.one()
            counter += 1
        elif keys[pygame.K_2]:
            run = 2
            run_pic = player1.two()
            counter += 1
        elif keys[pygame.K_3]:
            run = 3
            run_pic = player1.three()
            counter += 1
        elif keys[pygame.K_4]:
            run = 4
            run_pic = player1.four()
            counter += 1
        elif keys[pygame.K_5]:
            run = 5
            run_pic = player1.five()
            counter += 1
        elif keys[pygame.K_6]:
            run = 6
            run_pic = player1.six()
            counter += 1
    
    # counter 8 is for balling part of computer [connected to counter 7]
    if counter == 8:
        if comp.dot_count>=2:
            ball=random.choice(score_list[1:])
        else:
            ball=random.choice(score_list)

        if ball == 1:
            ball_pic = comp.one()
        elif ball == 2:
            ball_pic = comp.two()
        elif ball == 3:
            ball_pic = comp.three()
        elif ball == 4:
            ball_pic = comp.four()
        elif ball == 5:
            ball_pic = comp.five()
        elif ball == 6:
            ball_pic = comp.six()

        win.blit(run_pic,player1.area)
        win.blit(ball_pic,comp.area)
        pygame.display.update()
        time.sleep(1)
    
        if ball!=0:
            if player1.dot_count>2:
                screen_timer(win,200,bat_dots)
                counter = -2
            elif run==ball:
                screen_timer(win,200,out)
                counter = -2
            else:
                player1.total+=run
                if (player1.total-run < 50 and player1.total >= 50) or (player1.total-run < 100 and player1.total >= 100):
                    sound.play()
                counter = 7
                if counter_9 and (player1.total > comp.total):
                    counter = -2
        else:
            counter = 7
        

    # counter 9 is for balling part of player [connected with counter 10]
    if counter == 9:
        if not counter_9:
            player1.dot_count=0
            comp.dot_count=0
            comp.total = 0

        counter_9 = True
        win.blit(bg2, (0,0))
        write(win,"Comp Run: " + str(comp.total), 40, (550,20))
        if counter_7:
            write(win,"Target: " + str(player1.total), 40, (30,20))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            ball = 1
            ball_pic = player1.one()
            counter += 1
        elif keys[pygame.K_2]:
            ball = 2
            ball_pic = player1.two()
            counter += 1
        elif keys[pygame.K_3]:
            ball = 3
            ball_pic = player1.three()
            counter += 1
        elif keys[pygame.K_4]:
            ball = 4
            ball_pic = player1.four()
            counter += 1
        elif keys[pygame.K_5]:
            ball = 5
            ball_pic = player1.five()
            counter += 1
        elif keys[pygame.K_6]:
            ball = 6
            ball_pic = player1.six()
            counter += 1
    
    # counter 10 is for batting part of computer [connected with counter 9]
    if counter == 10:
        if comp.dot_count>=2:
            run=random.choice(score_list[1:])
        else:
            run=random.choice(score_list)

        if run == 1:
            run_pic = comp.one()
        elif run == 2:
            run_pic = comp.two()
        elif run == 3:
            run_pic = comp.three()
        elif run == 4:
            run_pic = comp.four()
        elif run == 5:
            run_pic = comp.five()
        elif run == 6:
            run_pic = comp.six()

        win.blit(run_pic,comp.area)
        win.blit(ball_pic,player1.area)
        pygame.display.update()
        time.sleep(1)

        if ball!=0:
            if player1.dot_count>2:
                screen_timer(win,200,ball_dots)
                counter = -2
            elif run==ball:
                screen_timer(win,200,out)
                counter = -2
            else:
                comp.total+=run
                if (comp.total-run < 50 and comp.total >= 50) or (comp.total-run < 100 and comp.total >= 100):
                    sound.play()
                counter = 9
                if counter_7 and (player1.total < comp.total):
                    counter = -2

        else:
            counter = 9
                

    # counter -2 is for result part of entire game
    if counter == -2:
        if counter_7 and counter_9:
            if player1.total > comp.total:
                screen_timer(win,200,won_game)
                counter = -3
            elif player1.total == comp.total:
                screen_timer(win,200,draw_game)
                counter = -3
            else:
                screen_timer(win,200,lost_game)
                counter = -3

        elif counter_7 and not counter_9:
            counter = 9
            screen_timer(win,150,now_balling)
        else:
            counter = 7
            screen_timer(win,150,now_batting)
    
    # counter -1 is for disagreement about we wont continue playing this game anymore.
    if counter == -1:
        pygame.quit()
        break
    
    # counter -3 is for rematch
    if counter == -3:
        win.blit(proposal2, (0,0))
        pygame.display.update()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_y]:
            screen_timer(win,50,great)
            counter = 2
            # refreshing the properties
            player1 = Player(player_area)
            comp = Player(comp_area)
            player1.total=0
            player1.dot_count=0
            comp.dot_count=0
            comp.total = 0
            counter_7 = False
            counter_9 = False
            counter_4 = False
            
        elif keys[pygame.K_n]:
            counter = -4

    # counter -4 is for credits
    if counter == -4:
        if not counter_4:
            pygame.quit()
            break
        counter_4 = True

# Quiting the pygame window.
pygame.quit()