import inflect, fileinput

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

    #TODO: there's an extra space when minutes are 00
    print("It's {}{}{}".format(shr, ' '+smn, ' '+ampm))
