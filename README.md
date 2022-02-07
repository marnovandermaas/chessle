# Chessle

Guess the Chess player. This game is inspired by the popular word guessing game [Wordle](https://www.powerlanguage.co.uk/wordle/), is based off of an open source code base [React Wordle](https://github.com/cwackerfuss/react-wordle) and inspired by [Bikle](https://github.com/giop98/bikle).
The logo is licensed in [the public domain](https://publicdomainvectors.org/en/free-clipart/Chess-piece-symbol-image/68163.html).

## Build and run

### To Run Locally:

Clone the repository and perform the following command line actions:

```bash
$> cd react-wordle
$> npm install
$> npm run start
```

Requirements `node --version` > 14.0.0 and `npm --version` > 5.6

### To build/run docker container:

```bash
$> docker build -t game .
$> docker run -d -p 3000:3000 game
```

Open [http://localhost:3000](http://localhost:3000) in browser.

## FAQ

### How can I change the length of a guess?

- Update the `MAX_WORD_LENGTH` variable in [src/constants/settings.ts](src/constants/settings.ts) to the desired length.
- Update the `WORDS` array in [src/constants/wordlist.ts](src/constants/wordlist.ts) to only include words of the new length.
- Update the `VALID_GUESSES` array in [src/constants/validGuesses.ts](src/constants/validGuesses.ts) arrays to only include words of the new length.

### How can I create a version in another language?

- In [public/index.html](public/index.html):
  - Update the title, the description, and the "You need to enable JavaScript" message
  - Update the language attribute in the HTML tag
  - If the language is written right-to-left, add `dir="rtl"` to the HTML tag
- Update the name and short name in [public/manifest.json](public/manifest.json)
- Update the strings in [src/constants/strings.ts](src/constants/strings.ts)
- Add all of the five letter words in the language to [src/constants/validGuesses.ts](src/constants/validGuesses.ts), replacing the English words
- Add a list of goal words in the language to [src/constants/wordlist.ts](src/constants/wordlist.ts), replacing the English words
- Update the "About" modal in [src/components/modals/AboutModel.tsx](src/components/modals/AboutModel.tsx)
- Update the "Info" modal in [src/components/modals/InfoModal.tsx](src/components/modals/InfoModal.tsx)
- If the language has letters that are not present in English update the keyboard in [src/components/keyboard/Keyboard.tsx](src/components/keyboard/Keyboard.tsx)
- If the language's letters are made of multiple unicode characters, use a grapheme splitter at various points throughout the app or normalize the input so that all of the letters are made of a single character
- If the language is written right-to-left, prepend `\u202E` (the unicode right-to-left override character) to the return statement of the inner function in `generateEmojiGrid` in [src/lib/share.ts](src/lib/share.ts)
