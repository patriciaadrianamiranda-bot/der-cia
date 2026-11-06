# AGENTS.md — Instruções para agentes de IA

## 1. Sobre este repositório
- Repositório de trabalho de uma **engenheira do DER-RO** (Departamento de Estradas de Rodagem, Infraestrutura e Serviços Públicos de Rondônia).
- Usado para apoiar atividades de **engenharia rodoviária**: análise de projetos, orçamentos, medições, fiscalização de obras, pareceres, relatórios técnicos e planilhas de cálculo.
- Quem usa: a engenheira responsável (dona do repositório). Os documentos produzidos podem ser anexados a processos oficiais.

## 2. Idioma e tom
- Escreva sempre em **português do Brasil**, inclusive commits, comentários e documentos.
- Use linguagem técnica e formal, adequada a documentos de órgão público.
- Siga a redação oficial: clareza, objetividade, impessoalidade.

## 3. Organização das pastas
> (Ajustar conforme o repositório crescer.)
- `docs/` — pareceres, relatórios, notas técnicas e modelos de documentos.
- `planilhas/` — orçamentos, memórias de cálculo, medições (`.xlsx`, `.csv`).
- `scripts/` — rotinas de cálculo e automação (ex.: Python).
- `referencias/` — normas, manuais e materiais de consulta.

## 4. Normas e referências técnicas
Ao fazer cálculos, análises ou textos técnicos, baseie-se em (e cite) as referências aplicáveis:
- **DNIT**: normas (especificações de serviço, procedimentos), manuais de pavimentação, drenagem, conservação e sinalização.
- **SICRO** (DNIT) e **SINAPI** (Caixa) para composições de custo e preços de referência — sempre informe a **data-base** e a região/UF.
- **ABNT NBR** aplicáveis (ex.: concreto, estruturas, ensaios de solos).
- **CTB** e Manual Brasileiro de Sinalização de Trânsito (CONTRAN).
- **Lei 14.133/2021** (licitações e contratos) e normas do TCU / TCE-RO sobre obras públicas (ex.: BDI, sobrepreço).
- Normas e procedimentos internos do DER-RO, quando fornecidos.

## 5. Regras de trabalho para o agente
- **Nunca invente dados**: quantitativos, preços, códigos de composição, números de normas ou de processos. Se não souber, diga e deixe marcado como `[A CONFIRMAR]`.
- **Mostre a memória de cálculo**: fórmulas, unidades, premissas e fontes de cada valor.
- **Confira unidades** (m, m², m³, t, km, t·km) e arredondamentos.
- Indique claramente o que é **estimativa/sugestão** e o que é **valor de referência oficial**.
- Todo documento gerado é um **rascunho** para revisão da engenheira; a responsabilidade técnica (ART) é dela. Não assine nem apresente nada como versão final.
- Em planilhas, preserve fórmulas (não substitua por valores fixos) e não altere a estrutura sem avisar.

## 6. Sigilo e LGPD
- **Não incluir** no repositório: CPF, dados pessoais de servidores, de empresas ou de cidadãos, senhas, tokens ou documentos sigilosos.
- Dados de licitações em andamento (ex.: orçamento sigiloso) não devem ser publicados nem enviados a serviços externos.
- Em caso de dúvida sobre sigilo, pergunte antes de prosseguir.

## 7. Git e commits
- Não fazer push direto na `main`; trabalhar em branch e abrir PR quando solicitado.
- Mensagens de commit em português, curtas e descritivas (ex.: `Adiciona memória de cálculo da drenagem da RO-XXX`).

## 8. Glossário rápido
- **DER-RO**: Departamento de Estradas de Rodagem de Rondônia.
- **RO-XXX / BR-XXX**: rodovias estaduais / federais.
- **SICRO / SINAPI**: sistemas de referência de custos.
- **BDI**: Benefícios e Despesas Indiretas.
- **ART**: Anotação de Responsabilidade Técnica (CREA).
- **Medição**: apuração dos serviços executados no período, para pagamento.
- **SEI**: Sistema Eletrônico de Informações (processos administrativos).

## 9. Responsável
- Engenheira do DER-RO, dona deste repositório. Dúvidas sobre escopo, dados ou sigilo: perguntar a ela antes de agir.
