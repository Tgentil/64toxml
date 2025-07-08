import os
import json
import base64
import xml.etree.ElementTree as ET

def extrair_nnf(xml_bytes):
    """
    Recebe bytes do XML e retorna o valor da tag <nNF>
    """
    try:
        raiz = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return None

    for elemento in raiz.iter():
        tag = elemento.tag
        if '}' in tag:
            tag = tag.split('}', 1)[1]
        if tag == 'nNF':
            return elemento.text
    return None


def main():
    # Caminho fixo do JSON na pasta data
    caminho_json = os.path.join('data', 'notas.json')
    pasta_saida = 'out'

    # Verifica existência do arquivo JSON
    if not os.path.exists(caminho_json):
        print(f"Arquivo JSON não encontrado em {caminho_json}")
        return

    # Lê e parseia o JSON
    try:
        with open(caminho_json, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except Exception as e:
        print(f"Erro ao ler JSON: {e}")
        return

    lista_xmls = dados.get('xmls', [])
    if not isinstance(lista_xmls, list):
        print("Chave 'xmls' não encontrada ou não é uma lista.")
        return

    # Garante a pasta de saída
    os.makedirs(pasta_saida, exist_ok=True)

    # Processa cada string base64
    for indice, b64 in enumerate(lista_xmls, start=1):
        try:
            conteudo_xml = base64.b64decode(b64)
        except Exception as e:
            print(f"[{indice}] Falha na decodificação base64: {e}")
            continue

        nnf = extrair_nnf(conteudo_xml)
        if nnf:
            nome_arquivo = f"NFe{nnf}.xml"
        else:
            nome_arquivo = f"desconhecido_{indice}.xml"
            print(f"[{indice}] Tag <nNF> não encontrada. Salvando como {nome_arquivo}")

        caminho_saida = os.path.join(pasta_saida, nome_arquivo)
        try:
            with open(caminho_saida, 'wb') as arquivo:
                arquivo.write(conteudo_xml)
            print(f"[{indice}] Gravado em {caminho_saida}")
        except Exception as e:
            print(f"[{indice}] Erro ao salvar {caminho_saida}: {e}")

if __name__ == '__main__':
    main()
