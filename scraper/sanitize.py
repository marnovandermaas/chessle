from unidecode import unidecode

debug = False
wordlen = 5

words = []

### GM names
def extractnames(filename, startline, endline, indicatorstring, prenamestring):
    retlist = []
    
    inputfile = open(filename)
    while inputfile.readline() != startline:
        None

    if debug:
        print('Found: ' + startline)

    indicatorflag = False
    while True:
        line = inputfile.readline()
        if indicatorflag:
            namesplit = ', '
            if namesplit not in line:
                namesplit = ' '
            familyname = line.split(prenamestring)[1].split(namesplit)[0]
            familyname = unidecode(familyname)
            if len(familyname) == wordlen:
                retlist.append(familyname)
        if line == endline:
            if debug:
                print('Found: ' + endline)
            break
        indicatorflag = indicatorstring in line
    
    inputfile.close()
    return retlist

words.extend(extractnames('List of chess grandmasters - Wikipedia.html', '<th>FIDE ID</th>\n', '</td></tr></tbody></table>\n', '<tr', '">'))

### Player names
playerfile = open('List of chess players - Wikipedia.html')

startline = '<h2><span class="mw-headline" id="A">A</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_chess_players&amp;action=edit&amp;section=1" title="Edit section: A">edit source</a><span class="mw-editsection-bracket">]</span></span></h2>\n'
endline = '<h2><span class="mw-headline" id="Computers">Computers</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_chess_players&amp;action=edit&amp;section=28" title="Edit section: Computers">edit source</a><span class="mw-editsection-bracket">]</span></span></h2>\n'

while playerfile.readline() != startline:
    None
if debug:
    print('Found: ' + startline)

while True:
    line = playerfile.readline()
    if '<li><a href="' in line:
        name = line.split('">')[1].split('</a>')[0].split(' ')
        if len(name) == 2:
            name = unidecode(name[1])
            if len(name) == wordlen:
                if name != 'Liren' and name != 'Zhong' and name != 'Weida':
                    words.append(name)
    if line == endline:
        if debug:
            print('Found: ' + endline)
        break

words.append('Zhang')
playerfile.close()

### Chess terms
termfile = open('Glossary of chess - Wikipedia.html')

startline = '<h2><span class="mw-headline" id="A">A</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Glossary_of_chess&amp;action=edit&amp;section=1" title="Edit section: A">edit source</a><span class="mw-editsection-bracket">]</span></span></h2>\n'
endline = '<h2><span class="mw-headline" id="Notes">Notes</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Glossary_of_chess&amp;action=edit&amp;section=26" title="Edit section: Notes">edit source</a><span class="mw-editsection-bracket">]</span></span></h2>\n'

while termfile.readline() != startline:
    None
if debug:
    print('Found: ' + startline)

while True:
    line = termfile.readline()
    if '<dt class="glossary" id="' in line:
        beforeterm = '<dfn class="glossary">'
        afterterm = ' <span class="anchor" id="'
        term = line.split(beforeterm)[1].split(afterterm)[0]
        if '<a href="/wiki/' in term:
            term = term.split('">')[1].split('</a>')[0]
        if ' ' in term or '<' in term or '.' in term or '-' in term:
            None
        else:
            term = unidecode(term)
            if len(term) == wordlen-1 and debug:
                print(term)
            if len(term) == wordlen:
                words.append(term)
    if line == endline:
        if debug:
            print('Found: ' + endline)
        break

termfile.close()

morewords = ['binds', 'chess', 'draws', 'edges', 'files', 'flags', 'forks', 'holes', 'kicks', 'kings', 'lines', 'mates', 'moves', 'norms', 'pawns', 'ranks', 'rooks', 'swaps', 'takes', 'traps', 'wings']

words.extend(morewords)

### Final processing
wordset = set(words)
if debug:
    print(wordset)

sanitizedset = set()
for word in wordset:
    if "'" in word:
        continue
    sanitizedset.add(word.lower())

if debug:
    print(sorted(sanitizedset))
    print(len(sanitizedset))

### Writing files
wordfile = open('wordlist.ts', 'w')
wordfile.write('export const WORDS = [\n')
for word in sanitizedset:
    wordfile.write("  '" + word + "',\n")
wordfile.write(']\n')

guessfile = open('validGuesses.ts', 'w')
guessfile.write('export const VALID_GUESSES = [\n')
for word in sorted(sanitizedset):
    guessfile.write("  '" + word + "',\n")
guessfile.write(']\n')
