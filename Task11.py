text = input("Enter a word or sentence: ").lower()
vowels = 0
consonants = 0
vowel_set = "aeiou"
for char in text:
    if char.isalpha():
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 
print("\nVowels:", vowels)
print("Consonants:", consonants)
