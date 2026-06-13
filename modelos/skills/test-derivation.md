# Skill - test-derivation

**Finalidade:** Derivação sistemática de casos de teste (positivos, negativos, borda e comportamentos proibidos) a partir de decisões técnicas e SDDs
**Versão:** `1.0.0`

---

## Quando Usar

- Após definição de SDD ou decisão técnica
- Durante planejamento de testes
- Apoio ao `agente-testes` na identificação de cenários não cobertos
- Revisão de critérios de aceite

## O que Valida

1. [ ] Todos os fluxos principais têm caso de teste positivo?
2. [ ] Fluxos de erro e exceção têm casos de teste negativos?
3. [ ] Limites de entrada, estado e integração têm casos de borda?
4. [ ] Comportamentos proibidos estão explicitamente cobertos?
5. [ ] Os casos de teste são rastreáveis aos requisitos?

## O que Analisa

- Cobertura de cenários: positivos, negativos, borda, proibidos
- Premissas que podem esconder casos de teste faltantes
- Rastreabilidade entre requisitos e casos de teste
- Completude dos critérios de aceite

## Entradas Necessárias e Saídas Esperadas

- **Entradas:** SDD, decisão técnica, requisitos, critérios de aceite
- **Saídas:** Lista de casos de teste categorizados com justificativa

## Regras de Execução e Bloqueios

- **Regras:** Derivar ao menos 1 caso positivo, 1 negativo e 1 de borda por requisito
- **Bloqueios:** Decisão sem critérios de aceite deve ser sinalizada como insuficiente para derivação

## Limitações da Skill

Esta skill deriva casos de teste conceituais, não implementa testes automatizados. O `agente-testes` é responsável pela estratégia e implementação.

## Critérios de Sucesso

Casos de teste derivados cobrindo todas as categorias (positivo, negativo, borda, proibido) com rastreabilidade clara aos requisitos.
