
from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home, name='home'),
    path('condiciones_uso', views.cond_uso, name='condiciones_uso'),
    path('proyecto', views.proyecto, name='proyecto'),
    path('', views.login_page, name='inicio'),
    path('registro/', views.registro_user, name='register'),
    
    # ZONAS
    path('crear_zona/', views.crear_zona, name='crear_zona'),
    #------------------------------------------------------------------------------------
    path('list_edit_zona/', views.list_edit_zona, name='list_edit_zona'),
    path('edit_zona/<int:id>/', views.editar_zona, name='editar_zona'),
    #------------------------------------------------------------------------------------
    path('list_delete_zona/', views.list_delete_zona, name='list_delete_zona'),
    path('eliminar_zona/<int:id>/', views.eliminar_zona, name='eliminar_zona'),
    
    # PARQUES
    path('crear_parque/', views.crear_parque, name='crear_parque'),
    #------------------------------------------------------------------------------------
    path('list_edit_parque/', views.list_edit_parque, name='list_edit_parque'),
    path('edit_parque/<int:id>/', views.editar_parque, name='editar_parque'),
    #------------------------------------------------------------------------------------
    path('list_delete_parque/', views.list_delete_parque, name='list_delete_parque'),
    path('eliminar_parque/<int:id>/', views.eliminar_parque, name='eliminar_parque'),
    
    # BRIGADAS
    path('crear_brigada/', views.crear_brigada, name='crear_brigada'),
    #------------------------------------------------------------------------------------
    path('list_edit_brigada/', views.list_edit_brigada, name='list_edit_brigada'),
    path('edit_brigada/<int:id>/', views.editar_brigada, name='editar_brigada'),
    #------------------------------------------------------------------------------------
    path('list_delete_brigada/', views.list_delete_brigada, name='list_delete_brigada'),
    path('eliminar_brigada/<int:id>/', views.eliminar_brigada, name='eliminar_brigada'),
    
    # USUARIOS
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    #------------------------------------------------------------------------------------
    path('list_edit_user/', views.list_edit_user, name='list_edit_user'),
    path('edit_usuario/<int:id>/', views.editar_usuario, name='editar_user'),
    #------------------------------------------------------------------------------------
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('list_delete_user/', views.list_delete_user, name='list_delete_user'),
    
    # VACACIONES
    path('list_crear_vacaciones', views.list_crear_vaca_1, name='list_crear_vacaciones'),
    path('crear_vacaciones/<int:id>/', views.crear_vaca_2, name='crear_vacaciones'),
    #------------------------------------------------------------------------------------
    path('list_edit_vacaciones', views.list_edit_vaca_1, name='list_edit_vacaciones'),
    path('edit_vacaciones/<int:id>/', views.list_edit_perm_2, name='edit_vacaciones'),
    path('edit_perm/<int:id>/', views.edit_perm_select_3, name='edit_perm'),
    #------------------------------------------------------------------------------------
    path('list_delete_vacaciones/', views.list_delete_vaca_1, name='list_delete_vacaciones'),
    path('delete_vacaciones/<int:id>/', views.list_delete_perm_2, name='delete_vacaciones'),
    path('delete_perm/<int:id>/', views.delete_vacaciones, name='delete_perm'),
]