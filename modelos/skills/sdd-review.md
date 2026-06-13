# Skill - sdd-review

**Finalidade:** Revisão estruturada de Software Design Documents com múltiplas perspectivas de crítica
**Versão:** `1.0.0`

---

## Quando Usar

- Revisão de SDD master ou derivado antes da aprovação final
- Validação de completude e consistência de SDD
- Identificação de lacunas em especificação antes da implementação
- Apoio ao `spec-agent` na qualidade do SDD

## O que Valida

1. [ ] O SDD cobre todos os requisitos funcionais e não funcionais?
2. [ ] As alternativas de design foram consideradas e documentadas?
3. [ ] Há riscos técnicos identificados e mitigados?
4. [ ] O SDD é claro o suficiente para implementação?
5. [ ] Casos de borda e erro foram especificados?
6. [ ] A complexidade da solução é justificada?

## O que Analisa

- Completude da especificação frente aos requisitos
- Clareza e precisão técnica do documento
- Riscos não documentados ou subestimados
- Complexidade acidental vs. essencial
- Consistência com padrões e arquitetura do projeto

## Entradas Necessárias e Saídas Esperadas

- **Entradas:** SDD, requisitos, contexto arquitetural
- **Saídas:** Parecer de revisão com lacunas, riscos e recomendações de melhoria

## Regras de Execução e Bloqueios

- **Regras:** Revisar de 3 perspectivas: conformidade, riscos e simplificação
- **Bloqueios:** SDD sem especificação de casos de erro deve ser sinalizado como incompleto

## Limitações da Skill

Esta skill não escreve ou modifica SDDs. Ela produz pareceres de revisão para que o autor do SDD faça os ajustes.

## Critérios de Sucesso

SDD revisado com lacunas documentadas, riscos explicitados e recomendações acionáveis para melhoria.
