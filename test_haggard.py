from bot.parser import haggard_parser as hp

def test_reader():
    tweet = "A HAGGARD tweet looks like this"
    words = ["haggard"]
    assert hp.reader(tweet) == words

def test_scorer():
    words = ["abz"]
    scores = ["14"]
    assert hp.scrabble_scores(words) == scores

def test_tweet_scores():
    tweet = "A HAGGY tweet looks like this"
    scores = ["13"]
    assert hp.scrabble_scores(hp.reader(tweet)) == scores

def test_already_tweeted():
    word = "finished"
    hp.add_word_to_log(word)
    assert hp.check_new(word) == False

def test_log_already_tweeted():
    word = "written"
    assert hp.check_new(word) == True
    hp.add_word_to_log(word)
    assert hp.check_new(word) == False
    hp.remove_word_from_log(word)

def test_add_and_remove():
    word = "temporary"
    assert hp.check_new(word) == True
    hp.add_word_to_log(word)
    assert hp.check_new(word) == False
    hp.remove_word_from_log(word)
    assert hp.check_new(word) == True

def test_null_tweet_scores():
    tweet = "A non-haggard tweet looks like this"
    scores = []
    assert hp.scrabble_scores(hp.reader(tweet)) == scores

def test_bingo_tweet_scores():
    tweet = "A HAGGARD tweet looks like this"
    scores = ["A BINGO! 63"]
    assert hp.scrabble_scores(hp.reader(tweet)) == scores

def test_tweet_scores_with_specials():
    tweet = "A HAGGARD.# tweet looks like this"
    scores = ["A BINGO! 63"]
    assert hp.scrabble_scores(hp.reader(tweet)) == scores

def test_original_lake_tweet():
    tweet = "There is a lake in Massachusetts called CHARGOGGAGOGGMANCHAUGGAUGGAGOGGCHAUBUNAGUNGAMAUGG."
    scores = ["A BINGO! 137"]
    assert hp.scrabble_scores(hp.reader(tweet)) == scores

def test_hyphen_tweet():
    tweet = "A CLEVER-CLUMSY is someone who makes a mess of something they were keen to do.(AE Baker, Northamptonshire Wordss & Phrases, 1854)"
    scores = ["A BINGO! 74"]
    assert hp.scrabble_scores(hp.reader(tweet)) == scores

def test_tweet_writer():
    words = ["HAGGARD"]
    scores = ["A BINGO! 63"]
    tweet_reply = "Nice word, @HaggardHawks; HAGGARD is worth A BINGO! 63pts in Scrabble!"
    assert hp.write_reply(words, scores) == tweet_reply

def test_multi_word_tweet_writer():
    words = ["HAGGARD", "HAGGY", "abz"]
    scores = ["A BINGO! 63", "13", "14"]
    tweet_reply = "Nice word, @HaggardHawks; HAGGARD is worth A BINGO! 63pts, HAGGY is worth 13pts, and ABZ is worth 14pts in Scrabble!"
    assert hp.write_reply(words, scores) == tweet_reply
    for w in words:
        hp.remove_word_from_log(w.lower())

def test_tweet_writer_score_integration():
    tweet = "A HAGGARD tweet looks like this"
    tweet_reply = "Nice word, @HaggardHawks; HAGGARD is worth A BINGO! 63pts in Scrabble!"
    words = hp.reader(tweet)
    scores = hp.scrabble_scores(words)
    assert hp.write_reply(words, scores) == tweet_reply
    for w in words:
        hp.remove_word_from_log(w.lower())

def test_tweet_writer_score_integration_multi_word():
    tweet = "A GIROUETTE is a weathercock. GIROUETTISM is a constant changing of opinions."
    tweet_reply = "Nice word, @HaggardHawks; GIROUETTE is worth A BINGO! 60pts, and GIROUETTISM is worth A BINGO! 64pts in Scrabble!"
    words = hp.reader(tweet)
    scores = hp.scrabble_scores(words)
    assert hp.write_reply(words, scores) == tweet_reply
    for w in words:
        hp.remove_word_from_log(w.lower())

def test_tweet_writer_null_word():
    tweet = "A non-haggard tweet looks like this"
    tweet_reply = None
    words = hp.reader(tweet)
    scores = hp.scrabble_scores(words)
    assert hp.write_reply(words, scores) == tweet_reply
    for w in words:
        hp.remove_word_from_log(w.lower())

def test_duplicate_tweet_scores():
    tweet = "A FINISHED tweet looks like this"
    tweet_reply = None
    words = hp.reader(tweet)
    scores = hp.scrabble_scores(words)
    assert hp.write_reply(words, scores) == tweet_reply
    for w in words:
        hp.remove_word_from_log(w.lower())


