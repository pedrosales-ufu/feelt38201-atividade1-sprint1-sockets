# FEELT38201 - Sprint 1 - 1ª Atividade Avaliativa - Sockets

Aluno: Pedro dos Santos Sales

O presente repositório hospeda os arquivos de código referentes à solução da primeira atividade avaliativa da disciplina FEELT38201 - Cibersegurança / Redes de Computadores, sendo estruturado da seguinte forma:

```
feelt38201-atividade1-sprint1-sockets/
├── src/
│   ├── tcp/
│       ├── tcp_client.py
│       └── tcp_server.py
│       └── word_domain.py
│   └── udp/
│   │   ├── time_domain.py
│   │   ├── udp_client.py
│   │   └── udp_server.py
└── README.md
```

## 1. Aplicação de Cliente-Servidor com UDP

O primeiro requisito da atividade é a implementação de uma aplicação cliente-servidor UDP, descrita na seção "2.7.1. Programação de sockets com UDP" do livro "Redes de Computadores e a Internet - Uma Abordagem Top-Down" (8ª Edição, Pearson), dos autores James F. Kurose e Keith W. Ross. Fundamentalmente, a aplicação deve possibilitar a abertura de uma conexão UDP e a troca de dados por meio dela. 

Nesta implementação, o cliente envia uma requisição via datagrama UDP e o servidor processa e retorna a data e a hora atualizadas do sistema.

### 1.1. O sentido da aplicação de Hora Certa na arquitetura cliente-servidor UDP

O protocolo UDP (User Datagram Protocol) é não orientado à conexão, leve, rápido e não garante entrega ordenada ou confiabilidade por si só (best-effort). A consulta de hora encaixa-se perfeitamente nessa natureza porque:

- Mensagens Curtas e Independentes (Datagramas): Tanto a requisição (`"TIME_REQUEST"`) quanto a resposta formatada são payloads pequenos que cabem confortavelmente em um único datagrama sem risco de fragmentação.
- Transações Sem Estado (Stateless): Cada solicitação de horário é um evento isolado. O servidor não precisa manter uma sessão contínua ou histórico de conversações anteriores com o cliente; ele recebe o datagrama, captura o timestamp atual e retorna a resposta instantaneamente.
- Agilidade e Tolerância a Perdas: Se um datagrama eventualmente se perder na rede, a aplicação do cliente conta com um mecanismo de timeout (`3.0s`) que protege o sistema contra travamentos, permitindo novas tentativas imediatas sem o overhead de handshake ou controle de fluxo complexo.

### 1.2. Arquivos de Código

- `time_domain.py`: Contém a lógica de domínio responsável por capturar o momento atual do sistema e formatar a string de data e hora.
- `udp_server.py`: Servidor UDP iterativo que escuta na porta `1205`, recebe o datagrama, processa a requisição chamando o módulo de domínio e retorna o resultado ao endereço de origem do cliente.
- `udp_client.py`: Interface CLI interativa em loop para o cliente enviar requisições de hora, contando com tratamento de exceções para timeout de rede e interrupções.

---

## 2. Aplicação de Cliente-Servidor com TCP

O segundo requisito da atividade é a implementação de uma aplicação cliente-servidor TCP, descrita na seção "2.7.2. Programação de sockets com TCP" do mesmo livro. Fundamentalmente, a aplicação deve possibilitar a abertura de uma conexão TCP e a troca de dados por meio dela. 

Nesta implementação, o cliente envia blocos de texto por uma conexão TCP persistente, e o servidor retorna a contagem de palavras utilizando expressões regulares.

### 2.1. O sentido do contador de palavras na aplicação cliente-servidor TCP

O protocolo TCP (Transmission Control Protocol) é orientado à conexão, confiável, baseado em fluxo de bytes (stream-oriented) e garante a entrega ordenada e sem perdas de dados. O contador de palavras encaixa-se perfeitamente nessa natureza porque:

- Mensagens Contínuas e Fluxo de Caracteres: Textos enviados pelo usuário para análise estatística podem variar em tamanho. O TCP divide e gerencia esse fluxo de bytes de forma transparente, assegurando que nenhum caractere seja corrompido ou chegue fora de ordem.
- Sessões Persistentes: O cliente e o servidor mantêm uma sessão ativa após o estabelecimento via *3-way handshake*, permitindo que múltiplos blocos de texto sejam enviados sequencialmente utilizando a mesma conexão estabilizada.
- Garantia de Integridade: Um contador de palavras precisa processar o texto completo enviado pelo usuário com exatidão. A confiabilidade do TCP garante que todo o payload do texto chegue integralmente ao servidor e que a resposta estruturada seja entregue com precisão ao cliente.

### 2.2. Arquivos de Código

- `word_domain.py`: Contém a lógica de análise e processamento de texto utilizando expressões regulares (`re.findall`) para extração e contagem de palavras.
- `tcp_server.py`: Servidor TCP sequencial/iterativo que aceita conexões na porta `1205` com suporte a reutilização de endereço (`SO_REUSEADDR`), gerencia fluxos orientados a streams de texto e encerra adequadamente as conexões.
- `tcp_client.py`: Cliente TCP interativo que conecta ao servidor, traduz a entrada do usuário em um fluxo baseado em requisições contínuas e exibe o resultado formatado recebido.
