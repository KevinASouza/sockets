import socket


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #(tipo_protocolo_ip, tipo_protocolo_transporte)

servidor.bind(('localhost', 9999))

servidor.listen(1)

sock, endereco = servidor.accept()

while True:

    mensagem = sock.recv(1024)

    mensagem_convertida = mensagem.decode()

    if mensagem_convertida == 'sair':
        break

    print(f'[Colega]: {mensagem_convertida}')

    sock.send(input('[Você]: ').encode())
 
servidor.close()

