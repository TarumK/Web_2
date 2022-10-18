egg = ['кхъу','гъу','къу','к1у','хъу','къ','к1','хъ', 'хь', 'ху', 'гу','дж','дз', 'лъ', 'жь','ц1', 'ы', 'а', 'э', 'б', 'н', 'д', 'р',
       'е','ф','й','з','м','н', 'т']
spam ='къарэкъурэцыжьбанэхэк1'
l_spam = list(spam)
ll = []

for i in range(len(l_spam)):
    if ''.join(l_spam[i:i+4]) in egg:
       ll.append(''.join(l_spam[i:i + 4]))
       del l_spam[i:i+3]
    elif ''.join(l_spam[i:i+3]) in egg:
       ll.append(''.join(l_spam[i:i + 3]))
       del l_spam[i:i + 2]
    elif ''.join(l_spam[i:i+2]) in egg:
       ll.append(''.join(l_spam[i:i + 2]))
       del l_spam[i:i + 1]
    elif ''.join(l_spam[i:i+1]) in egg:
       ll.append(''.join(l_spam[i:i + 1]))

    else:
        pass

print(ll)
print(''.join(ll))
