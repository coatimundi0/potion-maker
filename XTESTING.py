
from Containers import makeContainer
from HasLabel import makeLabel
from Title import makeTitle
from Accuracy import pickAccuracy
from Effect import determineLength
from FullLabel import makeFullTitle
from Description import makeDescription
from DiceRoll import effectLength
from EffectLength import makeTimePeriod
from Form import makeForm
from ServingSize import makeServings
from Colors import determineColors
from Textures import makeTexture
from HasChunks import makeChunky
from Senses import makeSmell, makeTaste

##### ##### ##### ##### ##### ##### ##### ##### ##### #####

form = makeForm()
container  = makeContainer(form)
has_label = makeLabel(container)
print(container[0] + " " + has_label[0])

if (has_label[1] == bool(True)):
    title = makeTitle(form)
    effect = determineLength()
    accuracy = pickAccuracy()
    full_title = makeFullTitle(title, effect)
    description = makeDescription()
    if description[1] == bool(True):
        dice = effectLength()
        time = makeTimePeriod()
        print(full_title + " " + description[0] + " Using this item " + effect[1] + " " + dice + " " + time + " " + accuracy + ")")
    else: 
        print(full_title + " " + description[0])
else:
    pass

    # form :: LIQUID (0)
if form[0] == 0:
    color = determineColors(form[0])
    chunks = makeChunky()
    servings = makeServings()
    smell = makeSmell()
    print(color + " " + chunks + " " + smell[0] + "\n" + form[1] + " " + servings)

    if form[2] == bool(True):
        texture = makeTexture(form[0])
        taste = makeTaste(smell)
        print(texture + " " + taste)
    else:
        pass

    # form :: POWDER (1)
elif form[0] == 1:
    color = determineColors(form[0])
    chunks = makeChunky()
    servings = makeServings()
    smell = makeSmell()
    print(color + " " + chunks + " " + smell[0] + "\n" + form[1] + " " + servings)

    if form[2] == bool(True):
        texture = makeTexture(form[0])
        taste = makeTaste(smell)
        print(texture + " " + taste)
    else:
        pass

    # form :: PASTE (2); GEL (3)
elif (form[0] == 2) or (form[0] == 3):
    color = determineColors(form[0])
    chunks = makeChunky()
    servings = makeServings()
    smell = makeSmell()
    texture = makeTexture(form[0])

    print(color + " " + chunks + "\n" + form[1] + " " + servings)
    print(texture + " " + smell[0])

else:
    pass

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
'''
print(container[0] + " " + has_label[0])

if has_label[1] == bool(True):
    if description[1] == 1:
        print(full_title + " " + description[0] + " Using this item " + effect[1] + " " + dice + " " + time + " " + accuracy + ")")
    else: 
        print(full_title + " " + description[0])
else:
    pass

    # form :: LIQUID (0); POWDER (1); PASTE (2); GEL (3)
if form[0] == 0:
    print(color + " " + chunks + " " + smell[0] + "\n" + form[1] + " " + servings)
    if form[2] == bool(True):
        print(texture + " " + taste)
    else:
        pass
elif form[0] == 1:
    print(color + " " + chunks + " " + smell[0] + "\n" + form[1] + " " + servings)
    if form[2] == bool(True):
        print(texture + " " + taste)
    else:
        pass
elif (form[0] == 2) or (form[0] == 3):
    print(color + " " + chunks + "\n" + form[1] + " " + servings)
    print(texture + " " + smell[0])
    pass
else:
    pass
'''
##### ##### ##### ##### ##### ##### ##### ##### ##### #####
