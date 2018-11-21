"""
classification of free text descriptions
"""

#-- Imports ---------------------------------------------------------------------

# Project specific
from woffle        import data
from woffle.models import spacy as model


#-- Definitions -----------------------------------------------------------------
def main():


    # load your data
    fp = 'data/test.txt'
    text = [i.replace('\n','') for i in open(fp, 'r').readlines()]
    if not text:
        raise ValueError("No descriptions to process")


    # compose your cleaning functions
    clean = compose( model.parse
                   , data.parse
                   )


    cleaned = [data.parse(line) for line in text]
    corpus  = [model.nlp(line) for line in cleaned]
    target = [word if word in model.nlp.vocab else None for word in cleaned]
    pairs = [(i,j) for i, j in zip(text, target)]

    print(pairs)



#-- Boilerplate -----------------------------------------------------------------
if __name__ == '__main__':
    main()
