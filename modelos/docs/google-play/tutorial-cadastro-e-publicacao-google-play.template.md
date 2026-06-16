# Tutorial: Cadastro e Publicação no Google Play

> Aplicável a: `{{APP_NAME}}` (package: `{{PACKAGE_NAME}}`)

## Pré-requisitos

- [ ] Conta Google Play Developer ativa (US$ 25, taxa única)
- [ ] Keystore de produção gerada (veja `tutorial-geracao-chave-e-configuracao.md`)
- [ ] AAB assinado compilado
- [ ] Dados do app preenchidos em `dados-aplicativo.md`
- [ ] Dados sensíveis preenchidos localmente em `dados-sensiveis.md`
- [ ] Política de privacidade hospedada em URL pública HTTPS
- [ ] Assets prontos (ícone, banner, screenshots)

---

## Passo 1: Criar app no Play Console

1. Acesse https://play.google.com/console
2. Clique em **Adicionar app**
3. Selecione:
   - **Idioma padrão** → português (ou o idioma principal)
   - **Título** → `{{STORE_TITLE}}`
   - **Aplicativo Android** → sim
   - **Nome do app** → `{{APP_NAME}}`
   - **Tipo** → Aplicativo / Jogo
   - **Gratuito ou pago** → Gratuito
4. Aceite os Termos e clique em **Criar app**

---

## Passo 2: Configurar App Signing

1. No menu **Configuração → Assinatura do app**
2. Escolher **Usar chave de assinatura do Google**  
   (recomendado para segurança e recuperação)
3. Fazer upload do certificado PEM gerado:
   ```bash
   keytool -export -rfc -alias {{KEYSTORE_ALIAS}} `
     -keystore {{KEYSTORE_FILENAME}}.jks `
     -file {{UPLOAD_CERT_FILENAME}}.pem
   ```
4. Baixar e salvar a **chave de assinatura** fornecida pelo Google

---

## Passo 3: Preencher Ficha da Loja

Acesse **Presença na Google Play → Ficha da loja**

| Campo | Valor |
|:---|:---|
| **Título** | `{{STORE_TITLE}}` |
| **Subtítulo** | `{{STORE_SUBTITLE}}` |
| **Descrição curta** | `{{SHORT_DESCRIPTION}}` |
| **Descrição longa** | `{{FULL_DESCRIPTION}}` |

Faça upload de:
- **Ícone** (512x512 PNG, máx 1MB)
- **Banner** (Feature Graphic 1024x500 JPG/PNG, máx 1MB)
- **Screenshots** (2-8 capturas, recomendado 4+)

---

## Passo 4: Preencher App Content

### 4.1 Política de Privacidade

URL: `{{PRIVACY_POLICY_URL}}`

### 4.2 Classificação de conteúdo

Responder questionário do **IARC**:
- Categoria do app, conteúdo gerado pelo usuário, compartilhamento de local, etc.

### 4.3 Anúncios

Declarar se o app exibe anúncios: `{{HAS_ADS}}`

### 4.4 Segurança dos Dados (Data Safety)

Preencher baseado nas permissões reais do manifesto. Veja `permissoes-e-politicas.md` para respostas sugeridas.

---

## Passo 5: Produção → Versão principal

1. **Criar nova versão**
2. Fazer upload do AAB: `build/app/outputs/bundle/release/app-release.aab`
3. Preencher **Novidades da versão** (release notes):
   ```
   {{RELEASE_NOTES}}
   ```
4. Salvar e revisar

---

## Passo 6: Revisar e Publicar

1. Acessar **Visão geral**
2. Verificar pendências (itens em vermelho)
3. Garantir que:
   - [ ] Dados de login para o revisor estão documentados
   - [ ] Conta de teste está ativa por 24h+ se app tiver login
   - [ ] Política de privacidade acessível
   - [ ] Classificação etária preenchida
   - [ ] Data Safety completo
4. Clicar em **Enviar para análise**

> ⏱ A análise pode levar de algumas horas a alguns dias.

---

## Passo 7: Pós-publicação

- [ ] Monitorar status no Play Console
- [ ] Verificar se o app aparece nas buscas
- [ ] Testar o download e instalação
- [ ] Acompanhar crashes e ANRs no painel
