import pandas as pd
import os

os.makedirs("dados_prontos", exist_ok=True)

# Leio os arquivos que baixei
df_reclama = pd.read_csv("dados_brutos/reclamacoes_ifood.csv", sep=";")
df_empresas = pd.read_csv("dados_brutos/empresas_sebrae.csv", sep=";")

# Limpo e padronizo os bairros
df_reclama["bairro"] = df_reclama["bairro"].str.strip().str.lower().str.title()
df_empresas["bairro"] = df_empresas["bairro"].str.strip().str.lower().str.title()

# Removo o que está repetido
df_reclama = df_reclama.drop_duplicates()
df_empresas = df_empresas.drop_duplicates()

# Junto tudo em um arquivo só
qtd_reclama = df_reclama.groupby("bairro").size().reset_index(name="qtd_reclamacoes")
qtd_empresas = df_empresas.groupby("bairro").size().reset_index(name="qtd_empresas")

base_final = pd.merge(qtd_empresas, qtd_reclama, on="bairro", how="left").fillna(0)

# Salvo pronto para o Power BI
base_final.to_csv("dados_prontos/base_final.csv", sep=";", index=False)
print("Pronto! Base final criada na pasta dados_prontos.")