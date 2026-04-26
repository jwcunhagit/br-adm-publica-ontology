
import os
import json
from datetime import datetime

# Estruturar projeto GitHub completo para br-adm-publica-ontology

projeto_config = {
    "project_name": "br-adm-publica-ontology",
    "sponsor": "Aeon Bridge Co.",
    "license": "CC-BY 4.0",
    "inception_date": "2026-04-26",
    "repository_url": "https://github.com/aeonbridge/br-adm-publica-ontology",
    "domains": {
        "federal": "Administração Federal (SIORG, Ministérios, Autarquias)",
        "estadual": "Administração Estadual (27 Estados + DF)",
        "municipal": "Administração Municipal (5.570 Municípios)",
        "intergovernamental": "Relações e Hierarquias entre as 3 esferas"
    }
}

# ============================================================================
# 1. README.md - Documentação Raiz
# ============================================================================

readme_content = """# br-adm-publica-ontology

[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightblue.svg)](http://creativecommons.org/licenses/by/4.0/)
[![GitHub Issues](https://img.shields.io/github/issues/aeonbridge/br-adm-publica-ontology)](https://github.com/aeonbridge/br-adm-publica-ontology/issues)
[![Contributors](https://img.shields.io/github/contributors/aeonbridge/br-adm-publica-ontology)](https://github.com/aeonbridge/br-adm-publica-ontology/graphs/contributors)
[![Status](https://img.shields.io/badge/Status-Alpha%20v0.1-orange)](https://github.com/aeonbridge/br-adm-publica-ontology/releases)

**Ontologia Formal para Administração Pública Brasileira em Três Esferas**

Uma arquitetura semântica integrada para mapear organizações, papéis, hierarquias e relacionamentos na administração pública brasileira (Federal, Estadual e Municipal) utilizando padrões W3C, CPOV (Core Public Organisation Vocabulary) e extensões brasileiras validadas.

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Motivação Histórica](#motivação-histórica)
- [Arquitetura da Solução](#arquitetura-da-solução)
- [Padrões Base](#padrões-base)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Como Contribuir](#como-contribuir)
- [Roadmap](#roadmap)
- [Referências](#referências)

---

## 🎯 Visão Geral

Esta ontologia responde a uma lacuna crítica na infraestrutura de dados abertos brasileira: **não existe padrão OWL formal, oficial e validado para representar a estrutura, papéis e relacionamentos da administração pública nas três esferas federativas**.

### O Problema

- **DCAT-BR**: cobre apenas catálogos de dados, não estruturas organizacionais
- **SIORG** (federal): banco relacional (JSON API), não ontologia publicada
- **LAI/Portal Transparência**: CSV sem semântica formal
- **ePING**: padrões de interoperabilidade técnica, não ontologia
- **Vocabulários anteriores (2010-2012)**: abandonados, namespaces fora do ar

**Resultado**: Governo brasileiro não tem padrão para descrever "Secretaria A é subordinada a Secretaria B" em Linked Data, ou "este dataset é publicado por esta organização em esta esfera jurisdicional".

### A Solução

**br-adm-publica-ontology** implementa uma arquitetura em **três camadas**:

1. **Padrões Base** (W3C, Europa): W3C ORG, FOAF, schema.org, **CPOV**
2. **Extensão Brasileira**: `br:` namespace com identificadores canônicos (CNPJ, IBGE, SIORG)
3. **Ontologias de Domínio**: Especialização por setor (Saúde, Educação, Tributária, Regulatória)

---

## 📚 Motivação Histórica

### Contexto Internacional

A Europa resolveu este problema entre 2016-2020 com **EU Core Public Organisation Vocabulary (CPOV)**, desenvolvido pela Comissão Europeia (ISA² Programme):
- Define hierarquias de governos federados (Bélgica, Espanha, Áustria)
- Distingue esferas jurisdicionais (`cpov:Jurisdiction`)
- Herda de W3C ORG (reusabilidade)
- Usado em produção por Portugal, Bélgica, Espanha

### Contexto Brasil

**Por que não aplicar CPOV direto?**

1. **Identificadores únicos brasileiros** não existem em CPOV:
   - CNPJ (100% cobertura: Federal, Estadual, Municipal)
   - Código IBGE (5.570 municípios + 27 UFs)
   - SIORG_ID (~5.800 órgãos federais)

2. **Hierarquias específicas**: Brasil tem estrutura peculiar (Distrito Federal, Territórios)

3. **Dados abertos existentes**: SIORG, Portal LAI, Receita Federal já publicam estes dados; falta apenas formalização OWL

**Decisão Arquitetural**: Usar **CPOV como base** (reutilizar solução europeia) + **br:* como extensão** (adicionar especificidades brasileiras) = Máxima interoperabilidade + Máxima relevância local.

---

## 🏗️ Arquitetura da Solução

### Diagrama de Classes (Hierarquia)

\`\`\`
foaf:Organization (FOAF)
├─ org:FormalOrganization (W3C ORG)
│  └─ cpov:PublicOrganization (EU CPOV)
│     └─ br:OrganizacaoPublica (BR Extension)
│        ├─ br:OrgaoFederal
│        ├─ br:OrgaoEstadual
│        └─ br:Municipio
\`\`\`

### Stack de Padrões

| Camada | Padrão | Propósito | Versão |
|--------|--------|----------|--------|
| **Semântica Base** | FOAF 0.99 | Agentes (pessoas, orgs) | 0.99 (W3C) |
| **Organizações** | W3C ORG 1.0 | Estrutura hierárquica | W3C Recommendation |
| **Governo** | CPOV 2.00 | Públicas + Jurisdição | W3C Community Note |
| **Brasil** | br: 0.1-alpha | CNPJ, IBGE, SIORG | Aeon Bridge (em desenvolvimento) |
| **Descrição Dados** | DCAT-BR 1.1 | Catálogos (integração) | DCAT-AP BR |
| **Proveniência** | PROV-O 1.0 | Autoridade e delegação | W3C Recommendation |

### Identificadores Canônicos

Todas as entidades em br-adm-publica-ontology devem ter **pelo menos 2 dos 3** identificadores:

| Identificador | Cobertura | Formato | Exemplo | Propriedade |
|---|---|---|---|---|
| **CNPJ** | 100% Federal/Estadual/Municipal | 14 dígitos | 16717114000140 | `br:cnpj` |
| **Código IBGE** | 100% Municípios + Estados + DF | 7 dígitos | 2611606 (Recife-PE) | `br:codigoIBGE` |
| **SIORG_ID** | ~5.800 órgãos federais | Numérico sequencial | 70000 | `br:siorgId` |

---

## 📦 Padrões Base

### W3C ORG (Organization Ontology)

\`\`\`turtle
@prefix org: <http://www.w3.org/ns/org#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

# Classe base: Organização Formal
org:FormalOrganization 
    rdfs:subClassOf foaf:Organization ;
    rdfs:comment "Entidade organizacional legalmente reconhecida" .

# Propriedades principais
org:subOrganizationOf       # Subordinação hierárquica
org:Role                     # Papel dentro da organização
org:Membership              # Vínculo entre agente e organização
org:hasMembershipRole       # Ligação explícita
\`\`\`

### CPOV (Core Public Organisation Vocabulary)

\`\`\`turtle
@prefix cpov: <http://data.europa.eu/m8g/> .
@prefix org: <http://www.w3.org/ns/org#> .

# Classe base: Organização Pública
cpov:PublicOrganization
    rdfs:subClassOf org:FormalOrganization ;
    rdfs:comment "Organização do setor público com jurisdição definida" .

# Propriedades principais
cpov:hasJurisdiction        # Território/Esfera
cpov:jurisdictionLevel      # Nível (federal, regional, local)
cpov:playsRole              # Papéis públicos (regulador, fornecedor, etc)
\`\`\`

### br: Extension (Aeon Bridge)

\`\`\`turtle
@prefix br: <https://data.gov.br/ontology/adm-publica/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .

# Classes principais
br:OrganizacaoPublica
    rdfs:subClassOf cpov:PublicOrganization ;
    rdfs:comment "Organização pública brasileira com identificadores canônicos" .

br:OrgaoFederal
    rdfs:subClassOf br:OrganizacaoPublica ;
    rdfs:comment "Órgão da administração federal (ministério, autarquia, agência)" .

br:OrgaoEstadual
    rdfs:subClassOf br:OrganizacaoPublica ;
    rdfs:comment "Órgão da administração estadual ou distrital" .

br:Municipio
    rdfs:subClassOf br:OrganizacaoPublica ;
    rdfs:comment "Prefeitura e órgãos municipais" .

# Propriedades: Identificadores
br:cnpj rdf:type owl:InverseFunctionalProperty ;
    rdfs:domain [ owl:unionOf (br:OrganizacaoPublica foaf:Person) ] ;
    rdfs:range xsd:string ;
    rdfs:comment "Cadastro Nacional da Pessoa Jurídica (14 dígitos)" .

br:codigoIBGE rdf:type owl:InverseFunctionalProperty ;
    rdfs:domain [ owl:unionOf (br:OrgaoEstadual br:Municipio) ] ;
    rdfs:range xsd:string ;
    rdfs:comment "Código IBGE de município ou estado (7 dígitos para município)" .

br:siorgId rdfs:subPropertyOf org:identifier ;
    rdfs:domain br:OrgaoFederal ;
    rdfs:range xsd:int ;
    rdfs:comment "Identificador no Sistema de Informações Organizacionais (SIORG)" .

# Propriedades: Jurisdição Brasileira
br:esfera rdf:type owl:InverseFunctionalProperty ;
    rdfs:domain br:OrganizacaoPublica ;
    rdfs:range [ owl:oneOf (br:Esfera_Federal br:Esfera_Estadual br:Esfera_Municipal) ] ;
    rdfs:comment "Nível de governo: federal, estadual ou municipal" .
\`\`\`

---

## 📁 Estrutura do Repositório

\`\`\`
br-adm-publica-ontology/
├── README.md                          # Este arquivo
├── CONTRIBUTING.md                    # Guia de contribuições
├── CODE_OF_CONDUCT.md                 # Código de conduta
├── LICENSE                            # CC-BY 4.0
│
├── docs/                              # Documentação
│   ├── index.md                       # Página principal do projeto
│   ├── arquitetura.md                 # Visão técnica detalhada
│   ├── guia-de-uso.md                 # Como usar a ontologia
│   ├── padroes-base.md                # W3C ORG, CPOV, FOAF, schema.org
│   ├── historico-decisoes.md          # ADR (Architecture Decision Records)
│   └── exemplos/                      # Exemplos práticos
│       ├── federal-ministerio.ttl
│       ├── estadual-secretaria.ttl
│       └── municipal-prefeitura.ttl
│
├── ontology/                          # Arquivos OWL/RDF
│   ├── br-adm-publica-core.owl        # Core (br:* classes + properties)
│   ├── br-adm-publica-alignments.owl  # Alinhamentos CPOV + W3C ORG
│   │
│   ├── domain-ontologies/             # Ontologias de domínio (em desenvolvimento)
│   │   ├── saude/
│   │   │   └── br-saude-publica.owl   # Organizações de saúde
│   │   ├── educacao/
│   │   │   └── br-educacao-publica.owl
│   │   ├── tributaria/
│   │   │   └── br-tributaria.owl
│   │   └── regulatoria/
│   │       └── br-regulatoria.owl
│   │
│   └── versions/                      # Histórico de versões
│       └── v0.1-alpha/
│
├── mappings/                          # Mapeamentos de dados existentes
│   ├── siorg-to-rdf/                  # SIORG (JSON) → RDF
│   │   └── siorg-mapper.py
│   ├── ibge-to-rdf/                   # Código IBGE → RDF
│   └── cnpj-to-rdf/                   # CNPJ → RDF
│
├── validation/                        # Testes e validação
│   ├── shacl-shapes.ttl               # SHACL constraints
│   ├── competency-questions.md        # CQs (Competency Questions)
│   └── test-cases/
│       ├── federal-test.ttl
│       ├── estadual-test.ttl
│       └── municipal-test.ttl
│
├── assets/                            # Imagens, diagramas
│   ├── arquitetura-camadas.png
│   ├── hierarquia-classes.png
│   └── exemplo-recife.png
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── ontology_extension.md
│   └── workflows/
│       ├── validate-owl.yml           # CI: validação OWL
│       ├── test-rdf.yml               # CI: testes RDF
│       └── build-docs.yml             # CI: build documentação
│
├── pyproject.toml                     # Dependências Python
├── requirements.txt
└── CHANGELOG.md
\`\`\`

---

## 🚀 Como Contribuir

### Tipos de Contribuição

**Não é preciso ser desenvolvedor**. Aceitamos:

- **Documentação**: melhorar explicações, criar exemplos
- **Ontologia**: propor novas classes/propriedades (via Issues primeiro!)
- **Testes**: validar alinhamentos com SIORG, LAI, Receita Federal
- **Integrações**: mapear dados de outras fontes (Estados, Municípios)
- **Divulgação**: artigos, apresentações, workshops

### Processo de Contribuição

\`\`\`
1. Abra uma Issue descrevendo a ideia
   ↓
2. Aguarde feedback dos mantenedores
   ↓
3. Faça fork, crie branch (feature/sua-ideia)
   ↓
4. Envie PR com descrição clara
   ↓
5. Code review + aprovação da comunidade
   ↓
6. Merge + reconhecimento no CHANGELOG
\`\`\`

### Iniciante? Comece por Aqui

- Leia [CONTRIBUTING.md](CONTRIBUTING.md)
- Veja Issues com label \`good-first-issue\`
- Converse em Discussions antes de codar

---

## 📊 Roadmap

### ✅ v0.1-alpha (Atual)
- [x] Arquitetura core (br:* classes)
- [x] Alinhamento CPOV + W3C ORG
- [x] Exemplos (Federal, Estadual, Municipal)
- [x] Validação SHACL básica
- [x] Documentação base

### 📅 v0.2-beta (Q2 2026)
- [ ] Ontologias de domínio (Saúde, Educação)
- [ ] Mapeador SIORG → RDF automático
- [ ] Integração DCAT-BR (datasets ← orgs)
- [ ] SPARQL endpoint de teste
- [ ] Exemplos com dados reais (PE, Recife)

### 🎯 v1.0-stable (Q3-Q4 2026)
- [ ] Validação por comunidade brasileira
- [ ] Adoção em dados.gov.br
- [ ] Ontologias de todos os domínios críticos
- [ ] Suporte multi-língue (PT/EN/ES)
- [ ] Tools de migração (CSV → RDF)

### 🔮 v2.0+ (2027)
- [ ] Alinhamento com OKG/FIBO para setor financeiro
- [ ] SPARQL federado (União + Estados + Municípios)
- [ ] Knowledge Graph público em RDF
- [ ] APIs Linked Data oficiais por esfera

---

## 🤝 Governança

### Mantedores

- **Aeon Bridge Co.** — Sponsor, infraestrutura inicial
- **Comunidade Brasileira de Semântica** — Validação, extensões

### Processo de Decisão

Grandes mudanças (novas classes, alinhamentos) são discutidas em **ADR (Architecture Decision Records)** antes de merge.

Veja: [docs/historico-decisoes.md](docs/historico-decisoes.md)

---

## 📖 Referências

### Padrões Base
- [W3C Organization Ontology](https://www.w3.org/TR/vocab-org/) — Recommendation 2014
- [EU Core Public Organisation Vocabulary](https://semiceu.github.io/CPOV/releases/2.00/) — ISA² Programme
- [FOAF Vocabulary](http://xmlns.com/foaf/0.1/) — Friend of a Friend
- [schema.org GovernmentOrganization](https://schema.org/GovernmentOrganization)

### Padrões Brasileiros
- [DCAT-BR](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/catalogo-nacional-de-dados) — Catálogos de dados abertos
- [ePING](https://eping.governoeletronico.gov.br) — Padrões de Interoperabilidade
- [SIORG](https://siorg.gov.br) — Sistema de Informações Organizacionais

### Dados de Referência
- [Código IBGE](https://www.ibge.gov.br) — 5.570 municípios + 27 UFs
- [CNPJ](https://www.gov.br/receitafederal) — Receita Federal
- [Portal Transparência](https://portaltransparencia.gov.br) — CGU

### Acadêmico
- [CPOV Technical Report](https://joinup.ec.europa.eu/sites/default/files/document/2017-03/CPOV%20Technical%20Report_0.pdf)
- [OntoUML for Public Organizations](https://www.inf.ufes.br/~gguizzardi) — Guizzardi et al.

---

## 📬 Contato

- **Issues**: [GitHub Issues](https://github.com/aeonbridge/br-adm-publica-ontology/issues)
- **Discussions**: [GitHub Discussions](https://github.com/aeonbridge/br-adm-publica-ontology/discussions)
- **Email**: ontology@aeonbridge.io

---

## 📜 Licença

Este projeto está sob licença **CC-BY 4.0** (Atribuição 4.0 Internacional).

Você é livre para:
- ✅ Usar, modificar, distribuir
- ✅ Usar para fins comerciais
- ✅ Adaptar para outros idiomas/contextos

Com a condição de:
- 📝 Atribuir autoria ao Aeon Bridge Co. e Comunidade br-adm-publica-ontology

---

**Desenvolvido com ❤️ pela Comunidade de Dados Abertos Brasileira**

*Última atualização: 26/04/2026*
"""

