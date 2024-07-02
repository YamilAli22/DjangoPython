from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage

def contacto(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            # Aquí guardas los datos del formulario si es necesario
            # form.save()
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            mensaje = request.POST.get("mensaje")
            
            email = EmailMessage("Recibiste un correo",
                                 """Del usuario con nombre {}, con la dirección {} 
                                 te escribe lo siguiente:\n\n {}""".format(nombre, email, mensaje),
                                 from_email="",to=['yamil.ali@mi.unc.edu.ar'], reply_to=[email])
            try:
                email.send()
                # Redireccionar con el parámetro 'valido' en la URL
                return redirect('/contacto/?valido=1')
            except:
                return redirect('/contacto/?novalido=1')
                
    return render(request, 'contacto/contacto.html', {'form': form})

  
