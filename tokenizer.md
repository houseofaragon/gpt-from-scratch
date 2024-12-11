Building tokenizer from scratch

Goal:
1. Take strings and feed them into language models.
2. To do this we need to tokenize the strings into integers in some fixed vocabulary.
3. Then use the integers to make a lookup into a lookup tabe of vectors.
4. Feed the vectors into the transformer as the input

Unicode - 150K chars - way to define all types of characters

```
ords = [ord(x) for x in "hello I am karen"]
[104, 101, 108, 108, 111, 32, 73, 32, 97, 109, 32, 107, 97, 114, 101, 110]

chars = [char(x) for x in ords]
```

UTF-8, UTF-16, UTF-32 -> take unicode of strings and encodes into binary

UTF-8 is preferred - backwards compatible to ascii encoding to text


Byte-Pair encoding algorithm
https://github.com/openai/gpt-2
https://github.com/openai/gpt-2/blob/master/src/encoder.py

only inferences code - which takes merges created and applies them to new piece of text