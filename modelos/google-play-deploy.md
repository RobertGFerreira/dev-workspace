# Google Play Deploy — app_v3

## Visão geral

Este manual operacional descreve como preparar, assinar, gerar o `.aab`, testar e publicar o projeto Flutter `app_v3` na Google Play Store.

Contexto validado no projeto:

| Item | Valor atual |
| --- | --- |
| Projeto | `app_v3` |
| Tipo | Flutter para Android |
| Nome Dart no `pubspec.yaml` | `fiscalizacao_condominio` |
| `applicationId` Android atual | `br.com.condominiorural.fiscal` |
| Nome exibido no AndroidManifest | `Fiscalização Condomínio Rural` |
| Versão atual no `pubspec.yaml` | `1.0.2+2` (última atualização: 30/05/2026) |
| Gradle | Kotlin DSL: `android/app/build.gradle.kts` |
| Banco local | SQLite via `sqflite` |
| Operação | Offline-first, com sincronização posterior via API HTTP configurável |
| Fluxo inicial | Seleção de base/cidade: `saojose` ou `vargem` |

O app permite selecionar a base/cidade, criar ou carregar o banco SQLite local, consultar trabalhadores, registrar fiscalizações, capturar/compactar fotos, enviar fotos pendentes, sincronizar trabalhadores/turmeiros e transmitir fiscalizações para uma API configurável no próprio app.

Observação importante: o contexto informado cita o package name `fiscalizacaocondominio`, mas o código atual usa `name: fiscalizacao_condominio` no `pubspec.yaml` e `applicationId = "br.com.condominiorural.fiscal"` no Gradle. Para a Google Play, o identificador definitivo é o `applicationId`; depois de criado o app na Play Store, ele não deve ser alterado.

> **Fonte**: Este guia foi gerado a partir do documento `Documentação/Guia Completo para Publicar App Flutter na Google Play Store (2024-2025-2026).docx` e adaptado ao estado real do projeto `app_v3` (código-fonte, configurações, permissões, endpoints e dados institucionais).

Endpoints observados no código atual:

| Recurso no app | Caminho montado no código | Observação |
| --- | --- | --- |
| Trabalhadores | `[API_URL]trabalhadores` | `TrabalhadorController.sincronizar()` |
| Turmeiros | `[API_URL]turmeiros` | `TurmeirosController.sincronizar()` |
| Fiscalização única | `[API_URL]fiscalizacao` | `FiscalizacaoController.enviarFiscalizacao()` |
| Fiscalizações pendentes | `[API_URL]fiscalizacoes` | `FiscalizacaoController.enviarFiscalizacoesPendentes()` |
| Fotos para baixar | `[API_URL]/fotos.zip` | `TrabalhadorController.baixarFotos()` |
| Fotos para enviar | `[API_URL]/imagens` | `TrabalhadorController.enviarFotos()` |

Os endpoints informados no contexto (`apitrabalhadores`, `apiturmeiros`, `apifiscalizacao`, `apifiscalizacoes`, `apiimagens`, `apifotos.zip`) podem existir no backend ou em documentação externa, mas não aparecem exatamente assim no código Dart atual. Antes da publicação, validar a URL configurada no app e a rota real do backend.

## Antes de começar

1. Confirmar que a conta Google Play Developer está ativa.
2. Confirmar autenticação em dois fatores na conta Google.
3. Ter Flutter instalado e funcional.
4. Ter Android Studio instalado com SDK, JDK e Gradle funcionais.
5. Rodar o projeto localmente antes de gerar release:

```bash
cd app_v3
flutter doctor -v
flutter pub get
flutter analyze
flutter run
```

6. Confirmar que o app compila em Android.
7. Confirmar acesso a `Documentação/dados.md`.
8. Preparar imagens da loja:
   - ícone de alta resolução;
   - feature graphic;
   - screenshots reais do app.
9. Hospedar política de privacidade em URL pública HTTPS.
10. Validar se a API configurável do app aceita HTTPS. Se o backend ainda usar apenas HTTP, tratar como risco de segurança e de aprovação.

Dados institucionais encontrados em `Documentação/dados.md`:

| Campo | Valor |
| --- | --- |
| Empresa/autoria | LFabris Consultoria em TI |
| Autor | Leonardo F. Fabris |
| Telefone | (19) 99750-1761 |
| E-mail | contato@lfabris.com.br |
| Site | https://condominio.leofabris.com.br |

Arquivos mínimos que devem ser revisados antes do envio:

```text
app_v3/pubspec.yaml
app_v3/android/app/build.gradle.kts
app_v3/android/app/src/main/AndroidManifest.xml
Documentação/dados.md
Documentação/google-play-deploy.md
```

## Criar keystore

A keystore é o arquivo privado usado para assinar o app antes do envio para a Play Console. Para apps novos, a Play Store usa Play App Signing: o arquivo local normalmente funciona como upload key. Guarde esse arquivo com backup seguro.

### Windows PowerShell

Padrão local deste projeto:

```text
Documentação/google-play-secrets/upload-keystore-app-v3.jks
Documentação/google-play-secrets/upload-keystore-app-v3.p12
```

Esses arquivos são locais e restritos. A pasta `Documentação/` está ignorada no Git, mas isso não substitui backup seguro fora do repositório.

Executar a partir de:

```text
C:\Users\Robert\Documents\GitHub\condominio-rural\app_v3
```

Criar a pasta local de segredos:

```powershell
$AppDir = (Resolve-Path ".").Path
if ((Split-Path $AppDir -Leaf) -ne "app_v3") {
    throw "Execute dentro da pasta app_v3."
}

$RepoRoot = (Resolve-Path (Join-Path $AppDir "..")).Path
$SecretsDir = Join-Path $RepoRoot "Documentação\google-play-secrets"
New-Item -ItemType Directory -Force -Path $SecretsDir
```

Se `keytool` estiver no PATH, gerar a chave JKS:

```powershell
keytool -genkey -v -keystore (Join-Path $SecretsDir "upload-keystore-app-v3.jks") -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 -alias upload
```

Se `keytool` não estiver no PATH, localize o Java usado pelo Flutter:

```powershell
flutter doctor -v
```

Procure a linha `Java binary at:` e use o caminho do `keytool.exe` na mesma instalação do Java.

No ambiente atual validado:

```text
Java binary at: C:\Program Files\Android\Android Studio\jbr\bin\java
```

Comando recomendado:

```powershell
& "C:\Program Files\Android\Android Studio\jbr\bin\keytool.exe" -genkey -v -keystore (Join-Path $SecretsDir "upload-keystore-app-v3.jks") -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 -alias upload
```

