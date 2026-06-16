# Comando: Ajustar Configuração Android

## Propósito

Configurar o `build.gradle.kts` do módulo app para usar a keystore de release.

## 1. Verificar arquivo atual

```bash
Get-Content -Path "android\app\build.gradle.kts" | Select-Object -First 80
```

## 2. Adicionar configuração de assinatura

No topo do arquivo `android/app/build.gradle.kts`, adicione:

```kotlin
import java.io.FileInputStream
import java.util.Properties

val keystoreProperties = Properties()
val keystorePropertiesFile = rootProject.file("key.properties")
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(FileInputStream(keystorePropertiesFile))
}
```

Dentro do bloco `android { }`, adicione:

```kotlin
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
        isDebuggable = false
        isMinifyEnabled = true
        isShrinkResources = true
        proguardFiles(
            getDefaultProguardFile("proguard-android-optimize.txt"),
            "proguard-rules.pro"
        )
    }
}
```

## 3. Atualizar versionName / versionCode

No `pubspec.yaml`:

```yaml
version: {{VERSION_NAME}}+{{VERSION_CODE}}
```

## 4. Verificar alterações

```bash
flutter analyze
```

## 5. Compilar AAB de release

```bash
flutter build appbundle --release
```
