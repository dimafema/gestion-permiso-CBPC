from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import UsuarioForm, ParqueForm, ZonaForm, BrigadaForm, UsuarioCreationForm, VacacionesForm
from .models import  Parque, Zona, Brigada, Usuario, Vacaciones
from datetime import timedelta
from django.db.models import Sum
from django.contrib.auth.models import User
from django.http import HttpResponse

# Crea tus vistas aquí.
def cond_uso(request):
    return render(request, 'condicionesuso.html')
def proyecto(request):
    return render(request, 'proyecto.html')

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html', {'form': form})
# Vista para crear un nuevo usuario
def registro_user(request):
    form = UsuarioCreationForm()
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Usuario creado correctamente')
            form.save()
            return redirect('/home')
    return render(request, 'user/registro_user.html', {'form': form})

# Vista para crear una lista filtrada de usuarios
def home(request):
        parque = None
        brigada = None      
     # Asegúrate de que el usuario esté autenticado
        if request.user.is_authenticated: 
            # Filtra los objetos Usuario por el usuario autenticado y otros criterios
            efectivo = Usuario.objects.filter(usuario_id=request.user.id)
            try:
                parque = efectivo[0].parque
                brigada = efectivo[0].brigada
            except IndexError:
                parque = None
                brigada = None
            usuarios_brigada = Usuario.objects.filter(parque_id=efectivo[0].parque_id, brigada_id=efectivo[0].brigada_id) if efectivo else None
        else:
            usuarios_brigada = None
        # Pasa los objetos filtrados al contexto de la plantilla
        return render(request, 'home.html', {'efectivos': usuarios_brigada, 'parque': parque, 'brigada': brigada})



# ZONAS
def crear_zona(request):
    if request.method == 'POST':
        form = ZonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = ZonaForm()
    return render(request, 'zona/crear_zona.html', {'form': form})
# Vista para editar una zona existente
def editar_zona(request, id):
    zona = get_object_or_404(Zona, id=id)
    if request.method == 'POST':
        form = ZonaForm(request.POST, instance=zona)
        if form.is_valid():
            form.save()
            return redirect('/home', id=id)
    else:
        form = ZonaForm(instance=zona)
    return render(request, 'zona/editar_zona.html', {'form': form})
# Vista para eliminar la zona seleccionada
def eliminar_zona(request,id):
    zona = get_object_or_404(Zona, id=id)
    if request.method == 'POST':
        form = ZonaForm(request.POST, instance=zona)
        for field in form.fields.values():
            field.disabled = True
        if form.is_valid():
            zona.delete()
            return redirect('list_delete_zona',)
    else:
        form = ZonaForm(instance=zona)
        for field in form.fields.values():
            field.disabled = True
    return render(request, 'zona/delete_zona.html', {'form': form})
# Vista que muestra una lista de zonas para editar
def list_edit_zona(request):
    zona = {'zona': Zona.objects.all()}
    return render(request, 'zona/lis_zona_edit.html', zona)
# Vista que muestra una lista de zonas para eliminar
def list_delete_zona(request):
    zona = {'zona': Zona.objects.all()}
    return render(request, 'zona/lis_zona_delete.html', zona)


# PARQUES
def crear_parque(request):
    if request.method == 'POST':
        form = ParqueForm(request.POST)
        if form .is_valid():
            form .save()
            return redirect('/home') 
    else:
        form  = ParqueForm()
    return render(request, 'parque/crear_parque.html', {'form': form })
# Vista para editar un parque existente
def editar_parque(request, id):
    parque = get_object_or_404(Parque, id=id)
    if request.method == 'POST':
        form = ParqueForm(request.POST, instance=parque)
        if form.is_valid():
            form.save()
            return redirect('/home', id=id)
    else:
        form = ParqueForm(instance=parque)
    return render(request, 'parque/editar_parque.html', {'form': form})
# Vista para eliminar el parque seleccionado
def eliminar_parque(request,id):
    parque = get_object_or_404(Parque, id=id)
    if request.method == 'POST':
        form = ZonaForm(request.POST, instance=parque)
        for field in form.fields.values():
            field.disabled = True
        if form.is_valid():
            parque.delete()
            return redirect('/list_delete_parque',)
    else:
        form = ParqueForm(instance=parque)
        for field in form.fields.values():
            field.disabled = True
    return render(request, 'parque/delete_parque.html', {'form': form})
# Vista que muestra una lista de parque a editar
def list_edit_parque(request):
    parque = {'parque': Parque.objects.all()}
    return render(request, 'parque/lis_parque_edit.html', parque)
