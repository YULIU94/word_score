Word Pair Problem
=================

The Basics
----------
Given a list of words, find a pair with the highest score. The score is
determined by multiplying the lengths of the words by one another. For instance:
<pre>
[Spoke, Branch] = 30
   5   *   6    = 30
</pre>
With the exception that if the words share any letters in common then the pair's score is zero. For
instance, the following pair yields a score of 0 because both words contain the
letter 'r' :
<pre>
[Sh<b><i>r</i></b>ink, B<b><i>r</i></b>anch] = 0
</pre>

Some Details
-----------
- Your method should return a single pair of words.
- In the event that multiple pairs tie for the highest score...
  - Any of these pairs is an acceptable answer
  - Pick one and only one, don't return a list of pairs
- Zero, while the lowest possible score, **is** a valid score
- Your method signatures and return values should match our template

How You'll Be Judged
--------------------
- Performance
  - Achieving the fastest runtime possible should be your primary goal
     - Your solution's runtime against the example list provided (~110K words) is a good benchmark...
      - Acceptable solutions will find the result in less than 60 seconds
      - Good solutions will take less than 10 seconds
      - Great solutions, less than 5 seconds
      - Our in-house solution runs in 2.1 seconds
  - Minimizing memory usage is a secondary concern, but still important
    - No brackets here, but keeping it under a gigabyte when running against the supplied 110K
      words is probably a good idea.
- Code readability
  - Comments are good
  - Self-describing code is better
  - Generally speaking, your code should be easy for another engineer to follow

The Sample Input
----------------
- Included as a text file
  - Named 'words_en.txt'
  - Contains ~110K words
  - One word per line
