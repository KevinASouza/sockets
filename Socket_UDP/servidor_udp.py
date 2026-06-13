import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind(('localhost', 9999))

print("Servidor UDP pronto e ouvindo na porta 9999...")

while True:

    dados, endereco_cliente = servidor.recvfrom(1024)
    mensagem = dados.decode('utf-8')
    
    print(f"Recebido de {endereco_cliente}: {mensagem}")
    
    if mensagem.lower() == 'sair':
        print("Encerrando servidor...")
        break
    resposta = f"UDP: {mensagem}"
    servidor.sendto(resposta.encode('utf-8'), endereco_cliente)

servidor.close()
print("Servidor encerrado.")