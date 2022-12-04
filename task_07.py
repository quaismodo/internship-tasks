def combine_anagrams(words_array):
    pair_list = [[''.join(sorted(word.lower())), word] for word in words_array]
    anagrams_dict = {}
    for pair_words in pair_list:
        if pair_words[0] in anagrams_dict:
            anagrams_dict[pair_words[0]].append(pair_words[1])
        else:
            anagrams_dict[pair_words[0]] = [pair_words[1]]
    return list(anagrams_dict.values())


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
