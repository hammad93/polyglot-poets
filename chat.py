from cobe.brain import Brain

def chat(text, b, learn = True) :
    '''
    Using the filename of the brain, b, this returns the 
    reply from the text. The learn boolean tells the 
    ai if it should learn from the text.
    '''
    brain = Brain(b)
    reply = brain.reply(text)

    if learn :
        brain.learn(text)
    
    return reply