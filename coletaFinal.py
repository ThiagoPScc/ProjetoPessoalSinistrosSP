Célula de código <QOI0ohh2eimT>
# %% [code]
import numpy as np
import pandas as pd
import geopandas as gpd

Célula de código <bsN_y0muxupf>
# %% [code]
dfSinistros = pd.read_csv(
    "/content/sinistros_2022-2024.csv",
    encoding="latin1",  sep=";"
)

Célula de código <eleQXbxIXssM>
# %% [code]
dfPessoas = pd.read_csv("/content/pessoas_2022-2024.csv", encoding="latin1", sep=";")

Célula de código <MQ8sxuXzZacy>
# %% [code]
dfVeiculos = pd.read_csv( "/content/veiculos_2022-2024.csv", encoding="latin1", sep=";")

Célula de texto <VSKXQjZAy9X4>
# %% [markdown]
Limpeza e normalização para dados final

Célula de código <ucBh_fAfzIm9>
# %% [code]
print(dfSinistros)

Célula de código <39L7L2JV39ft>
# %% [code]
dias = {
    'Terï¿½a-feira':'Terça-feira',
    'Sï¿½bado':'Sábado',
}
dfSinistros['dia_da_semana'] = dfSinistros['dia_da_semana'].replace(dias)
print(dfSinistros)

Célula de código <v3tkfC0E55lY>
# %% [code]
dfSinistros.drop(columns=['ano_sinistro','mes_sinistro','dia_sinistro','hora_sinistro','ano_mes_sinistro','tipo_local','regiao_administrativa','administracao','conservacao'], inplace=True)

Célula de código <s-ikEJWZ_hP->
# %% [code]
dfSinistros['qtd_pedestre'] = dfSinistros['qtd_pedestre'].fillna(0).astype(int)
dfSinistros['qtd_bicicleta'] = dfSinistros['qtd_bicicleta'].fillna(0).astype(int)
dfSinistros['qtd_automovel'] = dfSinistros['qtd_automovel'].fillna(0).astype(int)
dfSinistros['qtd_motocicleta'] = dfSinistros['qtd_motocicleta'].fillna(0).astype(int)
dfSinistros['qtd_caminhao'] = dfSinistros['qtd_caminhao'].fillna(0).astype(int)
dfSinistros['qtd_veic_outros'] = dfSinistros['qtd_veic_outros'].fillna(0).astype(int)
dfSinistros['qtd_veic_nao_disponivel'] = dfSinistros['qtd_veic_nao_disponivel'].fillna(0).astype(int)
dfSinistros['qtd_gravidade_fatal'] = dfSinistros['qtd_gravidade_fatal'].fillna(0).astype(int)
dfSinistros['qtd_gravidade_grave'] = dfSinistros['qtd_gravidade_grave'].fillna(0).astype(int)
dfSinistros['qtd_gravidade_leve'] = dfSinistros['qtd_gravidade_leve'].fillna(0).astype(int)
dfSinistros['qtd_gravidade_ileso'] = dfSinistros['qtd_gravidade_ileso'].fillna(0).astype(int)
dfSinistros['qtd_gravidade_nao_disponivel'] = dfSinistros['qtd_gravidade_nao_disponivel'].fillna(0).astype(int)
dfSinistros['qtd_onibus'] = dfSinistros['qtd_onibus'].fillna(0).astype(int)
dfSinistros['latitude'] = dfSinistros['latitude'].astype(str).str.replace(',', '.').astype(float)
dfSinistros['longitude'] = dfSinistros['longitude'].astype(str).str.replace(',', '.').astype(float)

Célula de código <hqWgZtfmA0pz>
# %% [code]
dfSinistros['total_pessoas'] = dfSinistros['qtd_pedestre'] + dfSinistros['qtd_bicicleta'] + dfSinistros['qtd_automovel'] + dfSinistros['qtd_motocicleta'] + dfSinistros['qtd_caminhao'] + dfSinistros['qtd_onibus']
print(dfSinistros[['qtd_automovel','qtd_pedestre','qtd_bicicleta','qtd_motocicleta','qtd_caminhao','qtd_onibus','qtd_veic_outros','qtd_veic_nao_disponivel','total_pessoas']])
dfSinistros[['qtd_gravidade_fatal','qtd_gravidade_grave','qtd_gravidade_leve','qtd_gravidade_ileso','qtd_gravidade_nao_disponivel']]


Célula de código <5qi2DiRFYfW2>
# %% [code]
dfSinistrosSP = dfSinistrosSP[
    (dfSinistrosSP['municipio'] == 'SAO PAULO') &
    (dfSinistrosSP['circunscricao'] == 'MUNICIPAL')
]

Célula de código <X_bCXZ4ja_sD>
# %% [code]
print(dfSinistrosSP)

Célula de código <7Jfx7n_wcOZt>
# %% [code]
dfPessoasSp = dfPessoas[dfPessoas['id_sinistro'].isin(dfSinistrosSP['id_sinistro'])]
dfVeiculosSp = dfVeiculos[dfVeiculos['id_sinistro'].isin(dfSinistrosSP['id_sinistro'])]