Converter a chave para PKCS12:

```powershell
& "C:\Program Files\Android\Android Studio\jbr\bin\keytool.exe" -importkeystore -srckeystore (Join-Path $SecretsDir "upload-keystore-app-v3.jks") -destkeystore (Join-Path $SecretsDir "upload-keystore-app-v3.p12") -deststoretype pkcs12
```

Validar arquivos:

```powershell
Test-Path (Join-Path $SecretsDir "upload-keystore-app-v3.jks")
Test-Path (Join-Path $SecretsDir "upload-keystore-app-v3.p12")
```

### macOS/Linux

Fluxo alternativo apenas se o build for feito fora do Windows:

```bash
keytool -genkey -v -keystore "$HOME/upload-keystore-app-v3.jks" -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 -alias upload
keytool -importkeystore -srckeystore "$HOME/upload-keystore-app-v3.jks" -destkeystore "$HOME/upload-keystore-app-v3.p12" -deststoretype pkcs12
```

### Como preencher o prompt

| Pergunta do `keytool` | Preencher com |
| --- | --- |
| Enter keystore password | Senha forte e única. Guardar em cofre de senhas. |
| Re-enter new password | Repetir a senha. |
| What is your first and last name? | `Leonardo F. Fabris` ou responsável legal da conta. |
| What is the name of your organizational unit? | `TI` ou `[SUBSTITUIR]`. |
| What is the name of your organization? | `LFabris Consultoria em TI`. |
| What is the name of your City or Locality? | `[SUBSTITUIR CIDADE]`. |
| What is the name of your State or Province? | `[SUBSTITUIR ESTADO]`. |
| What is the two-letter country code? | `BR`. |
| Is CN=... correct? | Digitar `yes` se estiver correto. |

### Onde salvar

Recomendado:

```text
C:\Users\Robert\Documents\GitHub\condominio-rural\Documentação\google-play-secrets\upload-keystore-app-v3.jks
C:\Users\Robert\Documents\GitHub\condominio-rural\Documentação\google-play-secrets\upload-keystore-app-v3.p12
```

Não salve diretamente em:

```text
app_v3/
app_v3/android/
```

Use apenas `Documentação/google-play-secrets/` para esse fluxo local.

### Backup obrigatório

1. Guardar uma cópia em cofre seguro de credenciais.
2. Guardar uma segunda cópia em mídia offline.
3. Guardar as senhas separadas dos arquivos `.jks`/`.p12`.
4. Nunca enviar `.jks`/`.p12` por WhatsApp, e-mail comum ou Git.

### Não subir para o Git

Confirmar que `app_v3/.gitignore` ou `.gitignore` da raiz contém:

```gitignore
# Android signing
app_v3/android/key.properties
app_v3/android/*.jks
app_v3/android/*.keystore
app_v3/android/*.p12
Documentação/google-play-secrets/
*.jks
*.keystore
*.p12
```

## Configurar key.properties

O arquivo deve ser criado em:

```text
app_v3/android/key.properties
```

Este arquivo contém senha de assinatura. Não versionar e não enviar para terceiros.

### Criar automaticamente no Windows

Executar dentro de:

```text
C:\Users\Robert\Documents\GitHub\condominio-rural\app_v3
```

Comando PowerShell:

```powershell
function Read-PlainSecret($Prompt) {
    $secure = Read-Host $Prompt -AsSecureString
    $ptr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
    try {
        [Runtime.InteropServices.Marshal]::PtrToStringBSTR($ptr)
    } finally {
        [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($ptr)
    }
}

$AppDir = (Resolve-Path ".").Path
if ((Split-Path $AppDir -Leaf) -ne "app_v3") {
    throw "Execute este comando dentro da pasta app_v3."
}

$RepoRoot = (Resolve-Path (Join-Path $AppDir "..")).Path
$SecretsDir = Join-Path $RepoRoot "Documentação\google-play-secrets"
$StoreFileNative = Join-Path $SecretsDir "upload-keystore-app-v3.p12"
$KeyProperties = Join-Path $AppDir "android\key.properties"

if (!(Test-Path $StoreFileNative)) {
    throw "Arquivo não encontrado: $StoreFileNative. Gere ou converta a keystore antes."
}

$StorePassword = Read-PlainSecret "storePassword"
$KeyPassword = Read-PlainSecret "keyPassword"
$StoreFile = $StoreFileNative.Replace("\", "/").Replace("ç", "\u00e7").Replace("ã", "\u00e3")

@"
storePassword=$StorePassword
keyPassword=$KeyPassword
keyAlias=upload
storeFile=$StoreFile
"@ | Set-Content -Encoding ASCII -NoNewline -Path $KeyProperties

Test-Path $KeyProperties
```

Resultado esperado em `app_v3/android/key.properties`:

```text
storePassword=SUA_SENHA
keyPassword=SUA_SENHA
keyAlias=upload
storeFile=C:/Users/Robert/Documents/GitHub/condominio-rural/Documenta\u00e7\u00e3o/google-play-secrets/upload-keystore-app-v3.p12
```

No Windows, preferir barras normais (`/`) no `storeFile`. Se o caminho tiver acentos, usar escapes Unicode como `Documenta\u00e7\u00e3o`, porque o Gradle carrega `key.properties` via Java `Properties`.

Validação rápida:

```powershell
Test-Path android\key.properties
Test-Path (Join-Path (Resolve-Path "$PWD\..") "Documentação\google-play-secrets\upload-keystore-app-v3.jks")
Test-Path (Join-Path (Resolve-Path "$PWD\..") "Documentação\google-play-secrets\upload-keystore-app-v3.p12")
```

## Configurar assinatura no Gradle

O projeto atual usa Kotlin DSL:

```text
app_v3/android/app/build.gradle.kts
```

> **Estado atual (30/05/2026)**: O `build.gradle.kts` já está configurado com `signingConfigs.create("release")` e `signingConfig = signingConfigs.getByName("release")`. A configuração abaixo reflete o estado já implementado. Se estiver restaurando de backup ou configurando um novo ambiente, siga o modelo completo.

O arquivo já carrega `key.properties`, define `signingConfigs.create("release")` e usa `signingConfigs.getByName("release")` no `buildTypes.release`.

### Modelo Kotlin DSL para `build.gradle.kts`

No topo do arquivo, antes de `plugins`, adicionar:

```kotlin
import java.io.FileInputStream
import java.util.Properties
```

Depois do bloco `plugins`, adicionar:

```kotlin
val keystoreProperties = Properties()
val keystorePropertiesFile = rootProject.file("key.properties")
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(FileInputStream(keystorePropertiesFile))
}
```

