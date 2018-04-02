def vowel_count(s):
    vowels = 'aeiou'
    result = {}
    for i in s:
        for c in vowels:
            if c in s:
                result[c] = s.lower().count(c)
    return result
    # return {(c, s.lower().count(c)) for c in vowels for i in s if c in vowels}


print(vowel_count('awesome'))  # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie'))  # {'e': 2, 'i': 1}
print(vowel_count('Colt'))  # {'o': 1}
