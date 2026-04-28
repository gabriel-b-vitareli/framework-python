# Relatório das Atividades de ARI

## Segurança no navegador:

<img width="771" height="210" alt="image" src="https://github.com/user-attachments/assets/cedd9085-8789-4c3d-8c75-4783f7c6f8a9" />
Com o endereço 127.0.0.1 (Local), não há avisos de seguraça pois o código é rodado no próprio computador

<img width="771" height="210" alt="image" src="https://github.com/user-attachments/assets/8a43a02b-e26f-4384-b3fe-59755e78eab1" />
Com o endereço 10.87.47.79 (Rede) há um aviso de segurança pois o protocolo não é seguro e o código, embora rodado pelo computador, é identificado pelo navegador apenas como um código vindo da rede.


## Conectando uma máquina real com uma virtual via SSH

Primeiro, vamos ativar o SSH na máquina virtual. No nosso caso, essa máquina virtual tem o sistema operacional Ubuntu (Linux). Para ver o status da conexão SSH, usamos "sudo systemctl status ssh". Se o SSH não estiver ativo (active), ativamos ele com o comando "sudo systemctl start ssh"
<img width="889" height="357" alt="image" src="https://github.com/user-attachments/assets/2636cae1-ccde-4450-a254-b37d8bdb8b00" />

Na nossa máquina real, vamos nos conectar com a virtual via SSH. Para isso, usamos o comando "ssh -p 2222 usuario-maquina-virtual@127.0.0.1", onde 2222 é a porta por onde vamos nos conectar e "usuario-maquina-virtual" deve ser substituído pelo nome da máquina virtual
<img width="1465" height="815" alt="image" src="https://github.com/user-attachments/assets/122c95e3-409b-4e24-a89a-a427361baf0f" />

Com isso, nosso terminal da máquina real já está conectada na máquina virtual. Isso signfica que todos os comandos que utilizarmos nele serão executados na máquina virtual
<img width="1919" height="1003" alt="image" src="https://github.com/user-attachments/assets/523c6c55-3f0a-4be6-9bf5-386bf58161db" />

Isso também significa que os comandos precisam funcionar na máquina virtual, que, como no nosso caso é uma Ubuntu, funciona com os comandos do Bash, e não com os do Windows (como vemos com o erro do comando "notepad", dizendo que ele é inexistente).
<img width="1919" height="987" alt="image" src="https://github.com/user-attachments/assets/910a5f3e-64d1-4328-b930-5e4c60113c9d" />

Agora, as modificações feitas pela máquina real surgem também na máquina virtual. Ao mesmo tempo, se editarmos um arquivo na máquina virtual, vamos ser capazes de ver essas alterações pela máquina real.
<img width="1919" height="960" alt="image" src="https://github.com/user-attachments/assets/0f4cfa9f-a945-40dd-af5e-d4baa0232466" />

## Conectando o VSCode pelo SSH:

1. Instalar a extensão RemoteSSH
2. Abrir a paleta de comandos (CTRL + Shift + P)
3. Selecionar a opção do Remote SSH (Add new SSH host). OBS: O ssh precisa estar rodando também na máquina em que queremos nos conectar
<img width="910" height="96" alt="image" src="https://github.com/user-attachments/assets/dd2a1c23-d501-4866-a4ea-98ea0be800f7" />
4. Inserir o comando do ssh -p nome do usuário e o @IP
<img width="916" height="165" alt="image" src="https://github.com/user-attachments/assets/a5039173-9e1e-4580-ad17-5fcccc6fd6e7" />
<img width="900" height="125" alt="image" src="https://github.com/user-attachments/assets/16eb4a4c-aca1-406b-b302-02c93873ada2" />
5. Clicar em Connect
<img width="343" height="59" alt="image" src="https://github.com/user-attachments/assets/8799b462-388e-49cf-94d2-ce9d3fd6960b" />
6. Digitar a senha da máquina que estamos tentando nos conectar
7. Pronto, agora o VSCode abrirá uma nova janela que está "localizada" na máquina que nos conectamos (Nesse caso, nosso Ubuntu)
<img width="961" height="538" alt="image" src="https://github.com/user-attachments/assets/42b9958c-ca0c-48c2-a505-89aa4c5653fd" />
Assim, temos acesso aos arquivos da máquina virtual e podemos editá-los, adicionar e remover arquivos, etc.
<img width="1919" height="1009" alt="image" src="https://github.com/user-attachments/assets/f2f2fbe2-c775-4ce6-b97e-1e9dca8aca75" />
