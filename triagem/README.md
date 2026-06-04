# Triagem de Agentes, Skills e Prompts

## Status

Esta pasta e uma area de auditoria e curadoria. Ela nao e biblioteca oficial, nao instala agentes e nao altera a governanca do ecossistema.

Fonte unica de observacoes:

- `notas_master.md`

Regras de uso:

1. Ver como referencia.
2. Comparar com `modelos/`.
3. Decidir antes de incorporar.
4. Incorporar somente via governanca correta.
5. Nao criar `notas.md` locais por agente, skill, prompt ou pasta.

`Utils/` continua como fonte externa local e deve permanecer fora do Git.

---

## Estrutura

| Pasta | Funcao |
|:---|:---|
| `agentes/` | Visao por agente, com agente, prompt, skills locais e referencias externas relacionadas. |
| `skills/` | Visao por categoria de skill. |
| `prompts/` | Area reservada para prompts em triagem. |
| `referencias/` | Referencias gerais que nao foram associadas a agente especifico. |
| `notas_master.md` | Observacoes, decisoes, fusoes, divisoes, descartes, referencias e proximos passos. |

---

## Estrutura por agente

Cada pasta em `agentes/` deve manter somente artefatos de triagem:

1. `AGENTE.md` ou arquivos de agente copiados.
2. `skills/` com skills locais ou referencias de skill relacionadas.
3. `prompts/` com prompts vinculados.
4. `referencias/` com materiais externos selecionados.

Notas locais nao devem existir dentro das pastas de agentes. Toda decisao fica em `notas_master.md`.

---

## Incorporacao

Fluxo minimo:

1. Ler o item em `triagem/`.
2. Comparar com a biblioteca oficial em `modelos/`.
3. Registrar ou atualizar a decisao em `notas_master.md`.
4. Incorporar apenas o minimo util.
5. Se afetar agentes, prompts, skills, permissoes ou governanca, acionar o guardiao.
