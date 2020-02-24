import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer


def rhyme(inp, level):
    entries = nltk.corpus.cmudict.entries()
    syllables = [(word, syl) for word, syl in entries if word == inp]
    rhymes = []
    for (word, syllable) in syllables:
        rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
    return set(rhymes)


def rhyme_similarity(inp, level, return_print=False):
    inp_synset = get_synset(inp)
    rhymes = rhyme(inp, level)
    r_w_sim = []
    for each in rhymes:
        try:
            r_sim = inp_synset.path_similarity(get_synset(each))
            if r_sim:
                r_w_sim.append((each, r_sim))
            else:
                r_w_sim.append((each, 0))
        except Exception:
            r_w_sim.append((each, 0))
    sorted_rhymes = sorted(r_w_sim, key=lambda x: x[1], reverse=False)
    if return_print:
        for i in sorted_rhymes:
            print(i)
    return sorted_rhymes


def get_synset(word_str):
    pos = nltk.pos_tag(nltk.word_tokenize(word_str))
    lemmatzr = WordNetLemmatizer()
    for token in pos:
        wn_tag = penn_to_wn(token[1])
        if not wn_tag:
            continue
        lemma = lemmatzr.lemmatize(token[0], pos=wn_tag)
        synset = wn.synsets(lemma, pos=wn_tag)
        if not synset:
            continue
        return synset[0]


def penn_to_wn(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None
