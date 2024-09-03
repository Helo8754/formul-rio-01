from django.shortcuts import render, redirect
from matricula.forms import AlunoForms
from .models import Alunos

# Create your views here.
# alunos/views.py

def listar_alunos(request):
    alunos = Alunos.objects.all()
    return render(request, 'listar_alunos.html', {"alunos": alunos})
            
def Cadastro_Aluno(request):
   if request.method =='POST':
      form=AlunoForms(request.POST)
      if form.is_valid():
       
        form.save()
        form = AlunoForms()
        return redirect('/')
   else:
     form = AlunoForms
    
   return render(request,'form.html', {'form' : form})

    