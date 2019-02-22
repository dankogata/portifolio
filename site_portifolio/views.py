from django.shortcuts import render

# Create your views here.
def home (request):
    eu = {
        'nome': 'Daniel',
        'altura': '1.65' ,
        'conhecimento' : ['HTML', 'JS','CSS', 'Python'],
        'endereco':{
            'cidade': 'Sao Paulo'
            'pais': 'Brasil',
        }
    # nome = 'Daniel'
    # conhecimentos = [ 'HTML' , 'css', 'JavaScript' , 'Python', 'Django', 'Git']
    # return render(request, 'index.html', {'conhecimentos' : conhecimentos , 'nome': nome})
    return render(request, 'index.html', { 'eu' : eu, 'numero' : 1})



def contato(request):
    return render (request, 'contato.html')
