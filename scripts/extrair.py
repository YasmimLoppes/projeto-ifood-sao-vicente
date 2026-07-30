import requests
import pandas as pd
import os
from datetime import datetime

os.makedirs("dados/brutos", exist_ok=True)

def buscar_procon():
    print("Buscando dados do Procon-SP...")
    try:
        url = "https://dados.procon.sp.gov.br/api/v1/reclamacoes"
        params = {
            "empresa": "iFood",
            "assunto": "Entrega; Cobertura; Atraso na entrega",
            "municipio": "São Vicente",
            "ano": 2025,
            "formato": "json"
        }
        resp = requests.get(url, params=params, timeout=60)
        resp.raise_for_status()
        df = pd.DataFrame(resp.json())
        caminho = f"dados/brutos/procon_{datetime.now().strftime('%Y%m%d')}.csv"
        df.to_csv(caminho, sep=";", encoding="utf-8", index=False)
        print(f"Salvo: {len(df)} registros")
        return df
    except Exception as e:
        print(f"Erro Procon: {e}")
        return None

def buscar_sebrae():
    print("\nBuscando dados do Sebrae...")
    try:
        url = "https://api.datasebrae.sebrae.com.br/v1/municipios/3551009/empresas"
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        df = pd.DataFrame(resp.json()["dados"])
        caminho = f"dados/brutos/sebrae_{datetime.now().strftime('%Y%m%d')}.csv"
        df.to_csv(caminho, sep=";", encoding="utf-8", index=False)
        print(f"Salvo: {len(df)} empresas")
        return df
    except Exception as e:
        print(f"Erro Sebrae: {e}")
        return None

if __name__ == "__main__":
    buscar_procon()
    buscar_sebrae()