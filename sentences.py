import random

articless = ["a", "the", "an", "one", "that"]

articlesp = ["the", "some", "those", "a few"]

nounss = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

nounsp = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

vsinglepast = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

vsinglepres = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

vsinglefut = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

vpluralpast = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

vpluralpres = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

vpluralfut = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]


word = random.choice(articless, articlesp)

cap_word = word.capitalize()

def get_determiner(quantity):

    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word

def get_noun(quantity):

    if quantity == 1:
        nooun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else: nooun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(nooun)

    return noun

def get_verb(quantity, tense):
     
    if quantity == 1:
        verb = random.choice(verbsp)
    else: 
        verb = random.choice(verbspr)

    return verb

def make_sentence(quantity, tense):
    get_determiner()
    get_noun()
    get_verb()