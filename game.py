import pygame
import time
import random
import json
import webbrowser
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("RPG Adventure")

clock = pygame.time.Clock()

tempRun = True
run = False

# Images and Assets
bg = pygame.image.load('bg.png')
main_menu = pygame.image.load('main menu.jpg')
walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
walkFront = [pygame.image.load('F1.png'),pygame.image.load('F2.png'),pygame.image.load('F3.png'),pygame.image.load('F4.png'),pygame.image.load('F5.png'),pygame.image.load('F6.png'),pygame.image.load('F7.png'),pygame.image.load('F8.png'),pygame.image.load('F9.png')]
walkBack = [pygame.image.load('B1.png'),pygame.image.load('B2.png'),pygame.image.load('B3.png'),pygame.image.load('B4.png'),pygame.image.load('B5.png'),pygame.image.load('B6.png'),pygame.image.load('B7.png'),pygame.image.load('B8.png'),pygame.image.load('B9.png')]
home_pic = pygame.image.load('house.png')
door_pic = pygame.image.load('door.png')
house_inside = pygame.image.load('house inside.png')
apple_tree = pygame.image.load('apple_tree.png')
inventory_item_pic = [pygame.image.load('apple.png'),pygame.image.load('stone.png'),pygame.image.load('money.png'),pygame.image.load('wood.png'),pygame.image.load('iron ore inventory.png'),pygame.image.load('iron ingot.png'),pygame.image.load('food.png')]
mine_pic = pygame.image.load('mine.png')
apple_obj_pic = pygame.image.load('apple_obj.png')
stoneTemp = pygame.image.load('stone temp.png')
waterfall_pic = pygame.image.load('waterfall.png')
pond_pic = pygame.image.load('pond coming.png')         # coming soon
market_pic = [pygame.image.load('market1.png'),pygame.image.load('market2.png'),pygame.image.load("shop dia box1.png"),pygame.image.load('op1.png'),pygame.image.load('op2.png'),pygame.image.load('sell.png'),pygame.image.load('buy.png')]
shop1 = pygame.image.load("shop1.png")
mine_inside_pic = [pygame.image.load('mine inside ruined.png'),pygame.image.load('mine inside.png')]
workbench_pic = pygame.image.load('workbench.png')
workbench_open = pygame.image.load('workbench open.png')
iron_mine_pic = pygame.image.load('iron mine.png')
iron_ore = [pygame.image.load('iron ore.png')]
stone_axe = pygame.image.load('stone axe.png')
iron_axe = pygame.image.load('iron axe.png')
smelter_pic = pygame.image.load('smelter.png')
hotbar_pic = pygame.image.load('hotbar.png')
zombie_pic = [pygame.image.load('zombie.png'),pygame.image.load('empty.png')]
fight_scene = pygame.image.load('fight.png')
map_pic = pygame.image.load('map.png')
sword_pic = pygame.image.load('sword.png')
help_pic = [pygame.image.load('help.png'),pygame.image.load('help2.png')]
website_pic = pygame.image.load('website.png')
stone_pickaxe = pygame.image.load('stone pick.png')
iron_pickaxe = pygame.image.load('iron pick.png')


music_paused=False
pygame.mixer.music.load('entry screen music.mp3')
pygame.mixer.music.play()