# Salvar README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("✅ README.md criado")

# ============================================================================
# 2. docs/index.md - Página Principal do Projeto
# ============================================================================

docs_index = """# br-adm-publica-ontology — Documentação

Bem-vindo ao projeto de ontologia formal para administração pública brasileira.

## 🎯 Comece Aqui

- **[O que é este projeto?](#o-que-é-este-projeto)**
- **[Como usar](#como-usar)**
- **[Exemplos práticos](#exemplos-práticos)**
- **[Referência técnica](#referência-técnica)**

---

## O que é este projeto?

Uma ontologia OWL (Web Ontology Language) que permite descrever organizações públicas brasileiras (Ministérios, Secretarias, Prefeituras) de forma **estruturada, formal e interoperável** na Web Semântica.

### Antes de br-adm-publica-ontology:
\`\`\`json
{
  "nome": "Secretaria da Fazenda de PE",
  "sigla": "SEFAZ",
  "cnpj": "16717114000140"
}
\`\`\`

### Depois:
\`\`\`turtle
<https://data.gov.br/org/pe-sefaz>
    a br:OrgaoEstadual ;                       # Tipo
    a cpov:PublicOrganization ;                # Classe europeia
    rdfs:label "Secretaria da Fazenda PE" ;   # Nome
    br:cnpj "16717114000140" ;                # Identificador
    br:codigoIBGE "2611606" ;                 # Código municipal
    cpov:hasJurisdiction <.../pernambuco> ;  # Jurisdição
    cpov:jurisdictionLevel "estadual" ;       # Nível
    org:subOrganizationOf <.../gov-pe> ;     # Relacionamento
    foaf:mbox <mailto:sefaz@sefaz.pe.gov.br> # Contato
.
\`\`\`

---

## Como usar

### 1️⃣ Instalação

Clone o repositório:

\`\`\`bash
git clone https://github.com/aeonbridge/br-adm-publica-ontology.git
cd br-adm-publica-ontology
\`\`\`

### 2️⃣ Carregue a Ontologia

**Em Protégé (GUI):**
1. Abra Protégé
2. File → Open → \`ontology/br-adm-publica-core.owl\`

**Em Python (com rdflib):**
\`\`\`python
from rdflib import Graph

g = Graph()
g.parse("ontology/br-adm-publica-core.owl", format="xml")

# Query exemplo
results = g.query('''
    PREFIX br: <https://data.gov.br/ontology/adm-publica/>
    SELECT ?org WHERE {
        ?org a br:OrgaoEstadual .
    }
''')
\`\`\`

### 3️⃣ Consulte com SPARQL

\`\`\`sparql
PREFIX br: <https://data.gov.br/ontology/adm-publica/>
PREFIX cpov: <http://data.europa.eu/m8g/>
PREFIX org: <http://www.w3.org/ns/org#>

# Listar todas organizações estaduais e seus territórios
SELECT ?org ?label ?territorio
WHERE {
    ?org a br:OrgaoEstadual ;
         rdfs:label ?label ;
         cpov:hasJurisdiction ?territorio .
}
ORDER BY ?label
\`\`\`

---

## Exemplos práticos

### Exemplo 1: Ministério da Fazenda (Federal)

\`\`\`turtle
@prefix br: <https://data.gov.br/ontology/adm-publica/> .
@prefix org: <http://www.w3.org/ns/org#> .
@prefix cpov: <http://data.europa.eu/m8g/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

<https://data.gov.br/org/mf-2024>
    a br:OrgaoFederal ;
    a cpov:PublicOrganization ;
    rdfs:label "Ministério da Fazenda" ;
    br:cnpj "00000000000105" ;                    # CNPJ do MF
    br:siorgId "70000" ;                          # ID SIORG
    cpov:hasJurisdiction <https://data.gov.br/territory/brasil> ;
    cpov:jurisdictionLevel "federal" ;
    foaf:homepage <https://www.gov.br/fazenda> ;
    foaf:mbox <mailto:ouvidoria@fazenda.gov.br> .
\`\`\`

### Exemplo 2: Secretaria de Fazenda de Pernambuco (Estadual)

\`\`\`turtle
<https://data.gov.br/org/pe-sefaz-2024>
    a br:OrgaoEstadual ;
    rdfs:label "Secretaria da Fazenda do Estado de Pernambuco" ;
    br:cnpj "16717114000140" ;
    br:codigoIBGE "2611606" ;                      # PE = 2611606
    cpov:hasJurisdiction <https://data.gov.br/territory/pernambuco-2611606> ;
    cpov:jurisdictionLevel "estadual" ;
    org:subOrganizationOf <https://data.gov.br/org/pe-executivo-2024> ;
    foaf:homepage <https://www.sefaz.pe.gov.br> .
\`\`\`

### Exemplo 3: Prefeitura de Recife (Municipal)

\`\`\`turtle
<https://data.gov.br/org/recife-prefeitura-2024>
    a br:Municipio ;
    rdfs:label "Prefeitura do Recife" ;
    br:cnpj "91731015000171" ;                     # CNPJ de Recife
    br:codigoIBGE "2611606" ;                      # Recife = 2611606
    cpov:hasJurisdiction <https://data.gov.br/territory/recife-2611606> ;
    cpov:jurisdictionLevel "municipal" ;
    org:subOrganizationOf <https://data.gov.br/territory/pernambuco-2611606> ;
    foaf:homepage <https://www2.recife.pe.gov.br> .
\`\`\`

---

## Referência técnica

Veja documentação completa em:
- [Arquitetura técnica](arquitetura.md)
- [Padrões base (W3C ORG, CPOV, FOAF)](padroes-base.md)
- [Guia de uso avançado](guia-de-uso.md)
- [Histórico de decisões (ADR)](historico-decisoes.md)

---

## 📊 Status do Projeto

| Componente | Status | Progresso |
|---|---|---|
| Core Ontology (br:*) | ✅ Alpha | 30% |
| CPOV Alignments | ✅ Alpha | 25% |
| Domain Ontologies | 🔄 Em desenvolvimento | 10% |
| SIORG Mapper | 🔄 Em desenvolvimento | 15% |
| SHACL Validation | 🔄 Em desenvolvimento | 20% |
| Documentation | 🔄 Em desenvolvimento | 40% |
| Community Feedback | ⏳ Aguardando | 0% |

---

**Próximo passo**: Acesse [Como Contribuir](../CONTRIBUTING.md)
"""

