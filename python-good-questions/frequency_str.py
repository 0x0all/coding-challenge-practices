import string
import collections

input_text = """In bed we concocted our plans for the morrow. But to my
surprise and no small concern, Queequeg now gave me to understand, that
he had been diligently consulting Yojo, the name of his black little god,
and Yojo had told him two or three times over, and strongly insisted upon
it everyway, that instead of our going together among the whaling-fleet in
harbor, and in concert selecting our craft; instead of this, I say, Yojo
earnestly enjoined that the selection of the ship should rest wholly with
me, inasmuch as Yojo purposed befriending us; and, in order to do so, had
already pitched upon a vessel, which, if left to myself, I, Ishmael, should
infallibly light upon, for all the world as though it had turned out by
chance; and in that vessel I must immediately ship myself, for the present
irrespective of Queequeg.

I have forgotten to mention that, in many things, Queequeg placed great
confidence in the excellence of Yojo's judgment and surprising forecast of
things; and cherished Yojo with considerable esteem, as a rather good sort
of god, who perhaps meant well enough upon the whole, but in all cases did
not succeed in his benevolent designs."""

def word_freq(input_text):
    """ Performs a frequency count of words in a block of text
        Input:
            input_text : block of text
        Output:
            dictionary. keys are the unique words in the text
            values are the count of those words
    """
    return collections.Counter([x.strip(string.punctuation).lower() for x in list(input_text.split())])

def top_N(word_dict, N=5):
    """ Selects the N most frequent words (i.e., the words
        with the highest count) from the word count dictionary
        Input:
            word_dict : dict returned by word_freq()
            N : number of items to select. Defaults to 5
        Output:
            list of tuples. Each tuple is (word, count). E.g., ('coconut', 42)
    """
    values = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    return values[:N]


if __name__ == '__main__':
    word_dict = word_freq(input_text)
    print top_N(word_dict)
