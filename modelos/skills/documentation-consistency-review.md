# Skill - documentation-consistency-review

**Finalidade:** Validar a consistência entre código e documentação — garantindo que README, specs, arquitetura e docs de requisitos reflitam o estado real do projeto.
**Versão:** 2.1.0

---

## 1. Quando Usar

Invocar sempre que um agente revisar ou atualizar documentação, ou quando mudanças no código podem ter invalidado docs existentes.

**Gatilhos:**
- Implementação de feature que adiciona, remove ou altera comportamento documentado.
- Refatoração que muda estrutura de módulos, APIs ou contratos.
- Revisão documental pós-demanda complexa.
- Discrepância observada entre README e código real.

---

## 2. O que Valida

- [ ] README descreve apenas funcionalidades existentes no código
- [ ] Funcionalidades ausentes marcadas como `[PLANEJADO]` — nunca como implementadas
- [ ] Specs e documentação de requisitos alinhadas com a implementação real
- [ ] Arquitetura documentada reflete a estrutura atual do código
- [ ] Mudanças estruturais atualizaram a documentação correspondente
- [ ] Marcadores de estado usados corretamente: `[INFERIDO]`, `[PENDENTE]`, `[PLANEJADO]`
- [ ] Nenhum dado sensível, caminho absoluto ou URL privada em documentação versionada
- [ ] ADRs (Architecture Decision Records) seguem a estrutura padrão (Contexto, Decisão, Consequências) e estão no diretório correto (ex: `docs/adr/` ou `governance/adr/`)
- [ ] O status do ADR é explícito e segue um ciclo de vida válido (`Proposto`, `Aprovado`, `Depreciado`, `Rejeitado`)
- [ ] Decisões obsoletas estão devidamente marcadas como `Depreciado` ou `Substituído por ADR-XXXX`

---

## 3. O que Analisa

- Divergências entre README e código — features documentadas que não existem
- Docs de arquitetura desatualizados após refatorações
- Specs com requisitos que não têm correspondência na implementação
- Documentação de API com endpoints inexistentes ou parâmetros errados
- Artefatos de planejamento (`plan.md`, `tasks.md`) com status desatualizado

---

## 4. Entradas e Saídas

**Entradas:**
- Arquivos de documentação (`README.md`, `architecture.md`, `spec.md`, etc.)
- Código-fonte ou diff relacionado
- Artefatos de planejamento quando disponíveis

**Saídas:**
- Lista de divergências com localização exata
- Documentos que precisam de atualização e o que deve mudar
- Status de cada documento: `coerente` | `desatualizado` | `ausente` | `pendente`

---

## 5. Regras de Execução e Bloqueios

**Regras:**
- Nunca documentar funcionalidade inexistente como implementada.
- Toda mudança estrutural deve disparar revisão da documentação correspondente.
- Usar marcadores de estado para preservar rastreabilidade sem inventar informação.

**Bloqueios:**
- Documentação declarando feature inexistente como ativa → sinalizar como `[PENDENTE]`
- Contradição entre documentação e código → registrar na auditoria; não fechar a demanda sem resolução
- URL privada, caminho absoluto ou dado sensível em doc versionada → **BLOQUEADO**

---

## 6. Limitações

- Não revisa qualidade de código — apenas consistência com documentação.
- Não valida lógica de negócio — verifica se o que está documentado existe no código.

---

## 7. Critérios de Sucesso

- Toda documentação coerente com o código na data de revisão.
- Divergências documentadas com marcadores de estado adequados.
- Nenhuma URL privada ou dado sensível presente em arquivos versionados.
