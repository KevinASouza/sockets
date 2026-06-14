import socket
from servidor_tcp import finalizar_socket

def conexao_socket_cliente_tcp(ip: str = 'localhost', porta: int = 9999):
    """Cria um socket e inicia o handshake de três vias junto ao socket servidor que esteja aguardando conexão.

    Args:
        ip (str, optional): Endereço IP do host. Defaults to 'localhost'.
        porta (int, optional): Porta na qual o host estará recebendo conexões. Defaults to 9999.
    """
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #(tipo_protocolo_ip, tipo_protocolo_transporte)

        cliente.connect((ip, porta))

        tarefa_socket_cliente_tcp(cliente)

    except socket.error as e:
        print(f'Erro: {e}\nNão foi possível estabelecer conexão.')

    except Exception as e:
        print(f'Erro: {e}\nOcorreu um erro inesperado.')
        
    finally:
        finalizar_socket(cliente)


def tarefa_socket_cliente_tcp(socket_cliente: socket.socket) -> bool:
    """Tarefa que o socket realiza ao se estabelecer uma conexão com o servidor.

    Args:
        socket_cliente (socket.socket): Recebe o socket criado anteriormente.

    Returns:
        bool: Retorna um valor genérico True.
    """
    
    print('Digite uma mensagem ou `sair` para encerrar a conexão\n')
    try:
        while True:

            mensagem = input('[Você]: ')

            socket_cliente.send(mensagem.encode())

            if not mensagem:
                break

            if mensagem.lower() == 'sair':
                break

            print(f'[Servidor]: {socket_cliente.recv(1024).decode()}')

    except socket.error as e:
        print(f'Erro: {e}\nA conexão foi encerrada inesperadamente.')

    except Exception as ex:
        print(f'Erro: {ex}\nOcorreu um erro inesperado.')

    finally:
        finalizar_socket(socket_cliente)

    return True

def main() -> None: 
    conexao_socket_cliente_tcp()

if __name__ == '__main__':
    main()

