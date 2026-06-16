# Dados Sensíveis — {{APP_NAME}}

> ⚠️ **NUNCA versionar este arquivo com valores reais.**
> Use apenas placeholders. O desenvolvedor preenche localmente.
> Este arquivo deve estar no `.gitignore` de cada projeto.

## Keystore

| Campo | Valor (exemplo / placeholder) |
|:---|:---|
| **Arquivo da keystore** | `{{KEYSTORE_FILENAME}}.jks` |
| **Alias da chave** | `{{KEYSTORE_ALIAS}}` |
| **Store password** | `{{STORE_PASSWORD}}` (preencher localmente) |
| **Key password** | `{{KEY_PASSWORD}}` (preencher localmente) |
| **Localização do arquivo** | `android/app/{{KEYSTORE_FILENAME}}.jks` |

## Upload Key (Google Play App Signing)

| Campo | Valor (exemplo / placeholder) |
|:---|:---|
| **Arquivo PEM de upload** | `{{UPLOAD_KEY_PEM}}` |
| **Key store de upload** | `{{UPLOAD_KEYSTORE}}` |

## Service Account (se aplicável)

| Campo | Valor (exemplo / placeholder) |
|:---|:---|
| **Arquivo JSON** | `{{SERVICE_ACCOUNT_JSON}}` |
| **E-mail da service account** | `{{SERVICE_ACCOUNT_EMAIL}}` |

## CI/CD Secrets

| Nome da secret | Exemplo / placeholder |
|:---|:---|
| `{{STORE_FILE_SECRET}}` | caminho codificado |
| `{{STORE_PASSWORD_SECRET}}` | variável de ambiente |
| `{{KEY_PASSWORD_SECRET}}` | variável de ambiente |
| `{{KEY_ALIAS_SECRET}}` | variável de ambiente |

## ⚠️ Lembretes de segurança

- [ ] Keystore adicionada ao `.gitignore`
- [ ] `key.properties` adicionado ao `.gitignore`
- [ ] Service account JSON adicionado ao `.gitignore`
- [ ] Nenhuma senha ou token em markdown versionado
- [ ] Backup da keystore armazenado em local seguro fora do repositório
