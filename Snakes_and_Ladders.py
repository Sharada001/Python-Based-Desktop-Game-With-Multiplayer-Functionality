

#---------------------------------------------------------   Developed by sharada shehan   ---------------------------------------------------------------------------

#---------------------------------------------------------      20th of August, 2021  --------------------------------------------------------------------------------

#--------------------------------------------------------------  Snakes and Ladders  ---------------------------------------------------------------------------------


    # importing  modules
    
from tkinter import *

from random import randint

import time

    # creating main window
    
master = Tk()

master.geometry("1350x900")

    # creating heading

canvasTop = Canvas(master,height=100,width=1000)
canvasTop.grid(row=0,column=0,columnspan=5)
imgTop = PhotoImage(file="LOGO.png")
img_Top = canvasTop.create_image(0,0,anchor=NW,image = imgTop )

    # creating main canvas
    
can1 = Canvas(master,height=700,width=700)
can1.grid(row=1,column=0,rowspan=10)



    # importing image of board
    
imgMain = PhotoImage(file="main.png")

    # placement of board

can1.image = imgMain

img_main = can1.create_image(0,0,anchor=NW,image = imgMain )

    # importing dice faces
    
img1 = PhotoImage(file="1.png")
img2 = PhotoImage(file="2.png")
img3 = PhotoImage(file="3.png")
img4 = PhotoImage(file="4.png")
img5 = PhotoImage(file="5.png")
img6 = PhotoImage(file="6.png")

imgs = [img1,img2,img3,img4,img5,img6]


    # variable for number of players
    
num_players = 0

    # lists for changes of movement
    
up = [x+1 for x in range(0,91,10)]
left =[y for y in range(1,101) if (y>10 and  float(str(y-1)[0])%2 == 1)]

    # change of movement at snakeheads
    
snakeHeads = [28,37,47,75,94,96]
snakeTails = [[140,140,-18],[-70,210,-34],[-140,210,-31],[210,280,-43],[210,140,-23],[-210,350,-54]]

    # change of movement at ladderbottoms
    
ladderBottoms = [4,12,14,22,41,54]
ladderTops = [[70,-350,52],[70,-210,38],[-70,-280,41],[70,-210,36],[70,-210,38],[70,-210,34]]

    # exit button function on main screen
    
def exit1() :
    master.destroy()


    # procedure of active program
    
