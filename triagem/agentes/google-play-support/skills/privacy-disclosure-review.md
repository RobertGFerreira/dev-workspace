# Skill - privacy-disclosure-review

| Campo | Valor |
|:---|:---|
| **Finalidade** | Auditoria de políticas de privacidade, termos de uso e declaração de coleta de dados |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Ao redigir ou auditar o formulário de "Segurança dos Dados" (Data Safety) no Google Play Console.
- Ao revisar o documento público de Política de Privacidade do aplicativo.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] Todos os dados coletados de fato pelo app (ex: localização, e-mail, contatos) estão declarados na política de privacidade.
- [ ] A política declara claramente se os dados são compartilhados com terceiros (ex: SDKs de anúncios ou analytics).
- [ ] O app oferece uma opção clara e simples para o usuário solicitar a exclusão de sua conta e dados.

---

## 3. O que Analisa (Área de Investigação)

- Divergências entre a coleta real de dados no código e o formulário preenchido na loja.
- Políticas de privacidade vagas, genéricas ou hospedadas em URLs inválidas.
- Coleta de dados pessoais sem o consentimento explícito e prévio do usuário.

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Código-fonte do app (verificação de requisições de dados), URL da política de privacidade, formulário de Data Safety preenchido.
- **Saídas Esperadas:** Relatório de conformidade de privacidade e integridade do formulário de Data Safety.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Em caso de dúvida, classificar o dado como coletado e justificar seu uso.
- **Bloqueios Obrigatórios (Veto):** Bloquear qualquer aplicativo que colete dados pessoais sensíveis (ex: localização, contatos) sem ter um link de política de privacidade ativo hospedado sob SSL (HTTPS).
