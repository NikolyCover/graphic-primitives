# TRABALHO 1 - primitivas gráficas

## Atividade 1

Especificação: "Em uma linguagem de programação de sua escolha,  utilize uma biblioteca gráfica para desenhar algo combinando primitivas gráficas (como  ponto, retas, círculos, polígonos, etc)."

Para isso foi utilizado a biblioteca turtle do python para desenhar um gatinho.

## Pré-requisitos

Para executar este projeto, você precisará ter o **Python 3** instalado no seu computador.

1.  **Como verificar se o Python está instalado:**
    * No terminal use o comando a seguir:
        ```bash
        python --version
        ```
    * A resposta deve ser algo como `Python 3.10.x`
    * Caso não tenha o python instalado ou a versão instalada seja muito antiga, baixe e instale a versão mais recente do Python em [python.org/downloads](https://www.python.org/downloads/).

## Como Executar no Windows

### Passo 1: Criar e Ativar o Ambiente Virtual

1.  Com o terminal aberto nesse pasta, digite o seguinte comando para criar um ambiente virtual chamado `.venv`:
    ```powershell
    python -m venv .venv
    ```

2.  Agora, ative este ambiente:
    ```powershell
    .\.venv\Scripts\activate
    ```

3.  Se tuo der certo, você verá `(.venv)` aparecer no início da linha do seu terminal.

### Passo 2: Executar o Desenho

1.  Digite o comando abaixo para executar o arquivo:
    ```powershell
    python src/cat_drawer.py
    ```

2.  Uma nova janela deve aparecer e começar a desenhar o gatinho