def start () :

    start["state"] = DISABLED
    start["bg"] = "grey"

    # pop window
    
    master1 = Toplevel(master)
    
    master1.geometry("350x200")

    # input number of players
    
    label1 = Label(master1 , text = "Enter number of players ( 2 -4 ) : ",font=50,fg="red",pady=20,padx=15)
    
    label1.grid(row=0,column=1)
    
    entry1 = Entry(master1 , font=50,fg="blue",bg='yellow')
    
    entry1.grid(row=1,column=1)

    # creation of structure based on number of players
    
    def select_num_players() :
        
        global num_players

        num_players += int(entry1.get())

        if num_players == 2 :

            # creation of coins
            
            coin_red = can1.create_oval(10,710,60,760,fill="red")
            coin_green = can1.create_oval(10,710,60,760,fill="green")
            coin_list = [coin_red,coin_green]
            
            # creation of player name labels
            
            labelRed = Label(master , text = "player1 ",font=50,fg="red",pady=10,padx=15)
            labelRed.grid(row=2,column=1)
            labelGreen = Label(master , text = "player2 ",font=50,fg="green",pady=10,padx=15)
            labelGreen.grid(row=2,column=2)

            # creation of dice buttons
            
            buttonRed = Button(master,text="dice",pady=2,height=1,width=10,font=50,command=lambda: movement(0))
            buttonRed.grid(row=3,column=1)
            buttonGreen = Button(master,text="dice",pady=2,height=1,width=10,font=50,command=lambda: movement(1))
            buttonGreen.grid(row=3,column=2)
            button_list = [buttonRed,buttonGreen]
            
            
            
        elif num_players == 3 :

            # creation of coins
            
            coin_red = can1.create_oval(10,710,60,760,fill="red")
            coin_green = can1.create_oval(10,710,60,760,fill="green")
            coin_blue = can1.create_oval(10,710,60,760,fill="blue")
            coin_list = [coin_red,coin_green,coin_blue]
            
            # creation of player name labels
            
            
            labelRed = Label(master , text = "player1 ",font=50,fg="red",pady=10,padx=15)
            labelRed.grid(row=2,column=1)
            labelGreen = Label(master , text = "player2 ",font=50,fg="green",pady=10,padx=15)
            labelGreen.grid(row=2,column=2)
            labelBlue = Label(master , text = "player3 ",font=50,fg="blue",pady=10,padx=15)
            labelBlue.grid(row=2,column=3)

            # creation of dice buttons
            
            buttonRed = Button(master,text="dice",pady=2,height=1,width=10,font=50,command=lambda: movement(0))
            buttonRed.grid(row=3,column=1)
            buttonGreen = Button(master,text="dice",pady=2,height=1,width=10,font=50,command=lambda: movement(1))
            buttonGreen.grid(row=3,column=2)
            buttonBlue = Button(master,text="dice",pady=2,height=1,width=10,font=50,command=lambda: movement(2))
            buttonBlue.grid(row=3,column=3)
            button_list = [buttonRed,buttonGreen,buttonBlue]
            
            
            
        elif num_players == 4 :

            # creation of coins
            
            coin_red = can1.create_oval(10,710,60,760,fill="red")
            coin_green = can1.create_oval(10,710,60,760,fill="green")
            coin_blue = can1.create_oval(10,710,60,760,fill="blue")
            coin_black = can1.create_oval(10,710,60,760,fill="black")
            coin_list = [coin_red,coin_green,coin_blue,coin_black]
            
            # creation of player name labels
            
            labelRed = Label(master , text = "player1 ",font=50,fg="red",pady=10,padx=15)
            labelRed.grid(row=2,column=1)
            labelGreen = Label(master , text = "player2 ",font=50,fg="green",pady=10,padx=15)
            labelGreen.grid(row=2,column=2)
            labelBlue = Label(master , text = "player3 ",font=50,fg="blue",pady=10,padx=15)
            labelBlue.grid(row=2,column=3)
            labelBlack = Label(master , text = "player4 ",font=50,fg="black",pady=10,padx=15)
            labelBlack.grid(row=2,column=4)

            # creation of dice buttons
            
            buttonRed = Button(master,text="dice",pady=2,height=1,width=10,font=50,command=lambda: movement(0))
            buttonRed.grid(row=3,column=1)
            buttonGreen = Button(master,text="dice",pady=2,height=1,width=10,font=50,command=lambda: movement(1))
            buttonGreen.grid(row=3,column=2)
            buttonBlue = Button(master,text="dice",pady=2,height=1,width=10,font=50,command=lambda: movement(2))
            buttonBlue.grid(row=3,column=3)
            buttonBlack = Button(master,text="dice",pady=2,height=1,width=10,font=50,command=lambda: movement(3))
            buttonBlack.grid(row=3,column=4)
            button_list = [buttonRed,buttonGreen,buttonBlue,buttonBlack]
            
        # invalid input
        
        else :
            print("error")

        # ending pop up window
        
        master1.destroy()

        # list to determine positions of coins
        
        button_var = [0,0,0,0]
        
        # movement of coin for selected player
        
        def movement (button_num) :

            can2 = Canvas(master,height=150,width=150,bg="yellow")
            can2.grid(row=4,column=button_num+1)

            # variable for slow motion movement
            
            a = 14

            # producing random integer
            
            x = randint(1,6)

            # relevant image for random number
            
            imgn = can2.create_image(75,75,anchor=CENTER,image = imgs[x-1] )
            
            print('  dice number of player {} is :  '.format(button_num+1) ,x)

            for y in range(x) :

                button_var[button_num] += 1

                # if a player won
                
                if button_var[button_num] == 100 :

                    # last move

                    for i in range(0,5) :
                        can1.move( coin_list[button_num] ,-a ,0 )
                        master.update()
                        time.sleep(0.001)
                    
                    # popup window
                    
                    master3 = Toplevel(master)
                    master3.geometry("400x400")

                    # exit from game
                    
                    def exit2() :
                        master3.destroy()
                        master.destroy()
                        
                    # print which player won
                    
                    label3 = Label(master3,text="Player {} WON ".format(button_num+1),font=50,fg="red",pady=20,padx=15)
    
                    label3.grid(row=0,column=1)

                    button3 = Button(master3,text="exit",pady=10,height=1,width=10,font=50,command=exit2,bg="#e1a900")
    
                    button3.grid(row=1,column=1)

                    break
                
                print(button_var[button_num])

                # move coin upward
                
                if button_var[button_num] in up :
                    for i in range(0,5) :
                        can1.move( coin_list[button_num] ,0 ,-a )
                        master.update()
                        time.sleep(.001)

                # move coin to left
                
                elif button_var[button_num] in left :
                    for i in range(0,5) :
                        can1.move( coin_list[button_num] ,-a ,0 )
                        master.update()
                        time.sleep(.001)

                # move coin to right
                
                else :
                    for i in range(0,5) :
                        can1.move( coin_list[button_num] ,a ,0 )
                        master.update()
                        time.sleep(.001)

            # movement of coin at snake
            
            if button_var[button_num] in snakeHeads :

                snake_num = snakeHeads.index(button_var[button_num])
                button_var[button_num] += snakeTails[snake_num][2]
                can1.move( coin_list[button_num] ,snakeTails[snake_num][0] ,snakeTails[snake_num][1] )

            # movement of coin at ladder
             
            if button_var[button_num] in ladderBottoms :

                snake_num = ladderBottoms.index(button_var[button_num])
                button_var[button_num] += ladderTops[snake_num][2]
                can1.move( coin_list[button_num] ,ladderTops[snake_num][0] ,ladderTops[snake_num][1] )        

            # indicating player's response
            
            var.set(1)

        
        while True :

            # variable for waiting player's response
            
            var = IntVar()
            
            for t in range(len(button_list)) :

                var.set(0)

                # disabling other players' chances
                
                for x in button_list :

                    if t == button_list.index(x) :

                        x['state'] = NORMAL
                        x['bg'] ="#00ff12"
                        continue

                    x["state"] = DISABLED
                    x['bg'] = "grey"
                    
                # waiting for player's response
                
                button_list[t].wait_variable(var)
                
    # accepting number of players
        
    button1 = Button(master1,text="ok",pady=10,height=1,width=10,font=50,command=select_num_players)
    
    button1.grid(row=2,column=1)

    master1.mainloop()

    # start button creation
    
start = Button(master,text="start",command=start,pady=2,height=1,width=10,font=50,bg= "green")
start.grid(row=1,column=1)

    # exit button creation
    
exit1 = Button(master,text="exit",command=exit1,pady=2,height=1,width=10,font=50,bg="red")
exit1.grid(row=1,column=2)

    # bottom canvas creation
    
canvasBottom = Canvas(master,height=50,width=500)
canvasBottom.grid(row=10,column=2,columnspan=4)
imgBottom = PhotoImage(file="last.png")
img_Bottom = canvasBottom.create_image(0,0,anchor=NW,image = imgBottom )


master.mainloop()



