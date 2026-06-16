# Comando: Gerar Keystore

## Propósito

Criar a keystore JKS para assinatura do AAB de release.

## Comando

```bash
keytool -genkey -v -keystore {{KEYSTORE_FILENAME}}.jks `
  -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 `
  -alias {{KEYSTORE_ALIAS}}
```

## O que será perguntado

1. **Senha da keystore** → `{{STORE_PASSWORD}}` (guarde em cofre de senhas)
2. **Senha da chave** → `{{KEY_PASSWORD}}` (guarde em cofre de senhas)
3. **Nome e Sobrenome** → `{{CERT_NAME}}`
4. **Unidade organizacional** → `{{ORG_UNIT}}`
5. **Organização** → `{{ORGANIZATION}}`
6. **Cidade** → `{{CITY}}`
7. **Estado** → `{{STATE}}`
8. **País (código 2 letras)** → `{{COUNTRY_CODE}}`

## Destino

Mover o arquivo `{{KEYSTORE_FILENAME}}.jks` para `android/app/`.

## ⚠️ Segurança

- Adicione `android/app/{{KEYSTORE_FILENAME}}.jks` ao `.gitignore`
- Faça backup em local seguro (fora do repositório)
- NUNCA compartilhe a keystore ou as senhas em repositórios, chats ou e-mails
