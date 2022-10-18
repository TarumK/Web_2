egg = ['кхъу', 'къу','к1у','хъу','къ','к1','хъ', 'ху','гъу', 'гу','дж','дз', 'жь','ц1', 'ы', 'а', 'э','б','е','ф','й','з','н']
spam ='хъыджэбзц1ык1у'
l_spam = list(spam)
ll = []

for i in range(len(l_spam)):
    if ''.join(l_spam[i:i+4]) in egg:
       ll.append(''.join(l_spam[i:i + 4]))
       del l_spam[i:i+4]
    if ''.join(l_spam[i:i+3]) in egg:
       ll.append(''.join(l_spam[i:i + 3]))
    if ''.join(l_spam[i:i+2]) in egg:
       ll.append(''.join(l_spam[i:i + 2]))
    if ''.join(l_spam[i:i+1]) in egg:
       ll.append(''.join(l_spam[i:i + 1]))
    else:
        pass

print(ll)
