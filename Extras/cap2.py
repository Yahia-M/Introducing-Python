
def just_do_it(text):
    """
    >>> just_do_it('a flock of ducks')
    'A Flock Of Ducks'
    """
    return text.capitalize()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