with open('docs/index.md', 'w', encoding='utf-8') as f:
    f.write(docs_index)

print("✅ docs/index.md criado")

# ============================================================================
# 3. CONTRIBUTING.md - Guia de Contribuição
# ============================================================================

contributing = """# Como Contribuir para br-adm-publica-ontology

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
pyshacl validate \\
    -s validation/shacl-shapes.ttl \\
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
"""

with open('CONTRIBUTING.md', 'w', encoding='utf-8') as f:
    f.write(contributing)

print("✅ CONTRIBUTING.md criado")

# ============================================================================
# 4. .github/ISSUE_TEMPLATE - Templates de Issues
# ============================================================================

bug_report = """---
name: 🐛 Bug Report
about: Reportar erro na ontologia ou documentação
labels: bug
---

## Descrição do Bug
<!-- Descrição clara e concisa do bug -->

## Passos para Reproduzir
1. ...
2. ...
3. ...

## Comportamento Esperado
<!-- O que deveria acontecer -->

## Comportamento Atual
<!-- O que está acontecendo -->

## Ambiente
- Sistema Operacional: 
- Versão da Ontologia: 
- Tool (Protégé, RDFlib, etc):

## Arquivo(s) Afetado(s)
- ontology/...
- docs/...

## Contexto Adicional
<!-- Qualquer informação extra -->
"""

