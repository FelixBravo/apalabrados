# Proyecto de Diagnóstico "Apalabrados"



## Acerca del proyecto Apalabrados

Apalabrados es un primer desafío del programa PlatziMaster, para evaluar las habilidades técnicas de los Masters (participantes del programa), del cual soy parte.

##Descripción del desafío

| Function name | Description                    |
| ------------- | ------------------------------ |
| `Categoria`      | MiniJuego.       |
| `Enfoque`      | Transversal.       |
| `Level`      | Basic.       |
| `Tipo`      | Lógica.       |


### ¡Juguemos a separar caracteres!

Para este reto debes crear una base de datos con las siguientes tablas: 

* numeros. Columnas: número, acumulado
* texto. Columnas: texto, inicial, final
* caracteres: Columnas: caracter

Debes realizar una aplicación que a través de un input analizará lo que ha ingresado el usuario y de acuerdo al tipo de valor, realizará las siguientes acciones:

* Si es un número, lo guarda en la tabla numeros. En la columna número guardará el input y acumulará el valor con los valores anteriores de la misma tabla, este se almacenará en acumulado.
* Si es un texto, debe almacenar en la tabla texto. Guarda el input en la columna texto, el caracter inicial se guarda en la columna inicial y el caracter final se guarda en la columna final.
* Si el input tiene algún caracter especial como tilde, coma, punto y coma, punto, numeral o parecidos, debe extraerlo del input y enviar el caracter a la tabla caracteres, columna caracter. El resto del input se descarta.

### Entregable

* Debes enviar la url de tu proyecto en github, debe estar público y contar con un README.md con las instrucciones de uso de la aplicación.
* Debes desplegar esta aplicación y enlazar esta url en el README del proyecto. 
* Debes dejar indicaciones de descarga del repositorio.
* Debes entregar el diagrama de flujo de esta aplicación como parte de tu README.

### Uso de la Aplicación

La aplicación fue desarrollada con python 3, es una aplicación de consola y para poder ejecutarla se deben seguir los siguientes pasos en ambiente mac, para windows o linux, podría haber alguna modificación en los comandos.

1. Clonar el repositorio de github donde esta alojado el proyecto, en una carpeta vacia para tener mayor control, el comando es el siguiente:
`$ git clone https://github.com/FelixBravo/apalabrados.git`

2. Después de clonar, entras al directorio "apalabrados".
`$ cd apalabrados`

3. Listas los archivos:
`$ ls`
		**README.md**: archivo que contiene la información del proyecto.
		**apalabrados.db**: archivo con la base de datos del proyecto.
		**base.py**: archivo python con la declaración base y motor de la base de datos.
		**main.py**: archivo principal del proyecto que contiene la programación.
		**modelo.py**: archivo secundario que contiene el modelo de la base de datos.

4. Instalar libreria sqlalchemy, se recomienda hacerlo en ambiente [Virtual](https://m-monroyc22.medium.com/configurar-entorno-virtual-python-a860e820aace "Virtual") para evitar conflictos con otros proyectos:
Iniciar ambiente virtual = `$ python3 -m venv venv`
Activar ambiente virtual = `$ source venv/bin/activate`
Finalmente para la instalación de la libreria:
`$ pip install sqlalchemy`

5. Ejecución del proyecto, siempre que quieras ejecutar el proyecto debes tipear lo siguiente:
`$ python3 main.py`

6. El proyecto pedira ingresar algo!
`$ Enter something:`
Debes ingresar lo que quieras, según lo solicitado en el desafío, números, letras, caracterés especiales, etc.

7. La Base de Datos que estoy utilizando para el desafío es "SQLite", que viene en el paquete de instalación de python3, por lo cual, no tendrás que instalar nada. Para revisar que todo lo que ingresas en el programa queda bien guardado en la Base de datos según el desafío, se debe realizar lo siguiente;

		Primero debes verificar que estas en la carpeta del proyecto y ejecutar: `$ sqlite3`
		Ahora se debe abrir el archivo de la base de datos apalabrados.db: `$ .open apalabrados.db`
		Con el comando `$ .tables` puedes ver las tablas del proyecto, "caracteres" "numeros" y "textos", las cuales contendrán la información según lo solicitado en el desafío.
		Para poder ver la información de una tabla, se debe realizar un select común y corriente como sigue: `$ select * from numeros;`


Fin!, muchas gracias por leer, sientete libre si quieres mejorar el proyecto. Saludos.
