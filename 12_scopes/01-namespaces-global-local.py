#scope and namespaces - local and global scope

############### scope ###############

#global scope - available to entire file
enemies = 1

def increase_enemies():
    #local scope only valid within the function
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")



def game():

### drink potion only available in the game walled garden
    def drink_potion():
        potion_stregnth = 2



##there is no such thing as block scope
#if and for statements do not count as fences.



####modify vars with global scope ######

##global scope
enemies = 1
def modify():
    #dont want to do it often because its confusing
    global enemies
    enemies += 1
    print(enemies)


##Global Constants - Uppcase variables
PI = 3.1415926
URL = "www.google.com"

