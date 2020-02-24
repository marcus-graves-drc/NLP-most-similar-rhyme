1. Install requirements
    1. `pip install -r requirements.txt`
2. Download nltk librariers
    1. `python -m nltk.downloader all` 
3. Run script
    1. `import main`
    2. `rhyme_similarity('fight', 2)`
    
```
from main import rhyme_similarity
rhyme_similarity('fight', 2)

>> ('fight', 1.0)
   ('invite', 0.125)
   ('slight', 0.125)
   ('rite', 0.125)
   ('mite', 0.1)
   ('night', 0.1)
   ('sprite', 0.1)
   ('tonight', 0.1)
   ('flight', 0.1)
   ('rewrite', 0.1)
   ('right', 0.09090909090909091)
   ('plight', 0.09090909090909091)
   ('sight', 0.09090909090909091)
   ('wight', 0.09090909090909091)
   ('byte', 0.09090909090909091)
   ('fright', 0.09090909090909091)
   ('delight', 0.09090909090909091)
   ('height', 0.09090909090909091)
   ('sleight', 0.09090909090909091)
   ('cite', 0.08333333333333333)
   ('spite', 0.07692307692307693)
   ('wright', 0.07692307692307693)
   ('knight', 0.07142857142857142)
   ('bight', 0.07142857142857142)
   ('reit', 0.07142857142857142)
   ('site', 0.07142857142857142)
   ('blight', 0.07142857142857142)
   ('kite', 0.06666666666666667)
   ('bite', 0.06666666666666667)
   ('light', 0.058823529411764705)
```

# Parameters
`rhyme_similarity(a,b,c=True)`
* where `a` is the string you want to find rhymes for
* where `b` is the position of the syllable in `a` which you want to find rhymes for
    * note: position is reversed. So when `a='fighter'` and `b=3` we are looking for words which rhyme with the syllable "igh"
* where `c` is an optional param for printing out the list (helpful for debugging or running in shell)
    * pass `c=True` to print, defaults to False

# Return 
Returns a list of words which rhyme with a, sorted by a similarity score of how likely the two words are to be used together.