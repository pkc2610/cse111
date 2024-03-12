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

def get_determiner(quantity):

    if quantity == 1:
        return random.choice(articless)
    else: 
        return random.choice(articlesp)

def get_noun(quantity):

    if quantity == 1:
        return random.choice(nounss)
    else: 
        return random.choice(nounsp)

def get_verb(quantity, tense):
     
    if quantity == 1 and tense == "past":
        return random.choice(vsinglepast)
    elif quantity == 1 and tense == "present":
        return random.choice(vsinglepres)
    elif quantity == 1 and tense == "future":
        return random.choice(vsinglefut)
    elif quantity <= 1 and tense == "past":
        return random.choice(vpluralpast)
    elif quantity <= 1 and tense == "present":
        return random.choice(vpluralpres)
    elif quantity <= 1 and tense == "future":
        return random.choice(vpluralfut)

def make_sentence(quantity, tense):
    det = get_determiner(quantity)
    nou = get_noun(quantity)
    ver = get_verb(quantity, tense)
    print(f"{det.capitalize()} {nou} {ver}.")

def main():
    quantity = int(input("How many people are in this sentence?"))
    tense=input("Is this in the past, present, or future?")
    make_sentence(quantity, tense)

main()