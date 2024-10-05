# Projeto Web Scrapy

[![NPM](https://img.shields.io/github/license/tvlemes/project-web-scraping)](https://github.com/tvlemes/project-web-scraping/blob/main/LICENSE)

<!-- TABLE OF CONTENTS --> 
<details open="open">
  <summary>Indície</summary>
  <ol>
    <li>
      <a href="#objetivo">Objetivo</a>
      <ul>
        <li><a href="#bibliotecas-utilizadas">Bibliotecas utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#pastas-e-arquivos">Criando um projeto</a>
    </li>
    <li>
      <a href="#pastas-e-arquivos">Pastas e Arquivos</a>
    </li>
    <li>
      <a href="#configuracoes-avancadas">Configurações Avançadas</a>
    </li>
    <li>
      <a href="#links">Links</a>
    </li>
    <li>
      <a href="#sobre">Sobre</a>
    </li>
  </ol>
</details>

## Objetivo

Este projeto tem por fim exemplificar de como criar um projeto para Scrapy na Web, é necessário fazer os devidos ajustes de acordo com as necessidades. Este template é apenas um modelo.

<!-- programas-e-bibliotecas -->
### Bibliotecas utilizadas

* scrapy (para instalar a bibliotteca <b>$ pip install scrapy</b>)
* datetime
* os

<!-- criando-o-projeto -->
## Criando um projeto

Assim que a biblioteca <b>scrapy</b> esteja instalada, no terminal digite o seguinte comando para criar a estrutura básica do projeto.
```
$ scrapy startproject nome_do_projeto
```
Será criado o projeto com a seguinte estrutura:

```
nome_do_projeto
    scrapy.cfg
    nome_do_projeto/
        __init__.py
        items.py
        middlewares.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
```

<!-- arquivos-e-pastas -->
## Pastas e Arquivos

Dentro da pasta <b>spiders/</b>, você pode criar seu próprio spider. Neste exemplo foi criado o <b>spider_links</b>, para capturar os links de downloads do Censo Escolar.


<!-- rodando-o-projeto -->
## Configurações Avançadas

As configurações avançadas podem ser setadas no arquivo <b>settings.py</b>
Ex.: Para respeitar o robots.txt:
<b>USER_AGENT = 'meu_projeto_scrapy (+http://www.meusite.com)'</b>

* settings.py: configurações avançadas
* Middlewares: Para gerenciar requisições e respostas.
* Pipelines: Para processar ou armazenar os dados extraídos.
* Seletores CSS e XPath: Para selecionar elementos HTML específicos.

<b> OBS.: O objetivo deste projeto não é explicar minuciosamente toda a biblioteca scrapy</b>

<!-- sobre -->
## Sobre

Autor: Thiago Vilarinho Lemes <br>
LinkedIn <a href="https://www.linkedin.com/in/thiago-v-lemes-b1232727">Thiago V. Lemes</a><br>
e-mail: contatothiagolemes@gmail.com | lemes_vilarinho@yahoo.com.br