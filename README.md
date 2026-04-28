# Relatório de Atividade de ARI
## Instalação e Configuração de Ambiente Virtual com Ubuntu Desktop 24.04 LTS

---

## 1. Criação da Máquina Virtual no VirtualBox

A máquina virtual foi criada no VirtualBox, seguindo os requisitos mínimos recomendados pela Canonical para o Ubuntu Desktop 24.04 LTS:

- **Sistema Operacional:** Ubuntu (64-bit)
- **Memória RAM:** 4096 MB (mínimo recomendado)
- **Armazenamento:** 25 GB (mínimo recomendado)
- **Memória de Vídeo (VRAM):** 128 MB
- **Placa de Rede:** NAT

---

## 2. Instalação do Ubuntu Desktop 24.04 LTS

A máquina virtual foi iniciada com a imagem ISO do Ubuntu Desktop 24.04 LTS. O processo de instalação foi seguido conforme o assistente do sistema operacional, resultando em um ambiente funcional ao final do processo.

---

## 3. Configuração da Rede NAT e Encaminhamento de Portas

Para permitir o acesso externo à VM, foi configurado o encaminhamento de portas na interface NAT do VirtualBox.
<img width="1337" height="771" alt="Encaminhamento de portas VirtualBox" src="https://github.com/user-attachments/assets/45b7b0e1-b720-416f-acf8-cb47b62f057a" />

---

## 4. Configuração e Teste do Servidor HTTP

### Segurança no navegador

Ao acessar o servidor HTTP via endereço local (`127.0.0.1`), não há avisos de segurança, pois o conteúdo é servido dentro do próprio computador.

<img width="771" height="210" alt="Acesso local sem aviso de segurança" src="https://github.com/user-attachments/assets/cedd9085-8789-4c3d-8c75-4783f7c6f8a9" />

Já ao acessar via endereço de rede (`10.87.47.79`), o navegador exibe um aviso de segurança. Isso ocorre porque o protocolo HTTP não é criptografado e, pelo ponto de vista do navegador, o conteúdo está sendo transmitido pela rede.

<img width="771" height="210" alt="Acesso por rede com aviso de segurança" src="https://github.com/user-attachments/assets/8a43a02b-e26f-4384-b3fe-59755e78eab1" />

---

## 5. Configuração do SSH

### Ativando o servidor SSH na VM

Dentro da máquina virtual (Ubuntu), o status do SSH foi verificado com o comando:

```bash
sudo systemctl status ssh
```

Caso o serviço não estivesse ativo, ele foi iniciado com:

```bash
sudo systemctl start ssh
```

<img width="889" height="357" alt="Status do SSH na VM" src="https://github.com/user-attachments/assets/2636cae1-ccde-4450-a254-b37d8bdb8b00" />

---

## 6. Testes dos Serviços

### Conexão SSH: máquina real → máquina virtual

Na máquina real (host), a conexão com a VM foi feita via terminal usando o comando:

```bash
ssh -p 2222 usuario-maquina-virtual@127.0.0.1
```

> Onde `2222` é a porta do host mapeada para a porta `22` do convidado, e `usuario-maquina-virtual` é o nome de usuário configurado no Ubuntu.

<img width="1465" height="815" alt="Conexão SSH estabelecida" src="https://github.com/user-attachments/assets/122c95e3-409b-4e24-a89a-a427361baf0f" />

Com a conexão estabelecida, o terminal da máquina real passa a executar comandos diretamente na máquina virtual.

<img width="1919" height="1003" alt="Terminal conectado à VM" src="https://github.com/user-attachments/assets/523c6c55-3f0a-4be6-9bf5-386bf58161db" />

Como o sistema da VM é Linux (Ubuntu), os comandos utilizados devem ser do Bash. Comandos exclusivos do Windows, como `notepad`, resultam em erro por não existirem no ambiente convidado.

<img width="1919" height="987" alt="Erro ao usar comando do Windows no Ubuntu" src="https://github.com/user-attachments/assets/bc69d30a-3504-4688-a616-c66beae7ab28" />

Modificações feitas via terminal da máquina real refletem diretamente nos arquivos da máquina virtual, e vice-versa.

<img width="1919" height="960" alt="Modificações refletindo entre host e VM" src="https://github.com/user-attachments/assets/0f4cfa9f-a945-40dd-af5e-d4baa0232466" />

---

## 7. Conexão via VSCode com Remote SSH

Além do terminal, foi configurado acesso remoto à VM diretamente pelo Visual Studio Code, utilizando a extensão **Remote - SSH**.

### Passo a passo

1. Instalar a extensão **Remote - SSH** no VSCode.
   <img width="1229" height="277" alt="image" src="https://github.com/user-attachments/assets/e8ab4fe4-6415-4511-8b95-d15dd896fb38" />

2. Abrir a paleta de comandos (`Ctrl + Shift + P`).
3. Selecionar **Remote-SSH: Add New SSH Host**.

> O SSH precisa estar ativo tanto na máquina host quanto na VM de destino.

<img width="910" height="96" alt="Paleta de comandos do VSCode" src="https://github.com/user-attachments/assets/dd2a1c23-d501-4866-a4ea-98ea0be800f7" />

4. Inserir o comando SSH no formato:

```bash
ssh -p 2222 usuario@127.0.0.1
```

<img width="916" height="165" alt="Inserindo comando SSH no VSCode" src="https://github.com/user-attachments/assets/a5039173-9e1e-4580-ad17-5fcccc6fd6e7" />

<img width="900" height="125" alt="Configuração salva" src="https://github.com/user-attachments/assets/16eb4a4c-aca1-406b-b302-02c93873ada2" />

5. Clicar em **Connect**.

<img width="343" height="59" alt="Botão Connect" src="https://github.com/user-attachments/assets/8799b462-388e-49cf-94d2-ce9d3fd6960b" />

6. Digitar a senha do usuário da VM quando solicitado.

7. O VSCode abrirá uma nova janela "localizada" na máquina virtual, com acesso ao sistema de arquivos do Ubuntu.

<img width="961" height="538" alt="VSCode conectado à VM via SSH" src="https://github.com/user-attachments/assets/42b9958c-ca0c-48c2-a505-89aa4c5653fd" />

Com o Remote SSH ativo, é possível navegar, criar, editar e remover arquivos da VM diretamente pelo VSCode, como se fosse um ambiente local.

<img width="1919" height="1009" alt="Gerenciando arquivos da VM pelo VSCode" src="https://github.com/user-attachments/assets/f2f2fbe2-c775-4ce6-b97e-1e9dca8aca75" />
