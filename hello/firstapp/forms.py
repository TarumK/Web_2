from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label = "Имя клиента")
    age = forms.IntegerField(label = "Возраст клиента")
    basket = forms.BooleanField(label="Пoлoжить товар в корзину", required=False)
    vyb = forms.NullBooleanField(label="Bы поедете в Сочи этим летом?")
    email = forms.EmailField(label="Введите электронный адрес")
    ip_adr = forms.GenericIPAddressField(label="IP address")
    reg_text = forms.RegexField(label="Teкc:'I'", regex="^[0-9] [A-F] [ 0-9]$")
    file_path = forms.FilePathField(label="Bыбepитe файл", path="C:/Windows", allow_folders="True", allow_files="True")
    file = forms.FileField(label="Фaйл")
    lang = forms.ChoiceField(choices=((1, "Английский"), (2, "Немецкий"), (3, "Французский")))