def letter_check(word, letter):
  for letters in word:
    if letter == letters: 
      return True 
  else:
    return False 

print (letter_check("hello", "h"))


