#test
from pydub import AudioSegment
from pydub.playback import play
# sound = AudioSegment.from_wav('myfile.wav')
# play(sound)
def splitcher(spam):

    egg = ['А', 'Э', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З',
           'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С',
           'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Ю',
           'Я', 'I', 'ГУ', 'ГЪ', 'ДЖ', 'ДЗ', 'ЖЬ', 'КУ', 'КI',
           'КЪ', 'ЛЪ', 'ЛI', 'ПI', 'ТI', 'ФI', 'ХУ', 'ХЬ',
           'ХЪ', 'ЦI', 'ЩI', 'IУ', 'ГЪУ', 'КIУ', 'КЪУ', 'КХЪ',
           'ХЪУ', 'КХЪУ', '.', ',', ' ']

    l_spam = list(spam.replace('1', 'I').upper())
    l_spam = list(spam.replace(' ', '_').upper())
    # l_spam = [s.upper() for s in l_spam]
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
    return ll

# stroka = input('Enter: ')
# print(splitcher(stroka))
# mm = splitcher(stroka)
# for i in mm:
#     sound = AudioSegment.from_wav('sound/'+i+'.wav')
#     play(sound)
# str_ll = ''.join(splitcher(stroka))
# print(''.join(str_ll).upper())