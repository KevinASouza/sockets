import socket

def conexao_socket_servidor_tcp(ip: str = 'localhost', porta: int = 9999) -> None:
    """Cria um socket e disponibiliza-o para conexão.

    Args:
        ip (str, optional): Endereço ip do host. . Defaults to 'localhost'.
        porta (int, optional): Porta na qual o host receberá conexões.. Defaults to 9999.
    """
    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #(tipo_protocolo_ip, tipo_protocolo_transporte)

        servidor.bind((ip, porta))

        servidor.listen(1)
        print('Servidor aguardando conexão...')

        info_socket, endereco_cliente = servidor.accept()
        print(f'Conexão estabelecida com {endereco_cliente}')

        tarefa_socket_servidor_tcp(info_socket)

    except socket.error as e:
        print(f'Erro: {e}\nNão foi possível estabelecer conexão.')

    except Exception as ex:
        print(f'Erro: {ex}\nOcorreu um erro inesperado.')
        
    finally:
        servidor.close()


def tarefa_socket_servidor_tcp(socket_servidor: socket.socket) -> bool:
    """Tarefa que o socket realiza ao se estabelecer uma conexão com o mesmo.

    Args:
        socket_servidor (socket.socket): Recebe o socket criado anteriormente.

    Returns:
        bool: Retorna um valor genérico True.
    """
    try:
        while True:

            if not mensagem_cliente:
                break
            
            mensagem_cliente = socket_servidor.recv(1024).decode()

            if mensagem_cliente.lower() == 'sair':
                break

            print(f'[Cliente]: {mensagem_cliente}')

            socket_servidor.send(input('[Você]: ').encode())

    except socket.error as e:
        print(f'Erro: {e}\nA conexão foi encerrada inesperadamente.')

    except Exception as ex:
        print(f'Erro: {ex}\nOcorreu um erro inesperado.')

    finally:
            finalizar_socket(socket_servidor)

    return True

def finalizar_socket(socket_servidor: socket.socket) -> None:
    socket_servidor.close()

conexao_socket_servidor_tcp()