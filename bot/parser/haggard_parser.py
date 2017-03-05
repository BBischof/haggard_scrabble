import re

letter_scores = {
  "a":1, "b":3, "c":3, "d":2, "e":1, "f":4,
  "g":2, "h":4, "i":1, "j":8, "k":5, "l":1,
  "m":3, "n":1, "o":1, "p":3, "q":10, "r":1,
  "s":1, "t":1, "u":1, "v":4, "w":4, "x":8,
  "y":4, "z":10
  }

'''returns the first all cap word that is longer than two characters'''
def reader(text):
  caps_words = [x.lower() for x in text.split(" ") if x.isupper() and len(x) > 2]
  try:
    return [re.sub('[^A-Za-z0-9]+', '', word) for word in caps_words]
  except:
    return ""

'''converts words to their scrabble value'''
def scrabble_scores(words):
  scores = []
  if words:
    for word in words:
      if len(word) >= 7:
        pass
        scores.append(('A BINGO! %s' % (sum([letter_scores[l] for l in word])+50)))
      else:
        scores.append(str(sum([letter_scores[l] for l in word])))
  return scores

'''
uses the word and score to write the reply tweet
(only uses 37 characters)
'''
def write_reply(words, scores):
  if not words:
    pass
  elif len(words)==1:
    return "Nice word, @HaggardHawks; %s is worth %spts in Scrabble!" % (words[0].upper(),scores[0])
  else:
    pairs = ['%s is worth %spts' % (x.upper(),y) for (x,y) in zip(words, scores)]
    return "Nice word, @HaggardHawks; " + ", ".join(pairs[:-1]) + ", and %s is worth %spts" % (words[-1].upper(), scores[-1]) + " in Scrabble!"
