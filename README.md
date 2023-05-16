# 2023-1-Grupo-16: RateYourSeat  
## Ingeniería de Software CC4401-1 Otoño 2023  
**Integrantes:**  
- Nicolás Calbucura  
- Gonzalo Cisternas  
- Leonel Espinoza  
- Katia Fredes  
- Javiera Jiménez  

# Sprint 1  
##### _Fecha:_ 16-05-2023   

## Notas de Versión:  
+ Se implemento el registro de usuarios, los cuales se agregan a la base de datos del proyecto.  
+ Se crearon todas las tablas que se proyectan necesarias para la aplicación.  
+ Se crearon los archivos del fornt-end del inicio, registro e inicio de sesion de la aplicación.  

## Direcciones y funcionalidades  
+ **`/home`**:  
Página principal de la aplicación. Aqui se presentarán las reseñas más recientes o populares y habrá un filtro para buscar reseñas. En la esquina superior derecha hay un botón para iniciar sesión el cuál dirige al usuario a `/log_in`.  

+ **`/log_in`**:  
Página para iniciar sesion donde se presenta un form simple que pide el email del usuario y su contraseña. Si la informacion entregada es correcta el botón iniciar sesion dirige a `/home`, si es incorrecta indica los campos a corregir. Abajo del botón para iniciar sesion se encuentra un link a `/sign_up` en caso de que el usuario necesite crear su cuenta.  

+ **`/sign_up`**:  
Página para registrarse en la aplicación y agregar un nuevo usuario a la base de datos. Aqui se encuentra un form donde se pide nombre de usuario, email y contraseña, una vez se completan correctamente se envia la informacion con `'POST'` y se procesan los datos para agregarlos a la base de datos. Una vez agregados a la base de datos redirige a `/home`  
