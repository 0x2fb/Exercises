def reverse_vowels(s):
    vowels = [i for i in s if i.lower() in 'aeiou']
    return ''.join((vowels.pop() if i.lower() in 'aeiou' else i for i in s))


print(reverse_vowels("Hello!"))  # "Holle!"
print(reverse_vowels("Tomatoes"))  # "Temotaos"
# "RivArsI Vewols en e Streng"
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))  # "uoiea"
print(reverse_vowels("why try, shy fly?"))  # "why try, shy fly?"
