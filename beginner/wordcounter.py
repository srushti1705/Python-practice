sentence = input("Enter a sentence: ")

word_count = len(sentence.split()) 
character_count = len(sentence) 

vowels = "AEIOUaeiou"
vowel_count = 0 
consonant_count = 0 

for i in sentence:
    if i in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print("Word Count:", word_count)
print("Character Count:", character_count)
print("Vowel Count:", vowel_count)
print("Consonant Count:", consonant_count)
