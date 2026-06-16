# Comando: Mover Arquivos de Assinatura

## Propósito

Mover keystore e certificados para os locais corretos dentro do projeto.

## Comandos

```bash
# Mover keystore para a pasta android/app
Move-Item -Path ".\{{KEYSTORE_FILENAME}}.jks" `
  -Destination "android\app\{{KEYSTORE_FILENAME}}.jks"

# Mover certificado PEM para docs (opcional)
Move-Item -Path ".\{{UPLOAD_CERT_FILENAME}}.pem" `
  -Destination "docs\{{UPLOAD_CERT_FILENAME}}.pem"
```

## Verificação

```bash
# Confirmar que os arquivos estão no local correto
Get-ChildItem -Path "android\app\*.jks"
Get-ChildItem -Path "android\app\*.pem"
```

## ⚠️ .gitignore

Certifique-se de que estas entradas estão no `.gitignore`:

```gitignore
android/app/*.jks
android/app/*.p12
android/app/*.keystore
```
