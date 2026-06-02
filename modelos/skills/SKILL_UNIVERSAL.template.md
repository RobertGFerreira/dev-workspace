# Skill - [NOME_DA_SKILL]

**Finalidade:** [Breve resumo da finalidade e especialidade técnica desta habilidade. Exemplo: *Auditoria de consistência de banco de dados SQLite local, versionamento e migrations...*]
**Versão:** [X.Y.Z]

---

## 1. Quando Usar
### Descrição
> *Gatilhos contextuais que indicam quando o agente deve invocar esta habilidade.*

- **O que deve ser escrito:** Cenários práticos, tipos de arquivos tocados ou comandos solicitados que exigem esta skill ativa (ex: *Sempre que houver alteração de schemas de banco, queries cruas SQL ou migrações de dados locais...*).

---

## 2. O que Valida (Foco de Auditoria)
### Descrição
> *Checklist técnico determinístico de itens que devem passar pela triagem rigorosa desta skill.*

- **Use esta seção para:** Enumerar verificações booleanas de conformidade inegociáveis.
- **Exemplos de Verificações:**
  1. [ ] As queries SQL estão devidamente parametrizadas para evitar falhas de injeção?
  2. [ ] As migrations estão modeladas de forma incremental e são perfeitamente reversíveis?
  3. [ ] Existe plano de backup ou contingência de dados antes de alterações destrutivas de schemas?

---

## 3. O que Analisa (Área de Investigação)
### Descrição
> *Camadas lógica, estrutural, de performance ou segurança inspecionadas pela skill.*

- **O que deve ser escrito:** Onde a skill deve aprofundar sua auditoria cognitiva (ex: *Auditoria de queries redundantes, travamentos de I/O na Main Thread, verificação de dados órfãos em chaves estrangeiras...*).

---

## 4. Entradas Necessárias e Saídas Esperadas
### Descrição
> *Insumos obrigatórios de entrada e o resultado esperado da aplicação da skill.*

- **Entradas Necessárias:** [Lista de arquivos, dados contextuais ou esquemas estruturais obrigatórios para que a skill funcione. Exemplo: *Mapeamento de tabelas, código-fonte do DAO/Repository, arquivo de versão de migração*].
- **Saídas Esperadas:** [Resultado esperado após a validação. Exemplo: *Validação boolean de integridade, relatório detalhado de gargalos identificados e código SQL de correção otimizado*].

---

## 5. Regras de Execução e Bloqueios
### Descrição
> *Instruções operacionais imperativas e critérios rígidos de veto de alterações.*

- **Regras Operacionais:** [Como a skill deve atuar durante a análise. Exemplo: *Sempre validar compatibilidade retroativa de versões anteriores de tabelas...*].
- **Bloqueios Obrigatórios (Veto):** [O que a skill deve barrar incondicionalmente. Exemplo: *Bloquear qualquer DROP TABLE, deleção de dados locais sem confirmação da API ou queries montadas com interpolação direta de texto do usuário*].

---

## 6. Limitações da Skill
### Descrição
> *Fronteiras funcionais onde a skill perde sua eficácia ou delega responsabilidades.*

- **O que deve ser escrito:** Cenários onde esta skill não possui capacidade de auditoria e deve ser combinada a outras skills (ex: *Esta skill não analisa layout de widgets ou gerenciamento de estado de telas, focando apenas na camada de banco de dados e persistência SQLite*).

---

## 7. Critérios de Sucesso
### Descrição
> *A definição exata de aprovação técnica desta skill.*

- **Use esta seção para:** Listar as metas ideais para que a auditoria da skill dê resultado positivo (ex: *Migração executada com sucesso com zero perda de informações, lint estático limpo e queries com tempo de resposta ideal*).
