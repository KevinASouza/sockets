import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #(tipo_protocolo_ip, tipo_protocolo_transporte)

endereco_servidor = ('localhost', 9999)

cliente.connect(endereco_servidor)

print('Digite uma mensagem ou `sair` para encerrar a conexão\n')

while True:

    mensagem = input('[Você]: ')

    cliente.send(mensagem.encode())

    if mensagem == 'sair':
        break

    print(f'[Colega]: {cliente.recv(1024).decode()}')

cliente.close()

