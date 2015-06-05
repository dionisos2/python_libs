# some useful operation on string

def replace_special_char(string):
    return string
    special_char = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    without_special_char = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
    special_char += [x.upper() for x in special_char]
    without_special_char += [x.upper() for x in without_special_char]
    # special_char += ["<", "-", "'", ":", "’"]
    # without_special_char += ["a", "a", "a", "a", "a"]

    for (a, w_a) in zip(special_char, without_special_char):
        string = string.replace(a, w_a)

    return string
