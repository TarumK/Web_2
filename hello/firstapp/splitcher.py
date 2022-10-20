def splitcher(strochka1):

    strochka1 = list(strochka1)

    for i in range(len(strochka1)):
        #кхъу
        if len(strochka1) >= i+4 and strochka1[i] == 'к' and strochka1[i+1] == 'х' and strochka1[i+2] == 'ъ' \
           and strochka1[i+3] == 'у':
            strochka1[i] = 'кхъу'
            del strochka1[i+1:i+4]
        #гъу
        elif len(strochka1) >= i+3 and strochka1[i] == 'х' and strochka1[i+1] == 'ъ' \
            and strochka1[i+2] == 'у':
            strochka1[i] = 'хъу'
            del strochka1[i+1:i+3]
        #къу
        elif len(strochka1) >= i+3 and strochka1[i] == 'к' and strochka1[i+1] == 'ъ' \
            and strochka1[i+2] == 'у':
            strochka1[i] = 'къу'
            del strochka1[i+1:i+3]
        #хъу
        elif len(strochka1) >= i+3 and strochka1[i] == 'х' and strochka1[i+1] == 'ъ' \
            and strochka1[i+2] == 'у':
            strochka1[i] = 'хъу'
            del strochka1[i+1:i+3]
        #гу
        elif len(strochka1) >= i+2 and strochka1[i] == 'г' and strochka1[i+1] == 'у':
            strochka1[i] = 'гу'
            del strochka1[i+1:i+2]
        #ку
        elif len(strochka1) >= i+2 and strochka1[i] == 'к' and strochka1[i+1] == 'у':
            strochka1[i] = 'ку'
            del strochka1[i+1:i+2]
        #гъ
        elif len(strochka1) >= i+2 and strochka1[i] == 'г' and strochka1[i+1] == 'ъ':
            strochka1[i] = 'гъ'
            del strochka1[i+1:i+2]
        #къ
        elif len(strochka1) >= i+2 and strochka1[i] == 'к' and strochka1[i+1] == 'ъ':
            strochka1[i] = 'къ'
            del strochka1[i+1:i+2]
        #хь
        elif len(strochka1) >= i+2 and strochka1[i] == 'х' and strochka1[i+1] == 'ь':
            strochka1[i] = 'хь'
            del strochka1[i+1:i+2]
    return strochka1
string = input()

print(splitcher(string))
# naoborot = strochka1[::-1]
# print(f'ХьэрфкIэ зэгуэудауэ: {strochka1}')
# print(f'Псалъэр зэпыгъэзауэ: {naoborot}')
# print(''.join(strochka1))
#
# print('Палиндром?')
#
# if naoborot == strochka1:
#     print('Нт1э')
# else:
#         print('Хьэуэ')


