import pygsheets
import arrow
client = pygsheets.authorize(service_account_file="../keys.json") 
spreadsheet2 = client.open("LAC Tournament Submission Form (Responses)")
worksheet2 = spreadsheet2.worksheet("title", "Form Responses 1")
date = arrow.utcnow()
c2 = []
d2 = []
e2 = []
f2 = []
g2 = []
h2 = []
i2 = []
j2 = []
k2 = []
l2 = []
m2 = []
n2 = []
o2 = []
p2 = []
q2 = []
r2 = []
s2 = []
cfiles2 = []
num = 2
while "''>" not in str(worksheet2.cell('C' + str(num))):
    c2.append(str(worksheet2.cell('C' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('D' + str(num))):
    d2.append(str(worksheet2.cell('D' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('E' + str(num))):
    e2.append(str(worksheet2.cell('E' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('F' + str(num))):
    f2.append(str(worksheet2.cell('F' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('G' + str(num))):
    g2.append(str(worksheet2.cell('G' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('H' + str(num))):
    h2.append(str(worksheet2.cell('H' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('I' + str(num))):
    i2.append(str(worksheet2.cell('I' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('J' + str(num))):
    j2.append(str(worksheet2.cell('J' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('K' + str(num))):
    k2.append(str(worksheet2.cell('K' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('L' + str(num))):
    l2.append(str(worksheet2.cell('L' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('M' + str(num))):
    m2.append(str(worksheet2.cell('M' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('N' + str(num))):
    n2.append(str(worksheet2.cell('N' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('O' + str(num))):
    o2.append(str(worksheet2.cell('O' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('P' + str(num))):
    p2.append(str(worksheet2.cell('P' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('Q' + str(num))):
    q2.append(str(worksheet2.cell('Q' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('R' + str(num))):
    r2.append(str(worksheet2.cell('R' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
num = 2
while "''>" not in str(worksheet2.cell('S' + str(num))):
    s2.append(str(worksheet2.cell('S' + str(num))).split("'")[1].replace("\\n", " "))
    num += 1
LAChome = open("index.html", "w")
LAChome.write("<!DOCTYPE html>")
LAChome.write("\n" + "<html lang='en'>")
LAChome.write("\n" + "    <head>")
LAChome.write("\n" + '        <meta charset="UTF-8">')
LAChome.write("\n" + '        <link rel="icon" type="image/x-icon" href="logo.png">')
LAChome.write("\n" + '        <link rel="stylesheet" href="style.css">')
LAChome.write("\n" + "        <title>LAC Official Website</title>")
LAChome.write("\n" + "    </head>")
LAChome.write("\n" + "    <body>")
LAChome.write("\n" + "        <table>")
LAChome.write("\n" + "            <tr>")
LAChome.write("\n" + '                <td class="logo"><a href="index.html"><img src="logo.png" class="img" alt="LAC Logo"></a></td>')
LAChome.write("\n" + '                <td class="LAC">LAC</td>')
LAChome.write("\n" + "                <td>")
LAChome.write("\n" + '                    <div class="dropdown">')
LAChome.write("\n" + '                        <button class="dropbtn">Chess Tournaments</button>')
LAChome.write("\n" + '                        <div class="dropdown-content">')
for thugs in range(len(d2)):
    if date >= arrow.get(j2[thugs], "M/D/YYYY"):
        continue
    elif date < arrow.get(j2[thugs], "M/D/YYYY"):
        LAChome.write("\n" + '                            <a href="Tournaments/' + d2[thugs] + '.html">' + d2[thugs] + '</a>')
LAChome.write("\n" + '                            <a href="https://docs.google.com/forms/d/e/1FAIpQLSdBI4i5PkiHpXEPjVms2GstaLb0_kRMcTuHdjkpptmYSYDGaw/viewform">Submit Tournament</a>')
LAChome.write("\n" + "                        </div>")
LAChome.write("\n" + "                    </div>")
LAChome.write("\n" + "                </td>")
LAChome.write("\n" + "            </tr>")
LAChome.write("\n" + "        </table>")
LAChome.write("\n" + "    </body>")
LAChome.write("\n" + "</html>")
entrylists = []
for entries in range(len(d2)):
    cfiles2.append(open("Tournaments/" + d2[entries] + ".html", "w"))
    cfiles2[entries].write("<!DOCTYPE html>")
    cfiles2[entries].write("\n" + "<html lang='en'>")
    cfiles2[entries].write("\n" + "    <head>")
    cfiles2[entries].write("\n" + '        <meta charset="UTF-8">')
    cfiles2[entries].write("\n" + '        <link rel="icon" type="image/x-icon" href="logo.png">')
    cfiles2[entries].write("\n" + '        <link rel="stylesheet" href="../style.css">')
    cfiles2[entries].write("\n" + "        <title>" + d2[entries] + "</title>")
    cfiles2[entries].write("\n" + "    </head>")
    cfiles2[entries].write("\n" + "    <body>")
    cfiles2[entries].write("\n" + "        <table>")
    cfiles2[entries].write("\n" + "            <tr>")
    cfiles2[entries].write("\n" + '                <td class="logo"><a href="../index.html"><img src="logo.png" class="img" alt="LAC Logo"></a></td>')
    cfiles2[entries].write("\n" + '                <td class="LAC">LAC</td>')
    cfiles2[entries].write("\n" + "                <td>")
    cfiles2[entries].write("\n" + '                    <div class="dropdown">')
    cfiles2[entries].write("\n" + '                        <button class="dropbtn">Chess Tournaments</button>')
    cfiles2[entries].write("\n" + '                        <div class="dropdown-content">')
    for thugs in range(len(d2)):
        if date >= arrow.get(j2[thugs], "M/D/YYYY"):
            continue
        elif date < arrow.get(j2[thugs], "M/D/YYYY"):
            cfiles2[entries].write("\n" + '                            <a href="' + d2[thugs] + '.html">' + d2[thugs] + '</a>')
    cfiles2[entries].write("\n" + '                            <a href="https://docs.google.com/forms/d/e/1FAIpQLSdBI4i5PkiHpXEPjVms2GstaLb0_kRMcTuHdjkpptmYSYDGaw/viewform">Submit Tournament</a>')
    cfiles2[entries].write("\n" + "                        </div>")
    cfiles2[entries].write("\n" + "                    </div>")
    cfiles2[entries].write("\n" + "                </td>")
    cfiles2[entries].write("\n" + "            </tr>")
    cfiles2[entries].write("\n" + "        </table>")
    cfiles2[entries].write("\n" + "        <h1>" + e2[entries] + "</h1>")
    cfiles2[entries].write("\n" + "        <h2>" + i2[entries] + "-" + j2[entries] + "</h2>")
    cfiles2[entries].write("\n" + '        <div id="forms">')
    cfiles2[entries].write("\n" + '            <div class="dropdown">')
    cfiles2[entries].write("\n" + '                <button class="dropbtn">Forms</button>')
    cfiles2[entries].write("\n" + '                <div class="dropdown-content">')
    cfiles2[entries].write("\n" + '                    <a href="' + q2[entries] + '">Registration Form</a>')
    cfiles2[entries].write("\n" + '                    <a href="' + r2[entries] + '">Withdrawal Form</a>')
    cfiles2[entries].write("\n" + '                    <a href="' + s2[entries] + '">Entry List</a>')
    cfiles2[entries].write("\n" + '                </div>')
    cfiles2[entries].write("\n" + '            </div>')
    cfiles2[entries].write("\n" + '        </div>')
    cfiles2[entries].write("\n" + "        <p>" + f2[entries] + "</p>")
    cfiles2[entries].write("\n" + "        <p>Tournament Format: " + g2[entries] + "</p>")
    cfiles2[entries].write("\n" + "        <p>Prizes: " + h2[entries] + "</p>")
    cfiles2[entries].write("\n" + "        <p>Round Times: " + k2[entries] + "</p>")
    cfiles2[entries].write("\n" + "        <p>Location: " + l2[entries] + "</p>")
    cfiles2[entries].write("\n" + "        <p>Entry Fee: " + m2[entries] + "</p>")
    cfiles2[entries].write("\n" + "        <p>Byes: " + o2[entries] + "</p>")
    cfiles2[entries].write("\n" + "        <p>Contact: " + p2[entries] + "</p>")
    cfiles2[entries].write("\n" + "        <p>Entry Limit: " + c2[entries] + "</p>")
    cfiles2[entries].write("\n" + "        <p><b><u><i>Other Requirements: " + n2[entries] + "</b></u></i></p>")
    cfiles2[entries].write("\n" + "    </body>")
    cfiles2[entries].write("\n" + "</html>")