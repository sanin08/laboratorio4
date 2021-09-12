import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('54.161.183.209', 5672, '/',
pika.PlainCredentials("user", "password")))
channel = connection.channel()
def callback(ch, method, properties, body):
    body=body.decode()
    indice1 = body.find("+")
    indice2 = body.find(",")
    indice3 = body.find("-")
    indice4 = body.find("_")
    correo=body[indice4+1:indice1]
    if body[indice1+1:indice2]=="SUMAR":
               numero1 = body[indice2+1:indice3]
               numero2 = body[indice3+1:len(body)]
               suma = int(numero1) + int(numero2)
               body = str(suma)+ " La respuesta fue enviada al correo:" + correo 
               #print("SUMA: " + str(body))
    if body[indice1+1:indice2]=="RESTAR":
               numero1 = body[indice2+1:indice3]
               numero2 = body[indice3+1:len(body)]
               resta = int(numero1) - int(numero2)
               body = str(resta)+ " La respuesta fue enviada al correo:" + correo 
               #print("RESTA: " + str(body))
    if body[indice1+1:indice2]=="MULTIPLICAR":
               numero1 = body[indice2+1:indice3]
               numero2 = body[indice3+1:len(body)]
               multiplicacion = int(numero1) * int(numero2)
               body = str(multiplicacion)+ " La respuesta fue enviada al correo:" + correo 
               #print("MULTIPLICACIÓN: " + str(body))
    if body[indice1+1:indice2]=="DIVIDIR":
               numero1 = body[indice2+1:indice3]
               numero2 = body[indice3+1:len(body)]
               division = int(numero1) / int(numero2)
               body = str(division)+ " La respuesta fue enviada al correo:" + correo 
               #print("DIVISIÓN: " + str(body))
    print(body)




channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()