Dentro de `android { ... }`, antes de `buildTypes`, adicionar:

```kotlin
signingConfigs {
    create("release") {
        keyAlias = keystoreProperties["keyAlias"] as String
        keyPassword = keystoreProperties["keyPassword"] as String
        storeFile = keystoreProperties["storeFile"]?.let { file(it) }
        storePassword = keystoreProperties["storePassword"] as String
    }
}
```

Trocar o bloco `buildTypes` por:

```kotlin
buildTypes {
    release {
        signingConfig = signingConfigs.getByName("release")
    }
}
```

Arquivo final esperado, mantendo os valores atuais do projeto:

```kotlin
import java.io.FileInputStream
import java.util.Properties

plugins {
    id("com.android.application")
    id("kotlin-android")
    id("dev.flutter.flutter-gradle-plugin")
}

val keystoreProperties = Properties()
val keystorePropertiesFile = rootProject.file("key.properties")
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(FileInputStream(keystorePropertiesFile))
}

android {
    namespace = "br.com.condominiorural.fiscal"
    compileSdk = flutter.compileSdkVersion
    ndkVersion = "28.2.13676358"

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }

    kotlinOptions {
        jvmTarget = JavaVersion.VERSION_11.toString()
    }

    defaultConfig {
        applicationId = "br.com.condominiorural.fiscal"
        minSdk = flutter.minSdkVersion
        targetSdk = flutter.targetSdkVersion
        versionCode = flutter.versionCode
        versionName = flutter.versionName
    }

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

flutter {
    source = "../.."
}
```

### Modelo Groovy para `build.gradle`

Usar apenas se o projeto for convertido para Groovy. O projeto atual não usa este formato.

```groovy
import java.util.Properties
import java.io.FileInputStream

plugins {
    id "com.android.application"
    id "kotlin-android"
    id "dev.flutter.flutter-gradle-plugin"
}

def keystoreProperties = new Properties()
def keystorePropertiesFile = rootProject.file('key.properties')
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(new FileInputStream(keystorePropertiesFile))
}

android {
    namespace "br.com.condominiorural.fiscal"

    defaultConfig {
        applicationId "br.com.condominiorural.fiscal"
        versionCode flutter.versionCode
        versionName flutter.versionName
    }

    signingConfigs {
        release {
            keyAlias keystoreProperties['keyAlias']
            keyPassword keystoreProperties['keyPassword']
            storeFile keystoreProperties['storeFile'] ? file(keystoreProperties['storeFile']) : null
            storePassword keystoreProperties['storePassword']
        }
    }

    buildTypes {
        release {
            signingConfig signingConfigs.release
        }
    }
}
```

## Ajustar versão do app

Editar:

```text
app_v3/pubspec.yaml
```

Versão atual:

```yaml
version: 1.0.2+2
```

Como funciona:

| Parte | Exemplo | Uso |
| --- | --- | --- |
| `versionName` | `1.0.0` | Versão visível para usuários. |
| `versionCode` | `1` | Número interno exigido pela Play. Deve aumentar em todo envio. |

Exemplos válidos:

```yaml
version: 1.0.0+2
```

Próximo envio:

```yaml
version: 1.0.1+3
```

Envio seguinte:

```yaml
version: 1.0.2+4
```

Regra prática:

1. Nunca repetir o número depois do `+`.
2. Sempre aumentar o `versionCode` antes de subir um novo `.aab`.
3. Não alterar `applicationId` após criar o app na Play Console.

## Gerar o arquivo .aab

Executar dentro do projeto Flutter:

```bash
cd app_v3
flutter clean
flutter pub get
flutter analyze
flutter build appbundle --release
```

Caminho esperado pelo Flutter em versões recentes:

```text
app_v3/build/app/outputs/bundle/release/app-release.aab
```

Em algumas versões do Flutter, o arquivo pode sair como:

```text
app_v3/build/app/outputs/bundle/release/app.aab
```

Validação no Windows:

```powershell
Get-ChildItem app_v3\build\app\outputs\bundle\release
```

Antes de subir:

1. Confirmar que o arquivo `.aab` foi criado.
2. Confirmar que o build não usou assinatura debug.
3. Confirmar que `versionCode` é novo.
4. Confirmar que `applicationId` é `br.com.condominiorural.fiscal`.
5. Instalar em teste interno pela Play Console antes de produção.

## Preparar os arquivos da loja

### Ícone do app

Preparar ícone de alta resolução para a ficha da loja:

| Campo | Recomendação |
| --- | --- |
| Formato | PNG |
| Tamanho | 512 x 512 px |
| Transparência | Evitar se a Play recortar/mascarar mal |
| Conteúdo | Ícone limpo, sem texto pequeno |

O app já possui assets:

```text
app_v3/assets/images/logo.png
app_v3/assets/images/iconApk.png
```

Validar visualmente se um deles serve como base. Se não servir, criar um ícone específico para loja.

### Feature graphic

Obrigatório para a ficha da loja:

| Campo | Valor |
| --- | --- |
| Dimensão | 1024 x 500 px |
| Formato | JPG ou PNG 24 bits sem alfa |
| Conteúdo | Visual limpo sobre fiscalização rural, sem promessas comerciais |

Texto recomendado dentro da imagem, se usar:

```text
Fiscalização Condomínio Rural
Controle de fiscalizações em campo
```

### Screenshots

Capturar telas reais do app. Não inventar fluxo que não existe.

Screenshots recomendados:

1. Tela de seleção de base/cidade.
2. Lista de trabalhadores.
3. Detalhe do trabalhador.
4. Tela de fiscalizações.
5. Tela de cadastro de fiscalização.
6. Tela de funções/sincronização.
7. Tela de parâmetros da API, sem expor host real se for sensível.

Requisitos operacionais:

| Item | Valor |
| --- | --- |
| Mínimo | 2 screenshots |
| Recomendado | 4 a 8 screenshots |
| Formato | JPG ou PNG 24 bits sem alfa |
| Menor dimensão | Pelo menos 320 px |
| Maior dimensão | Até 3840 px |
| Proporção | A maior dimensão não deve ser mais que 2x a menor |

Não incluir:

1. CPF real de trabalhador.
2. Nome real sem autorização.
3. Endereço real.
4. Endpoint interno da API.
5. Token, IP privado ou dados sensíveis.

### Nome do app

Sugestão:

```text
Fiscalização Condomínio Rural
```

Se passar de 30 caracteres na Play Console, usar:

```text
Fiscalização Rural
```

### Descrição curta

