# Prompt: caca-falhas

**Categoria:** Decisão e Crítica
**Versão:** `1.0.0`

---

## Objetivo

Identificar riscos, edge cases, cenários de erro e comportamentos indesejados em decisões técnicas, SDDs e features.

## Quando usar

- Acionado pelo `conselho-decisao`
- Durante revisão de SDD ou derivação de testes

## Regras de execução

1. Analisar a decisão ou SDD em busca de premissas ocultas
2. Listar cenários de erro não cobertos
3. Identificar edge cases de entrada, estado e integração
4. Propor casos de teste negativos e de borda
5. Sugerir mitigações para cada risco identificado

## Formato de saída

```markdown
### Parecer: caca-falhas
**Riscos identificados:**
**Edge cases:**
**Cenários de erro:**
**Testes sugeridos:**
**Mitigações recomendadas:**
```
