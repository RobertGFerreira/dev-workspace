# Skill - code-review-universal

**Finalidade:** Revisão de qualidade de código independente de linguagem ou framework — verificando princípios de design, segurança básica, legibilidade e testabilidade.
**Versão:** 1.0.0

---

## 1. Quando Usar

Invocar esta skill sempre que um agente revisor precisar auditar código-fonte de qualquer linguagem, framework ou tipo de projeto. É a base universal de revisão — agentes especializados (ex: `flutter-code-review`) a complementam com critérios de stack específica.

**Gatilhos:**
- Pull request ou merge request aberto para revisão.
- Implementação de feature marcada como concluída pelo desenvolvedor.
- Refatoração de módulo existente.
- Revisão de código em par (pair review).

---

## 2. O que Valida

- [ ] **Nomenclatura** — variáveis, funções, classes e arquivos seguem a convenção do projeto
- [ ] **Responsabilidade única** — cada função, classe ou módulo tem uma responsabilidade clara
- [ ] **Sem duplicação** — lógica repetida está abstraída em função ou classe reutilizável (DRY)
- [ ] **Tratamento de erros** — exceções e estados de erro são tratados explicitamente
- [ ] **Nenhum código morto** — sem funções, variáveis ou imports não utilizados
- [ ] **Sem debug em produção** — sem `print`, `console.log`, `debugger` ou equivalente
- [ ] **Sem credenciais expostas** — sem token, senha ou chave hardcoded
- [ ] **Inputs validados** — dados externos são validados antes do uso
- [ ] **Recursos liberados** — conexões, streams, timers e listeners têm ciclo de vida gerenciado
- [ ] **Documentação mínima** — funções públicas e interfaces têm docstring ou comentário

---

## 3. O que Analisa

- **Coesão e acoplamento** — módulos bem separados vs. dependências cruzadas desnecessárias
- **Complexidade ciclomática** — funções com muitos branches que deveriam ser refatoradas
- **Segurança básica** — inputs não sanitizados, dados sensíveis em logs, secrets expostos
- **Testabilidade** — código acoplado a dependências globais que impossibilitam testes unitários
- **Legibilidade** — código que exige comentário para ser entendido pode estar mal escrito

---

## 4. Entradas e Saídas

**Entradas:**
- Diff ou conjunto de arquivos a revisar
- Convenções de código do projeto (se disponíveis)
- Contexto do que a mudança faz

**Saídas:**
- Lista de issues por severidade (CRÍTICO | ALTO | MÉDIO | BAIXO | INFO)
- Para cada issue: localização, causa raiz e versão corrigida sugerida
- Resultado final: APROVADO | APROVADO COM RESSALVAS | REPROVADO

---

## 5. Regras de Execução e Bloqueios

**Regras:**
- Toda issue deve ter localização exata (arquivo e linha/função), não descrição genérica.
- Issues CRÍTICO e ALTO bloqueiam aprovação automaticamente.
- Issues MÉDIO e BAIXO geram ressalvas — não bloqueiam, mas devem ser registradas.

**Bloqueios obrigatórios:**
- Credencial ou secret hardcoded → **CRÍTICO / BLOQUEADO**
- Dados sensíveis em log → **CRÍTICO / BLOQUEADO**
- Statement de debug em produção → **ALTO / BLOQUEADO**
- Input externo não validado em endpoint crítico → **ALTO / BLOQUEADO**
- Recurso alocado sem liberação explícita → **ALTO / BLOQUEADO**

---

## 6. Limitações

- Esta skill não verifica lógica de negócio específica do domínio — apenas qualidade de código.
- Não substitui testes automatizados — complementa.
- Para revisão de performance, segurança avançada ou arquitetura, combinar com skills especializadas.

---

## 7. Critérios de Sucesso

- Zero issues CRÍTICO ou ALTO no diff.
- Issues MÉDIO e BAIXO documentados e priorizados pelo time.
- Código aprovado segue nomenclatura, tratamento de erros e ausência de debug/secrets.
