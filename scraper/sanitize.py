debug = True

gmfile = open('List of chess grandmasters - Wikipedia.html')
playerfile = open('List of chess players - Wikipedia.html')

startline = '<th>FIDE ID</th>\n'
endline = '</td></tr></tbody></table>\n'
while gmfile.readline() != startline:
    None

if debug:
    print('Found: ' + startline)

trline = False
while True:
    line = gmfile.readline()
    if trline:
        namesplit = ', '
        if namesplit not in line:
            namesplit = ' '
        if debug:
            print('Family Name : ' + line.split('">')[1].split(namesplit)[0])
    if line == endline:
        if debug:
            print('Found: ' + endline)
        break
    trline = '<tr' in line

for line in playerfile.readlines():
    None #print(line)

gmfile.close()
playerfile.close()
