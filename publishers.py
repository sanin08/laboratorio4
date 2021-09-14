import pika
import sys
def ipPuerto():

    if len(sys.argv) == 3:
        ipElastica = sys.argv[1]
        puerto = sys.argv[2]
        print('ip:', ipElastica,'\n puerto:', puerto)
        
    else:
        print('Para iniciar el programa debe ingresar de la siguiente forma: $python3 publisher.py ip-sever port')
        print('$python3 publisher.py 54.161.183.209 5672\n')

    return ipElastica, puerto
ipElastica,puerto = ipPuerto()
connection = pika.BlockingConnection(pika.ConnectionParameters(ipElastica, puerto, '/',
pika.PlainCredentials('user', 'password')))
channel = connection.channel()
seguir=True
print("Ingrese su usuario")
usuario = input(">")
print("Ingrese su correo")
correo=input(">")
while seguir:
    print("Escriba la solicitud que quiera hacerle a la calculadora(Mantener mayusculas en la petición)")
    print("Si desea sumar escriba SUMAR")
    print("Si desea sumar escriba RESTAR")
    print("Si desea sumar escriba MULTIPLICAR")
    print("Si desea sumar escriba DIVIDIR")
    print("Si desea salir escribir SALIR")
    operacion=input(">")
    if operacion=="SALIR":
        seguir=False
        numero1=0
        numero2=0
        mensaje= usuario + '_' + correo + '+' + operacion + ',' + numero1 + '-' + numero2
        channel.basic_publish(exchange='my_exchange', routing_key='test', body=mensaje)
        print("Runnning Producer Application...")
    else:
        print("Ingrese los numeros a operar")
        numero1=input(">")
        numero2=input(">")
        mensaje= usuario + '_' + correo + '+' + operacion + ',' + numero1 + '-' + numero2
        channel.basic_publish(exchange='my_exchange', routing_key='test', body=mensaje)
        print("Runnning Producer Application...")
mensaje= usuario + '_' + correo + '+' + operacion + ',' + numero1 + '-' + numero2
channel.basic_publish(exchange='my_exchange', routing_key='test', body=mensaje)
print("Runnning Producer Application...")
connection.close()