# Respostas para Play Console — {{APP_NAME}}

> Respostas prontas para copiar e colar nos formulários do Google Play Console.
> Adapte conforme necessário baseado no código real do app.

---

## Segurança dos Dados (Data Safety)

### 1. O app coleta ou compartilha dados?

`{{DATA_COLLECTION_ANSWER}}`

### 2. Tipo de dados coletados

| Categoria | Dados | Coleta? | Compartilha? | Uso |
|:---|:---|:---:|:---:|:---|
| Localização | Localização aproximada | `{{LOC_APPROX_COLLECT}}` | `{{LOC_APPROX_SHARE}}` | `{{LOC_APPROX_USE}}` |
| Localização | Localização precisa | `{{LOC_PRECISE_COLLECT}}` | `{{LOC_PRECISE_SHARE}}` | `{{LOC_PRECISE_USE}}` |
| Pessoais | Nome | `{{NAME_COLLECT}}` | `{{NAME_SHARE}}` | `{{NAME_USE}}` |
| Pessoais | E-mail | `{{EMAIL_COLLECT}}` | `{{EMAIL_SHARE}}` | `{{EMAIL_USE}}` |
| Pessoais | ID de usuário | `{{USER_ID_COLLECT}}` | `{{USER_ID_SHARE}}` | `{{USER_ID_USE}}` |
| Pessoais | Telefone | `{{PHONE_COLLECT}}` | `{{PHONE_SHARE}}` | `{{PHONE_USE}}` |
| Financeiros | Histórico de compras | `{{PURCHASE_COLLECT}}` | `{{PURCHASE_SHARE}}` | `{{PURCHASE_USE}}` |
| Saúde | Dados de saúde | `{{HEALTH_COLLECT}}` | `{{HEALTH_SHARE}}` | `{{HEALTH_USE}}` |
| Mensagens | E-mails/SMS | `{{MESSAGES_COLLECT}}` | `{{MESSAGES_SHARE}}` | `{{MESSAGES_USE}}` |
| Fotos | Fotos | `{{PHOTOS_COLLECT}}` | `{{PHOTOS_SHARE}}` | `{{PHOTOS_USE}}` |
| Fotos | Vídeos | `{{VIDEOS_COLLECT}}` | `{{VIDEOS_SHARE}}` | `{{VIDEOS_USE}}` |
| Áudio | Gravações de som | `{{AUDIO_COLLECT}}` | `{{AUDIO_SHARE}}` | `{{AUDIO_USE}}` |
| Armazenamento | Arquivos e docs | `{{FILES_COLLECT}}` | `{{FILES_SHARE}}` | `{{FILES_USE}}` |
| Atividade no app | Interações | `{{INTERACTIONS_COLLECT}}` | `{{INTERACTIONS_SHARE}}` | `{{INTERACTIONS_USE}}` |
| Navegação | Histórico web | `{{WEB_HISTORY_COLLECT}}` | `{{WEB_HISTORY_SHARE}}` | `{{WEB_HISTORY_USE}}` |
| Dispositivo | ID do dispositivo | `{{DEVICE_ID_COLLECT}}` | `{{DEVICE_ID_SHARE}}` | `{{DEVICE_ID_USE}}` |
| Dispositivo | Logs de crash | `{{CRASH_LOGS_COLLECT}}` | `{{CRASH_LOGS_SHARE}}` | `{{CRASH_LOGS_USE}}` |
| Dispositivo | Diagnóstico | `{{DIAGNOSTICS_COLLECT}}` | `{{DIAGNOSTICS_SHARE}}` | `{{DIAGNOSTICS_USE}}` |

### 3. Os dados são criptografados em trânsito?

`{{ENCRYPTED_IN_TRANSIT}}`

### 4. O usuário pode solicitar a exclusão dos dados?

`{{DATA_DELETION_POSSIBLE}}`

---

## Declaração de Permissões

### Permissão: `{{PERMISSION_NAME}}`

**Justificativa para o Google:**

> {{PERMISSION_JUSTIFICATION}}

---

## Novidades da Versão (Release Notes)

### {{VERSION_NAME}} ({{VERSION_CODE}})

```
{{RELEASE_NOTES}}
```

---

## Contato

### Dados de contato do desenvolvedor

- **E-mail de suporte:** `{{SUPPORT_EMAIL}}`
- **Telefone:** `{{CONTACT_PHONE}}`
- **Site:** `{{WEBSITE_URL}}`

---

## Contas de Teste

> Para apps com login, fornecer ao revisor do Google:

- **E-mail de teste:** `{{TEST_ACCOUNT_EMAIL}}`
- **Senha:** *(fornecer separadamente, nunca em arquivo versionado)*
- **Instruções:** Acessar `{{LOGIN_URL}}`, usar as credenciais acima