Célula de código <fYU6eSrcuOSt>
# %% [code]
dfSinistrosSP.dtypes

Célula de código <jesE_ftfvQsT>
# %% [code]
gdfMapa = gpd.read_file('/content/subprefeitura_v2.shp')
print(gdfMapa.head())

Célula de código <Dbh8rC8O0mAa>
# %% [code]
gdfMapa

Célula de código <fowJNqKw5bgN>
# %% [code]
gdfMapa = gdfMapa[['nm_regiao_','geometry']]

Célula de código <x5rArUEy0amS>
# %% [code]
gdfMapa

Célula de código <VlkBofc63C-L>
# %% [code]
#transformando os dados para fazer os pontos usando a latitude e longitude para comparar com o mapa
import geopandas as gpd

gdfSinistrosSP = gpd.GeoDataFrame(dfSinistrosSP,
    geometry=gpd.points_from_xy(dfSinistrosSP['longitude'], dfSinistrosSP['latitude']),
    crs="EPSG:4326")

gdfZonas = gdfMapa.to_crs(gdfSinistrosSP.crs)

dfSinistrosSPFinal = gpd.sjoin(gdfSinistrosSP, gdfZonas, how="left", predicate="within")

print(dfSinistrosSPFinal.head())

Célula de código <iZpEcU1E53pR>
# %% [code]
dfSinistrosSPFinal.drop(columns='geometry', inplace=True)

Célula de código <KCdrAJ6u6CjN>
# %% [code]
dfSinistrosSPFinal["nm_regiao_"].fillna('NAO DISPONIVEL', inplace=True)
dfSinistrosSPFinal

Célula de código <zZ6sw7iv6cb6>
# %% [code]
dfPessoasSPFinal = dfPessoas[dfPessoas['id_sinistro'].isin(dfSinistrosSPFinal['id_sinistro'])]
dfVeiculosSPFinal = dfVeiculos[dfVeiculos['id_sinistro'].isin(dfSinistrosSPFinal['id_sinistro'])]

Célula de código <pRweFzsm8m7i>
# %% [code]
dfVeiculosSPFinal.drop(columns=['ano_sinistro','mes_sinistro','dia_sinistro','ano_mes_sinistro','data_sinistro'],inplace=True)

Célula de código <LpzZlWsg-Hfz>
# %% [code]
dfVeiculosSPFinal['marca_modelo'].fillna('NAO DISPONIVEL')

Célula de código <P-as4d0A_GHX>
# %% [code]
cond = [
    dfVeiculosSPFinal['marca_modelo'].str.split('/').str[0] == "I",
    dfVeiculosSPFinal['marca_modelo'].str.split('/').str[0] != "I"
]
val = ["importado", "nacional"]


dfVeiculosSPFinal['importado'] = np.select(cond,val,default='NAO DISPONIVEL')

Célula de código <nzAmtjXiB53O>
# %% [code]
dfVeiculosSPFinal[dfVeiculosSPFinal["importado"] == "importado"]


Célula de código <oiyY2kMyHjBN>
# %% [code]
dfVeiculosSPFinal['marca_modelo'] = dfVeiculosSPFinal['marca_modelo'].fillna('NAO DISPONIVEL')
dfVeiculosSPFinal

Célula de código <kIAw4fR6CUEb>
# %% [code]
dfPessoasSPFinal.drop(columns=['ano_sinistro','mes_sinistro','dia_sinistro','ano_mes_sinistro','regiao_administrativa','tipo_via','faixa_etaria_demografica','tipo_veiculo_vitima','grau_de_instrucao','data_obito','local_via','ano_obito','mes_obito','dia_obito','ano_mes_obito','tempo_sinistro_obito'],inplace=True)

Célula de código <tEEte2LRDbJG>
# %% [code]
dfPessoasSPFinal['idade'] = dfPessoasSPFinal['idade'].fillna(0).astype(int)
dfPessoasSPFinal['id_veiculo'] = dfPessoasSPFinal['id_veiculo'].astype('Int64')
dfPessoasSPFinal['profissao'] = dfPessoasSPFinal['profissao'].fillna('NAO DISPONIVEL')
dfPessoasSPFinal['nacionalidade'] = dfPessoasSPFinal['nacionalidade'].fillna('NAO DISPONIVEL')

Célula de código <O5CRPVlYOzPp>
# %% [code]
dfSinistrosSPFinal.drop(columns=['index_right'], inplace=True)

Célula de código <lKSVU2b5N1as>
# %% [code]
print(dfSinistrosSPFinal['index_right'])

Célula de código <454ewvYE7Axy>
# %% [code]
dfPessoasSPFinal.to_csv("AmostraPessoasSPFinal.csv", index=False)
dfVeiculosSPFinal.to_csv("AmostraVeiculosSPFinal.csv", index=False)
dfSinistrosSPFinal.to_csv("AmostraSinistrosSPFinal.csv", index=False)

