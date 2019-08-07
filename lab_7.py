import turtle
import random
import time

turtle.tracer(1,0) 
UP_EDGE = 400
DOWN_EDGE = -400
RIGHT_EDGE = 400
LEFT_EDGE = -400

SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 2
TIME_STEP = 1000


pos_list = []
stamp_list = []
food_pos = []
food_stamps = []



stamp2_list=[]
pos_list2=[]
snake2=turtle.clone()
snake2.shape('square')
snake2.goto(10,0)
snake = turtle.clone()
snake.shape("square")
snake.goto(-10,0)
turtle2=turtle.Turtle()
turtle.penup()
turtle2.penup()
turtle.goto(-400,-400)
turtle.pendown()
turtle.goto(-400,400)
turtle.goto(400,400)
turtle.goto(400,-400)
turtle.goto(-400,-400)
turtle.penup()
turtle.goto(0,425)
style=("courier",60,'italic')
style3=("courier",28,'italic')
turtle.write("Save The Earth",False,"center",style)
style2=("courier",20,'italic')
turtle2.goto(0,-450)
turtle2.write("Score :0",False,"center",style2)
turtle2.hideturtle()
score1=[]
turtle.hideturtle()

fact=turtle.Turtle()
fact.hideturtle()
def facts():
    if len(score1)==5:
        fact.penup()
        fact.goto(0,360)
        fact.write("Springs are getting earlier :",False,"center",("Arial", 18, "normal"))
        fact.goto(0,340)
        fact.write("flowering dates advanced 7.3 days between 1936 and 1998",False,"center",("Arial", 18, "normal"))
        time.sleep(3)
        fact.clear()
    elif len(score1)==10:
        fact.penup()
        fact.goto(0,360)
        fact.write("At least 70 species of frogs have become extinct",False,"center",("Arial", 18, "normal"))
        fact.goto(0,340)
        fact.write("due to inceased temperatures",False,"center",("Arial", 18, "normal"))
        time.sleep(3)
        fact.clear()
    
    elif len(score1)==15:
        fact.penup()
        fact.goto(0,360)
        fact.write("Until 2007 the USA was the biggest emitter of greenhouse gases.",False,"center",("Arial", 18, "normal"))
        fact.goto(0,340)
        fact.write("Now China has overtaken them",False,"center",("Arial", 18, "normal"))
        time.sleep(3)
        fact.clear()
        
    elif len(score1)==20:
        fact.penup()
        fact.goto(0,360)
        fact.write("The last two decades of the 20th century ",False,"center",("Arial", 18, "normal"))
        fact.goto(0,340)
        fact.write("were the hottest in 400 years",False,"center",("Arial", 18, "normal"))
        time.sleep(3)
        fact.clear()
        
    elif len(score1)==25:
        fact.penup()
        fact.goto(0,360)
        fact.write("Emperor penguins have dropped from 300 breeding pars ",False,"center",("Arial", 18, "normal"))
        fact.goto(0,340)
        fact.write(" to jast 9 in the western Antarctic peninsula",False,"center",("Arial", 18, "normal"))
        time.sleep(3)
        fact.clear()
        
    elif len(score1)==30:
        fact.penup()
        fact.goto(0,360)
        fact.write("The numbe of nurricanes that develop each year has more then",False,"center",("Arial", 18, "normal"))
        fact.goto(0,340)
        fact.write("douled in thelast century as sea-surtace temperatures rise",False,"center",("Arial", 18, "normal"))
        time.sleep(3)
        fact.clear()
        
    elif len(score1)==35:
        fact.penup()
        fact.goto(0,360)
        fact.write("Coral reefs highly sensitive to temperature changes,",False,"center",("Arial", 18, "normal"))
        fact.goto(0,340)
        fact.write("suffered bleach increased warmth",False,"center",("Arial", 18, "normal"))
        fact.sleep(3)
        fact.clear()
        
    elif len(score1)==40:
        fact.penup()
        fact.goto(0,360)
        fact.write("Only about 8% of global energy comes ",False,"center",("Arial", 18, "normal"))
        fact.goto(0,340)
        fact.write("sources The remaining 92% comes from ",False,"center",("Arial", 18, "normal"))
        fact.goto(0,380)
        fact.write("non-venewables predominantly fossil fuels",False,"center",("Arial", 18, "normal"))
        fact.sleep(3)
        fact.clear()
    elif len(score1)==45:
        fact.penup()
        fact.goto(0,360)
        fact.write("The annual rate of sea level rise over the ",False,"center",("Arial", 18, "normal"))
        fact.goto(0,340)
        fact.write("past 20 years has been 0.13 inches a year-twice the fast than the last 80 years",False,"center",("Arial", 18, "normal"))
        time.sleep(3)
        fact.clear()
    elif len(score1)==50:
        fact.penup()
        fact.goto(0,360)
        fact.write("The world health organizantion arlready attributes",False,"center",("Arial", 18, "normal"))
        fact.goto(0,340)
        fact.write("150,000 deaths per year to climate change",False,"center",("Arial", 18, "normal"))
        time.sleep(3)
        fact.clear()

