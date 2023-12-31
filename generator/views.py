from django.shortcuts import render
import random

# запись из теминала Линукс

def password(request):
    thepassword=''
    characters = list('abcdefghigklmnopqrstuvxvz')

    '''если ставим флажок uppercase на странице сайта то рандом 
    сделает некоторые символы в верхнем регистре''' 
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIGKLMNOPQRSTUVXWZ'))
    
    '''если ставим флажок special на странице сайта то рандом 
    добавит спецсимволы''' 
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    '''если ставим флажок numbers на странице сайта то рандом 
    добавит числа''' 
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    # параметр lenght из home.html, значение 12 будет по умолчанию
    lenght = int(request.GET.get('lenght', 12))
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
