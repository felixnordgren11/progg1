import re
Fact = True
file = 'test.txt'
with open(file, encoding='utf8') as text:
    lines = text.read()

def p2(word):
    return word[1]
wordlist = re.findall(r'[a-zA-ZåäöÅÄÖ]+', lines)
wordnum = len(wordlist)

wcount = {}
for word in wordlist:
    word = word.lower()
    if word in wcount:
        wcount[word] += 1
    else:
        wcount[word] = 1

olika = len(wcount)

print(f'Antal ord: {wordnum}, antal olika ord: {olika}')
#print(wcount)

wcount_lst = list(wcount.items())

sorted_by_count = sorted(wcount_lst, key=p2, reverse=True)
#print(sorted_by_count)

def van(alist,n):
    vanligast_fk = []
    ovanligast_fk = []
    for i in range(n):
        vanligast_fk.insert(0, alist[n-1-i][0])
        ovanligast_fk.insert(0, alist[-1-i][0])
    print(vanligast_fk, ovanligast_fk)
    
van(sorted_by_count, 4)
    
#print(f'Antal ord: {wordnum}, antal olika ord: {olika}')
        



    

        
        



        


'''
for index, word in enumerate(wordlist, start=1):
    print(word, end=' ')
    if index % 8 == 0:
        print()
print('\n')


sbc = sorted(wcount, key=p2, reverse=False)
for index, word in enumerate(sbc, start = 1):
    print(f'{element[0]}:{element[1]:2d}', end='\t')
    if index % 5 == 0:
        print()
'''     

    
