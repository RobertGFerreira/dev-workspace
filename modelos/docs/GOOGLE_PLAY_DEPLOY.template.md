# Guia de Publicação na Google Play — {{PROJECT_NAME}}

> Manual operacional para preparar, assinar, gerar o pacote `.aab`, testar e publicar o projeto Flutter/Android na Google Play Store.

---

## 1. Informações de Configuração

| Item | Valor do Projeto |
| --- | --- |
| **Projeto** | `{{PROJECT_NAME}}` |
| **Tipo** | Flutter para Android |
| **Package Name (`applicationId`)** | `{{PACKAGE_NAME}}` |
| **Nome do App na Loja** | `{{APP_TITLE}}` |
| **E-mail de Suporte** | `{{EMAIL_SUPPORT}}` |
| **Site de Suporte** | `{{WEBSITE_URL}}` |
| **URL da Política de Privacidade** | `{{PRIVACY_POLICY_URL}}` |

---

## 2. Pré-Requisitos

1. Conta de desenvolvedor do Google Play Developer ativa.
2. Flutter SDK e Android SDK/NDK configurados e funcionais.
3. Imagens da loja prontas:
   - Ícone de alta resolução (512x512 PNG)
   - Imagem promocional (Feature Graphic - 1024x500 JPG/PNG)
   - Screenshots reais do app em celulares/tablets (mínimo 2, recomendado 4-8)

---

## 3. Geração e Configuração da Chave de Assinatura (Keystore)

A keystore é usada para assinar digitalmente o aplicativo. O arquivo gerado é crucial; se perdido, não será possível enviar atualizações para o app.

### Comando para Gerar Keystore (PowerShell / Terminal)

```bash
keytool -genkey -v -keystore {{KEYSTORE_FILENAME}}.jks -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 -alias {{KEYSTORE_ALIAS}}
```

### Configurar `key.properties`

Crie um arquivo em `android/key.properties` (adicione ao `.gitignore` imediatamente) com o seguinte formato:

```properties
storePassword={{STORE_PASSWORD}}
keyPassword={{KEY_PASSWORD}}
keyAlias={{KEYSTORE_ALIAS}}
storeFile={{PATH_TO_KEYSTORE}}/{{KEYSTORE_FILENAME}}.jks
```

### Configurar Assinatura no Gradle (`android/app/build.gradle.kts` ou `build.gradle`)

Adicione o carregamento de propriedades de assinatura no arquivo Gradle do módulo app:

```kotlin
import java.io.FileInputStream
import java.util.Properties

val keystoreProperties = Properties()
val keystorePropertiesFile = rootProject.file("key.properties")
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(FileInputStream(keystorePropertiesFile))
}

android {
    ...
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

---

## 4. Compilação do App Bundle (.aab)

Antes de gerar o build de produção, atualize o `versionCode` (deve ser incremental) e o `versionName` no arquivo `pubspec.yaml` (ex: `version: 1.0.0+1`).

Execute os comandos:

```bash
flutter clean
flutter pub get
flutter analyze
flutter build appbundle --release
```

O arquivo gerado estará localizado em:
`build/app/outputs/bundle/release/app-release.aab`

---

## 5. Declarações Obrigatórias e Classificações

### Segurança de Dados (Data Safety)
No Play Console, responda ao questionário de segurança de dados de acordo com o tratamento real de dados e as permissões requisitadas no `AndroidManifest.xml`. 
*Se o app coletar ou transmitir dados (como e-mail, nome, localização ou fotos), certifique-se de que a declaração esteja 100% alinhada à Política de Privacidade e que a transmissão seja feita exclusivamente via HTTPS.*

### Permissões Sensíveis
- Revise as permissões do `AndroidManifest.xml` antes do envio.
- Evite permissões de acesso amplo como `MANAGE_EXTERNAL_STORAGE` a menos que seja indispensável e previamente justificado.

---

## 6. Checklist de Publicação

- [ ] `flutter analyze` roda sem warnings.
- [ ] O `versionCode` no `pubspec.yaml` foi incrementado em relação ao build anterior.
- [ ] A assinatura de release foi gerada utilizando a Keystore correta (não debug).
- [ ] O arquivo `key.properties` e os arquivos `.jks` ou `.p12` estão adicionados ao `.gitignore`.
- [ ] A URL da Política de Privacidade HTTPS está acessível publicamente.
- [ ] Os dados de login de teste para os revisores do Google estão documentados no console.
