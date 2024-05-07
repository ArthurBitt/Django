from django.shortcuts import render
from app.form_model.forms import PassagemForms,PessoaForms

def index(request):
    form = PassagemForms()
    pessoa_form = PessoaForms()
    contexto = {'form':form, 'pessoa_form':pessoa_form}
    return render(request, 'form_model/pages/index.html', contexto)

def results(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        if form.is_valid():
            contexto = {'form': form, 'pessoa_form':pessoa_form}
            return render(request, 'form_model/pages/results.html',contexto)
        else:
            print('form inválido')
            contexto = {'form': form}
            return render(request, 'form_model/pages/index.html',contexto)