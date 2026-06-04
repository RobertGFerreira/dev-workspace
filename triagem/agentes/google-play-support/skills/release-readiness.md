# Skill - release-readiness

| Campo | Valor |
|:---|:---|
| **Finalidade** | Validação final de chaves, assinaturas, tamanho e bundle de produção (AAB) |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Na etapa imediatamente anterior ao upload do pacote de aplicativo (Android App Bundle - AAB) para a Play Store.
- Ao configurar chaves de assinatura do app (Keystores/Upload Keys).

---

## 2. O que Valida (Foco de Auditoria)

- [ ] O pacote gerado é um Android App Bundle (`.aab`) assinado com a chave de produção correta.
- [ ] O aplicativo está compilado em modo Release (com flags de depuração desabilitadas: `debuggable=false`).
- [ ] O código de versão (`versionCode`) e nome de versão (`versionName`) foram incrementados corretamente em relação à última release.

---

## 3. O que Analisa (Área de Investigação)

- Chaves de assinatura privadas vazadas no código ou incluídas em pastas públicas do repositório Git.
- Tamanho total do pacote otimizado (uso do Play App Delivery para recursos extras).

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Arquivo `.aab`, credenciais de assinatura (senha/alias/caminho da keystore), metadados da última versão publicada.
- **Saídas Esperadas:** Diagnóstico de assinatura e tamanho do bundle, com aprovação para distribuição.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Garantir que o arquivo keystore de assinatura seja armazenado de forma segura e nunca versionado no repositório.
- **Bloqueios Obrigatórios (Veto):** Bloquear qualquer tentativa de upload de pacotes AAB sem assinatura, ou assinados com keystores de debug padrões.
