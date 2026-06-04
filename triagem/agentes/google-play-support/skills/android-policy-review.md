# Skill - android-policy-review

| Campo | Valor |
|:---|:---|
| **Finalidade** | Auditoria de conformidade do aplicativo com as políticas de desenvolvedor do Google Play |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Antes de qualquer publicação (novo app ou atualização relevante) para evitar rejeições ou suspensões.
- Ao auditar o uso de permissões sensíveis (localização em segundo plano, acesso a arquivos, etc.).

---

## 2. O que Valida (Foco de Auditoria)

- [ ] O app não solicita permissões excessivas ou desnecessárias para seu funcionamento principal.
- [ ] Políticas de propriedade intelectual (uso de marcas de terceiros, direitos autorais) são respeitadas.
- [ ] O aplicativo atende aos requisitos de classificação etária declarados no questionário IARC.

---

## 3. O que Analisa (Área de Investigação)

- Risco de rejeição por violação de políticas de conteúdo (violência, linguagem, pornografia).
- Problemas com anúncios exibidos no aplicativo que possam violar as regras de apps voltados para crianças.
- Uso indevido de permissões que requeiram justificação formal adicional ao Google.

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Lista de permissões no `AndroidManifest.xml`, escopo do aplicativo, público-alvo.
- **Saídas Esperadas:** Diagnóstico de risco de violação de políticas do Google Play.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Analisar de forma extremamente conservadora a necessidade de permissões em segundo plano (background permissions).
- **Bloqueios Obrigatórios (Veto):** Bloquear qualquer compilação (build) que declare permissões críticas como `ACCESS_BACKGROUND_LOCATION` ou `QUERY_ALL_PACKAGES` sem uma justificativa técnica formalizada em ADR.
