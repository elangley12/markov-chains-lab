"""Generate Markov text from text files."""
import random
from random import choice



def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()               # open and read file and return as a string
    
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()

    for i in range(len(words) - 2):
        key = (words[i], words[i+1])
        if key in chains: 
            chains[key].append(words[i+2])
        else: 
            chains[key] = [words[i+2]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # links = {}

    # for chain in chains:
    #     for i in range(len(chain) - 2):
    #         link = tuple(chain[i:i+2])

    #         if link in links: 
    #             links[link].append(chain[i+2])
    #         else:
    #             links[link] = [chain[i+2]]
    #random_link 
    # print(":")
    # print(links.keys())
    
    # print(type(links.keys()))
    links = list(chains.keys())

    # words.extend(link)
    # links 
    
    for link in links:
        next_word = random.choice(chains[link])  
        words.append(next_word)
    #     link = tuple(words[-2:])
        

    return ' '.join(words)
    


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
