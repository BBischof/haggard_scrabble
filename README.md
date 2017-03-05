# Haggard Scrabble:

Originally inspired by this [tweet](https://twitter.com/bobblebardsley/status/819072678594314240).

Converts a Haggard Hawks'(HH) tweet into the Scrabble score of the defined word.

Discussion on my [blog](https://medium.com/100000-arrows/haggard-scrabble-twitter-bot-2d2b53307c4c#.wbsphdrhe).

## Tests

Tests are in `test_haggard`(obviously).

## Scrabblers

There are two "Scrabblers"--`scrabbler.py` and `stream_scrabbler.py`.

`scrabbler` takes the most recent HH tweet, computes the score, and replies to the tweet with our standard reply:

```
"Nice word, @HaggardHawks; HAGGY is worth 13pts in Scrabble!"
```

`stream_scrabbler` does similar, but it's persistant and looks for tweets by HH as they come in. It responds similarly.
