import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

endereco_servidor = ('localhost', 9999)

while True:
    
    mensagem = input("Digite a mensagem para o servidor UDP (ou 'sair'): ")

    cliente.sendto(mensagem.encode('utf-8'), endereco_servidor)
    
    if mensagem.lower() == 'sair':
        break
        
    dados_resposta, _ = cliente.recvfrom(1024)
    print(f"Resposta do Servidor: {dados_resposta.decode('utf-8')}")

cliente.close()
print("Cliente encerrado.")