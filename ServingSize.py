from random import randint

'''
SERVING SIZE
    It seems like this can be used [SERVINGS].
'''
# servings :: ONCE (0-69); TWICE (70-89); THRICE (90-99)

##### ##### ##### ##### ##### ##### ##### ##### ##### #####

def makeServings():
    servings = randint(0, 100)

    if 0 <= servings <= 69:
        size = "one time"
    elif 70 <= servings <= 89:
        size = "two times"
    elif 90 <= servings <= 100:
        size = "three times"
    else: 
        print("makeServings ERROR")
        return -1
    
    phrase = "It seems like this can be used " + size + "."
    return phrase