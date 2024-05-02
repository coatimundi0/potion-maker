from random import randrange 
from random import choice

'''
CHUNKS
'''
has_chunks = ["It looks like it as something in it, too... it's ", "Oh? There's something in it. It looks like... ", "In it, there's "]
pieces = ["a tiny heart. Gross.", "a tiny eyeball. Disgusting.", "a fucking eyeball? Oh, god.", "some kind of dried meat. Hopefully nothing gross.", "bits of herbs.", "little fruit chunks. Like a jam!", "bits of fruit. Nice!", "some kind of scales...", "a whole leaf.", "a bay leaf. Is this a soup?", "some hair. Whose hair is that?", "a fingernail. Disgusting.", "some fur. Oh...", "fairy wings."]

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

def makeChunky():
    # chunky ::  Y/N
    chunky = choice([True, False])

    if chunky == bool(True):
        verbiage = has_chunks[randrange(0, len(has_chunks)-1)]
        is_chunky = pieces[randrange(0, len(pieces)-1)]
        phrase = verbiage + is_chunky
    elif chunky == bool(False):
        phrase = ""
    else: 
        print("makeChunky ERROR")
        return -1

    return phrase

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
