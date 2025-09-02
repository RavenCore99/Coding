------------                            README                  -------                    

                        Actividad CADI: Operaciones con lenguajes Finitos


Trabajo elaborado por:

Grupo A
Miembros: Ethan Mateo Torres // Nicolas C. Ballesteros

Para el desarrollo de la actividad propuesta, se desempeño el trabajo conjunto, elaborado en Visual Studio con lenguaje Python, donde en la Rama 1 se trabajo en grupo, mientras que La Rama 2 Fue desarrollada por Etham Torres y la Rama 3 por Nicolas Ballesteros.

------
Comandos a utilizar
------
--- git init  : Utilizado dentro del directorio de la carpeta en el disco al ejecutar la ruta en la terminal Para inicializar el proceso de la transferencia de archivos al repositorio

--- git add .  : para agregar a dicho directorio las indicaciones siguientes

--- git commit -m "Primer repositorio"  : usado para dar el mensaje de actualizacion en el proceso

----- una vez actualizado, se cargan los archivos dentro de la carpeta (en este caso vendrian siendo // README.md / Rama1.py / Rama2.py /Rama3.py)

--- ahora para cargar directamente al repositorio hacemos lo siguiente

--- se copia la URL del repositiorio ej. (https://github.com/usuario/nombre_repositorio)
--- teniendo copiada la URL hacemos :

--- git remote add origin https://github.com/usuario/nombre_repositorio *

finalmente para subir los archivos ejecutamos

--- git push -u origin master/main    (segun como se haya creado se usa main o master)

y listo. Asi se pueden cargar los archivos por medio de comandos en la terminal

para ir actualizando procesos en el repositorio tambien se usaron comandos

usando

--- git status :  para comprobar cambios recientes
--- git add . / para reescribir cambios
--- git commit -m "se actualizo README"
--- git push origin master : para cargar nuevamente 

y asi queda actualizado el repositorio segun se vayan viendo cambios.


-----------------------------------------------

Sobre pull Request 
En el caso de nuestro equipo se desarrollo el codigo de forma colaborativa pero en diferentes archivos y al final se ajustaron y se cargaron a una misma carpeta para cargar en el repositorio. los ajustes se realizaron en su gran mayoria en Visual Studio antes de pasarse a GitHub. Tambien se usaron compiladores Online por fallas en archivos de instalacion de Python para comprobar funcionalidad del codigo. 

Para el desarrollo se usaron diversas definiciones en variables para organizar y estructurar el codigo por partes para mayor orden en la vista del codigo y facilidad de entendimiento. 

usando "def" como funcion principal para el request de los parametros que se iban definiendo de acuerdo a los requisitos de la actividad 

Se siguio la estructura logica que ofrece Python para escribir el codigo con variables correspondientes de acuerdo a los requisitos en la plataforma. A la vez que se estructuro los lenguajes dados por los datos y de ahi mismo se partio el desarrollo de cada ejercicio segun se iban siguiendo las indicaciones para mostrar lo que se esta solicitando en un codigo que se divide en 4 archivos .py distintos, cada uno de ellos muestra una estructura unica de acuerdo al ejercicio dado y uno de esos archivos .py se encarga de ejecutar los 3 anteriores ejercicios en un solo llamado a eleccion del usuario para facilitar mas el resultado. 
--------------------------- 

Guia de clonacion de repositorio 

----
En nuestro caso para ello hacemos lo siguiente:

-- en una carpeta vacia y reconocible -. clic derecho > abrir en terminal ---
-- > Se utiliza el comando en terminal "git clone" seguido de la URL del repositorio "https://github.com/RavenCore99/Coding.git"

"Se recomienda crear una carpeta vacia para almacenar los archivos del repositorio para evitar conflictos con perdida de datos"

una vez cargado el repositorio se puede hacer lo siguiente:
-- opcion 1.. Abrir directo la carpeta con el nombre del respositorio (Coding es el nombre del repositorio), luego clic derecho y abrir con terminal .... ahi ejecutas el script en terminal con "python main.py"

-- opcion 2.. Con la misma terminar que creaste la copia del repositorio usas el comando "cd" seguido de "Coding" que es el nombre de la carpeta contenedora de los archivos del repositorio / luego de estar en ruta con la carpeta ejecutas "python main.py"

-- opcion 3.. cargar la carpeta en visual studio y abrir el codigo del archivo "main.py" y dar ejecutar el codigo 

-------------------------------------------------------------------------------------------------

El codigo ejecutandose por "main.py" ejecuta de forma interactiva con el usuario que se desea hacer de acuerdo a los ejercicios planteaods.-----------------------------------------------