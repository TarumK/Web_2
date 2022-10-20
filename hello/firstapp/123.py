egg = ['а', 'э', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
       'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ю', 'я', '1',
       'гу', 'гъ', 'дж', 'дз', 'жь', 'ку', 'кI', 'къ', 'лъ', 'лI', 'пI', 'тI', 'фI', 'ху', 'хь',
       'хъ', 'цI', 'щI', 'Iу', 'гъу', 'кIу', 'къу', 'кхъ', 'хъу', 'кхъу', ' ']
spam =input('Enter: ').replace('1','I').lower()
    #'къарэкъурэцыжьбанэхэк1'
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
print(''.join(ll).capitalize())
