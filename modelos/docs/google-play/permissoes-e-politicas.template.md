# Permissões e Políticas — {{APP_NAME}}

> Análise das permissões do `AndroidManifest.xml` e conformidade com políticas do Google.

## Permissões Detectadas

| Permissão | Onde foi encontrada | Finalidade provável | Exige atenção no Play Console? | Texto sugerido para explicação | Alerta |
|:---|:---|:---|:---:|:---|:---|
| `{{PERMISSION_NAME}}` | `{{SOURCE_FILE}}` | `{{PURPOSE}}` | `{{NEEDS_ATTENTION}}` | `{{EXPLANATION_TEXT}}` | `{{ALERT}}` |

*(Repetir para cada permissão encontrada)*

## Permissões Sensíveis (alto risco de rejeição)

- [ ] `{{SENSITIVE_PERMISSION_1}}` — verificar necessidade real
- [ ] `{{SENSITIVE_PERMISSION_2}}` — verificar necessidade real

> ⚠️ Permissões de alto risco exigem justificativa detalhada e vídeo de demonstração.

## Política de Privacidade

| Item | Status |
|:---|:---:|
| URL acessível publicamente | `{{PRIVACY_POLICY_STATUS}}` |
| HTTPS | `{{HTTPS_STATUS}}` |
| Declara coleta de dados conforme uso real | `{{DATA_COLLECTION_ALIGNED}}` |
| Menciona identificadores de publicidade (Ad ID) | `{{AD_ID_MENTIONED}}` |
| Menciona compartilhamento com terceiros | `{{THIRD_PARTY_SHARING}}` |
| Idioma português (ou idioma do app) | `{{PRIVACY_POLICY_LANGUAGE}}` |

## Data Safety — Respostas Sugeridas

| Pergunta do Play Console | Resposta sugerida | Evidência |
|:---|:---:|:---:|
| Coleta de dados? | `{{DATA_COLLECTION_YES_NO}}` | `{{EVIDENCE_SOURCE}}` |
| Dados pessoais? | `{{PERSONAL_DATA_YES_NO}}` | `{{EVIDENCE_SOURCE}}` |
| Dados financeiros? | `{{FINANCIAL_DATA_YES_NO}}` | `{{EVIDENCE_SOURCE}}` |
| Dados de localização? | `{{LOCATION_DATA_YES_NO}}` | `{{EVIDENCE_SOURCE}}` |
| Identificadores de dispositivo? | `{{DEVICE_ID_YES_NO}}` | `{{EVIDENCE_SOURCE}}` |
| Dados criptografados em trânsito? | `{{ENCRYPTED_TRANSIT_YES_NO}}` | `{{EVIDENCE_SOURCE}}` |

## Check-list de Conformidade

- [ ] Nenhuma permissão desnecessária no manifesto
- [ ] Android Debuggable está `false` no build de release
- [ ] Componentes exportados (`exported=true`) justificados
- [ ] `minSdk` e `targetSdk` compatíveis com políticas atuais
- [ ] Uso de `MANAGE_EXTERNAL_STORAGE` (se aplicável) tem declaração `MANAGE_EXTERNAL_STORAGE_PERMISSION`
- [ ] Câmera / Localização / Microfone só após consentimento explícito do usuário
- [ ] Política de privacidade nomeia os SDKs de terceiros utilizados
