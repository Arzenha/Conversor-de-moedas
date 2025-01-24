import xmltodict


def nomes_moedas():
    """
    Abre o arquivo moedas.xml e retorna um dicionário com todos os nomes de moedas presentes nele.

    :return: Dicionário com os nomes de moedas.
    """
    with open("Bruto/moedas.xml", "rb") as arquivo_moedas:
        dic_moedas = xmltodict.parse(arquivo_moedas)

    moedas = dic_moedas['xml']

    return moedas

def conversoes_disponiveis():
    """
    Abre o arquivo conversoes.xml e itera sobre cada par de conversões presentes nele.
    
    Para cada par de conversão, separa a moeda de origem e a moeda de destino.
    
    :return: None
    """

    with open('Bruto/conversoes.xml', "rb") as arquivo_conversoes:
        dic_conversoes = xmltodict.parse(arquivo_conversoes)
    
    conversoes = dic_conversoes['xml']
    
    dic_conversoes_disponiveis = {}
    for par_conversao in conversoes:
        moeda_origem, moeda_destino = par_conversao.split("-")
        if moeda_origem in dic_conversoes_disponiveis:
            dic_conversoes_disponiveis[moeda_origem].append(moeda_destino)
        else:
            dic_conversoes_disponiveis[moeda_origem] = [moeda_destino]
    return dic_conversoes_disponiveis        