def new_stamp():
    snake_pos = snake.pos()
    pos_list.append(snake_pos)        
    snake_stamp = snake.stamp()     
    stamp_list.append(snake_stamp)


for i in range(START_LENGTH) :
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    
    x_pos+=SQUARE_SIZE 

    snake.goto(x_pos,y_pos) 
       
    
    new_stamp()
def remove_tail():
    old_stamp = stamp_list.pop(0) 
    snake.clearstamp(old_stamp) 
    pos_list.pop(0) 

snake.direction="Up"
def up():
    if snake.direction!="Down":
        snake.direction="Up" 
def down():
    if snake.direction!="Up":
        snake.direction="Down" 
def right():
    if snake.direction!="Left":
        snake.direction="Right"
    
def left():
    if snake.direction!="Right":
        snake.direction="Left"


turtle.onkeypress(up,"Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")




























turtle.listen()
turtle.register_shape("trash.gif")
turtle.register_shape("Lose.gif")

food = turtle.clone()
food.shape("trash.gif")


food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
food.hideturtle()


for this_food_pos in food_pos :
    food.goto(this_food_pos)
    food_stamp=food.stamp()
    food_stamps.append(food_stamp)


def make_food():
    min_x=-int(SIZE_X/3/SQUARE_SIZE)+2
    max_x=int(SIZE_X/3/SQUARE_SIZE)-2
    min_y=-int(SIZE_Y/3/SQUARE_SIZE)+2
    max_y=int(SIZE_Y/3/SQUARE_SIZE)-2
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food_random=(food_x,food_y)
    food.goto(food_random)
    food_pos.append(food_random)
    food_randoms=food.stamp()
    food_stamps.append(food_randoms)

def new_stamp2():
    snake2_pos = snake2.pos()
    pos_list2.append(snake2_pos)        
    snake2_stamp = snake2.stamp()
    print(snake2_stamp)
    stamp2_list.append(snake2_stamp)
    print(stamp2_list)

for i in range(START_LENGTH) :
    x_pos2=snake2.pos()[0]
    y_pos2=snake2.pos()[1]

    
    x_pos2+=SQUARE_SIZE 

    snake2.goto(x_pos2,y_pos2) 
       
    
    new_stamp2()
def remove_tail2():
    print(pos_list2)
    old2_stamp = stamp2_list.pop(0) 
    snake2.clearstamp(old2_stamp) 
    pos_list2.pop(0) 

snake2.direction="Up2"
def up2():
    if snake2.direction!="Down2":
        snake2.direction="Up2" 
def down2():
    if snake2.direction!="Up2":
        snake2.direction="Down2" 
def right2():
    if snake2.direction!="Left2":
        snake2.direction="Right2"
    
def left2():
    if snake2.direction!="Right2":
        snake2.direction="Left2"


turtle.onkeypress(up2,"w")
turtle.onkeypress(down2, "s")
turtle.onkeypress(right2,"d")
turtle.onkeypress(left2,"a")

def move_snake2():
    global TIME_STEP
    my_pos2 = snake2.pos()
    x_pos2 = my_pos2[0]
    y_pos2 = my_pos2[1]
    #eats the food
    if snake2.pos() in food_pos:
        food_index=food_pos.index(snake2.pos()) 
        food.clearstamp(food_stamps[food_index]) 
        food_pos.pop(food_index) 
        food_stamps.pop(food_index)
        score1.append(1)
        turtle2.clear()
        randomNumber = random.randint(0,5)
        myColorList = ["red","green","black","purple","blue","yellow"]
        new_color=myColorList[randomNumber]
        snake2.color(new_color)
        turtle2.write("Score :"+str(len(score1)),False,'center',style2)
        if TIME_STEP>=1:
            TIME_STEP-=1
        facts()
    
    new_pos2 = snake2.pos()
    new_x_pos2 = new_pos2[0]
    new_y_pos2 = new_pos2[1]
    if snake2.direction == "Up":
            snake2.goto(x_pos2, y_pos2 + SQUARE_SIZE)
    elif snake2.direction=="Down":
            snake2.goto(x_pos2, y_pos2 - SQUARE_SIZE)

    elif snake2.direction=="Left":
            snake.goto(x_pos2-SQUARE_SIZE,y_pos2)
    elif snake.direction=="Right":
             snake.goto(x_pos2+SQUARE_SIZE,y_pos2)

    
    if new_x_pos2 >= RIGHT_EDGE:
        print(len(pos_list))
        print("You hit the right edge! Game over!")
        turtle2.clear()
        turtle.showturtle()
        turtle.goto(0,0)
        turtle.shape("Lose.gif")
        turtle2.goto(0,200)
        print('ewjkfgsakfsjfgsjagfkjaseggsfsefghsefjsgaejfgjsefgsfdkshfmsefhjsfjhdbsf')
        turtle2.write("You have let world be consumed by polution",False,"center",style3)
        quit()
    elif new_x_pos2<=LEFT_EDGE:
        print(len(pos_list))
        print("You hit the left edge! Game over!")
        turtle2.clear()
        turtle.showturtle()
        turtle.goto(0,0)
        turtle.shape("Lose.gif")
        turtle2.goto(0,200)
        print('123456789')
        turtle2.write("You have let world be consumed by polution",False,"center",style3)
        quit()
    elif new_y_pos2>=UP_EDGE:
        print(len(pos_list))
        print("You hit the left edge! Game over!")
        turtle2.clear()
        turtle.showturtle()
        turtle.goto(0,0)
        turtle.shape("Lose.gif")
        turtle2.goto(0,200)
        print(')()()()()()(')
        turtle2.write("You have let world be consumed by polution",False,"center",style3)
        quit()
    elif new_y_pos2<=DOWN_EDGE:
        print(len(pos_list))
        turtle2.clear()
        turtle.showturtle()
        turtle.goto(0,0)
        turtle.shape("Lose.gif")
        turtle2.goto(0,200)
        print('this')
        turtle2.write("You have let world be consumed by polution",False,"center",style3)
        quit()
        print("You hit the left edge! Game over!")


        
    if len(food_stamps)<1 :
                make_food()
    if new_pos2 in pos_list2[:-1]:
        print(len(pos_list))
        turtle2.clear()
        turtle.showturtle()
        turtle.goto(0,0)
        turtle.shape("Lose.gif")
        turtle2.goto(0,200)
        print('hellllloooowwww')
        turtle2.write("You have let world be consumed by pollution",False,"center",style3)
        quit()
    if score1==50:
        turtle.goto(0,0)
        turtle.showturtle()
        turtle.shape("earth.gif")
        turtle2.goto(0,150)
        turtle2.write("Congratulations you have saved the environment",False,"center",style3)

    new_stamp2()
    turtle.ontimer(move_snake2,TIME_STEP)
    remove_tail2()
    









































