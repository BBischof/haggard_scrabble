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
  pairs = zip(words, scores)
  pairs = [x for x in pairs if check_new(x[0])]
  if not pairs:
    pass
  elif len(pairs)==1:
    add_word_to_log(pairs[0][0].lower())
    return "Nice word, @HaggardHawks; %s is worth %spts in Scrabble!" % (pairs[0][0].upper(),pairs[0][1])
  else:
    for p in pairs:
      add_word_to_log(p[0].lower())
      word_keys = ['%s is worth %spts' % (x.upper(),y) for (x,y) in pairs]
      return "Nice word, @HaggardHawks; " + ", ".join(word_keys[:-1]) + ", and %s is worth %spts" % (words[-1].upper(), scores[-1]) + " in Scrabble!"

def check_new(word):
  already_tweeted = open("bot/parser/already_tweeted.txt", 'r')
  for line in already_tweeted:
    # print word,line
    if word == line.strip("\n"):
      return False
  else:
    return True

def add_word_to_log(word):
  already_tweeted = open("bot/parser/already_tweeted.txt", 'a')
  already_tweeted.write(word+"\n")
  already_tweeted.close()

def remove_word_from_log(word):
  already_tweeted = open("bot/parser/already_tweeted.txt", 'r')
  lines = already_tweeted.readlines()
  already_tweeted.close()
  already_tweeted = open("bot/parser/already_tweeted.txt", 'w')
  for line in lines:
    if line!=word+"\n":
      already_tweeted.write(line)
  already_tweeted.close()

