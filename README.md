# Reconhecimento Vocal com Python

### Tabela de Conteúdos 📖
* [Descrição](#descrição-do-projeto)
* [Funcionalidades](#funcionalidades-)
* [Pré Requisitos](#pré-requisitos-pencil2)
* [Status](#status-chart_with_upwards_trend)
* [Como Rodar a Aplicação](#como-rodar-a-aplicação-)
* [Tecnologias](#tecnologias---ferramentas-eou-libs-)
* [Desenvolvedor](#desenvolvedor-)

### Descrição do Projeto
Código em Python voltado ao reconhecimento vocal, de maneira simples e intuitiva.

<h1 align="center">
    <img src="https://img.shields.io/github/license/VictorGM01/reconhecimento_vocal?style=for-the-badge"/>
    <img src="https://img.shields.io/static/v1?label=linguagem&message=python&color=blue&style=for-the-badge&logo=PYTHON"/>
    <img src="https://img.shields.io/static/v1?label=pip&message=21.2.4&color=purple&style=for-the-badge"/>
</h1>

### Funcionalidades 🏁
- [x] Reconhecer áudio e convertê-lo para texto.
- [x] Interpretar texto e convertê-lo para áudio.

### Pré Requisitos :pencil2:

Antes de começar, é preciso que você tenha instalado em sua máquina as seguintes ferramentas:

[Git](https://git-scm.com/), [Python3](https://www.python.org/downloads/release/python-390/).

Além disso, é interessante que você tenha uma IDE para conseguir rodar a aplicação de maneira simplificada. Recomendo o uso do [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)

### Status :chart_with_upwards_trend:

<h4 align="center">
    :heavy_check_mark: Reconhecimento de Fala 🚀 Em finalização :heavy_check_mark:
</h4>

### Como Rodar a Aplicação ▶
```bash
# No terminal, clone este repositório:
git clone <https://github.com/VictorGM01/reconhecimento_vocal>

# Acesse a pasta do projeto
cd reconhecimento_vocal

# Instale as dependências
pip install SpeechRecognition
pip install pipwin
pipwin install pyaudio
pip install playsound
pip install gTTS

# Para executar o programa 'fala_para_texto', execute (no terminal):
python fala_para_texto.py

# Para executar o programa 'texto_para_fala', execute (no terminal):
# Abra o console do Python
python
# Importe a função
from texto_para_fala import texto_para_fala
# Chame a função passando o argumento necessário
texto_para_fala('Insira o texto de sua preferência')

# Para rodar a aplicação 'fala_para_texto', no Pycharm:
# aperte 'shift' + f10

# Para rodar a aplicação 'texto_para_fala', no Pycharm:
# modifique o argumento texto da função e aperte 'shift' + f10
```

### Tecnologias - Ferramentas e/ou Libs 🛠

Para a construção deste projeto foram utilizadas as seguintes ferramentas e bibliotecas:

- [Python](https://www.python.org/downloads/release/python-390/)
- [Git](https://git-scm.com/)
- [pip](https://pypi.org/project/pip/)
- [pipwin](https://pypi.org/project/pipwin/)
- [gTTS](https://pypi.org/project/gTTS/)
- [Pyaudio](https://pypi.org/project/PyAudio/)
- [Playsound](https://pypi.org/project/playsound/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

### Desenvolvedor 👨🏻‍💻

[<img src="https://avatars.githubusercontent.com/u/86068797?s=400&u=043c0b1479770ac997f0cf5a31c986a2815ce810&v=4" width=115 > <br> <sub> By Victor G. Marques </sub>](https://www.linkedin.com/in/victor-gabriel-marques-4a327a208/) 