# Vista que muestra una lista de parque a eliminar
def list_delete_parque(request):
    parque = {'parque': Parque.objects.all()}
    return render(request, 'parque/lis_parque_delete.html', parque)


# BRIGADAS
def crear_brigada(request):
    if request.method == 'POST':
        form = BrigadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = BrigadaForm()
    return render(request, 'brigada/crear_brigada.html', {'form': form})
# Vista para editar un brigada existente
def editar_brigada(request, id):
    brigada = get_object_or_404(Brigada, id=id)
    if request.method == 'POST':
        form = BrigadaForm(request.POST, instance=brigada)
        if form.is_valid():
            form.save()
            return redirect('/home', id=id)
    else:
        form = BrigadaForm(instance=brigada)
    return render(request, 'brigada/editar_brigada.html', {'form': form})
# Vista para eliminar el brigada seleccionado
def eliminar_brigada(request,id):
    brigada = get_object_or_404(Brigada, id=id)
    if request.method == 'POST':
        form = BrigadaForm(request.POST, instance=brigada)
        for field in form.fields.values():
            field.disabled = True
        if form.is_valid():
            brigada.delete()
            return redirect('/list_delete_brigada',)
    else:
        form = BrigadaForm(instance=brigada)
        for field in form.fields.values():
            field.disabled = True
    return render(request, 'brigada/delete_brigada.html', {'form': form})
# Vista que muestra una lista de brigada a editar
def list_edit_brigada(request):
    brigada = {'brigada': Brigada.objects.all()}
    return render(request, 'brigada/lis_brigada_edit.html', brigada)
# Vista que muestra una lista de brigada a eliminar
def list_delete_brigada(request):
    brigada = {'brigada': Brigada.objects.all()}
    return render(request, 'brigada/lis_brigada_delete.html', brigada)


