# Comando: Exportar Certificado PEM

## Propósito

Extrair o certificado público da keystore no formato PEM para configurar o Google Play App Signing.

## Comando

```bash
keytool -export -rfc -alias {{KEYSTORE_ALIAS}} `
  -keystore {{KEYSTORE_FILENAME}}.jks `
  -file {{UPLOAD_CERT_FILENAME}}.pem
```

## Uso no Play Console

1. Acessar Play Console → App → Configuração → Assinatura do app
2. Escolher "Usar chave de assinatura do Google"
3. Fazer upload do arquivo `{{UPLOAD_CERT_FILENAME}}.pem`

## Segurança

O arquivo `.pem` contém apenas a chave pública. Pode ser versionado se necessário, mas por segurança mantenha fora do repositório.
