# Blumbot Clicker

Blumbot Clicker é um bot automatizado desenvolvido em Python que interage com o aplicativo Telegram Desktop para realizar ações automáticas baseadas em detecção de cores e botões na interface.

---

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados no seu sistema:

- **Python 3.x**: O Blumbot Clicker foi desenvolvido e testado com Python 3 (V3.10.6). Certifique-se de ter Python instalado.

  - **Windows**: [Download Python](https://www.python.org/downloads/windows/)
  - **macOS**: [Download Python](https://www.python.org/downloads/macos/)
  - **Linux**: Utilize o gerenciador de pacotes da sua distribuição, por exemplo:

    ```bash
    sudo apt-get update
    sudo apt-get install python3 python3-pip
    ```

- **Telegram Desktop**: O Blumbot Clicker interage com a versão desktop do Telegram. [Download Telegram Desktop](https://desktop.telegram.org/)

---

## Instalação

Siga os passos abaixo para instalar e configurar o Blumbot Clicker no seu sistema.

### 1. Clone o Repositório

Primeiro, clone o repositório do Blumbot para o seu computador. Se você ainda não tem o Git instalado, [faça o download e instale o Git](https://git-scm.com/downloads).



```bash
git clone https://github.com/gunnarhalen/Blumbot-Clicker.git
```

Ou faça o [download do .zip](https://github.com/gunnarhalen/Blumbot-Clicker/archive/refs/heads/main.zip) diretamente na sua máquina.
    
### 2. Abra diretório e execute o Blumbot

Certifique-se de que o Blum está aberto antes de executar.

Abra o Prompt de Comando no Windows, navegue até a pasta do Blumbot e execute os comandos abaixo para instalar as dependências e iniciar o Blumbot Clicker:

**Instalar dependências**
```bash
pip install -r requirements.txt
```
**Executar Blumbot Clicker**
```bash
python blumbot.py
```

## Aviso!!!

Este bot foi testado apenas no **Windows**. Atualmente, existe uma *issue* conhecida onde o Blumbot Clicker não é capaz de identificar janelas no **macOS**. Por favor, tenha isso em mente ao utilizar o bot.
