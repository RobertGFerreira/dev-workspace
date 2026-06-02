# Guia de Contribuição — {{NOME_DO_PROJETO}}

> **Tipo de projeto:** `{{TIPO_DO_PROJETO}}` <!-- OPEN SOURCE | CLOSED SOURCE | SOLO -->

---

## Ambiente de desenvolvimento

### Pré-requisitos

| Ferramenta | Versão mínima |
|:---|:---:|
| {{FERRAMENTA}} | `{{VERSAO}}` |

### Setup local

```bash
git clone {{REPOSITORY_URL}}
cd {{PROJECT_SLUG}}
{{COMANDO_DE_INSTALACAO}}
cp .env.example .env
```

### Verificação de qualidade local

```bash
{{COMANDO_DE_LINT}}
{{COMANDO_DE_TESTES}}
```

---

## Fluxo de branches

| Branch | Propósito |
|:---|:---|
| `main` | Versão estável de produção |
| `develop` <!-- OPCIONAL --> | Integração de features em progresso |
| `feature/{{descricao}}` | Nova funcionalidade |
| `fix/{{descricao}}` | Correção isolada |
| `chore/{{descricao}}` | Manutenção (infra, docs, deps) |

---

## Conventional Commits

```text
<tipo>(<escopo-opcional>): <descrição curta no imperativo>

[corpo opcional]

[rodapé opcional — ex: BREAKING CHANGE: ...]
```

| Tipo | Uso |
|:---|:---|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Alteração de documentação |
| `refactor` | Refatoração sem mudança de comportamento |
| `test` | Adição ou correção de testes |
| `perf` | Melhoria de performance |
| `chore` | Manutenção (build, deps, CI) |
| `security` | Correção de vulnerabilidade |

---

## Checklist de Pull Request

Antes de abrir um PR, confirme:

- [ ] Escopo pequeno e objetivo claro (um PR, uma mudança)
- [ ] Lint e testes mínimos executados sem falhas
- [ ] Documentação afetada atualizada
- [ ] Nenhum segredo, caminho local ou dado sensível incluído
- [ ] Mudanças de arquitetura acompanhadas de ADR ou justificativa

---

## Code Review

**Prioridades de revisão (em ordem):**
1. Bugs e regressões
2. Segurança e exposição de dados
3. Performance em fluxos críticos
4. Manutenibilidade e clareza
5. Cobertura de testes

**Regras:**
- Evitar refatorações oportunistas fora do escopo do PR.
- Solicitar teste demonstrável quando a mudança afetar fluxo crítico.
- Comentários de revisão devem ser acionáveis, não subjetivos.

---

## Projetos fechados (closed source) <!-- OPCIONAL: Remover para projetos open source -->

- Contribuições externas não são aceitas por padrão.
- Acesso ao repositório é gerenciado pela equipe responsável.
- Dúvidas e solicitações devem ser encaminhadas a `{{CONTATO_INTERNO}}`.
