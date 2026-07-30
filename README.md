# Análise de Cobertura Logística e Pequenos Negócios – São Vicente/SP

## Sobre o projeto
Percebi que quase todas as análises sobre o iFood são genéricas, e pouco se fala sobre a realidade de cada cidade. Aqui em São Vicente, muitos pequenos comerciantes dependem da plataforma, mas ouço frequentemente reclamações sobre tempo de entrega e áreas sem atendimento.

Esse projeto foi feito para entender de forma prática:
- Quais bairros concentram mais reclamações relacionadas a entrega
- Como isso se relaciona com a quantidade de pequenos negócios por região
- Quais locais merecem mais atenção para melhorar a operação e apoiar os comerciantes

## Fontes utilizadas
- Base pública de reclamações Procon-SP
- Dados de micro e pequenas empresas – Sebrae/SP
- Dados tratados e consolidados sem acesso a informações internas ou confidenciais

## Ferramentas
- Python / Pandas / Requests
- Power BI para visualização
- Organização por etapas: extração → validação → transformação

## Como rodar
1. Instale as dependências: `pip install -r requisitos.txt`
2. Extraia os dados: `python scripts/01_extrair.py`
3. Valide e padronize: `python scripts/02_validar.py`
4. Gere a base final: `python scripts/03_transformar.py`

## Resultado
A base final permite identificar pontos críticos de forma objetiva, sem análises subjetivas. Os dados mostram onde a operação funciona melhor e onde ajustes podem beneficiar tanto a plataforma quanto quem vende e quem compra aqui na cidade.