```text
Controle offline de fiscalizações, trabalhadores e fotos em campo.
```

### Descrição completa

Modelo pronto está em `Anexos prontos para copiar`.

## Criar o app no Google Play Console

1. Acessar:

```text
https://play.google.com/console
```

2. Clicar em `Criar app`.
3. Preencher:

| Campo | Valor recomendado |
| --- | --- |
| Nome do app | `Fiscalização Condomínio Rural` ou `Fiscalização Rural` |
| Idioma padrão | `Português (Brasil) - pt-BR` |
| App ou jogo | `App` |
| Gratuito ou pago | `Gratuito`, salvo decisão comercial diferente |

4. Aceitar declarações obrigatórias:
   - Programa para desenvolvedores do Google Play;
   - leis de exportação dos EUA;
   - políticas aplicáveis da Play Store.
5. Clicar em `Criar app`.

Observações críticas:

1. Se escolher `Gratuito`, normalmente não é possível transformar o mesmo app em pago depois.
2. O `applicationId` usado no primeiro upload deve ser definitivo.
3. Para este app, o `applicationId` atual é:

```text
br.com.condominiorural.fiscal
```

## Preencher a ficha da loja

Ir em:

```text
Crescer usuários > Presença na loja > Ficha principal da loja
```

Preencher:

| Campo | Valor para usar |
| --- | --- |
| Nome do app | `Fiscalização Condomínio Rural` |
| Descrição curta | `Controle offline de fiscalizações, trabalhadores e fotos em campo.` |
| Descrição completa | Usar modelo dos anexos. |
| Categoria | `Produtividade` ou `Corporativo`, conforme opções disponíveis na conta. |
| E-mail de suporte | `contato@lfabris.com.br` |
| Site | `https://condominio.leofabris.com.br` |
| Telefone | `(19) 99750-1761` |
| Política de privacidade | `https://condominio.leofabris.com.br/privacy_policy.html` |

Texto deve ser fiel ao app:

1. Pode citar operação offline-first.
2. Pode citar SQLite local.
3. Pode citar sincronização via API configurável.
4. Pode citar trabalhadores, fiscalizações, fotos e funções administrativas.
5. Não citar login, mapas, GPS, push notification, painel web, analytics ou recursos não encontrados no projeto.

## Configurar segurança de dados

Ir em:

```text
Política e programas > Conteúdo do app > Segurança de dados
```

A Google exige uma declaração completa e coerente com o app, permissões, SDKs e backend. A definição prática de "coleta" na Play inclui dados transmitidos para fora do dispositivo.

### Resposta base para o app_v3

| Pergunta | Resposta recomendada | Justificativa |
| --- | --- | --- |
| O app coleta ou compartilha dados de usuário? | `Sim` | O app envia fiscalizações e fotos para API HTTP configurável. |
| Os dados são criptografados em trânsito? | `Sim`, somente se a API estiver em HTTPS. Caso use HTTP, responder `Não` e corrigir o backend antes de publicar. | O app permite configurar `http` ou `https`; publicação profissional deve usar HTTPS. |
| O usuário pode solicitar exclusão de dados? | `Sim`, se houver e-mail/processo de suporte. | Usar `contato@lfabris.com.br` ou canal oficial. |
| O app permite criar conta? | `Não`, salvo se existir fluxo externo não identificado no código. | Não foi encontrado fluxo de cadastro/login de conta de usuário. |
| Dados são opcionais ou obrigatórios? | `Obrigatórios` para a operação de fiscalização. | O app depende de dados operacionais para funcionar. |

### Tipos de dados prováveis

Declarar apenas o que realmente é transmitido ao backend em produção.

| Tipo na Play Console | Declarar? | Base técnica |
| --- | --- | --- |
| Informações pessoais: nome | `Sim` | Tabela `trabalhadores`, novos trabalhadores e payload de fiscalização podem conter nome. |
| Informações pessoais: CPF/documentos | `Sim`, se a categoria estiver disponível como identificador pessoal/outro dado pessoal | Código exibe e armazena CPF em SQLite. |
| Fotos e vídeos: fotos | `Sim` | Fotos de trabalhadores são capturadas, compactadas e enviadas em Base64 para `/imagens`. |
| Arquivos e documentos | `Talvez` | O app baixa `fotos.zip` e compartilha backup SQLite; declarar se o backend receber arquivo de backup. |
| Informações financeiras | `Não`, salvo se produção/valor/conferência for classificada como dado financeiro pessoal no uso real | O app exibe produções e valores; validar juridicamente. |
| Localização | `Não` | Não foi encontrada permissão de localização. |
| Contatos | `Não` | Não foi encontrada permissão de contatos. |
| Saúde | `Não`, salvo se atestados forem tratados como dado sensível de saúde no processo real | O app possui tabela/tela de atestados; validar com responsável jurídico antes de responder. |
| IDs do dispositivo | `Não encontrado no fluxo atual` | Há modelo `Dispositivo`, mas não foi confirmado envio de identificador persistente. |
| Diagnóstico/crash logs | `Não`, salvo se SDK externo for adicionado | Não foi encontrado Firebase Crashlytics/Analytics. |

### Finalidade de uso

Usar finalidades compatíveis:

| Dado | Finalidade |
| --- | --- |
| Nome, CPF, situação, admissão, dados do trabalhador | Funcionalidade do app / gestão operacional |
| Fiscalizações e registros | Funcionalidade do app / produtividade |
| Fotos | Funcionalidade do app / identificação operacional |
| Dados de API configurável | Funcionalidade do app |

### Compartilhamento

Responder `Não compartilha com terceiros` se o backend for controlado pela mesma organização responsável pelo app e não houver repasse a terceiros. Se a API for de cliente, fornecedor ou operador externo, marcar de acordo com o contrato real. Usar `[SUBSTITUIR]` se não houver confirmação.

## Responder o questionário de classificação

Ir em:

```text
Política e programas > Conteúdo do app > Classificação do conteúdo
```

Selecionar categoria adequada: app utilitário/produtividade/corporativo.

Respostas recomendadas para o app_v3:

