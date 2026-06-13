# Matriz de Responsabilidades — Conselho de Decisão vs. Agentes Existentes

## Objetivo

Eliminar ambiguidade sobre responsabilidades entre o Conselho de Decisão e agentes existentes com escopo similar.

---

## Matriz

| Atividade | Conselho de Decisão | `spec-agent` | `agente-testes` | `ideias-exploracao` | `quality-gate` |
|:---|:---|:---|:---|:---|:---|
| **Criação de SDD** | Apoia com crítica e alternativas | **Dono:** cria e mantém SDD | — | — | — |
| **Revisão de SDD** | **Dono:** produz parecer multi-perspectiva | Revisa tecnicamente | — | — | Valida consistência final |
| **Derivação de testes** | Apoia: identifica cenários negativos, borda e proibidos | — | **Dono:** define estratégia e implementa | — | — |
| **Expansão de features** | **Dono:** propõe alternativas e expansões | Especifica tecnicamente | — | Explora ideias iniciais | — |
| **Decisão técnica** | **Dono:** produz parecer de crítica | Documenta no SDD | — | — | Valida entrega |
| **Ideação ampla** | — | — | — | **Dono:** discovery e ideação | — |
| **Validação final** | — | — | — | — | **Dono:** gate de qualidade |
| **Governança estrutural** | Não atua | Não atua | Não atua | Não atua | Não atua |

---

## Regras de Engajamento

1. Conselho **não substitui** nenhum agente existente — apenas apoia com perspectiva adicional
2. Conselho **não edita** SDD, testes ou implementação — apenas produz pareceres
3. Conselho **responde** ao `orquestrador-agentes` e ao usuário via `/conselho`
4. Conselho **não compete** com `ideias-exploracao` — este foca em ideação ampla; o conselho foca em crítica de decisão específica
5. Conselho **não substitui** `quality-gate` — este valida entrega; o conselho valida decisão antes da implementação
6. Conselho **não substitui** `agente-testes` — este define estratégia; o conselho ajuda a derivar casos
