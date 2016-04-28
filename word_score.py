'''
    word_score.py
    
    An implementation of the word score problem
    Cognius Programming challenge
'''
import sys
import time
from os import path

###### HELPER CLASS ##########
class Timer: 
    ''' Timer utility class '''      
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
        
WORDS_TO_SCORE = (
    "something",
    "red",
    "anything",
    "green",
    "mother",
    "yellow",
    "father",
    "blue",
    "foo",
    "purple",
    "bar",
    "orange",
    "baz",
    "black",
    "white",
)

def load_and_parse_words(file_name):
    ''' Read file from input 
        @param: str - file_name
        @rtype: List[str] - list of strings
    '''
#    file_name = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin 
    all_words_list = []
    if path.isfile(file_name):
        with open(file_name, 'r') as f:
            for line in f:
                if line:
                    all_words_list.append(line.rstrip())
    else:
        print '[ERROR] - File does not exist'
    return all_words_list

def score_word_pair(w1, w2):
    ''' 
        Return the score of two words
        @param: str - w1
        @param: str - w2
        @rtype: int - score of w1 and w2
        i.e multiply the lengths of both words by one another. 
        For instance:
        [Spoke, Branch] = 30
            5   *   6    = 30
    '''
    # if we do not have a valid score return -1
    return len(w1) * len(w2) if w1 and w2 else -1

def get_highest_scoring_pair(words):
    ''' 
        Get a pair of words with the highest scoring chance
        @param: List[str] - words
        Core algorithm: 
                Since highest score is based on length of words and uniqueness
                of comprising characters in string, we can use this to our advantage.
                If we can sort the words based on length in descending order, 
                then we do not need to traverse the entire list to find pairs that.
                  
                We simply filter out bad candidates that share characters between themselves.
                The moment we find a pair with no similiar characters, that's our highest
                scoring word pair.
    '''
    if not words:
        return [None, None]
    
    words = sorted(words, key=len, reverse=True)
    prev = words[0]
    for i in xrange(1, len(words)):
        cur = words[i]
        if not filter(lambda x: x in prev, cur):
            return [prev, cur]
        prev = cur
if __name__ == "__main__":
    with Timer() as t:
        # Accept input file as argument or use provided words_en.txt
        input_file_name = 'words_en.txt'
        if len(sys.argv) > 1:
            input_file_name = sys.argv[1]  
        all_input_words = load_and_parse_words(input_file_name)
        best_pair = get_highest_scoring_pair(all_input_words)
        best_score = score_word_pair(*best_pair)

        print "\n\nHighest scoring pair of words is '{0[0]}' and '{0[1]}' with a score of {1}.\n\n".format(best_pair, best_score)
    print 'Process took {0:.3f} sec.'.format(t.interval)
    
    