# Character's class
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.front= True
        self.back = False
        self.hitbox = (self.x, self.y, 50, 50)
        self.walkCount=0
        self.standing = True


    def draw(self,screen):
        if self.walkCount + 1 >= 27:
            self.walkCount=0
        if not(self.standing):
            if self.left:
                screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                self.hitbox = (self.x, self.y, 25, 50)
                # pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
            elif self.right:
                screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                self.hitbox = (self.x, self.y, 25, 50)
                # pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
            elif self.back:
                screen.blit(walkBack[self.walkCount//6], (self.x,self.y))
                self.walkCount += 1
                self.hitbox = (self.x, self.y, 25, 50)
                # pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
            elif self.front:
                screen.blit(walkFront[self.walkCount//5], (self.x,self.y))
                self.walkCount += 1
                self.hitbox = (self.x, self.y, 25, 50)
                # pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)
        else:
            if self.left:
                screen.blit(walkLeft[0], (self.x, self.y))
            elif self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            elif self.back:
                screen.blit(walkBack[0], (self.x, self.y))
            else:
                screen.blit(walkFront[0], (self.x, self.y))


# House's class
class home(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x-12, self.y-18, 230, 165)

    def draw(self,screen):
        if run == True:
            screen.blit(home_pic, (self.x,self.y))
        # pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)


# Door's class
class Door(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.hitbox=(self.x,self.y,80,75)

    def draw(self,screen):
        if run == True:
            screen.blit(door_pic, (self.x,self.y))
        if houseEntry==True:
            self.hitbox=(0,0,600,500)
        # pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)


class houseEntered(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.hitbox=(self.x,self.y,600,500)

    def draw(self,screen):
        if run == True:
            screen.blit(house_inside, (self.x,self.y))


# Apple Tree's class
class tree(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.hitbox1=(self.x, self.y+30, 100, 169)
        self.hitbox2=(self.x, self.y+195, 150, 25)

    def draw(self,screen):
        if run==True:
            screen.blit(apple_tree, (self.x,self.y))
        # pygame.draw.rect(screen, (255,0,0), self.hitbox1, 2)
        # pygame.draw.rect(screen, (255,0,0), self.hitbox2, 2)


# Inventory Item's class
class inventoryItem(object):
    def __init__(self,x,y,width,height,index):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.index=index

    def draw(self,screen):
        if inventory==1:
            screen.blit(inventory_item_pic[self.index], (self.x,self.y))


# Mine's claas
class Mine(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.hitbox=(self.x,self.y+30,350,205)
        self.hitbox2=(self.x,self.y+235,350,15)

    def draw(self,screen):
        if east_west==0 and north_south==1:
            screen.blit(mine_pic,(self.x,self.y))
        # pygame.draw.rect(screen,(255,0,0),self.hitbox,2)
        # pygame.draw.rect(screen,(255,0,0),self.hitbox2,2)


# Apples' class
class Apple(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def draw(self,screen):
        # time.sleep(10)
        screen.blit(apple_obj_pic,(self.x,self.y))


# Extra Hitboxes' class
class hitbox(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.hitbox=(self.x,self.y,self.width,self.height)
    def draw(self,screen):
        pygame.draw.rect(screen,(255,0,0),self.hitbox,1)


# Waterfall's class
class waterFall(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.hitbox=(self.x,self.y,400,230)
        if pondInside==False:
            self.hitbox2=(self.x+170,self.y+230,110,20)
        else:
            self.hitbox2=(0,0,600,500)

    def draw(self,screen):
        screen.blit(waterfall_pic,(self.x,self.y))
        # pygame.draw.rect(screen,(255,0,0),self.hitbox,2)
        # pygame.draw.rect(screen,(255,0,0),self.hitbox2,2)


# Market's class
class market(object):
    def __init__(self,x,y,width,height,index):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.index=index
    def draw(self,screen):
        screen.blit(market_pic[self.index],(self.x,self.y))


# Workbench's class
class Workbench(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def draw(self,screen):
        screen.blit(workbench_open,(self.x,self.y))


# Zombie's class
class enemy(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.health=20
    def draw(self,screen):
        screen.blit(zombie_pic[0],(self.x,self.y))
        # pygame.draw.rect(screen,(255,0,0),self.radar,2)


# Dialog boxes for help
class dialog(object):
    def __init__(self,x,y,width,height,write):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.write=write
    def draw(self,screen):
        pygame.draw.rect(screen,(228,200,63),(self.x,self.y,self.width,self.height),5)
        text_screen(self.write,(0,0,0),self.x+5,self.y+5)


def redrawGameWindow():
    global click
    global count
    global wb_wood_count
    global wb_stone_count
    global smeltOver
    global focus
    global hotbar
    global fight
    global fight2
    global manHealth
    global zombieHealth1
    global zombieHealth2
    global zombieHealth3
    global zombieHealth11
    global zombieHealth22
    global zombieHealth33
    screen.blit(bg,(0,0))
    text_screen(f"HP - {data['manHealth']}/50",(0,0,0),0,0)
    if houseEntry==True:
        enterHouse.draw(screen)
        # hitbox1.draw(screen)
        # hitbox2.draw(screen)
        # hitbox3.draw(screen)
        # hitbox4.draw(screen)
        # hitbox5.draw(screen)
        # hitbox6.draw(screen)
        # hitbox7.draw(screen)
        # hitbox8.draw(screen)
        # hitbox9.draw(screen)
        # hitbox10.draw(screen)
        # hitbox11.draw(screen)
        if data['workbench']==1:
            screen.blit(workbench_pic,(220,160))
            # hitbox24.draw(screen)
            # hitbox25.draw(screen)
        if data['smelter']==1:
            text_screen('Smelter',(249,153,11),390,90)
            hitbox30.draw(screen)
    if east_west==0 and north_south==1:
        mine.draw(screen)
        # hitbox18.draw(screen)
        if data['mf']==0:
            screen.blit(stoneTemp,(350,230))
        else:
            screen.blit(stoneTemp,(-1000,-1000))
    if east_west==1 and north_south==1:
        waterfall.draw(screen)
    if pondInside==True:
        screen.blit(pond_pic,(10,30))
    else:
        pass
    if east_west==-1 and north_south==-1:
        market1.draw(screen)
        market2.draw(screen)
        # hitbox12.draw(screen)
        # hitbox13.draw(screen)
        # hitbox14.draw(screen)
    if shopEntry==True:
        screen.blit(shop1,(0,0))
        # hitbox15.draw(screen)
        # hitbox16.draw(screen)
        # hitbox17.draw(screen)
    if mineEntry==True:
        if data['minepicchange']==0 and not(iron_mine==1):
            screen.blit(mine_inside_pic[0],(0,0))
        # hitbox19.draw(screen)
        # hitbox20.draw(screen)
        # hitbox21.draw(screen)
        # hitbox22.draw(screen)
        text_screen("Uh-oh! this mine looks very dusty and old.",(244,233,0),69,300)
        text_screen("Press 'c' to clean it.",(244,233,0),69,321)
        if data['minepicchange']==1 and not(iron_mine==1):
            screen.blit(mine_inside_pic[1],(0,0))
        # hitbox26.draw(screen)
        if iron_mine==1:
            screen.blit(iron_mine_pic,(0,0))
            # hitbox27.draw(screen)
            # hitbox28.draw(screen)
            # hitbox29.draw(screen)
    if east_west==-1 and north_south==1:
        hitbox23.draw(screen)
    
    if east_west==0 and north_south==-1:
        pygame.draw.rect(screen,(32,175,74),trap)
        mouse=pygame.mouse.get_pos()

        if fight==True:
            screen.blit(fight_scene,(0,0,0,0))
            damage1=random.randint(0,5)
            damage2=random.randint(0,5)
            damage3=random.randint(0,5)
            damage4=random.randint(0,5)
            damage5=random.randint(0,5)
            damage6=random.randint(0,5)
            manDamage1=random.randint(10,15)
            manDamage2=random.randint(7,10)
            manDamage3=random.randint(10,13)
            text_screen(f"HP - {data['manHealth']}/50",(255,255,255),440,240)
            if enemyCount==1:
                zombie1=enemy(50,25,0,0)
                zombie1.draw(screen)
                if (423 < mouse[0] < 506) and (404 < mouse[1] < 446) and click==1:
                    if focus=='sword':
                        data['sword health'] -= 2
                        zombieHealth1-=manDamage1
                        text_screen(f'-{manDamage1}',(250,0,0),80,40)
                    else:
                        zombieHealth1-=5
                        text_screen('-5',(250,0,0),80,40)
                    man.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    text_screen(f'-{damage1}',(255,0,0),420,110)
                    data['manHealth']-=damage1
                    pygame.display.update()
                    time.sleep(1)
                if (513 < mouse[0] < 594) and (453 < mouse[1] < 494) and click==1:
                    data['manHealth']-=damage1
                    text_screen(f'-{damage1}',(255,0,0),420,110)
                    man.draw(screen)
                    pygame.display.update()
                    fight=False
                    time.sleep(1)

            if enemyCount==2:
                if zombieHealth1>0:
                    zombie1=enemy(50,25,0,0)
                    zombie1.draw(screen)
                else:
                    zombie1=enemy(-1000,-1000,0,0)
                    zombie1.draw(screen)
                if zombieHealth2>0:
                    zombie2=enemy(50,125,0,0)
                    zombie2.draw(screen)
                else:
                    zombie2=enemy(-1000,-1000,0,0)
                    zombie2.draw(screen)
                if (423 < mouse[0] < 506) and (404 < mouse[1] < 446) and click==1:
                    if focus=='sword':
                        data['sword health'] -= 2
                        if zombieHealth1>0:
                            text_screen(f'-{manDamage1}',(250,0,0),80,40)
                            zombieHealth1-=manDamage1
                    else:
                        text_screen('-5',(250,0,0),80,40)
                        zombieHealth1-=5
                    man.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    if focus=='sword':
                        if zombieHealth2>0:
                            text_screen(f'-{manDamage2}',(250,0,0),80,140)
                            zombieHealth2-=manDamage2
                    else:
                        text_screen('-5',(250,0,0),80,140)
                        zombieHealth2-=5
                    man.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    text_screen(f'-{damage1+damage2}',(255,0,0),420,110)
                    data['manHealth']-=damage1
                    data['manHealth']-=damage2
                    pygame.display.update()
                    time.sleep(1)
                if (513 < mouse[0] < 594) and (453 < mouse[1] < 494) and click==1:
                    data['manHealth']-=damage1
                    data['manHealth']-=damage2
                    text_screen(f'-{damage1+damage2}',(255,0,0),420,110)
                    man.draw(screen)
                    pygame.display.update()
                    fight=False
                    time.sleep(1)

            if enemyCount==3:
                if zombieHealth1>0:
                    zombie1=enemy(50,25,0,0)
                    zombie1.draw(screen)
                else:
                    zombie1=enemy(-1000,-1000,0,0)
                    zombie1.draw(screen)
                if zombieHealth2>0:
                    zombie2=enemy(50,125,0,0)
                    zombie2.draw(screen)
                else:
                    zombie2=enemy(-1000,-1000,0,0)
                    zombie2.draw(screen)
                if zombieHealth3>0:
                    zombie3=enemy(50,225,0,0)
                    zombie3.draw(screen)
                else:
                    zombie3=enemy(-1000,-1000,0,0)
                    zombie3.draw(screen)
                if (423 < mouse[0] < 506) and (404 < mouse[1] < 446) and click==1:
                    if focus=='sword':
                        data['sword health'] -= 2
                        if zombieHealth1>0:
                            text_screen(f'-{manDamage1}',(250,0,0),80,40)
                            zombieHealth1-=manDamage1
                    else:
                        text_screen('-5',(250,0,0),80,40)
                        zombieHealth1-=5
                    man.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    if focus=='sword':
                        if zombieHealth2>0:
                            text_screen(f'-{manDamage2}',(250,0,0),80,140)
                            zombieHealth2-=manDamage2
                    else:
                        text_screen('-5',(250,0,0),80,140)
                        zombieHealth2-=5
                    man.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    if focus=='sword':
                        if zombieHealth3>0:
                            text_screen(f'-{manDamage3}',(250,0,0),80,240)
                            zombieHealth3-=manDamage3
                    else:
                        text_screen('-5',(250,0,0),80,240)
                        zombieHealth3-=5
                    man.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    text_screen(f'-{damage1+damage2+damage3}',(255,0,0),420,110)
                    data['manHealth']-=damage1
                    data['manHealth']-=damage2
                    data['manHealth']-=damage3
                    pygame.display.update()
                    time.sleep(1)
                if (513 < mouse[0] < 594) and (453 < mouse[1] < 494) and click==1:
                    data['manHealth']-=damage1
                    data['manHealth']-=damage2
                    data['manHealth']-=damage3
                    text_screen(f'-{damage1+damage2+damage3}',(255,0,0),420,110)
                    man.draw(screen)
                    pygame.display.update()
                    fight=False
                    time.sleep(1)

    if east_west==-1 and north_south==0:
        # pygame.draw.rect(screen,(32,175,74),trap2)
        # mouse=pygame.mouse.get_pos()

        # if fight2==True:
        #     screen.blit(fight_scene,(0,0,0,0))
        #     damage11=random.randint(0,5)
        #     damage22=random.randint(0,5)
        #     damage33=random.randint(0,5)
        #     text_screen(f"HP - {data['manHealth']}/50",(255,255,255),440,240)
        #     if enemyCount==1:
        #         zombie11=enemy(50,25,0,0)
        #         zombie11.draw(screen)
        #         if (423 < mouse[0] < 506) and (404 < mouse[1] < 446) and click==1:
        #             text_screen('-5',(250,0,0),80,40)
        #             zombieHealth11-=5
        #             man.draw(screen)
        #             pygame.display.update()
        #             time.sleep(1)
        #             text_screen(f'-{damage11}',(255,0,0),420,110)
        #             data['manHealth']-=damage11
        #             pygame.display.update()
        #             time.sleep(1)
        #         if (513 < mouse[0] < 594) and (453 < mouse[1] < 494) and click==1:
        #             data['manHealth']-=damage11
        #             text_screen(f'-{damage11}',(255,0,0),420,110)
        #             man.draw(screen)
        #             pygame.display.update()
        #             fight2=False
        #             time.sleep(1)

        #     if enemyCount==2:
        #         zombie11=enemy(50,25,0,0)
        #         zombie22=enemy(50,125,0,0)
        #         zombie11.draw(screen)
        #         zombie22.draw(screen)
        #         if (423 < mouse[0] < 506) and (404 < mouse[1] < 446) and click==1:
        #             text_screen('-5',(250,0,0),80,40)
        #             zombieHealth11-=5
        #             man.draw(screen)
        #             pygame.display.update()
        #             time.sleep(1)
        #             text_screen('-5',(250,0,0),80,140)
        #             zombieHealth22-=5
        #             man.draw(screen)
        #             pygame.display.update()
        #             time.sleep(1)
        #             text_screen(f'-{damage11+damage22}',(255,0,0),420,110)
        #             data['manHealth']-=damage11
        #             data['manHealth']-=damage22
        #             pygame.display.update()
        #             time.sleep(1)
        #         if (513 < mouse[0] < 594) and (453 < mouse[1] < 494) and click==1:
        #             data['manHealth']-=damage11
        #             data['manHealth']-=damage22
        #             text_screen(f'-{damage11+damage22}',(255,0,0),420,110)
        #             man.draw(screen)
        #             pygame.display.update()
        #             fight2=False
        #             time.sleep(1)

        #     if enemyCount==3:
        #         zombie11=enemy(50,25,0,0)
        #         zombie22=enemy(50,125,0,0)
        #         zombie33=enemy(50,225,0,0)
        #         zombie11.draw(screen)
        #         zombie22.draw(screen)
        #         zombie33.draw(screen)
        #         if (423 < mouse[0] < 506) and (404 < mouse[1] < 446) and click==1:
        #             text_screen('-5',(250,0,0),80,40)
        #             zombieHealth11-=5
        #             man.draw(screen)
        #             pygame.display.update()
        #             time.sleep(1)
        #             text_screen('-5',(250,0,0),80,140)
        #             zombieHealth22-=5
        #             man.draw(screen)
        #             pygame.display.update()
        #             time.sleep(1)
        #             text_screen('-5',(250,0,0),80,240)
        #             zombieHealth33-=5
        #             man.draw(screen)
        #             pygame.display.update()
        #             time.sleep(1)
        #             text_screen(f'-{damage11+damage22+damage33}',(255,0,0),420,110)
        #             data['manHealth']-=damage11
        #             data['manHealth']-=damage22
        #             data['manHealth']-=damage33
        #             pygame.display.update()
        #             time.sleep(1)
        #         if (513 < mouse[0] < 594) and (453 < mouse[1] < 494) and click==1:
        #             data['manHealth']-=damage11
        #             data['manHealth']-=damage22
        #             data['manHealth']-=damage33
        #             text_screen(f'-{damage11+damage22+damage33}',(255,0,0),420,110)
        #             man.draw(screen)
        #             pygame.display.update()
        #             fight2=False
        #             time.sleep(1)
        pygame.draw.rect(screen,(32,175,74),trap2)
        mouse=pygame.mouse.get_pos()

        if fight2==True:
            screen.blit(fight_scene,(0,0,0,0))
            damage11=random.randint(0,5)
            damage22=random.randint(0,5)
            damage33=random.randint(0,5)
            manDamage1=random.randint(10,15)
            manDamage2=random.randint(7,10)
            manDamage3=random.randint(10,13)
            text_screen(f"HP - {data['manHealth']}/50",(255,255,255),440,240)
            if enemyCount==1:
                zombie11=enemy(50,25,0,0)
                zombie11.draw(screen)
                if (423 < mouse[0] < 506) and (404 < mouse[1] < 446) and click==1:
                    if focus=='sword':
                        zombieHealth11-=manDamage1
                        text_screen(f'-{manDamage1}',(250,0,0),80,40)
                    else:
                        zombieHealth11-=5
                        text_screen('-5',(250,0,0),80,40)
                    man.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    text_screen(f'-{damage11}',(255,0,0),420,110)
                    data['manHealth']-=damage11
                    pygame.display.update()
                    time.sleep(1)
                if (513 < mouse[0] < 594) and (453 < mouse[1] < 494) and click==1:
                    data['manHealth']-=damage11
                    text_screen(f'-{damage11}',(255,0,0),420,110)
                    man.draw(screen)
                    pygame.display.update()
                    fight=False
                    time.sleep(1)

            if enemyCount==2:
                if zombieHealth11>0:
                    zombie11=enemy(50,25,0,0)
                    zombie11.draw(screen)
                else:
                    zombie11=enemy(-1000,-1000,0,0)
                    zombie11.draw(screen)
                if zombieHealth22>0:
                    zombie22=enemy(50,125,0,0)
                    zombie22.draw(screen)
                else:
                    zombie22=enemy(-1000,-1000,0,0)
                    zombie22.draw(screen)
                if (423 < mouse[0] < 506) and (404 < mouse[1] < 446) and click==1:
                    if focus=='sword':
                        if zombieHealth11>0:
                            text_screen(f'-{manDamage1}',(250,0,0),80,40)
                            zombieHealth11-=manDamage1
                    else:
                        text_screen('-5',(250,0,0),80,40)
                        zombieHealth11-=5
                    man.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    if focus=='sword':
                        if zombieHealth22>0:
                            text_screen(f'-{manDamage2}',(250,0,0),80,140)
                            zombieHealth22-=manDamage2
                    else:
                        text_screen('-5',(250,0,0),80,140)
                        zombieHealth22-=5
                    man.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    text_screen(f'-{damage11+damage22}',(255,0,0),420,110)
                    data['manHealth']-=damage11
                    data['manHealth']-=damage22
                    pygame.display.update()
                    time.sleep(1)
                if (513 < mouse[0] < 594) and (453 < mouse[1] < 494) and click==1:
                    data['manHealth']-=damage11
                    data['manHealth']-=damage22
                    text_screen(f'-{damage11+damage22}',(255,0,0),420,110)
                    man.draw(screen)
                    pygame.display.update()
                    fight=False
                    time.sleep(1)

            if enemyCount==3:
                if zombieHealth11>0:
                    zombie11=enemy(50,25,0,0)
                    zombie11.draw(screen)
                else:
                    zombie11=enemy(-1000,-1000,0,0)
                    zombie11.draw(screen)
                if zombieHealth22>0:
                    zombie22=enemy(50,125,0,0)
                    zombie22.draw(screen)
                else:
                    zombie22=enemy(-1000,-1000,0,0)
                    zombie22.draw(screen)
                if zombieHealth33>0:
                    zombie33=enemy(50,225,0,0)
                    zombie33.draw(screen)
                else:
                    zombie33=enemy(-1000,-1000,0,0)
                    zombie33.draw(screen)
                if (423 < mouse[0] < 506) and (404 < mouse[1] < 446) and click==1:
                    if focus=='sword':
                        if zombieHealth11>0:
                            text_screen(f'-{manDamage1}',(250,0,0),80,40)
                            zombieHealth11-=manDamage1
                    else:
                        text_screen('-5',(250,0,0),80,40)
                        zombieHealth11-=5
                    man.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    if focus=='sword':
                        if zombieHealth22>0:
                            text_screen(f'-{manDamage2}',(250,0,0),80,140)
                            zombieHealth22-=manDamage2
                    else:
                        text_screen('-5',(250,0,0),80,140)
                        zombieHealth22-=5
                    man.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    if focus=='sword':
                        if zombieHealth33>0:
                            text_screen(f'-{manDamage3}',(250,0,0),80,240)
                            zombieHealth33-=manDamage3
                    else:
                        text_screen('-5',(250,0,0),80,240)
                        zombieHealth33-=5
                    man.draw(screen)
                    pygame.display.update()
                    time.sleep(1)
                    text_screen(f'-{damage11+damage22+damage33}',(255,0,0),420,110)
                    data['manHealth']-=damage11
                    data['manHealth']-=damage22
                    data['manHealth']-=damage33
                    pygame.display.update()
                    time.sleep(1)
                if (513 < mouse[0] < 594) and (453 < mouse[1] < 494) and click==1:
                    data['manHealth']-=damage11
                    data['manHealth']-=damage22
                    data['manHealth']-=damage33
                    text_screen(f'-{damage11+damage22+damage33}',(255,0,0),420,110)
                    man.draw(screen)
                    pygame.display.update()
                    fight=False
                    time.sleep(1)

    man.draw(screen)
    house.draw(screen)
    door.draw(screen)
    appleTree.draw(screen)
    appleObj1.draw(screen)
    appleObj2.draw(screen)
    appleObj3.draw(screen)
    appleObj4.draw(screen)
    appleObj5.draw(screen)

    if db==1 and (hitbox17.hitbox[1] < man.y and man.y < hitbox17.hitbox[1] + hitbox17.hitbox[3]):
        db1.draw(screen)
        op1.draw(screen)
        op2.draw(screen)
    if mc1==1:
        sell.draw(screen)
    if mc2==1:
        buy.draw(screen)
    if shopEntry==True:
        if data['workbench']==1 and buyVar==1:
            text_screen('Workbench purchased!!',(0,0,0),150,300)
            text_screen('Your workbench has been placed in the house.',(0,0,0),150,320)
        if data['workbench']==1 and buyVar==0:
            text_screen('Workbench purchased!!',(0,0,0),-1000,-1000)
    if houseEntry == True and wb==1:
        workbench.draw(screen)
    if wb==1:
        mouse=pygame.mouse.get_pos()
        # print(mouse)
        if (5 < mouse[0] < 152) and (12 < mouse[1] < 40) and click==1:
            if data['wood']>=10 and data['stones']>=15 and data['stone axe']==0:
                data['stone axe'] = 1
                data['stone axe health'] = 20
                data['stones'] -= 15
                data['wood'] -= 10
                time.sleep(2)
        if (10 < mouse[0] < 132) and (60 < mouse[1] < 85) and click==1:
            if data['wood']>=10 and data['iron']>=15 and data['iron axe']==0:
                data['iron axe'] = 1
                data['iron axe health'] = 30
                data['iron'] -= 15
                data['wood'] -= 10
                time.sleep(2)
        if (15 < mouse[0] < 90) and (105 < mouse[1] < 140) and click==1:
            if data['stones'] >= 15 and data['smelter']==0:
                data['stones'] -= 15
                data['smelter'] += 1
                time.sleep(2)
        if (10 < mouse[0] < 180) and (150 < mouse[1] < 170) and click==1:
            if data['stones'] >= 15 and data['wood'] >= 10 and data['stone pickaxe']==0:
                data['stones'] -= 15
                data['stone pickaxe health'] = 20
                data['wood'] -= 10
                data['stone pickaxe'] += 1
        if (10 < mouse[0] < 165) and (195 < mouse[1] < 215) and click==1:
            if data['iron'] >= 15 and data['wood'] >= 10 and data['iron pickaxe']==0:
                data['iron'] -= 15
                data['iron pickaxe health'] = 30
                data['wood'] -= 10
                data['iron pickaxe'] += 1

    if sm==1:
        t=0
        screen.blit(smelter_pic,(0,0,0,0))
        mouse=pygame.mouse.get_pos()
        # print(mouse)
        if (10 < mouse[0] < 315) and (60 < mouse[1] < 90) and click==1:
            if data['iron ore']>0:
                t=data['iron ore']
                data['iron']+=data['iron ore']
                data['iron ore']=0
                time.sleep(10*t)
                smeltOver=True
        if smeltOver==True:
            text_screen('Finished',(0,0,0),270,400)

    if hotbar==1:
        screen.blit(hotbar_pic,(200,150,0,0))
        mouse=pygame.mouse.get_pos()
        # print(mouse)
        mouse_pressed=pygame.mouse.get_pressed()

        if (273 < mouse[0] < 327) and (218 < mouse[1] < 273) and click==1:
            focus=''
            pygame.display.update()
            time.sleep(0.1)
            hotbar=0

        if data['stone axe']==1:
            screen.blit(stone_axe,(348,205,0,0))
            if (355 < mouse[0] < 384) and (210 < mouse[1] < 244) and mouse_pressed[0]:
                screen.blit(stone_axe,(man.x,man.y))
                focus='stone axe'
                pygame.display.update()
                time.sleep(0.1)
                hotbar=0

        if data['iron axe']==1:
            screen.blit(iron_axe,(310,169,0,0))
            if (310 < mouse[0] < 348) and (169 < mouse[1] < 202) and mouse_pressed[0]:
                screen.blit(iron_axe,(man.x,man.y))
                focus='iron axe'
                pygame.display.update()
                time.sleep(0.1)
                hotbar=0

        if data['food'] > 0:
            screen.blit(inventory_item_pic[6],(340,255,0,0))
            if (340 < mouse[0] < 380) and (255 < mouse[1] < 290) and mouse_pressed[0]:
                focus='food'
                screen.blit(inventory_item_pic[6],(man.x,man.y))
                pygame.display.update()
                time.sleep(0.1)
                hotbar=0

        if data['sword']==1:
            screen.blit(sword_pic,(253,168,0,0))
            if (250 < mouse[0] < 288) and (170 < mouse[1] < 203) and mouse_pressed[0]:
                screen.blit(sword_pic,(man.x,man.y))
                focus='sword'
                pygame.display.update()
                time.sleep(0.1)
                hotbar=0

        if data['stone pickaxe']==1:
            screen.blit(stone_pickaxe,(305,290,0,0))
            if (305 < mouse[0] < 338) and (295 < mouse[1] < 327) and mouse_pressed[0]:
                screen.blit(stone_pickaxe,(man.x,man.y))
                focus='stone pickaxe'
                pygame.display.update()
                time.sleep(0.1)
                hotbar=0

        if data['iron pickaxe']==1:
            screen.blit(iron_pickaxe,(250,286,0,0))
            if (252 < mouse[0] < 295) and (290 < mouse[1] < 330) and mouse_pressed[0]:
                screen.blit(iron_pickaxe,(man.x,man.y))
                focus='iron pickaxe'
                pygame.display.update()
                time.sleep(0.1)
                hotbar=0

    if map==1:
        screen.blit(map_pic,(15,15,0,0))
    
    if inventory==1:
        pygame.draw.rect(screen, (200,200,200), (75,80, 450, 300))
        apple.draw(screen)
        text_screen(str(data['apples']), (0,0,0), 150,115)
        stone.draw(screen)
        text_screen(str(data['stones']), (0,0,0), 150,169)
        money.draw(screen)
        text_screen(str(data['money']), (0,0,0), 153,218)
        woods.draw(screen)
        text_screen(str(data['wood']), (0,0,0), 153,269)
        ironOre.draw(screen)
        text_screen(str(data['iron ore']), (0,0,0), 153,320)
        iron.draw(screen)
        text_screen(str(data['iron']), (0,0,0), 240,110)
        food.draw(screen)
        text_screen(str(data['food']), (0,0,0), 240,160)

    if data['new']==0:
        intro_controls = dialog(50,400,100,100,'Make sure you have checked out the HELP section in the main menu. If not then go check it out.')
        intro_controls.draw(screen)
        pygame.display.update()
        time.sleep(5)
        data['new']+=1
        intro_controls = dialog(60,420,100,100,'Press E to open inventory.')
    pygame.display.update()
    if data['new']==1:
        intro_controls.draw(screen)
        pygame.display.update()
        time.sleep(2)
        data['new']+=1
    
    def update():
        global t
        t += time.dt
        if t > .5:  # do every half second
            t = 0
            text_screen('hello',(0,0,0),300,300)


    pygame.display.update()


def house_entry():
    # print('entered')
    global houseEntry
    global enterHouse
    global house
    global door
    if enterHouse.hitbox[1] < man.y < enterHouse.hitbox[1] + enterHouse.hitbox[3] and enterHouse.hitbox[0] < man.x < enterHouse.hitbox[0] + enterHouse.hitbox[0] + enterHouse.hitbox[2]:
        houseEntry=True
    man.x=375
    man.y=440


def collectApples():
    global apples
    global money
    text_screen('Collecting apples...',(0,0,0),160,440)
    pygame.display.update()
    time.sleep(3)
    text_screen('Collecting apples...',(36,178,77),160,440)
    pygame.display.update()
    ap=random.randint(-1,2)
    if ap==1 or ap==2:
        data['apples']+=ap
        text_screen('Apple found!',(0,230,0),160,440)
        pygame.display.update()
        time.sleep(2)
    if ap==0 or ap==-1:
        text_screen('No apple found!',(255,0,0),160,440)
        pygame.display.update()
        time.sleep(2)


def enterShop():
    global shopEntry
    if hitbox14.hitbox[1] < man.y < hitbox14.hitbox[1] + hitbox14.hitbox[3] and hitbox14.hitbox[0] < man.x < hitbox14.hitbox[0] + hitbox14.hitbox[0] + hitbox14.hitbox[2]:
        shopEntry=True
        man.x=300
        man.y=440


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x,y])


def sell_shop():
    global sellVar
    while data['apples'] > 0:
        if data['apples'] >= 10:
            data['apples'] -= 10
            data['money'] += 1
        break


def buy_shop():
    global buyVar
    # print('buybuybuy')
    if data['workbench'] == 0 and data['money'] >= 30:
        data['workbench'] = 1
        data['money'] -= 30
    if data['workbench'] == 1:
        pass

    if data['food']>=0 and data['money'] >= 10:
        data['food'] += 1
        data['money'] -= 10


def wood():
    time.sleep(2)
    if focus=='':
        ap=random.randint(-5,1)
        if ap==1:
            data['wood']+=ap
            text_screen('Wood found!',(0,240,0),210,440)
            pygame.display.update()
            time.sleep(1)
        else:
            text_screen('No wood found!',(255,0,0),210,440)
            pygame.display.update()
            time.sleep(1)
    if focus=='stone axe':
        ap=random.randint(-3,2)
        if ap==1 or ap==2:
            data['wood']+=ap
            data['stone axe health'] -= 2
            text_screen('Wood found!',(0,240,0),210,440)
            pygame.display.update()
            time.sleep(1)
        else:
            data['stone axe health'] -= 2
            text_screen('No wood found!',(255,0,0),210,440)
            pygame.display.update()
            time.sleep(1)
    if focus=='iron axe':
        ap=random.randint(-1,2)
        if ap==1 or ap==2:
            data['wood']+=ap
            data['iron axe health'] -= 2
            text_screen('Wood found!',(0,240,0),210,440)
            pygame.display.update()
            time.sleep(1)
        else:
            data['iron axe health'] -= 2
            text_screen('No wood found!',(255,0,0),210,440)
            pygame.display.update()
            time.sleep(1)


# Game Variables
east_west =  0
north_south = 0
font = pygame.font.SysFont(None, 32)
man = player(300,300,10,10)
sense = 0
houseEntry = False
enterHouse = houseEntered(0,0,0,0)
inventory = 0
appleTree = tree(420,250,10,10)
data = {
    'manHealth': 50,
    'food': 0,
    'apples': 0,
    'stones': 0,
    'money': 0,
    'wood': 0,
    'mf': 0,
    'minepicchange': 0,
    'workbench': 0,
    'iron ore': 0,
    'stone axe': 0,
    'smelter': 0,
    'iron': 0,
    'iron axe': 1,
    'stone pickaxe': 0,
    'iron pickaxe': 1,
    'sword': 0,
    'new': 0,
    'stone axe health': 20,
    'iron axe health': 30,
    'stone pickaxe health': 20,
    'iron pickaxe health': 30,
    'sword health': 30
}
with open('game_data') as score_file:
    data = json.load(score_file)
appleObj1 = Apple(450,280)
appleObj2 = Apple(450,315)
appleObj3 = Apple(515,315)
appleObj4 = Apple(480,300)
appleObj5 = Apple(510,269)
pondInside=False
shopEntry = False
db = 0
mc1=0
mc2=0
mineEntry = False
sellVar = 0
buyVar = 0
wb=0
click = 0
wb_wood_count = 0
wb_stone_count = 0
iron_mine = 0
hotbar = 0
sm=0
smeltOver=False
focus=''
fight=False
fight2=False
zombieHealth1 = 20
zombieHealth2 = 20
zombieHealth3 = 20
zombieHealth11 = 20
zombieHealth22 = 20
zombieHealth33 = 20
eating = False
map = 0
help = 0
page=1
mclick = 0
t=3


while tempRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tempRun  = False

    screen.blit(main_menu,(0,0))
    text_screen('Version 1.1.0',(0,0,0),455,470)
    pygame.draw.rect(screen,(255,87,87),(175,139,163,48),0,20)
    text_screen('START',(255,255,255),218,153)
    pygame.draw.rect(screen,(255,87,87),(152,255,160,47),0,20)
    text_screen('OPTIONS',(255,255,255),178,267)
    pygame.draw.rect(screen,(255,87,87),(175,378,163,48),0,20)
    text_screen('HELP',(255,255,255),225,392)

    screen.blit(website_pic,(-5,465,0,0))
    pygame.draw.rect(screen,(0,0,255),(0,465,150,35),2)
    mouse=pygame.mouse.get_pos()
    mouse_pressed=pygame.mouse.get_pressed()

    if (175+163 > mouse[0] > 175 and 139+48 > mouse[1] > 139):
        pygame.draw.rect(screen,(255,125,125),(175,139,163,48),0,20)
        text_screen('START',(255,255,255),218,153)
        if pygame.mouse.get_pressed()[0]:
            music_paused = not music_paused
            if music_paused:
                pygame.mixer.music.pause()
                pygame.mixer.music.load('gtts.mp3')
                pygame.mixer.music.play(1)
            else:
                pygame.mixer.music.unpause()
            tempRun=False
            run=True
    if (175+163 > mouse[0] > 175 and 378+48 > mouse[1] > 378):
        pygame.draw.rect(screen,(255,125,125),(175,378,163,48),0,20)
        text_screen('HELP',(255,255,255),225,392)
        if pygame.mouse.get_pressed()[0]:
            # webbrowser.open('https://drive.google.com/file/d/1vt7jyqLvBIEHjQvGOWsi67SJ-iMCIhKU/view?usp=sharing')
            help = 1

    if help==1:
        if (258 < mouse[0] < 288 and 454 < mouse[1] < 484) and mouse_pressed[0] and page>0 and page==2:
            page-=1
            time.sleep(0.5)
        if (295 < mouse[0] < 325 and 454 < mouse[1] < 484) and mouse_pressed[0] and page>0 and page==1:
            page+=1
            time.sleep(0.5)
        if (580 < mouse[0] < 600) and (0 < mouse[1] < 20) and mouse_pressed[0]:
            help=0
            page=1

        if page==1:
            screen.blit(help_pic[0],(0,0,0,0))
            pygame.draw.rect(screen,(255,0,0),(580,0,20,20))
            pygame.draw.rect(screen,(255,125,125),(258,454,30,30),0,36)
            text_screen('<',(0,0,0),266,456)
            pygame.draw.rect(screen,(255,125,125),(295,454,30,30),0,36)
            text_screen('>',(0,0,0),305,456)
            text_screen('x',(0,0,0),585,-1)

        if page==2:
            screen.blit(help_pic[1],(0,0,0,0))
            pygame.draw.rect(screen,(255,0,0),(580,0,20,20))
            pygame.draw.rect(screen,(255,125,125),(258,454,30,30),0,36)
            text_screen('<',(0,0,0),266,456)
            pygame.draw.rect(screen,(255,125,125),(295,454,30,30),0,36)
            text_screen('>',(0,0,0),305,456)
            text_screen('x',(0,0,0),585,-1)

    if (-5<mouse[0]<155) and (465<mouse[1]<500) and mouse_pressed[0]:
        webbrowser.open('https://amaldeeppatra21.wixsite.com/amaldeepgamedev')
        time.sleep(1)

    pygame.display.update()


while run:
    clock.tick(45)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('game_data','w') as score_file:
                json.dump(data,score_file)
            run  = False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                if not(houseEntry==False and pondInside==False and shopEntry==False and mineEntry==False):
                    houseEntry=False
                    man.x = 215
                    man.y = 275
                    pondInside=False
                    shopEntry=False
                    sell=market(-1000,-1000,0,0,5)
                    buy=market(-1000,-1000,0,0,6)
                    mineEntry=False
                    wb=0
                    iron_mine=0
                    sm=0
                    smeltOver=False
            if event.key==pygame.K_e and inventory==0:
                # print('inventory opened')
                inventory = 1
            elif event.key==pygame.K_e and inventory==1:
                # print('inventory closed')
                inventory = 0
            if event.key==pygame.K_m and map==0:
                map=1
            elif event.key==pygame.K_m and map==1:
                map=0
            if event.key==pygame.K_b and shopEntry==True:
                mc2=1
                man.y=269
                buy=market(150,100,0,0,6)
            if event.key==pygame.K_s and shopEntry==True:
                mc1=1
                man.y=269
                sell=market(150,100,0,0,5)
            if shopEntry==True:
                if event.key==pygame.K_a and man.y == 269:
                    sellVar = 1
                elif event.key==pygame.K_a and sellVar==1:
                    sellVar = 0
                # if event.key==pygame.K_1 and man.y==269:
                #     buyVar = 1
                # if not(man.y==269) and buyVar==1:
                #     buyVar = 0
            if mineEntry==True:
                if event.key==pygame.K_c:
                    data['minepicchange']=1
            if event.key==pygame.K_h and hotbar==0:
                hotbar=1
            elif event.key==pygame.K_h and hotbar==1:
                hotbar=0

        if event.type == pygame.MOUSEBUTTONDOWN and click==0:
            if event.button == 1:
                click = 1
                # print(click)
        if event.type == pygame.MOUSEMOTION and click==1:
            click = 0

        # if event.type == pygame.MOUSEMOTION:
        #     print(event)

    keys = pygame.key.get_pressed()
    mouse_pressed = pygame.mouse.get_pressed()

    # Key Movements
    if keys[pygame.K_a]:
        man.x -= man.vel
        man.right = False
        man.left = True
        man.back = False
        man.front = False
        man.standing=False

        if man.y < house.hitbox[1] + house.hitbox[3] and man.y > house.hitbox[1]:
            if man.x > house.hitbox[0] and man.x < house.hitbox[0] + house.hitbox[2]:
                man.x += 5
        
        if man.y < appleTree.hitbox1[1] + appleTree.hitbox1[3] and man.y > appleTree.hitbox1[1]:
            if man.x > appleTree.hitbox1[0] and man.x < appleTree.hitbox1[0] + appleTree.hitbox1[2]:
                man.x += 5
        
        if ((east_west==-1 and north_south==0) and man.x < 5) or ((east_west==-1 and north_south==1) and man.x < 5) or ((east_west==-1 and north_south==-1) and man.x < 5):
            man.x += 5

        if (east_west==0 and north_south==1) and man.y < mine.hitbox[1] + mine.hitbox[3] and man.y > mine.hitbox[1]:
            if man.x > mine.hitbox[0] and man.x < mine.hitbox[0] + mine.hitbox[2]:
                man.x += 5

        if houseEntry==True:
            if man.y < hitbox4.hitbox[1] + hitbox4.hitbox[3] and man.y > hitbox4.hitbox[1]:
                if man.x > hitbox4.hitbox[0] and man.x < hitbox4.hitbox[0] + hitbox4.hitbox[2]:
                    man.x += 5
            if man.y < hitbox5.hitbox[1] + hitbox5.hitbox[3] and man.y > hitbox5.hitbox[1]:
                if man.x > hitbox5.hitbox[0] and man.x < hitbox5.hitbox[0] + hitbox5.hitbox[2]:
                    man.x += 5
            if man.y < hitbox6.hitbox[1] + hitbox6.hitbox[3] and man.y > hitbox6.hitbox[1]:
                if man.x > hitbox6.hitbox[0] and man.x < hitbox6.hitbox[0] + hitbox6.hitbox[2]:
                    man.x += 5
            if man.y < hitbox7.hitbox[1] + hitbox7.hitbox[3] and man.y > hitbox7.hitbox[1]:
                if man.x > hitbox7.hitbox[0] and man.x < hitbox7.hitbox[0] + hitbox7.hitbox[2]:
                    man.x += 5
            if man.y < hitbox8.hitbox[1] + hitbox8.hitbox[3] and man.y > hitbox8.hitbox[1]:
                if man.x > hitbox8.hitbox[0] and man.x < hitbox8.hitbox[0] + hitbox8.hitbox[2]:
                    man.x += 5
            if man.y < hitbox11.hitbox[1] + hitbox11.hitbox[3] and man.y > hitbox11.hitbox[1]:
                if man.x > hitbox11.hitbox[0] and man.x < hitbox11.hitbox[0] + hitbox11.hitbox[2]:
                    man.x += 5
        if east_west==1 and north_south==1:
            if man.y < waterfall.hitbox[1] + waterfall.hitbox[3] and man.y > waterfall.hitbox[1]:
                if man.x > waterfall.hitbox[0] and man.x < waterfall.hitbox[0] + waterfall.hitbox[2]:
                    man.x += 5
        if east_west==-1 and north_south==-1:
            if man.y < hitbox12.hitbox[1] + hitbox12.hitbox[3] and man.y > hitbox12.hitbox[1]:
                if man.x > hitbox12.hitbox[0] and man.x < hitbox12.hitbox[0] + hitbox12.hitbox[2]:
                    man.x += 5
            if man.y < hitbox13.hitbox[1] + hitbox13.hitbox[3] and man.y > hitbox13.hitbox[1]:
                if man.x > hitbox13.hitbox[0] and man.x < hitbox13.hitbox[0] + hitbox13.hitbox[2]:
                    man.x += 5
        if mineEntry==True:
            if man.y < hitbox21.hitbox[1] + hitbox21.hitbox[3] and man.y > hitbox21.hitbox[1]:
                if man.x > hitbox21.hitbox[0] and man.x < hitbox21.hitbox[0] + hitbox21.hitbox[2]:
                    man.x += 5
            if man.y < hitbox26.hitbox[1] + hitbox26.hitbox[3] and man.y > hitbox26.hitbox[1]:
                if man.x > hitbox26.hitbox[0] and man.x < hitbox26.hitbox[0] + hitbox26.hitbox[2]:
                    man.x += 5
            if iron_mine==1:
                if man.x < hitbox27.hitbox[0]:
                    man.x += 5
        if fight==True:
            if man.x < hitbox31.hitbox[0]:
                man.x += 5
        if fight2==True:
            if man.x < hitbox32.hitbox[0]:
                man.x += 5


    elif keys[pygame.K_d]:
        man.x += man.vel
        man.right = True
        man.left = False
        man.back = False
        man.front = False
        man.standing=False

        if man.y < house.hitbox[1] + house.hitbox[3] and man.y > house.hitbox[1]:
            if man.x > house.hitbox[0] and man.x < house.hitbox[0] + house.hitbox[2]:
                man.x -= 5

        if man.y < appleTree.hitbox1[1] + appleTree.hitbox1[3] and man.y > appleTree.hitbox1[1]:
            if man.x > appleTree.hitbox1[0] and man.x < appleTree.hitbox1[0] + appleTree.hitbox1[2]:
                man.x -= 5

        if ((east_west==1 and north_south==0) and man.x > 570) or ((east_west==1 and north_south==1) and man.x > 570) or ((east_west==1 and north_south==-1) and man.x > 570):
            man.x -= 5

        if (east_west==0 and north_south==1) and man.y < mine.hitbox[1] + mine.hitbox[3] and man.y > mine.hitbox[1]:
            if man.x > mine.hitbox[0] and man.x < mine.hitbox[0] + mine.hitbox[2]:
                man.x -= 5
        if fight==True:
            if man.x > hitbox31.hitbox[0]+hitbox31.hitbox[2]:
                man.x -= 5
        if fight2==True:
            if man.x > hitbox32.hitbox[0]+hitbox32.hitbox[2]:
                man.x -= 5
                
        if houseEntry==True:
            if man.y < hitbox2.hitbox[1] + hitbox2.hitbox[3] and man.y > hitbox2.hitbox[1]:
                if man.x > hitbox2.hitbox[0] and man.x < hitbox2.hitbox[0] + hitbox2.hitbox[2]:
                    man.x -= 5
            if man.y < hitbox6.hitbox[1] + hitbox6.hitbox[3] and man.y > hitbox6.hitbox[1]:
                if man.x > hitbox6.hitbox[0] and man.x < hitbox6.hitbox[0] + hitbox6.hitbox[2]:
                    man.x -= 5
            if man.y < hitbox6.hitbox[1] + hitbox6.hitbox[3] and man.y > hitbox6.hitbox[1]:
                if man.x > hitbox6.hitbox[0] and man.x < hitbox6.hitbox[0] + hitbox6.hitbox[2]:
                    man.x -= 5
            if man.y < hitbox7.hitbox[1] + hitbox7.hitbox[3] and man.y > hitbox7.hitbox[1]:
                if man.x > hitbox7.hitbox[0] and man.x < hitbox7.hitbox[0] + hitbox7.hitbox[2]:
                    man.x -= 5
            if man.y < hitbox8.hitbox[1] + hitbox8.hitbox[3] and man.y > hitbox8.hitbox[1]:
                if man.x > hitbox8.hitbox[0] and man.x < hitbox8.hitbox[0] + hitbox8.hitbox[2]:
                    man.x -= 5
            if man.y < hitbox9.hitbox[1] + hitbox9.hitbox[3] and man.y > hitbox9.hitbox[1]:
                if man.x > hitbox9.hitbox[0] and man.x < hitbox9.hitbox[0] + hitbox9.hitbox[2]:
                    man.x -= 5
            if man.y < hitbox10.hitbox[1] + hitbox10.hitbox[3] and man.y > hitbox10.hitbox[1]:
                if man.x > hitbox10.hitbox[0] and man.x < hitbox10.hitbox[0] + hitbox10.hitbox[2]:
                    man.x -= 5
            if man.y < hitbox11.hitbox[1] + hitbox11.hitbox[3] and man.y > hitbox11.hitbox[1]:
                if man.x > hitbox11.hitbox[0] and man.x < hitbox11.hitbox[0] + hitbox11.hitbox[2]:
                    man.x -= 5
            try:
                if man.y < hitbox24.hitbox[1] + hitbox24.hitbox[3] and man.y > hitbox24.hitbox[1]:
                    if man.x > hitbox24.hitbox[0] and man.x < hitbox24.hitbox[0] + hitbox24.hitbox[2]:
                        man.x -= 5
            except:
                pass
        
        if east_west==1 and north_south==1:         # Waterfall
            if man.y < waterfall.hitbox[1] + waterfall.hitbox[3] and man.y > waterfall.hitbox[1]:
                if man.x > waterfall.hitbox[0] and man.x < waterfall.hitbox[0] + waterfall.hitbox[2]:
                    man.x -= 5
        
        if east_west==-1 and north_south==-1:       # Markets
            if man.y < hitbox12.hitbox[1] + hitbox12.hitbox[3] and man.y > hitbox12.hitbox[1]:
                if man.x > hitbox12.hitbox[0] and man.x < hitbox12.hitbox[0] + hitbox12.hitbox[2]:
                    man.x -= 5
            if man.y < hitbox13.hitbox[1] + hitbox13.hitbox[3] and man.y > hitbox13.hitbox[1]:
                if man.x > hitbox13.hitbox[0] and man.x < hitbox13.hitbox[0] + hitbox13.hitbox[2]:
                    man.x -= 5
        
        if shopEntry==True:
            if man.y < hitbox16.hitbox[1] + hitbox16.hitbox[3] and man.y > hitbox16.hitbox[1]:
                if man.x > hitbox16.hitbox[0] and man.x < hitbox16.hitbox[0] + hitbox16.hitbox[2]:
                    man.x -= 5
        if mineEntry==True:
            if man.y < hitbox20.hitbox[1] + hitbox20.hitbox[3] and man.y > hitbox20.hitbox[1]:
                if man.x > hitbox20.hitbox[0] and man.x < hitbox20.hitbox[0] + hitbox20.hitbox[2]:
                    man.x -= 5
            if man.y < hitbox26.hitbox[1] + hitbox26.hitbox[3] and man.y > hitbox26.hitbox[1]:
                if man.x > hitbox26.hitbox[0] and man.x < hitbox26.hitbox[0] + hitbox26.hitbox[2]:
                    man.x -= 5
            if iron_mine==1:
                if man.x > hitbox27.hitbox[0]+hitbox27.hitbox[2]:
                    man.x -= 5


    elif keys[pygame.K_w]:
        man.y -= man.vel
        man.right = False
        man.left = False
        man.back = True
        man.front = False
        man.standing=False

        if man.y < house.hitbox[1] + house.hitbox[3] and man.y > house.hitbox[1]:
            if man.x > house.hitbox[0] and man.x < house.hitbox[0] + house.hitbox[2]:
                man.y += 5

        if man.y < appleTree.hitbox1[1] + appleTree.hitbox1[3] and man.y > appleTree.hitbox1[1]:
            if man.x > appleTree.hitbox1[0] and man.x < appleTree.hitbox1[0] + appleTree.hitbox1[2]:
                man.y += 5

        if ((east_west==0 and north_south==1) and man.y < 10) or ((east_west==-1 and north_south==1) and man.y < 10) or ((east_west==1 and north_south==1) and man.y < 10):
            man.y += 5

        if (east_west==0 and north_south==1) and man.y < mine.hitbox[1] + mine.hitbox[3] and man.y > mine.hitbox[1]:
            if man.x > mine.hitbox[0] and man.x < mine.hitbox[0] + mine.hitbox[2]:
                man.y += 5

        if houseEntry==True:
            if man.y < hitbox1.hitbox[1] + hitbox1.hitbox[3] and man.y > hitbox1.hitbox[1]:
                if man.x > hitbox1.hitbox[0] and man.x < hitbox1.hitbox[0] + hitbox1.hitbox[2]:
                    man.y += 5
            if man.y < hitbox5.hitbox[1] + hitbox5.hitbox[3] and man.y > hitbox5.hitbox[1]:
                if man.x > hitbox5.hitbox[0] and man.x < hitbox5.hitbox[0] + hitbox5.hitbox[2]:
                    man.y += 5
            if man.y < hitbox6.hitbox[1] + hitbox6.hitbox[3] and man.y > hitbox6.hitbox[1]:
                if man.x > hitbox6.hitbox[0] and man.x < hitbox6.hitbox[0] + hitbox6.hitbox[2]:
                    man.y += 5
            if man.y < hitbox7.hitbox[1] + hitbox7.hitbox[3] and man.y > hitbox7.hitbox[1]:
                if man.x > hitbox7.hitbox[0] and man.x < hitbox7.hitbox[0] + hitbox7.hitbox[2]:
                    man.y += 5
            if man.y < hitbox8.hitbox[1] + hitbox8.hitbox[3] and man.y > hitbox8.hitbox[1]:
                if man.x > hitbox8.hitbox[0] and man.x < hitbox8.hitbox[0] + hitbox8.hitbox[2]:
                    man.y += 5
            if man.y < hitbox9.hitbox[1] + hitbox9.hitbox[3] and man.y > hitbox9.hitbox[1]:
                if man.x > hitbox9.hitbox[0] and man.x < hitbox9.hitbox[0] + hitbox9.hitbox[2]:
                    man.y += 5
            if man.y < hitbox11.hitbox[1] + hitbox11.hitbox[3] and man.y > hitbox11.hitbox[1]:
                if man.x > hitbox11.hitbox[0] and man.x < hitbox11.hitbox[0] + hitbox11.hitbox[2]:
                    man.y += 5
            try:
                if man.y < hitbox24.hitbox[1] + hitbox24.hitbox[3] and man.y > hitbox24.hitbox[1]:
                    if man.x > hitbox24.hitbox[0] and man.x < hitbox24.hitbox[0] + hitbox24.hitbox[2]:
                        man.y += 5
            except:
                pass

        if east_west==1 and north_south==1:
            if man.y < waterfall.hitbox[1] + waterfall.hitbox[3] and man.y > waterfall.hitbox[1]:
                if man.x > waterfall.hitbox[0] and man.x < waterfall.hitbox[0] + waterfall.hitbox[2]:
                    man.y += 5

        if east_west==1 and north_south==1:
            if man.y < waterfall.hitbox2[1] + waterfall.hitbox2[3] and man.y > waterfall.hitbox2[1]:
                if man.x > waterfall.hitbox2[0] and man.x < waterfall.hitbox2[0] + waterfall.hitbox2[2]:
                    print('entered pond')
                    pondInside=True
            else:
                pondInside=False

        if east_west==0 and north_south==1 and data['mf']==0:
            if man.y < mine.hitbox2[1] + mine.hitbox2[3] and man.y > mine.hitbox2[1]:
                if man.x > mine.hitbox2[0] and man.x < mine.hitbox2[0] + mine.hitbox2[2]:
                    print('mine found')
                    data['mf']+=1
                    data['stones']+=10
                    pygame.draw.rect(screen,(255,255,0),(120,120,400,250))
                    text_screen('Congratulations!!! You have',(0,0,0),130,130)
                    text_screen('found the mine',(0,0,0),130,155)
                    pygame.display.update()
                    time.sleep(3)
        if east_west==0 and north_south==1:
            if man.y < hitbox18.hitbox[1] + hitbox18.hitbox[3] and man.y > hitbox18.hitbox[1] and data['mf']==1:
                if man.x > hitbox18.hitbox[0] and man.x < hitbox18.hitbox[0] + hitbox18.hitbox[2] and data['mf']==1:
                    print('entered mine')
                    man.x=15
                    man.y=120
                    mineEntry=True
        if east_west==-1 and north_south==-1:
            if man.y < hitbox12.hitbox[1] + hitbox12.hitbox[3] and man.y > hitbox12.hitbox[1]:
                if man.x > hitbox12.hitbox[0] and man.x < hitbox12.hitbox[0] + hitbox12.hitbox[2]:
                    man.y += 5
            if man.y < hitbox13.hitbox[1] + hitbox13.hitbox[3] and man.y > hitbox13.hitbox[1]:
                if man.x > hitbox13.hitbox[0] and man.x < hitbox13.hitbox[0] + hitbox13.hitbox[2]:
                    man.y += 5
        if shopEntry==True:
            if man.y < hitbox15.hitbox[1] + hitbox15.hitbox[3] and man.y > hitbox15.hitbox[1]:
                if man.x > hitbox15.hitbox[0] and man.x < hitbox15.hitbox[0] + hitbox15.hitbox[2]:
                    man.y += 5
        if iron_mine==1:
            if man.y < hitbox27.hitbox[1]:
                    man.y += 5
        if fight==True:
            if man.y < hitbox31.hitbox[1]:
                man.y += 5
        if fight2==True:
            if man.y < hitbox32.hitbox[1]:
                man.y += 5


    elif keys[pygame.K_s]:
        man.y += man.vel
        man.right = False
        man.left = False
        man.back = False
        man.front = True
        man.standing=False

        if man.y < house.hitbox[1] + house.hitbox[3] and man.y > house.hitbox[1]:
            if man.x > house.hitbox[0] and man.x < house.hitbox[0] + house.hitbox[2]:
                man.y -= 5
        
        if man.y < appleTree.hitbox1[1] + appleTree.hitbox1[3] and man.y > appleTree.hitbox1[1]:
            if man.x > appleTree.hitbox1[0] and man.x < appleTree.hitbox1[0] + appleTree.hitbox1[2]:
                man.y -= 5

        if ((east_west==0 and north_south==-1) and man.y > 440) or ((east_west==-1 and north_south==-1) and man.y > 440) or ((east_west==1 and north_south==-1) and man.y > 440):
            man.y -= 5

        if (east_west==0 and north_south==1) and man.y < mine.hitbox[1] + mine.hitbox[3] and man.y > mine.hitbox[1]:
            if man.x > mine.hitbox[0] and man.x < mine.hitbox[0] + mine.hitbox[2]:
                man.y -= 5

        if houseEntry==True:
            if man.y < hitbox3.hitbox[1] + hitbox3.hitbox[3] and man.y > hitbox3.hitbox[1]:
                if man.x > hitbox3.hitbox[0] and man.x < hitbox3.hitbox[0] + hitbox3.hitbox[2]:
                    man.y -= 5
            if man.y < hitbox6.hitbox[1] + hitbox6.hitbox[3] and man.y > hitbox6.hitbox[1]:
                if man.x > hitbox6.hitbox[0] and man.x < hitbox6.hitbox[0] + hitbox6.hitbox[2]:
                    man.y -= 5
            if man.y < hitbox7.hitbox[1] + hitbox7.hitbox[3] and man.y > hitbox7.hitbox[1]:
                if man.x > hitbox7.hitbox[0] and man.x < hitbox7.hitbox[0] + hitbox7.hitbox[2]:
                    man.y -= 5
            if man.y < hitbox8.hitbox[1] + hitbox8.hitbox[3] and man.y > hitbox8.hitbox[1]:
                if man.x > hitbox8.hitbox[0] and man.x < hitbox8.hitbox[0] + hitbox8.hitbox[2]:
                    man.y -= 5
            if man.y < hitbox10.hitbox[1] + hitbox10.hitbox[3] and man.y > hitbox10.hitbox[1]:
                if man.x > hitbox10.hitbox[0] and man.x < hitbox10.hitbox[0] + hitbox10.hitbox[2]:
                    man.y -= 5
            if man.y < hitbox11.hitbox[1] + hitbox11.hitbox[3] and man.y > hitbox11.hitbox[1]:
                if man.x > hitbox11.hitbox[0] and man.x < hitbox11.hitbox[0] + hitbox11.hitbox[2]:
                    man.y -= 5
        if east_west==1 and north_south==1:
            if man.y < waterfall.hitbox[1] + waterfall.hitbox[3] and man.y > waterfall.hitbox[1]:
                if man.x > waterfall.hitbox[0] and man.x < waterfall.hitbox[0] + waterfall.hitbox[2]:
                    man.y -= 5
        if east_west==-1 and north_south==-1:
            if man.y < hitbox12.hitbox[1] + hitbox12.hitbox[3] and man.y > hitbox12.hitbox[1]:
                if man.x > hitbox12.hitbox[0] and man.x < hitbox12.hitbox[0] + hitbox12.hitbox[2]:
                    man.y -= 5
            if man.y < hitbox13.hitbox[1] + hitbox13.hitbox[3] and man.y > hitbox13.hitbox[1]:
                if man.x > hitbox13.hitbox[0] and man.x < hitbox13.hitbox[0] + hitbox13.hitbox[2]:
                    man.y -= 5
        if mineEntry==True:
            if man.y < hitbox22.hitbox[1] + hitbox22.hitbox[3] and man.y > hitbox22.hitbox[1]:
                if man.x > hitbox22.hitbox[0] and man.x < hitbox22.hitbox[0] + hitbox22.hitbox[2]:
                    man.y -= 5
            if man.y < hitbox26.hitbox[1] + hitbox26.hitbox[3] and man.y > hitbox26.hitbox[1]:
                if man.x > hitbox26.hitbox[0] and man.x < hitbox26.hitbox[0] + hitbox26.hitbox[2]:
                    man.y -= 5
        if iron_mine==1:
            if man.y > hitbox27.hitbox[1]+hitbox27.hitbox[3]:
                    man.y -= 5
        if fight==True:
            if man.y > hitbox31.hitbox[1]+hitbox31.hitbox[3]:
                man.y -= 5
        if fight2==True:
            if man.y > hitbox32.hitbox[1]+hitbox32.hitbox[3]:
                man.y -= 5
    
    
    else:
        man.standing=True
        man.walkCount = 0


    #east_west and north_south updation
    if keys[pygame.K_d] and man.x > 600:
        man.x = 0
        east_west += 1
        # print((east_west,north_south))
    elif keys[pygame.K_a] and man.x < 0:
        man.x = 600
        east_west -= 1
        # print((east_west,north_south))
    elif keys[pygame.K_w] and man.y < 0:
        man.y = 500
        north_south += 1
        # print((east_west, north_south))
    elif keys[pygame.K_s] and man.y > 500:
        man.y = 0
        north_south -= 1
        # print((east_west, north_south))

    #Screen Transition
    if (east_west == 0 and north_south == 0) and (not houseEntry):
        house = home(100,100,265,168)
        door = Door(193,196,0,0)
        appleTree = tree(420,250,10,10)
        appleObj1 = Apple(450,280)
        appleObj2 = Apple(450,315)
        appleObj3 = Apple(515,315)
        appleObj4 = Apple(480,300)
        appleObj5 = Apple(510,269)
    elif (east_west == 0 and north_south == 0) and houseEntry:
        house = home(-1000,-1000,265,168)
        door = Door(-1000,1000,0,0)
        appleTree = tree(-1000,-1000,0,0)
        appleObj1 = Apple(-1000,-1000)
        appleObj2 = Apple(-1000,-1000)
        appleObj3 = Apple(-1000,-1000)
        appleObj4 = Apple(-1000,-1000)
        appleObj5 = Apple(-1000,-1000)
    else:
        house = home(-1000,-1000,265,168)
        door = Door(-1000,1000,0,0)
        appleTree = tree(-1000,-1000,0,0)
        appleObj1 = Apple(-1000,-1000)
        appleObj2 = Apple(-1000,-1000)
        appleObj3 = Apple(-1000,-1000)
        appleObj4 = Apple(-1000,-1000)
        appleObj5 = Apple(-1000,-1000)


    if east_west == 1 and north_south == 0:
        bg = pygame.image.load('10.png')
    elif east_west == 0 and north_south == 1:
        bg = pygame.image.load('01.png')
    elif east_west == -1 and north_south == 0:
        bg = pygame.image.load('-10.png')
    elif east_west == 0 and north_south == -1:
        bg = pygame.image.load('0-1.png')
    elif east_west == 1 and north_south == 1:
        bg = pygame.image.load('11.png')
    elif east_west == 1 and north_south == -1:
        bg = pygame.image.load('1-1.png')
    elif east_west == -1 and north_south == 1:
        bg = pygame.image.load('-11.png')
        hitbox23 = hitbox(230,280,100,50)
    elif east_west == -1 and north_south == -1:
        bg = pygame.image.load('-1-1.png')
    else:
        bg = pygame.image.load('bg.png')


    if (door.hitbox[1] < man.y < door.hitbox[1] + door.hitbox[3] and door.hitbox[0] < man.x < door.hitbox[0] + door.hitbox[2]) or data['manHealth'] <= 0:
        house_entry()
        hitbox1 = hitbox(0,0,600,10)
        hitbox2 = hitbox(565,0,10,500)
        hitbox3 = hitbox(0,430,600,10)
        hitbox4 = hitbox(0,0,10,500)
        hitbox5 = hitbox(0,0,320,160)
        hitbox6 = hitbox(0,310,80,190)
        hitbox7 = hitbox(265,160,45,120)
        hitbox8 = hitbox(265,305,45,175)
        hitbox9 = hitbox(355,0,235,170)
        hitbox10 = hitbox(500,250,90,235)
        hitbox11 = hitbox(385,200,115,80)

    if keys[pygame.K_SPACE] and appleTree.hitbox2[1] < man.y < appleTree.hitbox2[1] + appleTree.hitbox2[3] and appleTree.hitbox2[0] < man.x < appleTree.hitbox2[0] + appleTree.hitbox2[2]:
        collectApples()

    if east_west==-1 and north_south==1 and keys[pygame.K_SPACE] and appleTree.hitbox2[1] < man.y < hitbox23.hitbox[1] + hitbox23.hitbox[3] and hitbox23.hitbox[0] < man.x < hitbox23.hitbox[0] + hitbox23.hitbox[2]:
        wood()

    if inventory==1:
        apple = inventoryItem(100,100,0,0,0)
        stone = inventoryItem(100,154,0,0,1)
        money = inventoryItem(100,208,0,0,2)
        woods = inventoryItem(100,262,0,0,3)
        ironOre = inventoryItem(100,316,0,0,4)
        iron = inventoryItem(190,100,0,0,5)
        food = inventoryItem(190,154,0,0,6)

    if east_west==0 and north_south==1:
        mine = Mine(250,80,0,0)
        hitbox18 = hitbox(340,310,80,10)
    if east_west==1 and north_south==1:
        waterfall = waterFall(195,20,0,0)
    if pondInside==True:
        waterfall = waterFall(-1000,-1000,0,0)

    if (east_west==-1 and north_south==-1) and (not shopEntry):
        market1 = market(55,60,0,0,0)
        market2 = market(390,60,0,0,1)
        hitbox12 = hitbox(market1.x-25,market1.y-50,310,200)
        hitbox13 = hitbox(market2.x-25,market2.y-50,205,200)
        hitbox14 = hitbox(market1.x+115,market1.y+85,55,70)
    elif (east_west==-1 and north_south==-1) and shopEntry==True:
        market1 = market(-1000,-1000,0,0,0)
        market2 = market(-1000,-1000,0,0,1)
        hitbox12 = hitbox(-1000,-1000,0,0)
        hitbox13 = hitbox(-1000,-1000,0,0)
        hitbox14 = hitbox(-1000,-1000,0,0)
    else:
        market1 = market(-1000,-1000,0,0,0)
        market2 = market(-1000,-1000,0,0,1)
        hitbox12 = hitbox(-1000,-1000,0,0)
        hitbox13 = hitbox(-1000,-1000,0,0)
        hitbox14 = hitbox(-1000,-1000,0,0)

    if man.y < hitbox14.hitbox[1] + hitbox14.hitbox[3] and man.y > hitbox14.hitbox[1]:
        if man.x < hitbox14.hitbox[0] + hitbox14.hitbox[2] and man.x > hitbox14.hitbox[0]:
            enterShop()
            hitbox15 = hitbox(0,200,600,10)
            hitbox16 = hitbox(575,0,10,500)
            hitbox17 = hitbox(225,200,105,35)

    if shopEntry==True:
        if keys[pygame.K_SPACE] and hitbox17.hitbox[1] < man.y and man.y < hitbox17.hitbox[1]+hitbox17.hitbox[3]:
            db=1
            db1 = market(150,100,0,0,2)
            op1 = market(200,190,0,0,3)
            op2 = market(340,190,0,0,4)
        if not(hitbox17.hitbox[1] < man.y and man.y < hitbox17.hitbox[1]+hitbox17.hitbox[3]):
            db=0

    if sellVar==1:
        sell_shop()
    
    if shopEntry==True:
        mouse=pygame.mouse.get_pos()
        # print(mouse)
        if (150 < mouse[0] < 292) and (100 < mouse[1] < 120) and click==1:
            buyVar=1
            if buyVar==1:
                buy_shop()
        if not(150 < mouse[0] < 292) and (100 < mouse[1] < 120):
            buyVar=0
        
        if (152 < mouse[0] < 288) and (132 < mouse[1] < 150) and click==1:
            buyVar=1
            if buyVar==1:
                buy_shop()
        if not(152 < mouse[0] < 288) and (132 < mouse[1] < 150):
            buyVar=0

    if mineEntry==True:
        mine = Mine(-1000,-1000,0,0)
        hitbox18 = hitbox(-1000,-1000,80,10)
        hitbox19 = hitbox(0,0,600,20)
        hitbox20 = hitbox(580,0,20,500)
        hitbox21 = hitbox(0,0,15,500)
        hitbox22 = hitbox(0,440,600,60)
        hitbox26 = hitbox(421,42,121,166)
        
        if man.y < hitbox26.hitbox[1] + hitbox26.hitbox[3] and man.y > hitbox26.hitbox[1]:
                if man.x > hitbox26.hitbox[0] and man.x < hitbox26.hitbox[0] + hitbox26.hitbox[2]:
                    man.x=280
                    man.y=350
                    iron_mine=1
                    hitbox27 = hitbox(270,340,46,21)
                    hitbox28 = hitbox(270,340,71,71)

    if houseEntry==True:
        if data['workbench']==1:
            hitbox24 = hitbox(195,160,94,110)
            hitbox25 = hitbox(190,160,30,110)
        if data['workbench']==1 and keys[pygame.K_SPACE] and man.y < hitbox25.hitbox[1] + hitbox25.hitbox[3] and man.y > hitbox25.hitbox[1] and man.x < hitbox25.hitbox[0] + hitbox25.hitbox[2] and man.x > hitbox25.hitbox[0]:
            wb=1
            workbench = Workbench(0,0,600,500)
        if wb==1:
            if keys[pygame.K_q]:
                wb=0

    if iron_mine==1:
        hitbox29 = hitbox(260,255,90,90)
        mouse=pygame.mouse.get_pos()
        mouse_click=pygame.mouse.get_pressed()

        if focus=='':
            if (260 < mouse[0] < 350) and (255 < mouse[1] < 345):
                if mouse_click[0]:
                    # print('mine')
                    time.sleep(2)
                    fe=random.randint(-5,1)
                    if fe==1:
                        data['iron ore']+=1
                        text_screen('Iron ore found!',(0,240,0),210,440)
                        pygame.display.update()
                        time.sleep(1)
                    else:
                        text_screen('No iron ore found!',(255,0,0),210,440)
                        pygame.display.update()
                        time.sleep(1)
                    if fe==-3 or fe==0 or fe==-5:
                        data['stones']+=1

        if focus=='stone pickaxe':
            if (260 < mouse[0] < 350) and (255 < mouse[1] < 345):
                if mouse_click[0]:
                    time.sleep(2)
                    fe=random.randint(-2,1)
                    if fe==1:
                        data['iron ore']+=1
                        data['stone pickaxe health'] -= 2
                        text_screen('Iron ore found!',(0,240,0),210,440)
                        pygame.display.update()
                        time.sleep(1)
                    else:
                        data['stone pickaxe health'] -= 2
                        text_screen('No iron ore found!',(255,0,0),210,440)
                        pygame.display.update()
                        time.sleep(1)
                    if fe==-2 or fe==0:
                        data['stones']+=1
                        data['stone pickaxe health'] -= 2
        
        if focus=='iron pickaxe':
            if (260 < mouse[0] < 350) and (255 < mouse[1] < 345):
                if mouse_click[0]:
                    fe=random.randint(-1,2)
                    if fe==1 or fe==2:
                        data['iron ore']+=fe
                        data['iron pickaxe health'] -= 2
                        text_screen('Iron ore found!',(0,240,0),210,440)
                        pygame.display.update()
                        time.sleep(1)
                    else:
                        data['iron pickaxe health'] -= 2
                        text_screen('No iron ore found!',(255,0,0),210,440)
                        pygame.display.update()
                        time.sleep(1)
                    if fe==-1 or fe==0:
                        data['stones']+=2
                        data['iron pickaxe health'] -= 2

    if houseEntry==True and data['smelter']==1:
        hitbox30=hitbox(392,169,80,11)
        if keys[pygame.K_SPACE] and hitbox30.hitbox[1] < man.y < hitbox30.hitbox[1] + hitbox30.hitbox[3] and hitbox30.hitbox[0] < man.x < hitbox30.hitbox[0] + hitbox30.hitbox[2]:
            sm=1
        if sm==1:
            if keys[pygame.K_q]:
                sm=0

    if not(east_west==0 and north_south==-1):       # Next Update --> 6 enemies
        enemy_x=random.randint(0,450)
        enemy_y=random.randint(10,323)
        zombieHealth1=20
        zombieHealth2=20
        zombieHealth3=20

    if (east_west==0 and north_south==-1):
        trap = pygame.Rect(enemy_x,enemy_y,169,169)
        if man.x > enemy_x and man.x < enemy_x+169 and man.y > enemy_y and man.y < enemy_y+169:
            fight=True
            enemyCount = random.randint(1,3)
            # enemyCount = 3
            if fight==True:
                man.x=505
                man.y=130
                hitbox31=hitbox(505,130,1,1)
                
        if zombieHealth1<=0 and enemyCount==1:
            fight=False
        if zombieHealth1<=0 and zombieHealth2<=0 and enemyCount==2:
            fight=False
        if zombieHealth1<=0 and zombieHealth2<=0 and zombieHealth3<=0 and enemyCount==3:
            fight=False
        if data['manHealth']<=0:
            fight=False
            man.x=125
            man.y=210
            east_west=0
            north_south=0
            houseEntry=True
            text_screen('You Died!',(255,0,0),185,305)
            pygame.display.update()
            time.sleep(2)
            data['manHealth']=50

    if not(east_west==-1 and north_south==0):
        enemy_x2=random.randint(0,450)
        enemy_y2=random.randint(0,400)
        zombieHealth11=20
        zombieHealth22=20
        zombieHealth33=20

    if east_west==-1 and north_south==0:
        trap2 = pygame.Rect(enemy_x2,enemy_y2,169,169)
        if man.x > enemy_x2 and man.x < enemy_x2+169 and man.y > enemy_y2 and man.y < enemy_y2+169:
            fight2=True
            enemyCount = random.randint(1,3)
            if fight2==True:
                man.x=505
                man.y=130
                hitbox32=hitbox(505,130,1,1)
        if zombieHealth11<=0 and enemyCount==1:
            fight2=False
        if zombieHealth11<=0 and zombieHealth22<=0 and enemyCount==2:
            fight2=False
        if zombieHealth11<=0 and zombieHealth22<=0 and zombieHealth33<=0 and enemyCount==3:
            fight2=False
        if data['manHealth']<=0:
            fight2=False
            man.x=125
            man.y=210
            east_west=0
            north_south=0
            houseEntry=True
            text_screen('You Died!',(255,0,0),185,305)
            pygame.display.update()
            time.sleep(2)
            data['manHealth']=50

    if focus=='food' and data['food'] > 0:
        pygame.display.update()
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[2]:
            print('eat')
            if data['manHealth'] >= 46 and data['manHealth'] < 50:
                data['manHealth'] = 50
                text_screen('Eating...',(0,0,0),160,440)
                data['food'] -= 1
                pygame.display.update()
                time.sleep(2)
            elif data['manHealth']==50:
                text_screen('HP Full!',(0,0,0),160,440)
                pygame.display.update()
                time.sleep(2)
            else:
                text_screen('Eating...',(0,0,0),160,440)
                data['manHealth'] += 5
                data['food'] -= 1
                pygame.display.update()
                time.sleep(2)

    if data['stone axe health']==0 and not(data['stone axe']==1):
        data['stone axe']=0
        focus=''
    if data['iron axe health']==0 and not(data['iron axe']==1):
        data['iron axe']=0
        focus=''
    if data['stone pickaxe health']==0 and not(data['stone pickaxe']==1):
        data['stone pickaxe']=0
        focus=''
    if data['iron pickaxe health']==0 and not(data['iron pickaxe']==1):
        data['iron pickaxe']=0
        focus=''

    # mouse_click = pygame.mouse.get_pressed()
    # mouse_pos = pygame.mouse.get_pos()

    # if data['new']==0 and mouse_click[0] and (190<mouse_pos[0]<290) and (390<mouse_pos[1]<490):
    
    



    redrawGameWindow()

pygame.quit()