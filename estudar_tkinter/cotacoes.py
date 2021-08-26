import requests


def pegar_cotacoes():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    requisicao_dic = requests.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bib']
    cotacao_euro = requisicao_dic['EURBRL']['bib']
    cotacao_btc = requisicao_dic['BTCBRL']['bib']

    texto = f''''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    print(texto)


pegar_cotacoes()
