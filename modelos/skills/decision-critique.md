# Skill - decision-critique

**Finalidade:** Crítica estruturada de decisões técnicas e de produto com múltiplas perspectivas
**Versão:** `1.0.0`

---

## Quando Usar

- Revisão de decisão técnica antes da implementação
- Avaliação de trade-offs entre abordagens concorrentes
- Análise de impacto de decisão em arquitetura, performance ou manutenibilidade
- Validação de alinhamento entre decisão e requisitos

## O que Valida

1. [ ] A decisão está alinhada com os requisitos documentados?
2. [ ] Os trade-offs foram explicitamente considerados?
3. [ ] Há riscos não mitigados na decisão?
4. [ ] A decisão é justificada com evidência técnica?
5. [ ] Alternativas foram consideradas antes da escolha final?

## O que Analisa

- Alinhamento da decisão com restrições do projeto
- Impacto em arquitetura, performance, segurança e manutenibilidade
- Premissas ocultas que podem invalidar a decisão
- Custo de implementação e manutenção de cada alternativa

## Entradas Necessárias e Saídas Esperadas

- **Entradas:** Decisão técnica documentada, contexto do projeto, requisitos relacionados
- **Saídas:** Parecer de crítica com riscos, trade-offs e recomendação

## Regras de Execução e Bloqueios

- **Regras:** Sempre considerar ao menos 2 perspectivas (conformidade + risco)
- **Bloqueios:** Decisão sem justificativa técnica deve ser bloqueada para esclarecimento

## Limitações da Skill

Esta skill não avalia qualidade de código ou cobertura de testes. Foca exclusivamente na decisão anterior à implementação.

## Critérios de Sucesso

Decisão revisada com riscos documentados, trade-offs explicitados e recomendação clara de aprovação, ajuste ou rejeição.
