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

def score_word_pair(w1, w2):
    pass

def get_highest_scoring_pair(words):
    pass

if __name__ == "__main__":
    best_pair = get_highest_scoring_pair(WORDS_TO_SCORE)
    best_score = score_word_pair(*best_pair)

    print("\n\nHighest scoring pair of words is '{0[0]}' and '{0[1]}' with a score of {1}.\n\n".format(best_pair, best_score))

