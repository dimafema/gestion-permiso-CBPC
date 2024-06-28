from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UsuarioForm, ParqueForm, ZonaForm, BrigadaForm, RegisterForm, UsuarioCreationForm
from .models import  Parque, Zona, Brigada, Usuario
from datetime import timedelta

# página de incio
def panel_crear(request):
    usuarios = {'usuarios': Usuario.objects.all()}
    return render(request, 'panel_crear.html', usuarios)

def cond_uso(request):
    return render(request, 'condicionesuso.html')

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

def registro_user(request):
    form = UsuarioCreationForm()
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Usuario creado correctamente')
            form.save()
            return redirect('/home')
    return render(request, 'user/registro_user.html', {'form': form})

# Vista para crear un nuevo usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/crear_user.html', {'form': form},)


# Vista para crear un nueva zona
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


# Vista para crear un nuevo parque
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


# Vista para crear un nueva brigada
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


# Vista para editar un usuario existente
def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('/', id=id)
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
    usuarios = {'usuarios': Usuario.objects.all()}
    return render(request, 'usuario/lis_user_edit.html', usuarios)
# Vista que muestra una lista de usuarios para eliminar
def list_delete_user(request):
    usuarios = {'usuarios': Usuario.objects.all()}
    return render(request, 'usuario/lis_user_delete.html', usuarios)


# # Vista para crear los permisos de descansos anuales (vacaiones)
# def crear_vacaciones(request):
#     if request.method == 'POST':
#         form = VacacionesForm(request.POST)
#         if form.is_valid():
#             vacaciones = form.save(commit=False)
#             vacaciones.dias_totales = ((vacaciones.fecha_fin - vacaciones.fecha_inicio) + timedelta(days=1)).days
#             vacaciones.save()
#             return redirect('/home')
#     else:
#         form = VacacionesForm()
#     return render(request, 'vacaciones/crear_vacaciones.html', {'form': form},)
# # Vista para editar los permisos de descansos anuales (vacaiones)
# def editar_vacaciones(request,id):
#     vacaciones = get_object_or_404(Vacaciones, id=id)
#     if request.method == 'POST':
#         form = VacacionesForm(request.POST, instance=vacaciones)
#         if form.is_valid():
#             vacaciones = form.save(commit=False)
#             vacaciones.dias_totales = ((vacaciones.fecha_fin - vacaciones.fecha_inicio) + timedelta(days=1)).days
#             vacaciones.save()
#             return redirect('/list_edit_vacaciones',)
#     else:
#         form =VacacionesForm(instance=vacaciones)
#     return render(request, 'vacaciones/editar_vacaciones.html', {'form': form})
# # Vista para eliminar los permisos de descansos anuales (vacaiones)
# def eliminar_vacaciones(request,id):
#     vacaciones = get_object_or_404(Vacaciones, id=id)
#     if request.method == 'POST':
#         form = VacacionesForm(request.POST, instance=vacaciones)
#         for field in form.fields.values():
#             field.disabled = True
#         if form.is_valid():
#             vacaciones.delete()
#             return redirect('/list_delete_vacaciones',)
#     else:
#         form =VacacionesForm(instance=vacaciones)
#         for field in form.fields.values():
#             field.disabled = True
#     return render(request, 'vacaciones/delete_vacaciones.html', {'form': form})
# # Vista que muestra una lista de usuarios para crear permisos de vacaciones
# def list_vacaciones_user(request):
#     vacaciones = { 'vacaciones': Vacaciones.objects.all()}
#     return render(request, 'vacaciones/lis_user_vacaciones.html', vacaciones)
# # Vista que muestra una lista de usuarios para editar permisos de vacaciones
# def list_edit_vacaciones(request):
#     vacaciones = {'vacaciones': Vacaciones.objects.all()}
#     return render(request, 'vacaciones/lis_vacaciones_edit.html', vacaciones)
# # Vista que muestra una lista de usuarios para eliminar permisos de vacaciones
# def list_delete_vacaciones(request):
#     vacaciones = {'vacaciones': Vacaciones.objects.all()}
#     return render(request, 'vacaciones/lis_vacaciones_delete.html', vacaciones)
