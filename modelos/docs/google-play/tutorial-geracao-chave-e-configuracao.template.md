# Tutorial: Geração de Chave e Configuração de Assinatura

> Aplicável a: `{{APP_NAME}}` (package: `{{PACKAGE_NAME}}`)

## 1. Gerar Keystore (JKS)

```bash
keytool -genkey -v -keystore {{KEYSTORE_FILENAME}}.jks `
  -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 `
  -alias {{KEYSTORE_ALIAS}}
```

Você será perguntado por:
- Senha da keystore (`{{STORE_PASSWORD}}`)
- Senha da chave (`{{KEY_PASSWORD}}`)
- Nome, unidade, organização, cidade, estado, país

Guarde as respostas. Sem elas não é possível publicar atualizações.

## 2. Criar `key.properties`

Arquivo: `android/key.properties` (NUNCA versionar)

```properties
storePassword={{STORE_PASSWORD}}
keyPassword={{KEY_PASSWORD}}
keyAlias={{KEYSTORE_ALIAS}}
storeFile={{KEYSTORE_RELATIVE_PATH}}\{{KEYSTORE_FILENAME}}.jks
```

## 3. Adicionar ao `.gitignore`

```gitignore
# Assinatura Android
android/key.properties
**/*.jks
**/*.keystore
**/*.p12
```

## 4. Configurar `build.gradle.kts`

No arquivo `android/app/build.gradle.kts`, adicione:

```kotlin
import java.io.FileInputStream
import java.util.Properties

val keystoreProperties = Properties()
val keystorePropertiesFile = rootProject.file("key.properties")
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(FileInputStream(keystorePropertiesFile))
}

android {
    signingConfigs {
        create("release") {
            keyAlias = keystoreProperties["keyAlias"] as String
            keyPassword = keystoreProperties["keyPassword"] as String
            storeFile = keystoreProperties["storeFile"]?.let { file(it) }
            storePassword = keystoreProperties["storePassword"] as String
        }
    }

    buildTypes {
        release {
            signingConfig = signingConfigs.getByName("release")
        }
    }
}
```

## 5. Gerar AAB de Release

```bash
flutter clean
flutter pub get
flutter analyze
flutter build appbundle --release
```

O AAB estará em: `build/app/outputs/bundle/release/app-release.aab`

## 6. Extrair certificado PEM (para Google Play App Signing)

```bash
keytool -export -rfc -alias {{KEYSTORE_ALIAS}} `
  -keystore {{KEYSTORE_FILENAME}}.jks `
  -file {{UPLOAD_CERT_FILENAME}}.pem
```

Envie o `.pem` para o Google Play no momento de configurar o **App Signing**.

## 7. Backup

Armazene em local seguro (fora do repositório):
- `{{KEYSTORE_FILENAME}}.jks`
- `{{KEYSTORE_FILENAME}}.jks.bkp`
- Anotações com senhas (cofre de senhas)
