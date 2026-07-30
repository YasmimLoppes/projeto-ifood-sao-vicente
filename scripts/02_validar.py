import pandas as pd
import os

os.makedirs("dados/tratados", exist_ok=True)

def pegar_arquivo_mais_recente(pasta, prefixo):
    arquivos = [f for f in os.listdir(pasta) if f.startswith(prefixo)]
    return max(arquivos) if arquivos else None

def validar():
    arq_procon = pegar_arquivo_mais_recente("dados/brutos", "procon")
    arq_sebrae = pegar_arquivo_mais_recente("dados/brutos", "sebrae")

    if not arq_procon or not arq_sebrae:
        print("Faltam arquivos para validar")
        return

    df_p = pd.read_csv(f"dados/brutos/{arq_procon}", sep=";", low_memory=False)
    df_s = pd.read_csv(f"dados/brutos/{arq_sebrae}", sep=";", low_memory=False)

    # Padroniza bairros
    for col in ["bairro", "endereco_bairro"]:
        if col in df_p.columns:
            df_p[col] = df_p[col].astype(str).str.strip().str.lower().str.title()
        if col in df_s.columns:
            df_s[col] = df_s[col].astype(str).str.strip().str.lower().str.title()

    # Remove duplicatas
    df_p = df_p.drop_duplicates()
    df_s = df_s.drop_duplicates()

    # Salva validado
    df_p.to_csv("dados/tratados/procon_validado.csv", sep=";", index=False)
    df_s.to_csv("dados/tratados/sebrae_validado.csv", sep=";", index=False)
    print("Validação concluída")

if __name__ == "__main__":
    validar()