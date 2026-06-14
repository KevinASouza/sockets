# Comunicação via Sockets

Este projeto foi desenvolvido com o objetivo acadêmico de compreender o funcionamento dos **Sockets** e entender como processos em diferentes computadores (ou no próprio host) se comunicam através da rede.

## 📝 Resumo do Projeto

O projeto simula um **chat dinâmico** para o envio de mensagens bilaterais entre duas pontas (Cliente e Servidor). 

---

## 🏗️ Arquitetura do Projeto

A aplicação é dividida em dois componentes principais:

### 🖥️ Socket Servidor
Responsável por inicializar a aplicação e disponibilizar um *endpoint* de escuta. Para simplificar o escopo acadêmico, o servidor foi projetado para aceitar a conexão de **um cliente por vez**.

### 💻 Socket Cliente
Responsável por iniciar o processo de estabelecimento de conexão com o servidor. Ao conectar-se com sucesso, o cliente e o servidor completam o ciclo conhecido na camada de transporte como ***Three-way Handshake***.

---

## ⚙️ Características do Sistema

* **Comunicação Síncrona:** A troca de mensagens ocorre de forma alternada (Half-Duplex), ou seja, apenas um dos *endpoints* pode enviar uma mensagem por vez.
* **Configuração Padrão:**
    * **Endereço IP:** `127.0.0.1` (*localhost*)
    * **Porta de Comunicação:** `9999`

---

## 🚀 Como Executar (Exemplo)

> [!TIP]
> Certifique-se de iniciar o **Servidor** antes de tentar conectar o **Cliente**.

1. Execute o arquivo do Servidor para abrir a porta de comunicação.
2. Execute o arquivo do Cliente para conectar-se ao IP e porta configurados.
