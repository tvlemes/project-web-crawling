import scrapy
from datetime import datetime
import os

class MeuSpider(scrapy.Spider):
    name = "spider_links"
    start_urls = ['https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar']  # URL inicial para o spider
    links_web = []

    def parse(self, response):
        """
        Este é o Spider para capturar os links do Censo Escola.
        O Spider irá procurar no endereço start_urls na classe 
        delcarada external-link em todos os atributors(attr)
        cujo seja referência seja o  link(href) Ex.: $ a.external-link\\:\\:attr(href)
        (O \ \  é o escape do python).

        Para rodar o comando digite no terminal na raiz do projeto: <b>scrapy crawl nome_spider -o links.json \n</b> \n
        :param nome_spider: é o nome do arquivo spider 
        :param links.json: é o nome do arquivo .json que será gerado na rais do projeto. <b>OBS.: ao rodar
        novamente o Spider ele adiciona um novo dicionário a lista.</b>
        :param: links_web: é a lista de links para downloas dos arquivos de dados
        """

        # # Diretório do arquivo .json que será deletados
        # caminho_arquivo = ".\links.json"

        # # Verificando se o arquivo existe antes de deletá-lo
        # if os.path.exists(caminho_arquivo):
        #     os.remove(caminho_arquivo)
        #     print(f"Arquivo '{caminho_arquivo}' foi deletado.")
        # else:
        #     print(f"O arquivo '{caminho_arquivo}' não existe.")
        
        # Função para apagar o arquivo links.json na raiz caso exista
        self.dir_del(".\links.json")

        links = response.css('a.external-link::attr(href)').getall()
        
        yield {
            'date': datetime.now(),
            'links': links
        }

        # Para verificação da lista de links 
        print("\n\n****************************************************************")
        print(f"O valor na posição 0 é: {links[0]}") 
        print(f"O valor na posição 1 é: {links[1]}") 
        print(f"O valor na posição 2 é: {links[2]}")
        print(f"O total de arquivos é: {len(links)}")
        print("\n\n****************************************************************")

        
    def dir_del(self, file_path: str) -> None:
        """
        Função que irá apagar o arquivo json no diretório raiz
        """
        # Diretório do arquivo .json que será deletados
        caminho_arquivo = file_path

        # Verificando se o arquivo existe antes de deletá-lo
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)
            print(f"Arquivo '{caminho_arquivo}' foi deletado.")
        else:
            print(f"O arquivo '{caminho_arquivo}' não existe.")