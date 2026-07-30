import pandas as pd
import os

os.makedirs("saida", exist_ok=True)

def transformar():
    df_p = pd.read_csv("dados/tratados/procon_validado.csv", sep=";")
    df_s = pd.read_csv("dados/tratados/sebrae_validado.csv", sep=";")

    # Define coluna de bairro para cada base
    bairro_p = "bairro" if "bairro" in df_p.columns else "endereco_bairro"
    bairro_s = "bairro" if "bairro" in df_s.columns else "endereco_bairro"

    # Agrupa por bairro
    reclamo = df_p.groupby(bairro_p).size().reset_index(name="qtd_reclamacoes")
    empresas = df_s.groupby(bairro_s).size().reset_index(name="qtd_empresas")

    # Junta e cria métrica
    base = pd.merge(empresas, reclamo, left_on=bairro_s, right_on=bairro_p, how="outer")
    base["bairro"] = base[bairro_s].combine_first(base[bairro_p])
    base = base.drop([bairro_s, bairro_p], axis=1)
    base = base.fillna(0)
    base["reclamacoes_por_100_empresas"] = round((base["qtd_reclamacoes"] / base["qtd_empresas"]) * 100, 1)

    # Salva base final
    base.to_csv("saida/base_analise.csv", sep=";", index=False)
    print("Base pronta em saida/base_analise.csv")

if __name__ == "__main__":
    transformar()