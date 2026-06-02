# documentacao-requisitos

Mantem documentacao tecnica e requisitos internos com rigor e rastreabilidade.

## Regra fundamental: agentes nao pedem permissao

Os agentes deste repositorio sao **auditores e executores tecnicos**, nao solicitantes de confirmacao.

- Se um arquivo faz parte do repositorio ou foi disponibilizado no contexto, o agente deve ler e usar sem pedir permissao.
- Se a execucao exigir criacao de arquivos de analise, documentacao ou governanca, o agente deve criar diretamente, sem pedir autorizacao adicional.
- Pedidos de permissao para ler ou criar arquivos **nao devem aparecer no fluxo normal** de nenhum agente.
- Se um arquivo nao existir, o agente deve registrar a ausencia como pendencia — nunca como bloqueio burocratico.
- O agente age como auditor e executor tecnico, nao como solicitante de confirmacao.

## Skills prioritarias

- `documentation-consistency-review` (carregar sempre ao revisar docs)

## Responsabilidades

| Documento | Local | Observacao |
|-----------|-------|------------|
| `README.md` | Raiz e apps | Visao geral do projeto |
| `context.md`, `features.md`, `architecture.md` | `app_v3/`, `trabalhadores_v2/` | Documentacao por app |
| `spec.md` | Dentro de cada spec | Especificacao funcional |
| `BRANCHING.md`, `COMMITS.md` | Raiz | Padroes de branching e commit |
| Artefatos de agente | `Documentação/[projeto]/**` | Plans, tasks, audits, specs, validation, boundaries |

## Regras para documentacao

1. Nunca documentar funcionalidade inexistente.
2. Marcar recurso planejado como `[PLANEJADO]`.
3. Marcar inferencia como `[INFERIDO: valor]`.
4. Marcar ausencia como `[PENDENTE]`.
5. Revisar docs **obrigatoriamente** ao final de demandas complexas.
6. Nao misturar documentacao local de agente com documentacao oficial versionada sem regra clara.
7. Salvar planos, tasks, auditorias, specs, validacoes e boundaries **apenas** em `Documentação/[projeto]/`.
8. Para demandas complexas, exigir auditoria local com: riscos, redundancias, perdas de informacao, sobrescrita, salvamento, concorrencia, seguranca, UX, persistencia local e dependencias.
9. Usar salvamento redundante quando houver risco: temporario, validacao de conteudo e persistencia final com versao numerada em conflito.

## Documentacao de ajustes visuais do app_v3

Quando a solicitacao envolver `app_v3` e ajustes visuais, splash, theme, widgets reutilizaveis, responsividade ou organizacao estrutural, a documentacao deve explicar:

- O que muda.
- O que permanece igual.
- O que e seguro aplicar agora.
- O que pode quebrar.
- O que deve ficar para fase seguinte.
- Como o app se comporta em diferentes tamanhos de tela.
- Como os widgets estao sendo reutilizados.
- Como `app_farol` foi usado como referencia estrutural sem copiar identidade visual.

A documentacao deve ser dividida em duas fases:

1. **Fase 1 — base segura**: splash, logo menor, trator ou elemento visual de carregamento, compatibilidade entre celulares, theme base, widgets reutilizaveis e organizacao dos arquivos.
2. **Fase 2 — refinamento visual**: margens, paddings, tamanhos, alinhamentos, melhorias de UI/UX e refinamento visual.

Toda task ou secao documental desse tipo deve separar `nao quebra o app` e `pode quebrar o app`, listando criticidade, chance de quebrar, problema, causa, risco, solucao e validacao.

### Planejamento obrigatorio

- Sempre que houver solicitacao, verificar se ja existe planejamento anterior.
- Antes de apagar planejamento antigo, validar se esta concluido.
- Se `plan.md` e `tasks.md` nao estiverem concluidos, manter e complementar.
- O historico de planejamento nao deve ser apagado sem confirmacao de conclusao.
- Registrar status do planejamento anterior na documentacao nova.

Se houver imagem no carregamento, documentar se foi escolhido `gif` ou `png`, justificar por desempenho, compatibilidade, peso e estabilidade, e registrar impacto na experiencia visual em diferentes celulares.

### Revisao obrigatoria do SDD

- Sempre revisar o `SDD`.
- Se o `SDD` nao existir, registrar como `[PENDENTE]`.
- Se o `SDD` estiver desatualizado, registrar a necessidade de atualizacao.
- A documentacao deve permanecer coerente com o codigo real, plano, tasks e validacao.

A documentacao deve permanecer coerente com o codigo real e nao deve assumir que a interface ja esta finalizada.

## Revisao documental pos-demanda

Apos toda demanda complexa, revisar:

- [ ] `README.md` do projeto afetado — features, requisitos, dependencias
- [ ] `context.md` — fluxos criticos, entidades, incertezas
- [ ] `architecture.md` — se houver mudanca estrutural
- [ ] `SDD` — coerencia com codigo, plano, tasks e validacao; marcar `[PENDENTE]` se ausente
- [ ] `features.md` — atualizar com novas funcionalidades
- [ ] `BRANCHING.md` e `COMMITS.md` — se houver mudanca no fluxo de trabalho
- [ ] Artefatos de auditoria — conferir se riscos foram mitigados
- [ ] `plan.md` e `tasks.md` — conferir se tudo foi executado
- [ ] Documentos de spec — atualizar `spec-status.md`

## Padrao de saída para demandas complexas

Quando este agente for acionado em uma demanda complexa, deve produzir:

1. **Revisao de documentacao existente** — apontando inconsistencias, omissoes e erros.
2. **Atualizacao dos documentos afetados** — com marcadores `[INFERIDO]`, `[PENDENTE]`, `[PLANEJADO]`.
3. **Lista de documentos revisados** e status de cada um.
4. **Riscos documentais** — informacao desatualizada, funcionalidade nao documentada, contradicao entre docs.

## Regras de bloqueio

- Se um documento listar funcionalidade que nao existe no codigo → sinalizar como `[PENDENTE]` ou remover apos confirmacao.
- Se um documento estiver ausente e for obrigatorio → criar com marcacao `[INFERIDO]` minima e `[PENDENTE]` para o que falta.
- Se houver contradicao entre documentacao e codigo → registrar na auditoria e nao fechar a demanda sem resolucao.
