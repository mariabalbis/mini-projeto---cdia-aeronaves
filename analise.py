import pandas as pd

ocorrencias = pd.read_csv("ocorrencia.csv", encoding="iso-8859-1", sep=";")
tipos = pd.read_csv("ocorrencia_tipo.csv", encoding="iso-8859-1", sep=";")
aeronaves = pd.read_csv("aeronave.csv", encoding="iso-8859-1", sep=";")

dados = pd.merge(ocorrencias, tipos, on="codigo_ocorrencia1", how="inner")
dados = pd.merge(dados, aeronaves, on="codigo_ocorrencia2", how="inner")

graves = dados[dados["ocorrencia_classificacao"] == "INCIDENTE GRAVE"]

print("\nAeroportos com incidentes graves:")

aeroportos = []

for aeroporto in graves["ocorrencia_aerodromo"]:
    if pd.notna(aeroporto) and aeroporto not in aeroportos:
        aeroportos.append(aeroporto)

for aeroporto in aeroportos:
    print(aeroporto)

print("\nFrequência dos incidentes:")

frequencia = dados["ocorrencia_classificacao"].value_counts()
print(frequencia)

qtd_graves = 0
qtd_acidentes = 0

for classificacao in dados["ocorrencia_classificacao"]:
    if classificacao == "INCIDENTE GRAVE":
        qtd_graves += 1

    if classificacao == "ACIDENTE":
        qtd_acidentes += 1

print("\nQuantidade de incidentes graves:", qtd_graves)
print("Quantidade de acidentes:", qtd_acidentes)

print("\nAeronaves envolvidas em incidentes graves:")

modelos = graves["aeronave_modelo"].value_counts()
print(modelos)

print("\nEstados com mais ocorrencias:")

estados = dados["ocorrencia_uf"].value_counts()

contador = 0
for estado, quantidade in estados.items():
    if contador < 10:
        print(estado, quantidade)
        contador += 1

print("\nTipos de ocorrências mais comuns:")

tipos_ocorrencia = dados["ocorrencia_tipo"].value_counts()

contador = 0
for tipo, quantidade in tipos_ocorrencia.items():
    if contador < 10:
        print(tipo, quantidade)
        contador += 1

dados["ocorrencia_dia"] = pd.to_datetime(dados["ocorrencia_dia"], errors="coerce")
dados["ano"] = dados["ocorrencia_dia"].dt.year

print("\nOcorrências por ano:")

ocorrencias_por_ano = dados["ano"].value_counts().sort_index()
print(ocorrencias_por_ano)