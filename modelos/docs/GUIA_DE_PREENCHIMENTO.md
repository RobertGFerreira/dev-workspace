# Guia de Preenchimento dos Templates

> **Audiência:** Autores de documentação, responsáveis por projetos, tech leads.
> **Propósito:** Orientar o preenchimento dos templates sem poluir os arquivos finais com instruções pedagógicas.

---

## Hierarquia e Propósito dos Documentos

| Arquivo | Audiência | Nível de detalhe | Obrigatório |
|:---|:---|:---:|:---:|
| `README.md` | Qualquer pessoa que abre o repositório | Rápido | ✅ |
| `DOCUMENTO_UNIVERSAL.md` | Stakeholders, produto, PM | Negócio/produto | Recomendado |
| `SDD.md` | Engenheiros, arquitetos | Técnico completo | Recomendado |
| `ARCHITECTURE.md` | Arquitetos, tech leads | Decisões macro | Recomendado |
| `SECURITY.md` | Todos | Política | ✅ (projetos públicos) |
| `CONTRIBUTING.md` | Contribuidores | Processo | ✅ (projetos públicos) |
| `CHANGELOG.md` | Todos | Histórico | ✅ |
| `ROADMAP.md` | Time, stakeholders | Planejamento | Opcional |
| `AGENTE.md` | Engenheiros de IA | Configuração | Opcional |

---

## Padrão de Placeholders

| Sintaxe | Significado | Ação |
|:---|:---|:---|
| `{{CAMPO_EM_MAIUSCULAS}}` | Campo obrigatório | Substituir pelo valor real |
| `{{CAMPO_OPCIONAL}}` + comentário `<!-- OPCIONAL -->` | Campo que pode ser removido | Preencher ou deletar o bloco |
| `<!-- REMOVER SE NÃO APLICÁVEL -->` | Bloco condicional inteiro | Deletar o bloco se não se aplicar |
| `<!-- OPCIONAL: ... -->` | Seção inteira opcional | Manter ou deletar conforme o projeto |
| `<!-- RECOMENDADO para ... -->` | Seção com recomendação de contexto | Manter para o tipo de projeto indicado |

---

## Orientações por Tipo de Projeto

### Projeto Privado / Corporativo

- **README:** Foque em instalação, execução e variáveis de ambiente. Omita repository URL se for interna.
- **DOCUMENTO_UNIVERSAL:** Detalhe stakeholders internos, área de negócio e conformidade (LGPD, fiscal).
- **SDD:** Máximo nível de detalhe. Inclua banco de dados, autenticação, CI/CD.
- **SECURITY:** Canal de reporte interno. Defina SLA com o time de segurança.
- **CONTRIBUTING:** Use o bloco de projetos fechados. Especifique o contato interno.
- **Screenshots:** Opcional — verifique políticas de privacidade de produto antes de incluir.

### Showcase / Portfólio

- **README:** Simplifique ao máximo. Setup deve funcionar sem ambiguidade para recrutadores.
- **DOCUMENTO_UNIVERSAL:** Destaque motivação técnica, decisões de engenharia e complexidade.
- **SDD:** Pode ser simplificado. Foque na arquitetura e nos diferenciais técnicos.
- **ARCHITECTURE:** Documente o padrão arquitetural adotado e justifique as escolhas.
- **Screenshots:** Crítico — inclua mockups das telas principais e GIFs de fluxos.
- **CONTRIBUTING:** Simplificar ou omitir. Showcase geralmente não aceita contribuições externas.

### Site / Landing Page

- **README:** Mínimo — instalação local e build de produção.
- **DOCUMENTO_UNIVERSAL:** Foque no objetivo de conversão e público-alvo da landing.
- **SDD:** Enxuto — stack, rotas, SEO, analytics.
- **ARCHITECTURE:** Opcional — use apenas se houver CDN, edge functions ou stack relevante.
- **SECURITY:** Simplificar — foque em variáveis de analytics e formulários.

---

## Orientações de Segurança no Preenchimento

### Nunca incluir em documentação

- Caminhos absolutos locais (`C:/Users/`, `/home/nome/`)
- IPs ou hostnames de servidores de produção/staging
- Tokens de API, mesmo que expirados
- Chaves privadas de qualquer natureza
- Strings de conexão com credenciais reais
- Nomes completos de usuários internos sem consentimento
- URLs de webhooks de produção

### Sempre usar

- Placeholders no formato `{{NOME_DA_VARIAVEL}}`
- `.env.example` com valores completamente fictícios
- Descrição funcional de variáveis, não valores reais

---

## Adaptações por Tipo de Projeto: Seções Chave

### README

| Seção | Privado | Showcase | Site |
|:---|:---:|:---:|:---:|
| Visão geral | ✅ | ✅ | ✅ |
| Pré-requisitos | ✅ | ✅ | ✅ |
| Instalação | ✅ | ✅ | ✅ |
| Variáveis de ambiente | ✅ | ✅ | ✅ |
| Repository URL | ❌ | ✅ | ✅ |
| Funcionalidades detalhadas | Link para DOC | ✅ | Mínimo |

### DOCUMENTO_UNIVERSAL

| Seção | Privado | Showcase | Site |
|:---|:---:|:---:|:---:|
| Fluxos principais | Recomendado | ✅ | Funil de vendas |
| Integrações | ✅ | Opcional | Analytics/CRM |
| Screenshots | Opcional | ✅ Crítico | ✅ |

### SDD

| Seção | Privado | Showcase | Site |
|:---|:---:|:---:|:---:|
| Banco de dados | ✅ | Conforme o projeto | Raramente |
| CI/CD | ✅ | Opcional | Opcional |
| Performance SLA | ✅ | Opcional | Core Web Vitals |
| Compliance | ✅ LGPD | Conforme | Conforme |

---

## Checklist Final Antes de Publicar

- [ ] Todos os `{{PLACEHOLDERS}}` foram substituídos ou removidos
- [ ] Nenhum caminho local, IP ou URL interna foi incluído
- [ ] `.env.example` contém apenas placeholders e descrições
- [ ] Screenshots aprovadas para publicação pública
- [ ] Histórico git verificado para segredos (`git log`, `trufflehog`)
- [ ] Dependências auditadas (`npm audit` ou equivalente)
- [ ] CHANGELOG e ROADMAP sem referências ao sistema gerador
- [ ] Status e versão atualizados em todos os documentos
