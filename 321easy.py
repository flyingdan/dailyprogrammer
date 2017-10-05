import inflect, fileinput
'''
Sample input:
00:00
01:30
12:05
14:01
20:29
21:00
Sample output:
It's twelve am
It's one thirty am
It's twelve oh five pm
It's two oh one pm
It's eight twenty nine pm
It's nine pm
'''
p = inflect.engine()
hr_corner_cases = {'00':'twelve'}
min_corner_cases = {'00':''}
ampm = 'am'

for t in fileinput.input():
    hr, mn = (t.strip()).split(":")

    if hr in hr_corner_cases:
        shr = hr_corner_cases[hr]
    else:
        if int(hr) > 12:
            hr = str(int(hr) - 12)
            ampm = 'pm'
        shr = p.number_to_words(hr)

    if mn in min_corner_cases:
        smn = min_corner_cases[mn]
    else:
        smn = p.number_to_words(mn)
        if int(mn) < 10:
            smn = 'oh ' + smn
        smn = ' ' + smn

    print("It's {}{}{}".format(shr, smn, ' '+ampm))