| Tema IARC | Resposta | Justificativa |
| --- | --- | --- |
| Violência | `Não` | O app controla fiscalizações e trabalhadores; não há conteúdo violento. |
| Medo/terror | `Não` | Não há esse tipo de conteúdo. |
| Conteúdo sexual/nudez | `Não` | Não há esse tipo de conteúdo. |
| Linguagem imprópria | `Não` | Não há conteúdo gerado para comunicação pública. |
| Drogas, álcool ou tabaco | `Não` | Não há promoção desses itens. |
| Jogos de azar | `Não` | Não é jogo. |
| Compras digitais | `Não` | Não foi encontrada integração com Google Play Billing. |
| Comunicação entre usuários | `Não` | Não há chat, fórum ou rede social. |
| Compartilhamento de localização | `Não` | Não há permissão de localização. |
| Conteúdo gerado pelo usuário | `Não` para conteúdo público; `Sim` somente se fotos/registros forem tratados como UGC visível a outros usuários | As fotos e registros são operacionais e enviados ao backend, não publicados em comunidade. |
| Público infantil | `Não` | App operacional de fiscalização rural, não direcionado a crianças. |

Se o questionário perguntar sobre coleta de dados pessoais, responder coerente com a seção `Segurança de dados`.

## Configurar permissões

Permissões declaradas atualmente em:

```text
app_v3/android/app/src/main/AndroidManifest.xml
```

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.CAMERA"/>
```

### Análise por permissão

| Permissão | Por que existe no app | Runtime permission? | Play Console | Impacto |
| --- | --- | --- | --- | --- |
| `INTERNET` | Sincronizar trabalhadores, turmeiros, fiscalizações, fotos e baixar `fotos.zip`. | Não. | Normalmente não exige formulário específico. | Baixo. |
| `ACCESS_NETWORK_STATE` | Verificar estado de rede por plugins/rotinas de sincronização. | Não. | Normalmente não exige formulário específico. | Baixo. |
| `CAMERA` | Capturar foto de trabalhador via `image_picker`. | Sim. | Pode ser revisada; precisa estar coerente com ficha e política. | Médio. |
| `READ_EXTERNAL_STORAGE` | Selecionar/ler imagens em Android antigo. | Sim em Android antigo. | Pode aparecer na revisão. | Médio; pode exigir ajuste para Android moderno. |
| `WRITE_EXTERNAL_STORAGE` | Escrita legada de fotos/arquivos. | Sim em Android antigo. | Pode aparecer na revisão. | Médio; em Android moderno é legado/depreciado. |
| `MANAGE_EXTERNAL_STORAGE` | Acesso amplo a todos os arquivos. Pelo código atual, parece desnecessária. | Permissão especial. | Sim, alto risco. Exige formulário e aprovação se mantida. | Alto risco de rejeição. |

### Recomendação técnica antes de publicar

Remover `MANAGE_EXTERNAL_STORAGE`, salvo se houver uma justificativa central e comprovável para acesso a todos os arquivos do dispositivo. O app usa diretório próprio via `getExternalStorageDirectory()` e fotos selecionadas/capturadas, o que normalmente não justifica acesso amplo a todos os arquivos.

Trecho recomendado após revisão:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" android:maxSdkVersion="32" />
```

Se o app realmente precisar selecionar fotos no Android 13+, avaliar permissão moderna:

```xml
<uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />
```

Não adicionar `READ_MEDIA_IMAGES` sem testar o fluxo real de galeria em Android 13+.

Texto para declaração de câmera:

```text
O aplicativo usa a câmera para capturar fotos de trabalhadores durante o fluxo operacional de fiscalização. As fotos são armazenadas localmente no dispositivo, compactadas e podem ser enviadas posteriormente para a API configurada pelo operador do app.
```

Texto para armazenamento, se perguntado:

```text
O aplicativo usa armazenamento local para manter banco SQLite, fotos capturadas e arquivos temporários necessários ao funcionamento offline-first. O acesso é usado para operação interna do app, sem leitura indiscriminada de arquivos pessoais do usuário.
```

## Política de privacidade

A política de privacidade é obrigatória porque o app manipula dados pessoais/operacionais de trabalhadores, fotos, CPF, fiscalizações e sincronização com backend.

### Onde hospedar

Usar uma URL pública HTTPS:

```text
https://condominio.leofabris.com.br/privacy_policy.html
```

Arquivo local da política no projeto:

```text
app_v3/Site/privacy_policy.html
```

Arquivo local de compatibilidade/redirecionamento:

```text
app_v3/Site/privacy-policy.html
```

Opções aceitáveis:

1. Site institucional.
2. GitHub Pages.
3. Google Sites.
4. Página estática em domínio próprio.

Não usar:

1. Arquivo local.
2. Link privado.
3. Google Drive com permissão restrita.
4. PDF sem acesso público estável.

### O que a política deve citar

1. Nome do app.
2. Responsável pelo app.
3. E-mail de suporte.
4. Dados tratados:
   - nomes;
   - CPF;
   - dados de trabalhadores;
   - registros de fiscalização;
   - fotos;
   - informações de produção/conferência, se aplicável;
   - dados de atestados/bloqueios, se usados na operação real.
5. Armazenamento local em SQLite.
6. Sincronização via API configurável.
7. Uso offline-first.
8. Uso de câmera.
9. Exclusão/remoção de dados mediante solicitação.
10. Prazo e canal de atendimento.

### Modelo pronto

Usar o modelo completo em `Anexos prontos para copiar`.

## Configurar teste interno

Ir em:

```text
Testar e lançar > Teste > Teste interno
```

Passos:

1. Clicar em `Criar nova versão`.
2. Enviar o arquivo:

```text
app_v3/build/app/outputs/bundle/release/app-release.aab
```

3. Preencher notas da versão:

```text
Versão inicial para validação interna do app Fiscalização Condomínio Rural.
Inclui seleção de base, banco SQLite local, consulta de trabalhadores, controle de fiscalizações, captura de fotos e sincronização via API configurável.
```

4. Criar lista de testadores.
5. Adicionar e-mails Google dos testadores.
6. Salvar.
7. Revisar versão.
8. Iniciar lançamento para teste interno.
9. Copiar o link de participação.
10. Enviar o link aos testadores.

Validações obrigatórias no teste interno:

1. Instalar pelo link da Play.
2. Abrir app.
3. Selecionar `São José`.
4. Selecionar `Vargem`.
5. Configurar API em `Parâmetros`.
6. Sincronizar trabalhadores.
7. Sincronizar turmeiros.
8. Baixar fotos.
9. Capturar foto.
10. Criar fiscalização.
11. Fechar fiscalização.
12. Enviar fiscalização.
13. Enviar fotos pendentes.
14. Testar sem internet.
15. Testar com internet instável.

## Configurar teste fechado

Teste fechado é diferente de teste interno:

| Tipo | Uso | Observação |
| --- | --- | --- |
| Teste interno | Validação rápida com equipe pequena. | Distribuição costuma ser mais rápida. |
| Teste fechado | Validação com grupo controlado maior. | Pode ser obrigatório para contas pessoais novas. |