# BOMBEROS
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/crear_user.html', {'form': form},)
# Vista para editar un usuario existente
def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('/home', id=id)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario/editar_usuario.html', {'form': form})
# Vista para eliminar el usuario seleccionado
def eliminar_usuario(request,id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        for field in form.fields.values():
            field.disabled = True
        if form.is_valid():
            usuario.delete()
            return redirect('/list_delete_user',)
    else:
        form = UsuarioForm(instance=usuario)
        for field in form.fields.values():
            field.disabled = True
    return render(request, 'usuario/delete_usuario.html', {'form': form})
# Vista que muestra una lista de usuarios para editar
def list_edit_user(request):
    # Asegúrate de que el usuario esté autenticado
        if request.user.is_authenticated: 
            # Filtra los objetos Usuario por el usuario autenticado y otros criterios
            efectivo = Usuario.objects.filter(usuario_id=request.user.id)
            if efectivo:
                parque = efectivo[0].parque
            usuarios_brigada = Usuario.objects.filter(parque_id=efectivo[0].parque_id) if efectivo else None
        else:
            usuarios_brigada = None
        # Pasa los objetos filtrados al contexto de la plantilla
        return render(request, 'usuario/lis_user_edit.html',  {'efectivos': usuarios_brigada, 'parque': parque})
# Vista que muestra una lista de usuarios para eliminar
def list_delete_user(request):
    usuarios = {'usuarios': Usuario.objects.all()}
    return render(request, 'usuario/lis_user_delete.html', usuarios)




# VACACIONES
# 1) lista los usuarios, selecciona el usuario y crea permisos de descansos anuales (vacaciones) del usuario seleccionado
def list_crear_vaca_1(request):
    if request.user.is_authenticated: 
            # Filtra los objetos Usuario por el usuario autenticado y otros criterios
            efectivo = Usuario.objects.filter(usuario_id=request.user.id)
            if efectivo:
                parque = efectivo[0].parque
                brigada = efectivo[0].brigada
            usuarios_brigada = Usuario.objects.filter(parque_id=efectivo[0].parque_id, brigada_id=efectivo[0].brigada_id) if efectivo else None
    else:
            usuarios_brigada = None
    # Pasa los objetos filtrados al contexto de la plantilla
    return render(request, 'vacaciones/crear_vaca_list.html', {'efectivos': usuarios_brigada, 'parque': parque, 'brigada': brigada})
# 2) Formulario para ingresar permisos de descansos anuales (vacaiones), del usuario seleccionado
def crear_vaca_2(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = VacacionesForm(request.POST)
        if form.is_valid():
            vacaciones = form.save(commit=False)
            vacaciones.usuario = usuario
            vacaciones.dias_totales = ((vacaciones.fecha_fin - vacaciones.fecha_inicio) + timedelta(days=1)).days
            vacaciones.save()
            return redirect('/home')
    else:
        form = VacacionesForm()
    return render(request, 'vacaciones/crear_vaca.html', {'form': form})
# 1) Lista los de usuarios, selecciona el usuario y edita los permisos de descansos anuales (vacaciones) del usuario seleccionado
def list_edit_vaca_1(request):
    if request.user.is_authenticated: 
            # Filtra los objetos Usuario por el usuario autenticado y otros criterios
            efectivo = Usuario.objects.filter(usuario_id=request.user.id)
            if efectivo:
                parque = efectivo[0].parque
                brigada = efectivo[0].brigada
                
            usuarios_brigada = Usuario.objects.filter(parque_id=efectivo[0].parque_id, brigada_id=efectivo[0].brigada_id) if efectivo else None
    else:
            return HttpResponse('<h2>No hemos encotrado usuario</h2>')
    return render(request, 'vacaciones/edit_vaca_list_0.html',  {'efectivos': usuarios_brigada, 'parque': parque, 'brigada': brigada}) 
# 2) lista de los permisos de descansos anuales (vacaciones) del usuario seleccionado
def list_edit_perm_2(request,id):
    vacaciones = Vacaciones.objects.filter(usuario_id=id).order_by('fecha_inicio')
    if vacaciones:
        for acumulados in vacaciones:
            acumulados = vacaciones.aggregate(total_dias=Sum('dias_totales'))['total_dias']
            if acumulados > 30:
                acumulados = "Has excedido el límite de días de vacaciones"
    else:
        return HttpResponse('<h2>No hemos encontrado permisos de vacaciones</h2>')
    return render(request, 'vacaciones/edit_vaca_list_1.html', {'vacaciones': vacaciones, 'usuario': vacaciones[0].usuario,'sumatorio_dias': acumulados,})
# 3) formulario para editar el permiso (vacacicones) seleccionado del un usuario específico ------PENDIENTE-----
def edit_perm_select_3(request, id):
    vacacion = Vacaciones.objects.get(id=id) # Obtiene el objeto Vacaciones que es igual al id de la url
    if request.method == 'POST':
        form = VacacionesForm(request.POST, instance=vacacion)
        if form.is_valid():
            vacacion = form.save(commit=False)
            vacacion.dias_totales = ((vacacion.fecha_fin - vacacion.fecha_inicio) + timedelta(days=1)).days
            vacacion.save()
            return redirect('/home')
        else:
            return HttpResponse('<h2>No hemos podido editar el permiso de vacaciones</h2>')
    form = VacacionesForm(instance=vacacion)
    return render(request, 'vacaciones/edit_vaca.html', {'form': form, 'permiso': vacacion})


# 1) Lista usuarios para eliminar permisos de vacaciones
def list_delete_vaca_1(request):
    if request.user.is_authenticated: 
            # Filtra los objetos Usuario por el usuario autenticado y otros criterios
            efectivo = Usuario.objects.filter(usuario_id=request.user.id)
            if efectivo:
                parque = efectivo[0].parque
                brigada = efectivo[0].brigada
                
            usuarios_brigada = Usuario.objects.filter(parque_id=efectivo[0].parque_id, brigada_id=efectivo[0].brigada_id) if efectivo else None
    else:
            return HttpResponse('<h2>No hemos encotrado usuario</h2>')
    return render(request, 'vacaciones/delete_vaca_list_0.html', {'efectivos': usuarios_brigada, 'parque': parque, 'brigada': brigada})
# 2) lista de los permisos de descansos anuales (vacaciones) del usuario seleccionado
def list_delete_perm_2(request,id):
    vacaciones = Vacaciones.objects.filter(usuario_id=id).order_by('fecha_inicio')
    if vacaciones:
        for acumulados in vacaciones:
            acumulados = vacaciones.aggregate(total_dias=Sum('dias_totales'))['total_dias']
            if acumulados > 30:
                acumulados = "Has excedido el límite de días de vacaciones"
    else:
        return HttpResponse('<h2>No hemos encontrado permisos de vacaciones</h2>')
    
    return render(request, 'vacaciones/delete_vaca_list_1.html', {'vacaciones': vacaciones, 'usuario': vacaciones[0].usuario,'sumatorio_dias': acumulados,})
# 3) Vista para eliminar los permisos de descansos anuales (vacaiones)
def delete_vacaciones(request,id):
    vacacion = Vacaciones.objects.get(id=id) # Obtiene el objeto Vacaciones que es igual al id de la url
    vacacion.delete()
    return redirect('/home')