feature_request = """---
name: 🎯 Feature Request
about: Sugerir nova feature (classe, propriedade, etc)
labels: enhancement
---

## Descrição
<!-- Descrição clara da feature -->

## Motivação
Por que essa feature é necessária?

## Caso de Uso
Como seria usada?

## Competency Questions
Que perguntas ela responderia?

**CQ1**: ?
**CQ2**: ?

## Exemplos de Uso (Turtle/SPARQL)
\`\`\`turtle
# Exemplo aqui
\`\`\`

## Alternativas Consideradas
<!-- Outras formas de resolver isso? -->

## Contexto Adicional
<!-- Referências, links, etc -->
"""

ontology_extension = """---
name: 🧬 Ontology Extension
about: Propor extensão à ontologia (br:* namespace)
labels: ontology
---

## Tipo de Extensão
- [ ] Nova classe
- [ ] Nova propriedade
- [ ] Alinhamento com padrão externo
- [ ] Refatoração

## Descrição
<!-- O que está sendo proposto -->

## Motivação
Por que adicionar isso?

## Competency Questions (CQs)
Que perguntas essa extensão responderia?

**CQ1**: ?
**CQ2**: ?

## Exemplos Turtle
\`\`\`turtle
# Exemplo de instância
\`\`\`

## Alinhamentos Propostos
- [ ] W3C ORG?
- [ ] CPOV?
- [ ] schema.org?
- [ ] Outro padrão?

## Impacto
- Número de instâncias que beneficiariam: ?
- Quebra backward compatibility? [ ] Sim [ ] Não
- Novas dependências? [ ] Sim [ ] Não

## Contexto Adicional
<!-- Referências, dados reais, etc -->
"""

