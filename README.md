# Potion Maker

i'm a dm for a dnd campaign (realistically, it's homebrewed pathfinder). my players are deeply obsessed with looting fallen enemies, chests, and drawers. it gets kinda lame if they only find the same 50 preset potions, so i've decided to make a randomizer. the generic description is that the players can find potions, powders, pastes and gels with special effects.

this is **HEAVILY inspired** by [this post on reddit](https://reddit.com/r/DnDBehindTheScreen/comments/4btnkc/random_potions_table/). i really loved the concept of this post, but i hated the idea of having to slow down our already *really* long sessions by rolling a bunch of dice over and over again for all four of my players. because it's inspired by another person's post and because i love the idea of collaborative efforts, this code is totally public and free to use, even when i end up making this into an app. it's more of a passion project than anything.
just be cool about it!

***

## Short Term Plans
- [ ] remove unnecessary comments/files/functions/etc.
- [ ] add items to lists in: Colors, Containers, Effect, HasChunks, Senses, Textures
- [ ] make a file for preset potions and include that possibility in XTESTING

## Long Term Plans
- [ ] create UI for Web Application.
- [ ] use Android Studio to make an Android phone application.
- [ ] allow user to determine the highest number of dice rolls.

***

## File List (Alphabetical Order)
### Accuracy.py
> randomly decides if the item's given name and effect is accurate.
> there's a 10% chance that the user has to roll 1d100 and beat a random DC.

### Colors.py
> randomly decides the main color of the item. The item has a chance of having two colors.
> dependent on [Form.py](###Form.py)

### Containers.py
> the item can be an ingestible potion, a splash potion, a small liquid, a powder, or a paste/gel.
> dependent on [Form.py](###Form.py)

### Description.py
> if the label is legible, randomly determines if the item has a description of the effects, may have a generic sublabel, or no label at all.

### DiceRoll.py
> randomly decides the dice roll for bonus/penalty. maximum number of rolls is the player level.
> currently have it set between 1 and 5 rolls because my players are at level 5.

### Effect.py
> randomly decides the effect that the item has.

### EffectLength.py
> randomly decides how long the effect lasts.
> there is a 60% chance that it lasts all day; a 10% chance that it lasts a random number dice rolls of rounds/hours/days; and a 10% chance that it lasts a random number of rounds/hours/days.

### Form.py
> determines the form of the item: liquid (ingestible, splash, droplet), powder (puff, sprinkle, edible, ingredient), paste, or gel.

### FullLabel.py
> determines the verbiage of the sentence declaring the title if the label is legible. titles may be "TITLE of EFFECT" or "EFFECT TITLE".
> dependent on [Title.py](###Title.py) and [Effect.py](###Effect.py).

### HasChunks.py
> randomly decides if the item has chunks of something in it.

### HasLabel.py
> randomly decides if the item has a label on it.
> if the item is a droplet liquid, there is a randomized perception DC. if the item has a label, randomly decides if the label is legible.
> dependent on [Containers.py](###Containers.py)

### Senses.py
> randomly decides the smell and taste of the item and how strong it is. makes sure that, if the randomly decided taste is the same as the smell, it doesn't repeat itself.

### ServingSize.py
> determines how many servings the item is (aka how many times it can be used).

### Textures.py
> determines the texture of the item when ingested (as a potion or powder) or touched (as a gel or paste).
> dependent on [Form.py](###Form.py)

### Title.py
> if the label is legible, randomly decides the title of the item based on the form it is (liquid, powder, paste, gel).
> dependent on [Form.py](###Form.py)

### XTESTING.py
> a file for testing the potential outcomes.
