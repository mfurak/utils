#reverse a string in a recursive way
def reverse(word):
  l = len(word)
  if(l<=1):
    return word;
  return reverse(word[1:l]) + word[0]
