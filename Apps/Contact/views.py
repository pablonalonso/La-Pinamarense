from django.shortcuts import redirect, render
from .forms import formulario
from django.core.mail import EmailMessage

# Create your views here.

def contacts(request):
    formulario_contacto = formulario()
    if request.method == "POST":
        formulario_contacto = formulario(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("name")
            apellido = request.POST.get("last_name")
            gmail = request.POST.get("gmail")
            mensaje = request.POST.get("message")
            
            mail = EmailMessage(
                "Sucripcion exitosa a Alarcon  BarberShop", 
                "Hola {} {}! Gracias por registrate en nuestra pagina!".format(nombre, apellido),
                "pabloalonnso21@gmail.com",
                [gmail],
                reply_to=["pabloalonnso21@gmail.com"])
            try:
                mail.send()
                return redirect("/contacts/?valido")
            except:
                return redirect("/contacts/?novalido")


    return render(request, 'contact.html', {"formulario_key": formulario_contacto})

    

    
