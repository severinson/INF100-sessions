'''Assignment 4 template solution.

'''

def iscapitalized(s):
    '''return True if s is capitalized.'''
    if not isinstance(s, str):
        raise TypeError('s must be a string')
    if len(s) == 0:
        return False
    return s[0].isupper()

def capitalize(s):
    '''return s with its first letter capitalized.'''
    if not isinstance(s, str):
        raise TypeError('s must be a string')
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s[0].upper()
    return s[0].upper() + s[1:]

def endswidth(s, ending):
    '''return True if s ends with ending and False otherwise.'''
    if s[-len(ending):] == ending:
        return True
    return False

def l33tify_replace(result):
    '''replace norm-speak words with corresponding leet-speak'''
    result = result.replace("elite", "leet")
    result = result.replace("for the win", "ftw")
    result = result.replace("hacker", "haxzor")
    result = result.replace("you", "joo")
    result = result.replace("oh well", "meh")
    result = result.replace("newcomer", "noob")
    result = result.replace("the", "teh")
    result = result.replace("oh my god", "zoMG!!!11!")
    result = result.replace("no way", "nowai")
    result = result.replace("strong", "stronk")
    result = result.replace("good luck", "gl")
    result = result.replace("have fun", "hf")
    return result

def l33tify_ending(result):
    '''add leet word endings'''
    if endswidth(result, 'er'):
        result = result[:-2] + 'xor'
    elif endswidth(result, 'e'):
        result = result[:-1] + 'zor'
    elif endswidth(result, 'ed'):
        result = result[:-2] + '\'d'
    return result

def l33tify(norm_speak):
    '''convert the string norm_speak from normal speak into
    l33t sp34k.

    '''
    # input validation
    if not isinstance(norm_speak, str):
        raise TypeError('norm_speak must be a string')

    # input normalization
    result = norm_speak.lower()

    # replace with leet-speak words
    result = l33tify_replace(result)

    # handle word endings
    result = l33tify_ending(result)

    # handle capitalization
    if iscapitalized(norm_speak):
        result = capitalize(result)
        if result == 'Gl':
            result = 'GL'
        elif result == 'Hf':
            result = 'HF'
        elif result == 'Ftw':
            result = 'FTW'

    return result

def del33tify_replace(result):
    '''replace leet-speak words with corresponding norm-speak'''
    result = result.replace("leet", "elite")
    result = result.replace("ftw", "for the win")
    result = result.replace("haxzor", "hacker")
    result = result.replace("joo", "you")
    result = result.replace("meh", "oh well")
    result = result.replace("noob", "newcomer")
    result = result.replace("teh", "the")
    result = result.replace("zomg!!!11!", "oh my god")
    result = result.replace("nowai", "no way")
    result = result.replace("stronk", "strong")
    result = result.replace("gl", "good luck")
    result = result.replace("hf", "have fun")
    return result

def del33tify_ending(result):
    '''remove leet endings'''
    if endswidth(result, 'xor'):
        result = result[:-3] + 'er'
    elif endswidth(result, 'zor'):
        result = result[:-3] + 'e'
    elif endswidth(result, '\'d'):
        result = result[:-2] + 'ed'
    return result

def del33tify(leet_speak):
    '''convert the string l33t_speak from l33t sp34k into
    normal speak.

    '''
    # input validation
    if not isinstance(leet_speak, str):
        raise TypeError('leet_speak must be a string')

    # input normalization
    result = leet_speak.lower()

    # replace with norm-speak words
    result = del33tify_replace(result)

    # handle word endings
    result = del33tify_ending(result)

    # handle capitalization
    if iscapitalized(leet_speak):
        result = capitalize(result)

    return result

# getting ahead
def l33tify_many(norm_speak):
    '''convert the string norm_speak containing several words
    from normal speak into l33t sp34k.

    '''
    result = norm_speak.lower()
    result = l33tify_replace(result)
    words = list()
    for word in result.split(' '):
        leet_word = l33tify_ending(word)
        leet_word += ' '
        words.append(leet_word)
    result = ''.join(words) # strip extra whitespace
    result = result.strip()
    return result

def del33tify_many(leet_speak):
    '''convert the string l33t_speak containing several words
    from l33t sp34k into normal speak.

    '''
    result = leet_speak.lower()
    words = list()
    for word in result.split(' '):
        norm_word = del33tify_ending(word)
        norm_word += ' '
        words.append(norm_word)
    result = ''.join(words)
    result = result.strip() # strip extra whitespace
    result = del33tify_replace(result)
    return result
