# Azaan Dawson amdg 11/11/20

word1 = input("Please enter a word ")
word2 = input("Please input a second word ")

lst_word1 = list(word1)
lst_word2 = list(word2)
lst_word1.sort()
lst_word2.sort()

if lst_word1 == lst_word2 :
  print(word1 +' and ' + word2 + ' are anagrams')
else:
  print(word1 + ' and ' + word2 + ' are not anagrams')
