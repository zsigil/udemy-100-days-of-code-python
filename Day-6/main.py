def my_function():
    print("Hello")
    print('Bye')

my_function()

#! Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
        
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

    
# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         jump()

#MAZE
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def go_right():
#     turn_right()
#     move()

# right_turns = 0;

# while not at_goal():
#     #go right if possible
#     if right_is_clear() and right_turns<4:
#         go_right()
#         right_turns +=1
#     #move straight if going right is not possible
#     elif not wall_in_front():
#         move()
#         right_turns = 0
#     #else turn left
#     else:
#         turn_left()
#         right_turns = 0