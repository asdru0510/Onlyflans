from django.contrib import messages
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

def crear_usuario(request, username:str, first_name:str, email:str, password:str,pass_confirm:str):
    if password != pass_confirm:
        messages.warning(request, 'Las contraseñas no coinciden')
        return False
    #Si llega aqui es porque el password coincide
    if len(password) > 50: 
        messages.warning(request,'La contraseña supera los 50 caracteres maximos permitidos')
        return False
    #Si llega aqui es porque password es menor a 50 caracteres
    try:
        user = User.objects.create_user(
            username=username, 
            first_name=first_name, 
            email=email, 
            password=password
            )
    except IntegrityError:
        messages.warning(request, 'El usuario ya existe')
        return False
    
    except Exception:
        messages.warning(request, 'Error al crear el usuario')
        return False
    #Si llega aqui es porque se creo el usuario
    messages.success(request, 'Usuario creado exitosamente.')
    return True