def move_snake():
    global TIME_STEP
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    #eats the food
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) 
        food.clearstamp(food_stamps[food_index]) 
        food_pos.pop(food_index) 
        food_stamps.pop(food_index)
        score1.append(1)
        turtle2.clear()
        randomNumber = random.randint(0,5)
        myColorList = ["red","green","black","purple","blue","yellow"]
        new_color=myColorList[randomNumber]
        snake.color(new_color)
        turtle2.write("Score :"+str(len(score1)),False,'center',style2)
        if TIME_STEP>=1:
            TIME_STEP-=1
        facts()
    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if snake.direction == "Up":
            snake.goto(x_pos, y_pos + SQUARE_SIZE)
    elif snake.direction=="Down":
            snake.goto(x_pos, y_pos - SQUARE_SIZE)

    elif snake.direction=="Left":
            snake.goto(x_pos-SQUARE_SIZE,y_pos)
    elif snake.direction=="Right":
             snake.goto(x_pos+SQUARE_SIZE,y_pos)

    
    if new_x_pos >= RIGHT_EDGE:
        print(len(pos_list))
        print("You hit the right edge! Game over!")
        turtle2.clear()
        turtle.showturtle()
        turtle.goto(0,0)
        turtle.shape("Lose.gif")
        turtle2.goto(0,200)
        turtle2.write("You have let world be consumed by polution",False,"center",style3)
        quit()
    elif new_x_pos<=LEFT_EDGE:
        print(len(pos_list))
        print("You hit the left edge! Game over!")
        turtle2.clear()
        turtle.showturtle()
        turtle.goto(0,0)
        turtle.shape("Lose.gif")
        turtle2.goto(0,200)
        turtle2.write("You have let world be consumed by polution",False,"center",style3)
        quit()
    elif new_y_pos>=UP_EDGE:
        print(len(pos_list))
        print("You hit the left edge! Game over!")
        turtle2.clear()
        turtle.showturtle()
        turtle.goto(0,0)
        turtle.shape("Lose.gif")
        turtle2.goto(0,200)
        turtle2.write("You have let world be consumed by polution",False,"center",style3)
        quit()
    elif new_y_pos<=DOWN_EDGE:
        print(len(pos_list))
        turtle2.clear()
        turtle.showturtle()
        turtle.goto(0,0)
        turtle.shape("Lose.gif")
        turtle2.goto(0,200)
        turtle2.write("You have let world be consumed by polution",False,"center",style3)
        quit()
        print("You hit the left edge! Game over!")


        
    if len(food_stamps)<1 :
                make_food()
    if new_pos in pos_list[:-1]:
        print(len(pos_list))
        turtle2.clear()
        turtle.showturtle()
        turtle.goto(0,0)
        turtle.shape("Lose.gif")
        turtle2.goto(0,200)
        turtle2.write("You have let world be consumed by pollution",False,"center",style3)
        quit()
    if score1==50:
        turtle.goto(0,0)
        turtle.showturtle()
        turtle.shape("earth.gif")
        turtle2.goto(0,150)
        turtle2.write("Congratulations you have saved the environment",False,"center",style3)

    new_stamp()
    turtle.ontimer(move_snake,TIME_STEP)

    remove_tail()
move_snake()
move_snake2()


facts()
turtle.mainloop()






