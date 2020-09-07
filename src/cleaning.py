import re

def cast(element):
    """Take an element and cast it into a string"""
    x=str(element)
    return x


def cleaning(word):
    """Using Redex, this function will search for a given parameter in a string and if it is there will substitute the string for 'Multi_player' or 'Single_player' if isn´t there will pass."""


    textobuscar='Multi'
    textobuscar2='Single'
    if re.search(textobuscar, word) is not None:
        word='Multi_player'
        return word
    elif re.search(textobuscar2, word) is not None:
        word='Single_player'
        return word
    else:
        pass


def clean(word):
    """Using Redex, this function will search for a given parameter in a string and if it is there will substitute the string, if isn´t there will pass."""


    action='Action'
    casual='Casual'
    adventure='Adventure'
    gore='Gore'
    rpg='RPG'
    strategy='Strategy' 
    racing='Racing'
    simulation='Simulation'
    sports='Sports'
    
    if re.search(action, word) is not None:
        word=action
        return word
    elif re.search(casual, word) is not None:
        word=casual
        return word
    elif re.search(adventure, word) is not None:
        word=adventure
        return word
    elif re.search(gore, word) is not None:
        word=gore
        return word
    elif re.search(rpg, word) is not None:
        word=rpg
        return word
    elif re.search(strategy, word) is not None:
        word=strategy
        return word
    elif re.search(racing, word) is not None:
        word=racing
        return word
    elif re.search(simulation, word) is not None:
        word=simulation
        return word
    elif re.search(sports, word) is not None:
        word=sports
        return word
    
    else:
        pass



def find_numbers(word):
    """Using Redex, this function will search for a given parameter in a string and if it is there  will return the integer else pass"""

    if re.search(r'\d+', word) is not None:
        num = int(re.search(r'\d+', word).group(0))
        word=num
        return word
    else:
        pass