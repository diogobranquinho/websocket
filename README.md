# Exemplo de WebSocket em Python

Exemplos simples de comunicação entre o navegador e um servidor via WebSocket, usando o
microframework Tornado.

Numa página web comum, o navegador pede e o servidor responde. Com o **WebSocket** a
conexão fica aberta: o navegador e o servidor podem enviar mensagens um para o outro a
qualquer momento. É isso que permite, por exemplo, o servidor avisar todos os navegadores
quando chega uma mensagem nova no chat.

## Pré-requisitos

- Python 3
- Microframework Tornado:

```
pip install tornado
```

## Arquivos

| Pasta    | Arquivos                         | O que faz                                                  |
|----------|----------------------------------|------------------------------------------------------------|
| `repete` | `serverrepete.py`, `repete.html` | O servidor devolve cada mensagem enviada pelo navegador    |
| `chat`   | `serverchat.py`, `chat.html`     | Chat: cada mensagem é enviada para todos os conectados     |

Em cada pasta, o servidor entrega a página (`.html`), e o JavaScript da página abre a
conexão WebSocket com o servidor.

## Passo a passo

### 1. Repete

```
cd repete
python3 serverrepete.py
```

Abra no navegador http://localhost:8888 e envie mensagens. O servidor devolve cada uma:

```
Você disse: Ola turma
Servidor repete: Ola turma
```

### 2. Chat na sua máquina

```
cd chat
python3 serverchat.py
```

Abra http://localhost:8887 em duas ou mais abas do navegador, informe um nome diferente
em cada uma e converse. Cada mensagem aparece em todas as abas.

### 3. Chat com a turma

Agora um colega será o servidor e todos os outros vão se conectar a ele.

No computador do colega que será o servidor:

1. Descubra o IP da máquina (`ipconfig` no Windows, `ip addr` no Linux, `ifconfig` no macOS).
2. No arquivo `chat.html`, troque `localhost` por esse IP:

```
var ws = new WebSocket("ws://192.168.0.10:8887/websocket");
```

3. Pare o servidor (CTRL+C) e execute de novo:

```
python3 serverchat.py
```

Os demais alunos não alteram nada: basta abrir no navegador o endereço do servidor,
por exemplo http://192.168.0.10:8887.

## Exercícios sugeridos

1. No exemplo repete, abra duas abas. A mensagem enviada em uma aparece na outra? Por quê?
2. No chat, abra uma nova aba depois que algumas mensagens já foram enviadas. O que ela mostra? Por quê?
3. Compare o repete e o chat: o que o servidor do chat faz de diferente com cada mensagem recebida?

## Observações importantes

**Reinicie o servidor depois de alterar o HTML.** O Tornado guarda a página em memória
enquanto está rodando. Se o `chat.html` for alterado com o servidor ligado, os
navegadores continuam recebendo a versão antiga.

**Abra a página pelo endereço do servidor.** Abrir o arquivo `chat.html` direto no
navegador (clicando duas vezes no arquivo) não funciona: o servidor recusa a conexão.
Sempre use `http://IP_DO_SERVIDOR:8887`.

**Firewall.** Na máquina do servidor, o firewall do sistema pode bloquear as conexões dos
colegas ou pedir permissão na primeira execução.

**Uso didático.** Estes exemplos são para estudo: não possuem autenticação nem
criptografia e não devem ser usados como base para sistemas em produção.

## Referências

https://www.tornadoweb.org/en/stable/websocket.html

## Autor

* **Diogo Branquinho Ramos** - [diogobranquinho](https://github.com/diogobranquinho)
