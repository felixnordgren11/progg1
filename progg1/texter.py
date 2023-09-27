text = """Kvällens gullmoln fästet kransa.
Älvorna på ängen dansa,
och den bladbékrönta näcken
gigan rör i silverbäcken.
"""

#print(text.count('\n'))

#count = len([char for char in text]) - len([char for char in text if char.lower() not in 'åäöüéáèîÇôÁ'])

tranny_dick = {
    'å' : 'aa',
    'ä' : 'ae',
    'ö' : 'oe',
    'Å' : 'Aa',
    'Ä' : 'Ae',
    'Ö' : 'Oe',
    'é' : 'e'
}

new_text = ''

for char in text:
    if char in tranny_dick:
        new_text += tranny_dick[char]
    else:
        new_text += char
    
count = {}

for char in text:
    if char.isalpha():
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
            
def part2(element):
    return element[1]

a = ('a',1)
def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


count_lst = list(count.items())

'''
sbc = sorted(count_lst, key=part2, reverse=True)
for index, element in enumerate(sbc, start = 1):
    print(f'{element[0]}:{element[1]:2d}', end='\t')
    if index % 5 == 0:
        print()
'''

new_lst = []
for element in count_lst:
    element = Reverse(element)
    new_lst.insert(0, element)
    new_lst.sort(reverse=True)
print(new_lst)

#OR

swapped = sorted([(elem[1], elem[0]) for elem in count_lst], reverse=True)





