import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

endereco_servidor = ('127.0.0.1', 9999)

while True:
    
    mensagem = input("Digite a mensagem para o servidor UDP (ou 'sair'): ")

    cliente.sendto(mensagem.encode('utf-8'), endereco_servidor)
    
    if mensagem.lower() == 'sair':
        break
        
    dados_resposta, endereco = cliente.recvfrom(1024) 

    if endereco == endereco_servidor:
        print(f"Resposta do Servidor: {dados_resposta.decode('utf-8')}")
    else: 
        'Acesso Negado'

    

cliente.close()
print("Cliente encerrado.")