from django.shortcuts import render

from .models import Cliente

from .forms import ClienteForm

from django.shortcuts import redirect

# Create your views here.

def client_list(request):
    clientes = Cliente.objects.all()
    return render(request,'blog/client_list.html',{'clientes':clientes})

def Registro(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data['nombre_cliente'])
        return redirect('/')
    else:
        form = ClienteForm()

    return render(request,'blog/Registro.html',{'form':form})