Para contas pessoais criadas após 13/11/2023, a Google exige teste fechado com pelo menos 12 testadores opt-in por 14 dias contínuos antes de solicitar acesso à produção. Essa exigência pode variar conforme tipo e histórico da conta; confirmar no painel da própria Play Console.

Passos:

1. Ir em:

```text
Testar e lançar > Teste > Teste fechado
```

2. Criar uma faixa de teste fechado.
3. Criar lista de testadores.
4. Adicionar pelo menos 12 e-mails Google, se a conta estiver sujeita à exigência.
5. Enviar o `.aab`.
6. Preencher notas da versão.
7. Publicar o teste fechado.
8. Enviar link de opt-in aos testadores.
9. Confirmar que todos aceitaram o convite.
10. Manter os testadores opt-in por 14 dias contínuos, se aplicável.
11. Coletar evidências:
    - instalação;
    - abertura;
    - execução de sincronização;
    - registro de fiscalização;
    - captura de foto;
    - envio posterior.

Texto para orientar testadores:

```text
Por favor, acesse o link de teste, aceite participar, instale o app e execute pelo menos uma validação completa: abrir o app, selecionar uma base, acessar trabalhadores, abrir uma fiscalização e testar o fluxo offline/online conforme orientação. Mantenha-se inscrito no teste até o fim do período de avaliação.
```

## Publicar em produção

Antes da produção, concluir:

1. Ficha da loja.
2. Política de privacidade.
3. Segurança de dados.
4. Classificação de conteúdo.
5. Público-alvo.
6. Permissões.
7. Países/regiões.
8. Teste interno.
9. Teste fechado, se exigido.
10. Correção da assinatura release.
11. Correção de `MANAGE_EXTERNAL_STORAGE`, se não houver justificativa aprovada.

Passos:

1. Ir em:

```text
Testar e lançar > Produção
```

2. Clicar em `Criar nova versão`.
3. Enviar o `.aab`.
4. Conferir App Signing.
5. Preencher notas da versão:

```text
Primeira versão de produção do app Fiscalização Condomínio Rural, com suporte a operação offline-first, banco SQLite local, controle de fiscalizações, trabalhadores, fotos e sincronização via API configurável.
```

6. Clicar em `Revisar versão`.
7. Corrigir alertas da Play Console.
8. Escolher lançamento:
   - `100%` se for distribuição controlada e já validada;
   - gradual, por exemplo `10%`, se houver base grande de usuários.
9. Enviar para revisão.
10. Acompanhar e-mail da conta desenvolvedora.

Se a Play Console mostrar alerta de política:

1. Não insistir no envio sem corrigir.
2. Abrir o detalhe do alerta.
3. Conferir se o alerta envolve permissões, privacidade, Data Safety ou target SDK.
4. Corrigir código/configuração.
5. Gerar novo `.aab` com `versionCode` incrementado.

## Checklist final

Antes de clicar em publicar:

```text
[ ] O app abre instalado pela Play em teste interno.
[ ] O app seleciona São José e cria/carrega sao_jose.db.
[ ] O app seleciona Vargem e cria/carrega vargem.db.
[ ] A tela de parâmetros salva protocolo, endereço e porta.
[ ] A API de produção/homologação usa HTTPS.
[ ] Sincronizar trabalhadores funciona.
[ ] Sincronizar turmeiros funciona.
[ ] Baixar fotos funciona.
[ ] Capturar foto funciona.
[ ] Compactar foto funciona.
[ ] Enviar fotos pendentes funciona.
[ ] Criar fiscalização funciona.
[ ] Fechar fiscalização funciona.
[ ] Enviar fiscalização funciona.
[ ] Enviar fiscalizações pendentes funciona.
[ ] Fluxo offline sem internet não quebra o app.
[ ] `flutter analyze` foi executado.
[ ] `flutter build appbundle --release` foi executado.
[ ] `app-release.aab` existe.
[ ] `versionCode` foi incrementado.
[ ] `applicationId` está correto: br.com.condominiorural.fiscal.
[ ] Release usa keystore release, não debug.
[ ] `key.properties` não está no Git.
[ ] `.jks`/`.p12` não está no Git.
[ ] `MANAGE_EXTERNAL_STORAGE` foi removida ou justificada com aprovação.
[ ] Política de privacidade está pública em HTTPS.
[ ] E-mail de suporte está correto: contato@lfabris.com.br.
[ ] Ficha da loja não promete funcionalidades inexistentes.
[ ] Screenshots não expõem dados reais sensíveis.
[ ] Segurança de dados corresponde ao app e à política.
[ ] Classificação IARC foi respondida.
[ ] Permissões foram revisadas.
[ ] Testadores instalaram e validaram o app.
```

## Erros comuns e solução

| Erro | Causa provável | Solução |
| --- | --- | --- |
| `keystore not found` | Caminho errado no `storeFile`. | Usar caminho absoluto e barras `\\` no Windows. |
| `Keystore was tampered with, or password was incorrect` | Senha incorreta. | Conferir `storePassword` e `keyPassword`. |
| `version code already exists` | `versionCode` repetido. | Aumentar número depois do `+` no `pubspec.yaml` e gerar novo `.aab`. |
| `package name already exists` | `applicationId` já usado em outro app. | Para app novo, escolher ID único antes do primeiro upload. Para app já criado, não trocar sem estratégia. |
| Build release assinado como debug | `build.gradle.kts` ainda aponta para `signingConfigs.getByName("debug")`. | Trocar para `signingConfigs.getByName("release")`. |
| Play bloqueia por `MANAGE_EXTERNAL_STORAGE` | Permissão de alto risco sem justificativa. | Remover permissão ou preencher declaração com evidência forte. Recomendado remover. |
| Política de privacidade ausente | URL não preenchida ou privada. | Publicar página HTTPS e inserir no Play Console. |
| Data Safety inconsistente | Declaração diz que não coleta, mas app envia dados para API. | Declarar dados transmitidos: trabalhadores, fiscalizações, fotos etc. |
| API HTTP marcada como criptografada | App usa `http` em produção. | Usar HTTPS ou responder que não criptografa. Recomendado corrigir para HTTPS. |
| Screenshots rejeitados | Tamanho/formato inadequado ou dados sensíveis expostos. | Usar PNG/JPG válido e dados fictícios. |
| App rejeitado por conteúdo enganoso | Descrição promete recursos não existentes. | Remover qualquer menção a login, GPS, dashboard, analytics ou recursos não encontrados. |
| App não instala no teste | `minSdk`, assinatura ou bundle inválido. | Testar via Play Console e conferir relatório de pré-lançamento. |
| Fotos não funcionam em Android novo | Permissões de mídia/câmera incompatíveis. | Testar Android 13+ e ajustar permissões conforme necessidade real. |

