[![Build Status](https://snap-ci.com/srmf9/Proyecto-IV/branch/master/build_image)](https://snap-ci.com/srmf9/Proyecto-IV/branch/master) [![Heroku](https://www.herokucdn.com/deploy/button.png)](http://dai-bares.herokuapp.com/)

# Bares DAI

##Práctica 7. Puesta en producción.

Lo primero que realize es poner el parámetro DEBUG del archivo settings.py a False,para que no muestre los posibles errores que puede generar la aplicación.
Tambíen  en este archivo modificaremos la siguiente línea:  
``ALLOWED_HOSTS = ['*']
``  
Con esto ya tenemos la depuración para el desarrolo desactivada. Ahora debemos desplegar la aplicación en un servidor web de producción como Heroku. Lo he conseguido de la siguiente manera:  
## Despliege en un Paas: Heroku  

Lo primero de todo será crear un nuevo fichero llamado Procfile con el siguiente contenido: 
 
web: gunicorn aplicacion.wsgi --log-file -  

Actualizaremos nuestro fichero de requirements.txt con las siguientes líneas:  

Django==1.8.5  
djangorestframework==3.3.0   
wheel==0.24.0  
django-toolbelt==0.0.1  
gunicorn==19.3.0  

Y también deberé crear un fichero llamado runtime.txt para indicarle a Heroku que versión de Python es la que estoy utilizando. El contenido del archivo es el siguiente:  

python-2.7.10  

Para conseguir que me funcione bootstrap he tenido que añadir en el archivo settings.py  la siguiente línea para que me coja las imagenes del static:     
``STATICFILES_STORAGE = whitenoise.django.GzipManifestStaticFilesStorage'
``  
Tambien en el archivo  wsgi.py he añadido las siguientes líneas:  
```
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
```
Una vez que realizamos estos pasos procedo a subir la aplicación a [GitHub](https://github.com/srmf9/Bares.git)
 
 Ahora procemos a subirla a Heroku para ello me situo en el directorio raiz de la aplicación y introduzco las siguientes ordenes:    


* heroku login
* heroku create


* git push heroku master

Y ya la tendriamos desplegada en Heroku: [enlace a la aplicación](http://dai-bares.herokuapp.com/)    
![imagen](http://i1028.photobucket.com/albums/y349/Salva_Rueda/Captura%20de%20pantalla%20de%202015-11-30%20020029_zpsopmgr62l.png)

##Snap CI

Nuestro objetivo ahora es automatizar para que cuando realizemos un "push" a nuestro repositorio se realice el despliegue automático. Para este objetivo he utilizado Snap CI porque es el que he comprendido con más facilidad. 
Lo primero que debemos hacer es registarnos a través de GitHub, darle permisos para que pueda acceder a nuestro GitHub e indicarle en los repositorios que queremos que trabaje.   
Ahora para que pase los test debemos insertar las siguientes líneas por la terminal:  

* pip install -r requirements.txt   
* make test
 
Ahora añadimos un nuevo stage con las credenciales de Heroku y el nombre de nuestra aplicación:  
![foto](http://i1028.photobucket.com/albums/y349/Salva_Rueda/Captura%20de%20pantalla%20de%202015-11-30%20013710_zpsxbohqpcc.png)    

Recordar tener activado la opción wait for CI  to pass before  deploy en Heroku:  
![foto](http://i1028.photobucket.com/albums/y349/Salva_Rueda/7_4_zpsoo6veo9a.png)  
Ya tenemos la integración continua que se pasará siempre que realizemos un push:  
![foto](http://i1028.photobucket.com/albums/y349/Salva_Rueda/Captura%20de%20pantalla%20de%202015-11-30%20014357_zpsy9ftmkcr.png)  

Por último comentar que me fue muy util a la hora de encontrar un fallo en mi aplicación consultar los logs que nos devuelve Heroku. Se consulta de la siguiente forma:  
 
 heroku logs --app encuesta > log.txt
  