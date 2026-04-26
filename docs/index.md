# br-adm-publica-ontology — Documentação

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
