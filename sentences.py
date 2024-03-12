import random

#"articles singular"
articless = ["a", "the", "an", "one", "that"]

#"articles plural"
articlesp = ["the", "some", "those", "a few"]

#"nouns singular"
nounss = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

#"nouns plural"
nounsp = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

#"verbs singular past tense"
vsinglepast = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

#"verbs singular present tense"
vsinglepres = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

#"verbs singular future tense"
vsinglefut = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

#"verbs plural past tense"
vpluralpast = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

#"verbs plural present tense"
vpluralpres = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

#"verbs plural future tense"
vpluralfut = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]


word = random.choice(articless, articlesp)

cap_word = word.capitalize()

def get_determiner(quantity):

    if quantity == 1:
        return articless
    else: 
        return articlesp

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