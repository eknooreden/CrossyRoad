from time import sleep
from turtle import Screen
from bird import Bird
from level_tracker import LevelTracker
from cars_spawner import CarSpawner

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("gray")

bird = Bird()
carspawner = CarSpawner()
leveltracker = LevelTracker()

screen.listen()
screen.onkey(bird.go_forward, "Up" or "w")

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()

    carspawner.create_car()
    carspawner.move_cars()

    #Detect collision with car
    for car in carspawner.all_cars:
        if car.distance(bird) < 20:
            game_is_on = False
            leveltracker.game_over()

    #Detect succesful crossing
    if bird.is_at_finish_line():
        bird.go_to_start()
        carspawner.level_up()
        leveltracker.increase_level()

screen.exitonclick()