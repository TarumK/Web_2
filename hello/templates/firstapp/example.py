input_text = input("Введите слово: ")
list_letter = list(input_text)
gl_letters = ['а', 'е', 'у', 'ы','о','и']
gl_count = 0
sogl_count = 0
for i in list_letter:
    if i in gl_letters:
        print(i)
        gl_count += 1
    else:
        sogl_count += 1
        pass
print ('Количество гласных букв: ',gl_count)
print ('Количество согласных букв: ',sogl_count)

