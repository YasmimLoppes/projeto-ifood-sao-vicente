# Análise de Cobertura Logística e Impacto nos Pequenos Negócios – São Vicente/SP

---

##  POR QUE RESOLVI FAZER ESSE PROJETO?
Sempre vejo muitas análises sobre plataformas de entrega, mas quase todas falam de Brasil inteiro ou de capitais grandes ninguém para para olhar a realidade de cada cidade.

Aqui em São Vicente, vejo que milhares de pequenos comerciantes — padarias, lanchonetes, restaurantes familiares usam o iFood para conseguir vender mais e manter o negócio funcionando. Mas também ouço muita gente reclamando: "meu bairro não tem entrega", "demora muito para chegar", "o entregador não encontra o endereço". E pensei: **como isso afeta realmente esses pequenos negócios? Será que tem lugares que precisam de mais atenção?**

Não encontrei nenhum estudo ou dado organizado só sobre a nossa cidade. Então resolvi criar esse projeto para responder essas perguntas, usando apenas informações públicas e confiáveis, sem precisar de dados confidenciais de dentro da empresa.

---

##  QUAIS PERGUNTAS ESSE PROJETO TENTA RESPONDER?
1. Quais bairros de São Vicente têm mais reclamações sobre entrega, atraso ou falta de cobertura?
2. Essas reclamações aparecem mais em lugares com poucos negócios ou em lugares que já tem bastante comércio?
3. Onde a logística está funcionando bem, e onde ainda dá para melhorar para ajudar tanto a plataforma quanto quem vende aqui?

---

##  DE ONDE VIERAM OS DADOS?
Usei apenas fontes oficiais e gratuitas, que qualquer pessoa pode acessar:
- **Procon-SP**: Todas as reclamações registradas contra o iFood aqui em São Vicente, filtradas para assuntos de entrega, cobertura e atraso
- **Sebrae/SP**: Relação de todas as micro e pequenas empresas ativas na cidade, com informação de bairro e tipo de comércio
- **Nenhuma informação interna ou confidencial da empresa foi usada**  tudo o que fiz foi unir e organizar o que já está disponível publicamente

---

##  COMO FIZ: CADA PASSO EXPLICADO
Segui todo o caminho completo de trabalho com dados, do começo ao fim:

### 1️ BUSCAR OS DADOS
Criei um código em Python que acessa automaticamente essas fontes e baixa os arquivos. Guardei tudo do jeito que veio, sem mudar nada assim ninguém pode dizer que alterei a informação original.

### 2️ VERIFICAR E ARRUMAR
Os dados públicos quase sempre têm erros: nomes de bairro escritos de jeito diferente, coisas repetidas, informações faltando. Então:
- Tirei tudo o que aparecia mais de uma vez
- Arrumei os nomes: "vl guilherme" virou "Vila Guilherme", "centro." virou "Centro"
- Conferi se as datas e locais faziam sentido
- Separei o que era realmente problema de entrega do que era outro assunto

### 3️ JUNTAR E CALCULAR
Depois juntei as duas informações:
- Quantas reclamações tem em cada bairro
- Quantos pequenos negócios existem no mesmo lugar
- E calculei: para cada 100 negócios, quantas reclamações aparecem? Isso mostra onde o problema é maior, mesmo que o bairro seja pequeno.

### 4️ MOSTRAR OS RESULTADOS
Criei painéis no Power BI para que qualquer pessoa consiga ver de cara: um mapa da cidade, gráficos comparando os bairros e os pontos que mais chamam atenção.

---

##  O QUE DESCOBRI E O QUE ISSO SIGNIFICA?
Os dados mostram que:
- Bairros mais centrais têm mais reclamações no total, mas proporcionalmente ao número de negócios, funcionam melhor
- Regiões mais afastadas ou com acesso mais difícil têm poucos registros, mas quando aparecem, a proporção de problemas é muito maior
- Isso significa que não é só "tem mais gente reclamando": em certos lugares, a dificuldade de entrega realmente atrapalha mais o funcionamento do comércio local

Essas informações podem ajudar a decidir onde vale a pena testar novas rotas, colocar mais entregadores ou criar ações para apoiar os comerciantes que estão nessas regiões.

---

##  FERRAMENTAS QUE USEI
- **Python**: para buscar, limpar e organizar todas as informações
- **Pandas**: a ferramenta que ajuda a mexer com tabelas e dados
- **Requests**: para acessar as páginas oficiais e pegar os arquivos
- **Power BI**: para criar os gráficos e mapas fáceis de entender
- **Git/GitHub**: para organizar todo o trabalho e deixar tudo registrado

---

##  COMO VOCÊ PODE REPETIR OU VERIFICAR ESSE TRABALHO?
Se quiser rodar você mesmo:
1. Instale o Python na sua máquina
2. Baixe os arquivos deste repositório
3. No terminal, instale o que precisa:
   ```bash
   pip install -r requisitos.txt

## 4 Rode os códigos na ordem:

python scripts/extrair.py
python scripts/02_validar.py
python scripts/03_transformar.py

## 5 Pronto! Você vai ter os mesmos dados organizados que eu usei.

Importante: Esse projeto não tem nenhuma ligação oficial com o iFood nem com o Sebrae ou Procon. Foi feito apenas com objetivo de estudo e de entender melhor a realidade da nossa cidade, de forma transparente e pública.


---