## Anexos prontos para copiar

### Modelo de key.properties

```text
storePassword=[SUBSTITUIR]
keyPassword=[SUBSTITUIR]
keyAlias=upload
storeFile=C:/Users/Robert/Documents/GitHub/condominio-rural/Documenta\u00e7\u00e3o/google-play-secrets/upload-keystore-app-v3.p12
```

### Modelo de build.gradle.kts

```kotlin
import java.io.FileInputStream
import java.util.Properties

plugins {
    id("com.android.application")
    id("kotlin-android")
    id("dev.flutter.flutter-gradle-plugin")
}

val keystoreProperties = Properties()
val keystorePropertiesFile = rootProject.file("key.properties")
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(FileInputStream(keystorePropertiesFile))
}

android {
    namespace = "br.com.condominiorural.fiscal"
    compileSdk = flutter.compileSdkVersion
    ndkVersion = "28.2.13676358"

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }

    kotlinOptions {
        jvmTarget = JavaVersion.VERSION_11.toString()
    }

    defaultConfig {
        applicationId = "br.com.condominiorural.fiscal"
        minSdk = flutter.minSdkVersion
        targetSdk = flutter.targetSdkVersion
        versionCode = flutter.versionCode
        versionName = flutter.versionName
    }

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

flutter {
    source = "../.."
}
```

### Modelo de descrição curta

```text
Controle offline de fiscalizações, trabalhadores e fotos em campo.
```

### Modelo de descrição longa

```text
Fiscalização Condomínio Rural é um aplicativo operacional para apoio a fiscalizações em campo.

O app permite selecionar a base de trabalho, carregar dados em banco SQLite local, consultar trabalhadores, registrar fiscalizações, controlar trabalhadores registrados e sem registro, capturar fotos e sincronizar dados posteriormente com uma API configurável.

Principais recursos:
- operação offline-first com banco SQLite local;
- seleção de base/cidade;
- consulta de trabalhadores;
- controle de fiscalizações;
- registro de trabalhadores em fiscalização;
- cadastro de trabalhador sem registro durante a fiscalização;
- captura, compactação e envio de fotos;
- sincronização de trabalhadores, turmeiros, fotos e fiscalizações via API configurável;
- funções administrativas para manutenção local do banco.

O aplicativo é voltado a uso operacional em contexto de fiscalização de condomínio rural. A sincronização depende da configuração correta da API pelo responsável técnico.
```

### Modelo de política de privacidade

```text
Política de Privacidade — Fiscalização Condomínio Rural

Última atualização: [SUBSTITUIR DATA]

Esta Política de Privacidade descreve como o aplicativo Fiscalização Condomínio Rural trata dados durante sua operação.

1. Responsável

Responsável pelo aplicativo: LFabris Consultoria em TI
Contato: contato@lfabris.com.br
Telefone: (19) 99750-1761
Site: https://condominio.leofabris.com.br

2. Finalidade do aplicativo

O aplicativo é usado para apoio a fiscalizações em campo em contexto de condomínio rural. Ele permite selecionar uma base/cidade, consultar trabalhadores, registrar fiscalizações, capturar fotos, armazenar informações localmente e sincronizar dados posteriormente com uma API configurável.

3. Dados tratados

Conforme a configuração e uso operacional, o aplicativo pode tratar:
- nome de trabalhadores;
- CPF;
- data de nascimento;
- filiação;
- endereço;
- situação cadastral;
- dados de admissão;
- registros de fiscalização;
- trabalhadores registrados em fiscalização;
- trabalhadores sem registro informados durante a fiscalização;
- produções e conferências;
- atestados e bloqueios, quando disponíveis na base operacional;
- fotos associadas a trabalhadores;
- parâmetros técnicos de conexão com a API.

4. Armazenamento local

O aplicativo usa banco SQLite local para permitir operação offline-first. Dados e fotos podem permanecer no dispositivo até que sejam sincronizados ou removidos conforme procedimento operacional.

5. Sincronização

Quando houver conexão e a API estiver configurada, o aplicativo pode enviar e receber dados por rede para sincronizar trabalhadores, turmeiros, fiscalizações e fotos. A configuração da API é feita dentro do próprio app por usuário autorizado ou responsável técnico.

6. Câmera e fotos

O aplicativo pode usar a câmera do dispositivo para capturar fotos de trabalhadores durante o fluxo operacional. As imagens podem ser compactadas, armazenadas localmente e enviadas posteriormente para a API configurada.

7. Compartilhamento

Os dados são usados para a finalidade operacional do aplicativo. Não há venda de dados pessoais. Caso a API configurada pertença a terceiro, cliente ou operador externo, o tratamento seguirá também os contratos e políticas desse ambiente. [SUBSTITUIR SE NECESSÁRIO]

8. Segurança

Recomenda-se que toda sincronização seja feita por HTTPS. O acesso ao dispositivo, à API e às bases de dados deve ser restrito a pessoas autorizadas.

9. Exclusão de dados

Solicitações de exclusão, correção ou consulta de dados podem ser enviadas para contato@lfabris.com.br. O atendimento dependerá da identificação da base, do vínculo operacional e das obrigações legais ou contratuais aplicáveis.

10. Alterações

Esta política pode ser atualizada para refletir mudanças no aplicativo, no backend ou em requisitos legais e de publicação.
```

### Modelo de resposta de Data Safety

```text
O app coleta dados? Sim.

Justificativa:
O aplicativo Fiscalização Condomínio Rural opera em modo offline-first, armazenando dados em SQLite local, e pode sincronizar posteriormente dados de trabalhadores, fiscalizações e fotos com uma API configurável.

Dados tratados:
- informações de trabalhadores, como nome, CPF e dados cadastrais;
- registros de fiscalização;
- fotos capturadas durante o fluxo operacional;
- dados de produção/conferência, quando disponíveis;
- informações de atestados e bloqueios, quando disponíveis na base operacional.

Finalidade:
Funcionalidade do app e gestão operacional de fiscalizações em campo.

Compartilhamento:
[SUBSTITUIR conforme backend real]. Se o backend for próprio/controlado pela mesma organização, declarar que não há compartilhamento com terceiros, salvo operadores de infraestrutura que atuem como prestadores de serviço.

Criptografia em trânsito:
Responder Sim somente se a API de produção usar HTTPS. Se houver uso de HTTP, corrigir para HTTPS antes de publicar.

Exclusão de dados:
Usuários ou responsáveis podem solicitar exclusão/correção pelo e-mail contato@lfabris.com.br.
```

