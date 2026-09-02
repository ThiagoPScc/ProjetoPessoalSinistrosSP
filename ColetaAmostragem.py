import numpy as np
import pandas as pd
dfSinistros = pd.read_csv(
    "/content/sinistros_2022-2024.csv",
    encoding="latin1",  sep=";"
)
dfVeiculos = pd.read_csv( "/content/veiculos_2022-2024.csv", encoding="latin1", sep=";")
dfPessoas = pd.read_csv("/content/pessoas_2022-2024.csv", encoding="latin1", sep=";")
amostra = dfSinistros.sample(n=500, random_state=11)
amostraPessoas = dfPessoas[dfPessoas["id_sinistro"].isin(amostra["id_sinistro"])]
amostraVeiculos = dfVeiculos[dfVeiculos["id_sinistro"].isin(amostra["id_sinistro"])]

amostraPessoas.to_csv("AmostraPessoasCompleta.csv", index=False)
amostraVeiculos.to_csv("AmostraVeiculosCompleta.csv", index=False)
amostra.to_csv("AmostraSinistrosCompleta.csv", index=False)
