from copy import copy


##open snake scoreboard
with open("./01_snake/highscore.txt") as file:
    contents = file.read()
    print(contents)

# use . for current working directory
# use .. to back up one level
# can always use entire directory path to reference a file