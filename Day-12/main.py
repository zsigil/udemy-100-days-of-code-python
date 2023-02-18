################### Scope ####################

# modifying global scope

enemies = 1

def increase_enemies():
  global enemies #avoid modifying global scope!
  enemies += 2 
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


#use this instead, do not modify global variable in function!
def decrease_enemies():
  return enemies-1

enemies = decrease_enemies()


#global constants
#all uppercase
PI = 3.1416