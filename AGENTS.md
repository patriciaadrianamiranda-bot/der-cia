# AGENTS.md — Repositório de trabalho da Patricia

Este repositório é o espaço de trabalho de engenharia da Patricia, engenheira civil
do DER-RO (Departamento de Estradas de Rodagem de Rondônia), na Coordenadoria de
Infraestrutura de Aeroportos. Os agentes ajudam em todas as etapas: levantamento de
dados, estimativa de custos, redação e revisão dos documentos.

## O que se produz aqui

- **ETPs (Estudos Técnicos Preliminares)** — a principal demanda.
- Termos de referência e documentos para contratação de empresas e licitações.
- Pareceres técnicos e relatórios.

Quase não existem modelos padrão no órgão. Quando um documento ficar bom, salve a
estrutura em `modelos/` para reaproveitar.

## Regra obrigatória: arquivos de no máximo 20 KB

**Nenhum arquivo do repositório pode passar de 20 KB (20.480 bytes).** O CI
(`.github/workflows/verificacoes.yml`) bloqueia o que passar do limite.

- Antes de cada commit, rode: `uv run scripts/verificar_tamanho.py`
- Se um arquivo passar do limite, **divida-o**, não resuma nem apague conteúdo:
  - Documentos longos: um arquivo por seção (ex.: `etp/01-necessidade.md`,
    `etp/02-requisitos.md`) e um `README.md` com o índice.
  - Normas e regulamentos: um arquivo por capítulo ou grupo de artigos.
  - Planilhas/dados: divida em vários CSVs por tema ou por trecho.
  - PDFs grandes: converta para Markdown por partes; não versione o PDF inteiro.
- Prefira texto (Markdown, CSV) a formatos binários.
- Desenhos (DWG/DXF), PDFs e fotos que não couberem: guarde no SEI ou no Drive e
  registre aqui apenas o link e uma descrição.

## Regra obrigatória: scripts só em Python com PEP 723 e uv

**Todo script do repositório deve ser em Python, com metadados PEP 723, e ser
executado com `uv run`.** Não crie scripts em shell, JavaScript, PowerShell etc.
O CI (`scripts/verificar_pep723.py`) bloqueia o que não seguir a regra.

Cada script começa assim (declare as dependências no próprio arquivo):

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["ezdxf"]
# ///
```

- Execute com `uv run scripts/nome_do_script.py`.
- Não use `pip install`, `requirements.txt` nem ambientes virtuais manuais.
- Antes de cada commit, rode também: `uv run scripts/verificar_pep723.py`

## SEI de Rondônia — use o IES

A Patricia escreve os documentos diretamente no **SEI de Rondônia**. Para operar o
SEI, use o **IES** (`franklinbaldo/ies`, "SEI" ao contrário), um aplicativo em Rust
feito para agentes trabalharem no SEI. `[A CONFIRMAR]`: instalação e configuração
do IES neste ambiente ainda não foram feitas.

- Consulte o README do IES para os comandos disponíveis antes de usar.
- Fluxo recomendado: redigir e revisar aqui no repositório → Patricia aprova →
  inserir no SEI pelo IES.
- **Nunca assine, envie ou tramite processos sem pedido explícito da Patricia.**

## Ferramentas de engenharia

- **SICRO (DNIT)** — referência de custos para obras de infraestrutura. Sempre
  informe a data-base, o estado/região e o código de cada composição usada.
- **SINAPI (Caixa)** — para serviços de edificação (terminal, cercas, instalações),
  com a mesma exigência de data-base, UF e código.
- **Compor 90** — sistema de orçamento usado pela Patricia para montar e conferir
  composições e orçamentos.
- **CAD** — para gerar ou ler desenhos, prefira DXF (ex.: biblioteca Python
  `ezdxf`, em script PEP 723).
- **Mapas** — QGIS ou Python (`geopandas`, `folium`) para mapas de localização,
  croquis e áreas de intervenção. Guarde dados em GeoJSON/CSV pequenos.

## Normas de referência

Os documentos podem se apoiar em **todos** os regulamentos da ANAC e normas técnicas
aplicáveis; não exclua nenhum por padrão. Principais:

- Lei 14.133/2021 (licitações e contratos) e regulamentações do Estado de Rondônia.
- Regulamentos da ANAC (RBACs, Resoluções e Instruções Suplementares),
  especialmente os de projeto, operação e manutenção de aeródromos (ex.: RBAC 154 e
  RBAC 153).
- Normas do COMAER/DECEA sobre zonas de proteção de aeródromos, quando aplicáveis.
- Normas ABNT e manuais/especificações do DNIT aplicáveis a pavimentação.

Guarde trechos de normas públicas (ANAC, DNIT, legislação) em `referencias/`
(respeitando os 20 KB). **Normas ABNT têm direitos autorais**: guarde apenas a
referência e resumos próprios, não o texto. **Cite sempre número, artigo/item e
versão**. Nunca invente citação: se não encontrar a fonte, diga que não encontrou.

## Estrutura do ETP (Lei 14.133/2021, art. 18, §1º)

1. Descrição da necessidade
2. Previsão no plano de contratações anual
3. Requisitos da contratação
4. Estimativa das quantidades
5. Levantamento de mercado
6. Estimativa do valor da contratação
7. Descrição da solução como um todo
8. Justificativa para o parcelamento ou não
9. Resultados pretendidos
10. Providências prévias à celebração do contrato
11. Contratações correlatas e/ou interdependentes
12. Possíveis impactos ambientais e medidas mitigadoras
13. Posicionamento conclusivo sobre a viabilidade

Os itens 1, 4, 6, 8 e 13 são obrigatórios (§2º); os demais, se não couberem,
precisam de justificativa.

## Projeto atual

- **Aeroporto de Guajará-Mirim** — ETP para contratação de empresa que elaborará o
  projeto de revitalização da pista de pouso e decolagem. Material em
  `projetos/guajara-mirim/` (a Patricia vai adicionar os documentos já reunidos).

## Estrutura sugerida de pastas

```
projetos/<aeroporto>/   documentos de cada projeto (dividido em seções)
referencias/            normas e regulamentos em partes
modelos/                estruturas de documentos reaproveitáveis
orcamentos/             composições e planilhas (CSV)
scripts/                scripts Python (PEP 723, uv)
```

## Sigilo e LGPD

- Não coloque no repositório CPF, dados pessoais de servidores, empresas ou
  cidadãos, senhas ou tokens.
- **Orçamento estimado sigiloso** (Lei 14.133/2021, art. 24) não deve ser versionado
  nem enviado a serviços externos.
- Na dúvida sobre sigilo, pergunte à Patricia antes de prosseguir.

## Regras gerais para os agentes

- Escreva em português formal, no padrão de documentos públicos.
- Não invente números, preços, quantidades ou dados de campo; marque como
  `[A CONFIRMAR]` o que depender de informação da Patricia.
- Mostre a origem de cada valor (SICRO, SINAPI, Compor 90, cotação, levantamento)
  e a memória de cálculo: fórmulas, premissas, unidades e arredondamentos.
- Em planilhas, preserve as fórmulas; não troque por valores fixos.
- Tudo o que o agente produz é **rascunho**: a responsabilidade técnica (ART) é da
  Patricia, que revisa e aprova antes de qualquer uso oficial.
- Commits pequenos e com mensagens claras em português.
