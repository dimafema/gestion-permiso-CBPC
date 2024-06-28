from django import forms
from .models import Usuario, Parque, Zona, Brigada
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

class UsuarioCreationForm(UserCreationForm):
    numero_casco = forms.IntegerField(required=True)
    zona = forms.ModelChoiceField(queryset=Zona.objects.all(), required=True)
    parque = forms.ModelChoiceField(queryset=Parque.objects.all(), required=True)
    brigada = forms.ModelChoiceField(queryset=Brigada.objects.all(), required=True)

    class Meta:
        model = User  # Aquí especificas el modelo User, no tu modelo Usuario
        fields = ('username','email','first_name', 'last_name','password1', 'password2', 'numero_casco', 'zona', 'parque', 'brigada')

    def save(self, commit=True):
        user = super().save(commit=False)
        # Aquí puedes manejar los campos adicionales
        if commit:
            user.save()
            # Crear y guardar el objeto Usuario relacionado
            Usuario.objects.create(
                usuario=user,
                numero_casco=self.cleaned_data['numero_casco'],
                zona=self.cleaned_data['zona'],
                parque=self.cleaned_data['parque'],
                brigada=self.cleaned_data['brigada']
            )
        return user

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'numero_casco',
            'zona',
            'parque',
            'brigada',
        ]
       

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
         ]


    
class ParqueForm(forms.ModelForm):
    class Meta:
        model = Parque
        fields = '__all__'
        
class ZonaForm(forms.ModelForm):
    class Meta:
        model = Zona
        fields = '__all__'
        
class BrigadaForm(forms.ModelForm):
    class Meta:
        model = Brigada
        fields = '__all__'
        
# class VacacionesForm(forms.ModelForm):
#     class Meta:
#         model = Vacaciones
#         fields ='__all__'
#         widgets = {
#             'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
#             'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
#             'dias_totales': forms.HiddenInput(),
#         }  

class LoginForm(AuthenticationForm):
   class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }