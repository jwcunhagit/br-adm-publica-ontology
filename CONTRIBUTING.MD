# Como Contribuir para br-adm-publica-ontology

Obrigado por considerar contribuir! Este documento explica como fazer isso de forma clara e organizada.

## 📋 Índice

- [Código de Conduta](#código-de-conduta)
- [Tipos de Contribuição](#tipos-de-contribuição)
- [Processo de Contribuição](#processo-de-contribuição)
- [Diretrizes Técnicas](#diretrizes-técnicas)
- [Perguntas Frequentes](#perguntas-frequentes)

---

## Código de Conduta

Este projeto segue o [Código de Conduta do Contributor Covenant](CODE_OF_CONDUCT.md).
Ao participar, você concorda em manter um ambiente respeitoso e inclusivo.

---

## Tipos de Contribuição

### 📚 Documentação
- Melhorar explicações em README, docs/
- Criar exemplos práticos
- Traduzir para outros idiomas
- Corrigir typos

**Como começar:**
1. Fork e edite diretamente em \`docs/\`
2. Abra PR com label \`documentation\`

### 🧬 Ontologia
- Propor novas classes (ex: br:PortoAutarquia)
- Propor novas propriedades (ex: br:orçamentoPrevisto)
- Alinhar com novos padrões (ex: LKIF para regulação)
- Validar alinhamentos com CPOV/W3C ORG

**Como começar:**
1. Abra uma **Issue** primeiro (template: \`ontology_extension.md\`)
2. Descreva: motivação, exemplos de uso (Competency Questions)
3. Aguarde feedback antes de codar

### ✅ Testes e Validação
- Criar testes RDF (exemplos em \`validation/test-cases/\`)
- Validar com SHACL
- Testar integração com SIORG real
- Reportar bugs

**Como começar:**
1. Abra Issue: \`bug_report.md\`
2. Clone, reproduza o erro
3. Envie PR com teste que demonstra o problema + correção

### 🔌 Integrações
- Mapear dados de novos portais (LAI, SIORG, IBGE)
- Criar exportadores (CSV → RDF, JSON → RDF)
- Integrar com tools (Protégé, Apache Jena, GraphDB)

**Como começar:**
1. Abra Issue: \`feature_request.md\`
2. Descreva fonte de dados e formato
3. Contribua com scripts em \`mappings/\`

---

## Processo de Contribuição

### Passo 1: Abra uma Issue (Geralmente Necessário)

\`\`\`
Para Documentação: Pode fazer PR direto
Para Ontologia: SEMPRE abra Issue PRIMEIRO
Para Bugs: Use template bug_report.md
Para Features: Use template feature_request.md
\`\`\`

**Título descritivo:**
- ✅ "Adicionar classe br:PortoEstadual para autarquias portuárias"
- ❌ "Nova classe"

### Passo 2: Faça Fork e Configure Ambiente

\`\`\`bash
git clone https://github.com/SEU_USUARIO/br-adm-publica-ontology.git
cd br-adm-publica-ontology

# Crie branch descritivo
git checkout -b feature/adicionar-porto-estadual
# ou
git checkout -b fix/alinhamento-cpov-typo
# ou
git checkout -b docs/melhorar-readme-pt
\`\`\`

### Passo 3: Código + Testes + Docs

**Se for Ontologia:**
\`\`\`bash
# Edite arquivo OWL
vim ontology/br-adm-publica-core.owl

# Valide sintaxe (requer Apache Jena ou Protégé)
# (ver Diretrizes Técnicas)

# Crie teste que demonstra uso
vim validation/test-cases/seu-teste.ttl

# Documente em ADR
vim docs/historico-decisoes.md
\`\`\`

**Se for Documentação:**
\`\`\`bash
# Edite markdown
vim docs/seu-documento.md

# Rode teste de links (futura CI)
# (Manual por enquanto)
\`\`\`

**Se for Código Python (Mappers):**
\`\`\`bash
# Instale deps
pip install -r requirements.txt

# Code
vim mappings/seu-mapper.py

# Teste
python -m pytest mappings/test_seu_mapper.py

# Lint
flake8 mappings/seu-mapper.py
\`\`\`

### Passo 4: Commit com Mensagem Clara

\`\`\`bash
git add .
git commit -m "feat: adicionar br:PortoEstadual com exemplos e testes

- Nova classe br:PortoEstadual subclasse de br:OrgaoEstadual
- Adicionado exemplo de Porto do Recife (SUAPE)
- Alinhado com CPOV:PublicOrganization
- Incluído teste de validação SHACL
- Atualizado docs/exemplos/estadual-secretaria.ttl

Closes #42"
\`\`\`

**Convenção de Commit (Conventional Commits):**
- \`feat:\` nova feature
- \`fix:\` correção de bug
- \`docs:\` mudanças em documentação
- \`refactor:\` mudanças sem nova feature
- \`test:\` testes novos
- \`chore:\` infraestrutura, CI/CD

### Passo 5: Push e Abra Pull Request

\`\`\`bash
git push origin feature/adicionar-porto-estadual
# GitHub notificará para criar PR
\`\`\`

**Template de PR (automático no GitHub):**

\`\`\`markdown
## Descrição
Breve resumo do que muda

## Tipo de Mudança
- [ ] Nova feature
- [ ] Correção de bug
- [ ] Melhoria de documentação
- [ ] Refatoração

## Mudanças Propostas
1. Item 1
2. Item 2

## Testes Executados
- [ ] Validação OWL
- [ ] SHACL constraints
- [ ] Exemplos práticos

## Checklist
- [ ] Meu código segue o style guide
- [ ] Fiz self-review do meu código
- [ ] Adicionei documentação
- [ ] Adicionei testes
- [ ] Não quebrei builds existentes
\`\`\`

### Passo 6: Code Review

Mantenedores vão:
1. Revisar código/documentação
2. Pedir ajustes se necessário
3. Aprovar com \`LGTM\` (Looks Good To Me)
4. Fazer merge

---

## Diretrizes Técnicas

### Validação OWL

**Com Protégé:**
1. Abra \`ontology/br-adm-publica-core.owl\`
2. Menu: Reasoner → Start
3. Procure por ⚠️ inconsistências
4. Conserte antes de fazer commit

**Com Apache Jena (CLI):**
\`\`\`bash
# Valide sintaxe RDF/XML
riot --check ontology/br-adm-publica-core.owl

# Se usar Turtle
riot --check ontology/br-adm-publica-core.ttl
\`\`\`

### SHACL Validation

\`\`\`bash
# Valide dados contra shapes
pyshacl validate \
    -s validation/shacl-shapes.ttl \
    -d ontology/br-adm-publica-core.owl
\`\`\`

### Convenção de Namespaces

\`\`\`turtle
@prefix br: <https://data.gov.br/ontology/adm-publica/> .
@prefix cpov: <http://data.europa.eu/m8g/> .
@prefix org: <http://www.w3.org/ns/org#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
\`\`\`

### Estrutura de Competency Questions (CQs)

Todo novo conceito deve ter **pelo menos 2 Competency Questions**:

\`\`\`markdown
**CQ1**: Listar todos os órgãos estaduais da esfera de Pernambuco

SPARQL:
SELECT ?org WHERE {
    ?org a br:OrgaoEstadual ;
         cpov:hasJurisdiction <.../pernambuco-2611606> .
}

**CQ2**: Qual é a prefeitura que contém um secretaria de educação?

SPARQL:
SELECT ?municipio WHERE {
    ?secretaria a br:SecretariaEducacao ;
                org:subOrganizationOf ?municipio .
}
\`\`\`

---

## Perguntas Frequentes

**P: Sou iniciante em ontologias. Posso ainda contribuir?**
R: Sim! Comece com documentação ou reportando bugs. Depois evolua para ontologia.

**P: Preciso que minha contribuição seja aceita? (deadline)**
R: Entendemos pressões. Marque PR como "WIP" (Work In Progress) e comunique.

**P: E se minha PR for rejeitada?**
R: Sem problemas! Pedimos feedback construtivo. Pode refazer e reenviar.

**P: Quanto tempo demora review?**
R: Ideal: 1-2 semanas. Complexas: até 1 mês. Acompanhe comentários.

**P: Posso conversar em Discussions antes de fazer PR?**
R: Sim! Recomendado para features grandes.

---

**Obrigado por contribuir! 🎉**
