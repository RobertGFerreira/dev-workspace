# Skill - agent-instructions-review

**Finalidade:** Auditar e orientar a criação e manutenção do arquivo `AGENTS.md` (ou `CLAUDE.md`) na raiz de projetos, garantindo instruções concisas, de alto sinal e baseadas no ferramental real do projeto.
**Versão:** 1.0.0

---

## 1. Quando Usar

Invocar sempre que for necessário criar, atualizar ou auditar as instruções gerais de desenvolvimento do repositório destinadas a agentes de IA.

**Gatilhos:**
- Solicitação de criação ou revisão de `AGENTS.md` ou `CLAUDE.md`.
- Início de um novo projeto (Day-0) para documentar comandos essenciais.
- Instruções de agentes muito longas, obsoletas ou divergentes das convenções reais do projeto.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] Arquivo criado na raiz como `AGENTS.md` com symlink para `CLAUDE.md` (quando aplicável ao ambiente).
- [ ] O tamanho do arquivo está contido (idealmente abaixo de 60 linhas, máximo de 100 linhas).
- [ ] Contém informações exatas sobre o gerenciador de pacotes e comandos principais do projeto.
- [ ] Inclui a seção obrigatória de atribuição de commits do agente.
- [ ] Apresenta comandos com escopo de arquivo (para testes e lints rápidos) em vez de comandos globais pesados, quando disponíveis.
- [ ] Não duplica regras de linters (como eslint, biome, ruff) que já estão em arquivos de configuração locais.

---

## 3. Estrutura Padrão Recomendada

O arquivo `AGENTS.md` gerado deve seguir a seguinte estrutura mínima:

```markdown
# Agent Instructions

## Package Manager
Use **[gerenciador]**: `[comando install]`, `[comando dev]`, `[comando test]`

## Commit Attribution
AI commits MUST include:
\`\`\`
Co-Authored-By: [Nome do Modelo] <[email-byline]>
\`\`\`

## File-Scoped Commands
| Task | Command |
|------|---------|
| Typecheck | [comando específico por arquivo] |
| Lint | [comando específico por arquivo] |
| Test | [comando específico por arquivo] |

## Key Conventions
- [Regra de design ou padrão crítico 1]
- [Regra de design ou padrão crítico 2]
```

---

## 4. Antipadrões a Evitar e Bloquear

- Textos introdutórios longos ("Bem-vindo ao projeto...", "Este documento serve para...").
- Descrições detalhadas de regras de formatação (ex: "use 2 espaços de indentação") que devem ser resolvidas via linter.
- Listagem manual de skills ou plugins instalados na governança local (os agentes as descobrem dinamicamente).
- Explicações em prosa longa; prefira tabelas e blocos de código.

---

## 5. Regras de Execução e Limitações

- **Regras:** Sempre priorize comandos de escopo restrito (ex: testar um único arquivo) para economizar tempo e contexto de execução.
- **Limitações:** Esta skill não substitui lints automáticos nem testes de CI/CD; ela apenas valida a clareza e precisão do guia de bordo dos agentes.