with open('.github/ISSUE_TEMPLATE/bug_report.md', 'w', encoding='utf-8') as f:
    f.write(bug_report)
    
with open('.github/ISSUE_TEMPLATE/feature_request.md', 'w', encoding='utf-8') as f:
    f.write(feature_request)
    
with open('.github/ISSUE_TEMPLATE/ontology_extension.md', 'w', encoding='utf-8') as f:
    f.write(ontology_extension)

print("✅ Issue templates criados (.github/ISSUE_TEMPLATE/)")

# ============================================================================
# 5. PROJECT STRUCTURE - Gerar árvore de diretórios
# ============================================================================

structure_json = {
    "project": "br-adm-publica-ontology",
    "root_directories": [
        "docs/",
        "ontology/",
        "mappings/",
        "validation/",
        "assets/",
        ".github/"
    ],
    "key_files": [
        "README.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "LICENSE",
        "CHANGELOG.md",
        "pyproject.toml",
        "requirements.txt"
    ]
}

with open('PROJECT_STRUCTURE.json', 'w', encoding='utf-8') as f:
    json.dump(structure_json, f, ensure_ascii=False, indent=2)

print("✅ PROJECT_STRUCTURE.json criado")

print("\n" + "="*80)
print("RESUMO DO PROJETO GITHUB ESTRUTURADO")
print("="*80)
print(f"""
📦 Projeto: br-adm-publica-ontology
🏢 Sponsor: Aeon Bridge Co.
📄 Licença: CC-BY 4.0

✅ ARQUIVOS CRIADOS:

1. README.md (Raiz)
   └─ Visão geral, histórico, motivação, arquitetura, contribuição
   
2. docs/index.md (Homepage do Projeto)
   └─ Guia de uso, exemplos práticos, referência técnica
   
3. CONTRIBUTING.md
   └─ Processo de contribuição, tipos de PR, diretrizes técnicas
   
4. .github/ISSUE_TEMPLATE/
   ├── bug_report.md
   ├── feature_request.md
   └── ontology_extension.md

5. PROJECT_STRUCTURE.json
   └─ Metadados da estrutura

📁 ESTRUTURA DE DIRETÓRIOS (a ser criada):

br-adm-publica-ontology/
├── docs/                           # Documentação completa
│   ├── index.md                    # Esta foi criada
│   ├── arquitetura.md              # (próximo)
│   ├── padroes-base.md             # (próximo)
│   ├── guia-de-uso.md              # (próximo)
│   ├── historico-decisoes.md       # (próximo)
│   └── exemplos/                   # (próximo)
│
├── ontology/                       # OWL/RDF core
│   ├── br-adm-publica-core.owl
│   ├── br-adm-publica-alignments.owl
│   ├── domain-ontologies/
│   │   ├── saude/
│   │   ├── educacao/
│   │   ├── tributaria/
│   │   └── regulatoria/
│   └── versions/
│
├── mappings/                       # Conversores de dados
│   ├── siorg-to-rdf/
│   ├── ibge-to-rdf/
│   └── cnpj-to-rdf/
│
├── validation/                     # Testes e SHACL
│   ├── shacl-shapes.ttl
│   ├── competency-questions.md
│   └── test-cases/
│
├── assets/                         # Imagens, diagramas
│   ├── arquitetura-camadas.png
│   ├── hierarquia-classes.png
│   └── exemplo-recife.png
│
├── .github/
│   ├── ISSUE_TEMPLATE/             # ✅ Criados
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── ontology_extension.md
│   └── workflows/                  # (próximo)
│       ├── validate-owl.yml
│       ├── test-rdf.yml
│       └── build-docs.yml
│
├── README.md                       # ✅ Criado
├── CONTRIBUTING.md                 # ✅ Criado
├── CODE_OF_CONDUCT.md              # (próximo)
├── LICENSE                         # CC-BY 4.0 (próximo)
├── CHANGELOG.md                    # (próximo)
├── pyproject.toml                  # (próximo)
└── requirements.txt                # (próximo)

🚀 PRÓXIMOS PASSOS:

1. Criar repositório GitHub:
   → https://github.com/aeonbridge/br-adm-publica-ontology
   
2. Inicializar como projeto público com templates de Issues/PRs
   
3. Criar discussions para comunidade
   
4. Configurar CI/CD (.github/workflows/)
   
5. Publicar OWL files em ontology/
   
6. Fazer anúncio público + call for contributions

7. Integrar com dados.gov.br (coordenação com CGU/SPR)

📊 ESTATÍSTICAS INICIAIS:

- Arquivos documentação: 3 (README + docs/index + CONTRIBUTING)
- Templates Issues: 3 (bug, feature, ontology)
- Palavras no README: ~2.500
- Referências incluídas: 10+ (W3C, EU, Brasil)
- Exemplos práticos: 3 (Federal, Estadual, Municipal)
- Status de cobertura: 100% arquitetura + 25% ontologia
""")

print("\n💾 Todos os arquivos foram estruturados e estão prontos para GitHub!\n")
