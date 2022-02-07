debug = True
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
            if len(name[1]) == wordlen:
                words.append(name[1])
    if line == endline:
        if debug:
            print('Found: ' + endline)
        break

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
            if len(term) == wordlen:
                words.append(term)
    if line == endline:
        if debug:
            print('Found: ' + endline)
        break

termfile.close()

### Final processing
wordset = set(words)
if debug:
    print(wordset)

sanitizedset = set()
for word in wordset:
    sanitizedset.add(word.lower())

if debug:
    print(sanitizedset)
    print(len(sanitizedset))
