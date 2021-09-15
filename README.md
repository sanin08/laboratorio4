# ST0263-jssaninv

# Titulo
Laboratorio 4

# Autor
Juan Sebastián Sanín Villarreal

# Software
Reto 2 colas

# Descripción
El programa consiste en agregar a una cola en el Middleware en Rabbitmq, donde tenemos varios publisher enviando requerimientos, los subscribers toman las solicitudes en la cola de la manera en la que llegaron y empiezan a dar respuesta a cada solicitud, las solicitudes son suma, resta, multiplicación y división, tomando este programa como una calculadora, el subscriber toma los valores numericos y la operación y le da respuesta la cual es enviada al correo como notificación 

# Diseño
Hay una instancia en AWS la cual esta clonado todo el proyecto en él, también se puede ingresar a rabbitmq donde podemos ver todo el comportamiento de las colas, tanto cuando el publisher manda una solicitud y queda registrada en la cola, como también podemos ver cuando el subscriber cumple todas las peticiones y la cola queda vacia. En sintesis el diseño se basa en un intermediario middleware en vez de un protocolo, donde conecta a los publishers con los subscribers

# Instalación
Instalar pika `pip install pika`

# Ejecución
Para evitar la utilización de ip quemada en código, al ejecutar el programa en la instancia con el siguiente código:
para el publisher: `$python3 publishers.py 54.161.183.209 5672`
para el subscriber:`$python3 subscribers.py 54.161.183.209 5672`
El user de rabbitmq es user
El password de rabbitmq es password