### Modelo de resposta de permissões

```text
Permissão de câmera:
O aplicativo usa a câmera para capturar fotos de trabalhadores durante o fluxo de fiscalização. As fotos são usadas para identificação operacional, armazenadas localmente e podem ser enviadas posteriormente para a API configurada.

Permissão de armazenamento:
O aplicativo usa armazenamento local para manter banco SQLite, fotos capturadas, fotos baixadas e arquivos temporários necessários à operação offline-first. O uso é restrito aos arquivos operacionais do aplicativo.

Permissão de internet:
O aplicativo usa internet para sincronizar trabalhadores, turmeiros, fiscalizações e fotos com a API configurada pelo responsável técnico.

Permissão MANAGE_EXTERNAL_STORAGE:
Não recomendada para este app, salvo justificativa técnica indispensável. Pelo código atual, remover antes da publicação para reduzir risco de rejeição.
```

### Comandos finais copiáveis

```bash
cd app_v3
flutter clean
flutter pub get
flutter analyze
flutter build appbundle --release
```

### Mapa de referência: Guia completo .docx → Este documento

O conteúdo deste guia foi adaptado do documento `Documentação/Guia Completo para Publicar App Flutter na Google Play Store (2024-2025-2026).docx`.
Abaixo, o mapeamento entre as seções do documento original e as seções correspondentes neste guia:

| Seção no .docx original | Seção correspondente neste guia |
|---|---|
| 1. Pré-Requisitos | Antes de começar |
| 2. Geração do AAB (keystore, key.properties, build.gradle, versionamento, build) | Criar keystore, Configurar key.properties, Configurar assinatura no Gradle, Ajustar versão do app, Gerar o arquivo .aab |
| 3. Criar Conta no Google Play Console | Antes de começar (item 1: conta ativa) |
| 4. Cadastrar App no Play Console | Criar o app no Google Play Console, Preencher a ficha da loja |
| 4.2 Segurança de Dados | Configurar segurança de dados |
| 4.3 Classificação de Conteúdo (IARC) | Responder o questionário de classificação |
| 4.4 Política de Privacidade | Política de privacidade |
| 5. Permissões | Configurar permissões |
| 6. Recursos Gráficos | Preparar os arquivos da loja |
| 7. Categoria e Classificação | Preencher a ficha da loja (categoria) |
| 8. Descrições (curta, completa) | Preparar os arquivos da loja (descrições) |
| 9. Teste Interno | Configurar teste interno |
| 9.3 Teste Fechado (14 dias, 12 testadores) | Configurar teste fechado |
| 10. Publicar em Produção | Publicar em produção |
| 11. Processo de Revisão (questionário) | Publicar em produção (revisão) |
| 12. Pós-Lançamento | (Não implementado — monitoramento contínuo além do escopo inicial) |
| 13. Políticas Google Play | (Coberto nas declarações obrigatórias e checklist) |
| 14. Troubleshooting | Erros comuns e solução |
| 15. Checklist Definitivo | Checklist final |

### Conteúdo do .docx não incorporado

Os seguintes tópicos do documento original **não foram incorporados** por não se aplicarem ao estado atual do `app_v3`:

- **Uso de `permission_handler`**: O app_v3 gerencia permissões de forma nativa/reativa, sem essa dependência. Se no futuro for necessário, adicionar e documentar.
- **Uso de `flutter_launcher_icons`**: O app_v3 não usa esse pacote. Os ícones nativos (`mipmap`) devem ser substituídos manualmente.
- **Firebase Crashlytics / Analytics**: Não há SDKs do Firebase no projeto. Sem monitoramento de crashes no backend.
- **Google Play Billing**: O app é gratuito e não tem compras internas ou assinaturas.
- **Login/Autenticação**: O app não possui fluxo de login ou Firebase Auth.
- **Geolocalização**: Não há permissão `ACCESS_FINE_LOCATION` ou `ACCESS_BACKGROUND_LOCATION`.
- **Notificações push**: Não há `POST_NOTIFICATIONS` ou Firebase Cloud Messaging.
- **`QUERY_ALL_PACKAGES`**: Não declarada e não necessária.
- **Fluxo de criação de conta de usuário**: O app não permite criar contas.
- **Conteúdo gerado pelo usuário público**: Fotos e registros são operacionais, não públicos.
- **Público infantil**: App direcionado a operadores rurais, não a crianças.

### Divergências entre o .docx e o estado real do projeto

| Item | .docx (genérico) | app_v3 (real) | Ação |
|---|---|---|---|
| Versão do Flutter recomendada | 3.22+ | SDK `^3.7.0` (pubspec.yaml) | Compatível |
| JDK / compileOptions | Java 17 | Java 11 (`JavaVersion.VERSION_11`) | Dentro do compatível, mas desatualizado para Gradle 8.5+ |
| Exemplo de app | CarteiraPay (finanças) | Fiscalização Condomínio Rural (fiscalização rural) | Substituído integralmente |
| Gerenciamento de permissões | `permission_handler` package | Nativo com `image_picker` / câmera direta | Documentado conforme código real |
| `minifyEnabled` / `shrinkResources` | Recomenda `true` com ProGuard | Não configurado no `build.gradle.kts` | Pendente de avaliação |
| `RECORD_AUDIO` | Mencionado | Não aplicável | Ignorado |
| `ACCESS_FINE_LOCATION` | Mencionado | Não aplicável | Ignorado |

## Links oficiais usados para validação

- Flutter Android release: https://docs.flutter.dev/deployment/android
- Android app signing / Play App Signing: https://developer.android.com/studio/publish/app-signing
- Upload de App Bundle na Play Console: https://developer.android.com/studio/publish/upload-bundle
- Segurança de dados: https://support.google.com/googleplay/android-developer/answer/10787469
- Permissões na Play Console: https://support.google.com/googleplay/android-developer/answer/9214102
- Acesso a todos os arquivos (`MANAGE_EXTERNAL_STORAGE`): https://support.google.com/googleplay/android-developer/answer/10467955
- Teste interno/fechado: https://support.google.com/googleplay/android-developer/answer/9845334
- Requisitos de teste para contas pessoais novas: https://support.google.com/googleplay/android-developer/answer/14151465
- Assets da loja: https://support.google.com/googleplay/android-developer/answer/9866151
- Criar e configurar app: https://support.google.com/googleplay/android-developer/answer/9859152
- Políticas do programa para desenvolvedores: https://play.google.com/console/about/policy/
- Leis de exportação dos EUA: https://support.google.com/googleplay/android-developer/answer/113770
