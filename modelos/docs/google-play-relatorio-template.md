# Relatório de Publicação — Google Play

> Template mestre para preparação, auditoria e publicação de aplicativos Android na Google Play Store.
> Versão do template: `1.0.0`

---

## 1. Identificação do Aplicativo

| Campo | Valor |
|:---|:---|
| **Nome do app** | `{{APP_NAME}}` |
| **Nome interno do projeto** | `{{PROJECT_NAME}}` |
| **Package name (applicationId)** | `{{PACKAGE_NAME}}` |
| **Plataforma** | Android |
| **Versão atual (versionName)** | `{{VERSION_NAME}}` |
| **Version code (versionCode)** | `{{VERSION_CODE}}` |
| **Categoria no Play Console** | `{{PLAY_CATEGORY}}` |
| **Desenvolvedor / empresa responsável** | `{{DEVELOPER_NAME}}` |
| **E-mail de suporte** | `{{SUPPORT_EMAIL}}` |
| **Telefone de contato** | `{{CONTACT_PHONE}}` |
| **Site oficial** | `{{WEBSITE_URL}}` |
| **URL da política de privacidade** | `{{PRIVACY_POLICY_URL}}` |
| **Público-alvo** | `{{TARGET_AUDIENCE}}` |
| **Países/regiões alvo** | `{{TARGET_COUNTRIES}}` |
| **Status da publicação** | `{{PUBLICATION_STATUS}}` |

---

## 2. Resumo Executivo

| Item | Descrição |
|:---|:---|
| **Objetivo do app** | `{{APP_PURPOSE}}` |
| **Estágio atual** | `{{CURRENT_STAGE}}` |
| **Pendências para publicação** | `{{PENDING_ITEMS}}` |
| **Riscos identificados** | `{{IDENTIFIED_RISKS}}` |
| **Situação geral de conformidade** | `{{COMPLIANCE_STATUS}}` |

---

## 3. Escopo do Release

| Campo | Valor |
|:---|:---|
| **Tipo de release** | `{{RELEASE_TYPE}}` (novo app / atualização / hotfix / teste aberto / teste fechado / teste interno) |
| **Versão publicada** | `{{VERSION_NAME}}` (code `{{VERSION_CODE}}`) |
| **Mudanças principais** | `{{MAIN_CHANGES}}` |
| **Correções** | `{{FIXES}}` |
| **Novas features** | `{{NEW_FEATURES}}` |
| **Impactos em permissões** | `{{PERMISSION_IMPACTS}}` |
| **Impactos em política/compliance** | `{{POLICY_IMPACTS}}` |

---

## 4. Checklist Geral de Publicação

### 4.1 Configuração do App

- [ ] `AndroidManifest.xml` revisado — sem permissões excessivas ou desnecessárias
- [ ] `build.gradle` / `build.gradle.kts` revisado e configurado corretamente
- [ ] `minSdk` e `targetSdk` compatíveis com as políticas vigentes do Google
- [ ] `versionCode` incrementado em relação à última release
- [ ] `versionName` atualizado seguindo semântica do projeto
- [ ] Componentes exportados (`exported=true`) revisados e justificados
- [ ] `Debuggable=false` no build de release
- [ ] ProGuard / R8 configurado e `mapping.txt` preservado

### 4.2 Build e Compilação

- [ ] `flutter analyze` ou equivalente roda sem erros
- [ ] `flutter clean && flutter pub get` executado
- [ ] Build release gerado sem warnings críticos
- [ ] AAB assinado com a keystore de produção (não debug)
- [ ] Tamanho do AAB verificado e otimizado
- [ ] Play Feature Delivery / Play Asset Delivery configurado se aplicável

### 4.3 Assinatura

- [ ] Keystore de produção gerada e armazenada em local seguro
- [ ] `key.properties` adicionado ao `.gitignore`
- [ ] Certificado PEM exportado e registrado no Play Console
- [ ] Play App Signing configurado ou confirmado
- [ ] Alias e senhas documentados em local não versionado
- [ ] Keystore de backup preservada fora do repositório

### 4.4 Manifesto e Permissões

- [ ] Permissões no manifesto são estritamente necessárias para as features atuais
- [ ] Permissões sensíveis têm justificativa documentada
- [ ] `ACCESS_BACKGROUND_LOCATION` ou `QUERY_ALL_PACKAGES` ausentes ou justificados em ADR
- [ ] `MANAGE_EXTERNAL_STORAGE` ausente ou com justificativa formal
- [ ] Declaração de uso de permissões no Play Console corresponde ao manifesto

### 4.5 Assets e Mídia

- [ ] Ícone 512x512 PNG (32 bits, < 1MB)
- [ ] Feature Graphic 1024x500 PNG ou JPG
- [ ] Screenshots de celular (mínimo 4, proporção 16:9 ou 9:16)
- [ ] Screenshots de tablet se aplicável
- [ ] Screenshots sem barra de status de iOS ou marcas d'água
- [ ] Textos em screenshots legíveis em telas pequenas
- [ ] Vídeo de promoção (opcional) — formato e duração conforme políticas

### 4.6 Política de Privacidade

- [ ] URL da política de privacidade acessível via HTTPS
- [ ] Política cobre todos os dados coletados pelo app
- [ ] Declara compartilhamento com terceiros (SDKs, analytics, anúncios)
- [ ] Oferece opção de exclusão de conta e dados
- [ ] Coerente com o formulário de Data Safety preenchido
- [ ] Atualizada para a versão atual do app

### 4.7 Play Console

- [ ] Conta de desenvolvedor Google Play ativa e paga
- [ ] Classificação etária IARC preenchida
- [ ] Formulário de Data Safety (Segurança dos Dados) preenchido e coerente
- [ ] App access (instruções de acesso) preenchido se app exigir login
- [ ] Declaração de anúncios preenchida (Ads ID)
- [ ] Países de distribuição configurados
- [ ] Preço definido (gratuito ou pago)
- [ ] Categoria e tags definidas

### 4.8 Revisão Final

- [ ] Release notes (Novidades da versão) escritas para cada idioma
- [ ] Conta de teste funcional fornecida (se aplicável)
- [ ] Instruções de review claras e testadas
- [ ] Fluxos críticos demonstráveis sem necessidade de cadastro externo
- [ ] Nenhum segredo, token ou credencial real no repositório
- [ ] Histórico git verificado para vazamentos (`git log`, secret scanning)
- [ ] CHANGELOG atualizado

### 4.9 Publicação

- [ ] Rollout programado (percentual gradual ou imediato)
- [ ] Release monitoring configurado (crash reporting, ANR, reviews)
- [ ] Contato de suporte monitorado para feedback pós-publicação

---

## 5. Store Listing

### 5.1 Metadados

| Campo | Valor |
|:---|:---|
| **Título (max 50 caracteres)** | `{{STORE_TITLE}}` |
| **Descrição curta (max 80 caracteres)** | `{{SHORT_DESCRIPTION}}` |
| **Descrição completa (max 4000 caracteres)** | `{{FULL_DESCRIPTION}}` |

### 5.2 Palavras-chave e Posicionamento

| Item | Observação |
|:---|:---|
| **Palavras-chave alvo** | `{{TARGET_KEYWORDS}}` |
| **Diferenciais competitivos** | `{{COMPETITIVE_DIFFERENTIALS}}` |
| **Termos proibidos verificados** | ✅ / ❌ — "melhor", "grátis", "nº 1", marcas registradas |
| **CTA principal** | `{{MAIN_CTA}}` |
| **Textos alternativos por idioma** | `{{LOCALIZED_TEXTS}}` |

---

## 6. Política de Privacidade

| Campo | Valor |
|:---|:---|
| **URL da política** | `{{PRIVACY_POLICY_URL}}` |
| **Status** | `{{PRIVACY_POLICY_STATUS}}` (publicada / rascunho / pendente) |
| **Cobre os dados do app?** | ✅ / ❌ / parcialmente |
| **Publicada em URL acessível?** | ✅ / ❌ |
| **Coerente com comportamento real do app?** | ✅ / ❌ / pendente validação |
| **Pendências encontradas** | `{{PRIVACY_POLICY_ISSUES}}` |

### Checklist da Política

- [ ] Declara quais dados são coletados
- [ ] Declara finalidade da coleta
- [ ] Declara compartilhamento com terceiros
- [ ] Declara período de retenção
- [ ] Oferece opção de exclusão de dados
- [ ] Oferece contato para exercício de direitos LGPD/GDPR
- [ ] URL acessível via HTTPS (não HTTP)
- [ ] URL funcional e não quebrada
- [ ] Idioma correspondente ao público do app

---

## 7. App Content e Data Safety

### 7.1 Coleta e Compartilhamento de Dados

Para cada categoria abaixo, preencher:

| Categoria | Coletado? | Compartilhado? | Confirmado no código? | Confirmado manualmente? | Precisa validação humana? | Fonte da evidência |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| Localização aproximada | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| Localização precisa | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| Nome | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| E-mail | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| Telefone | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| IDs de usuário | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| Fotos | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| Vídeos | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| Arquivos e docs | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| Mensagens | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| Áudio | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| Compras no app | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| Histórico de busca | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| Histórico de navegação | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| ID de publicidade (Ad ID) | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| Diagnóstico (crash logs) | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |
| Dados de uso do app | `{{SIM_NAO}}` | `{{SIM_NAO}}` | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ | `{{EVIDENCE}}` |

### 7.2 Políticas Específicas

| Item | Resposta | Observação |
|:---|:---|:---|
| **App infantil ou não?** | `{{SIM_NAO}}` | Se sim, políticas de COPPA/Google Families se aplicam |
| **Recursos financeiros** | `{{SIM_NAO}}` | Investimentos, cripto, pagamentos |
| **Recursos de saúde** | `{{SIM_NAO}}` | Se sim, políticas específicas se aplicam |
| **Exige login?** | `{{SIM_NAO}}` | Se sim, App Access deve ser preenchido |
| **Conteúdo gerado por usuário** | `{{SIM_NAO}}` | Se sim, moderação e denúncia são exigidas |
| **Uso governamental** | `{{SIM_NAO}}` | Se sim, processo de verificação adicional |
| **Anúncios exibidos** | `{{SIM_NAO}}` | Declaração de anúncios no Play Console |

---

## 8. Permissões do Aplicativo

### 8.1 Tabela de Permissões

| Permissão | Encontrada em | Finalidade aparente | Necessária para feature atual? | Exige justificativa no Play? | Texto sugerido para justificativa | Risco / Observação |
|:---|:---|:---|:---:|:---:|:---|:---|
| `{{PERMISSION_NAME}}` | `{{FILE_PATH}}` | `{{PURPOSE}}` | ✅ / ❌ | ✅ / ❌ | `{{JUSTIFICATION_TEXT}}` | `{{RISK_OBSERVATION}}` |
| `{{PERMISSION_NAME}}` | `{{FILE_PATH}}` | `{{PURPOSE}}` | ✅ / ❌ | ✅ / ❌ | `{{JUSTIFICATION_TEXT}}` | `{{RISK_OBSERVATION}}` |

### 8.2 Permissões Sensíveis — Atenção Redobrada

As seguintes permissões exigem declaração formal e justificativa no Play Console:

- `ACCESS_FINE_LOCATION` / `ACCESS_BACKGROUND_LOCATION` — localização em segundo plano
- `CAMERA` — acesso à câmera
- `RECORD_AUDIO` — gravação de áudio
- `READ_CONTACTS` / `WRITE_CONTACTS` — contatos
- `READ_EXTERNAL_STORAGE` / `WRITE_EXTERNAL_STORAGE` / `MANAGE_EXTERNAL_STORAGE` — armazenamento
- `READ_PHONE_STATE` — estado do telefone
- `ACTIVITY_RECOGNITION` — atividade física
- `BODY_SENSORS` — sensores corporais
- `SMS` / `CALL_LOG` — SMS e chamadas
- `QUERY_ALL_PACKAGES` — consulta de pacotes instalados (Uses Permissions)

---

## 9. Manifesto e Configuração Android

### 9.1 Identificação

| Parâmetro | Valor |
|:---|:---|
| **package** | `{{PACKAGE_NAME}}` |
| **versionName** | `{{VERSION_NAME}}` |
| **versionCode** | `{{VERSION_CODE}}` |
| **minSdkVersion** | `{{MIN_SDK}}` |
| **targetSdkVersion** | `{{TARGET_SDK}}` |
| **compileSdkVersion** | `{{COMPILE_SDK}}` |

### 9.2 Componentes Exportados

| Componente | Tipo | Exportado? | Justificativa |
|:---|:---|:---:|:---|
| `{{COMPONENT_NAME}}` | Activity / Service / Receiver / Provider | ✅ / ❌ | `{{JUSTIFICATION}}` |

### 9.3 Observações Técnicas

- `{{TECHNICAL_NOTES}}`

---

## 10. Assinatura do App

| Campo | Valor |
|:---|:---|
| **Usa Play App Signing?** | ✅ / ❌ |
| **Tipo de chave** | RSA 2048 bits / ECDSA |
| **Formato da keystore** | JKS / PKCS12 |
| **Status da upload key** | Gerada / Exportada / Registrada no Play Console |
| **Local seguro da keystore** | `{{KEYSTORE_SECURE_LOCATION}}` (não versionado) |
| **Certificado PEM exportado?** | ✅ / ❌ |
| **Data de expiração da chave** | `{{KEY_EXPIRY_DATE}}` |
| **Pendências de assinatura** | `{{SIGNING_PENDING_ITEMS}}` |

> **⚠️ Atenção:** Keystore real, senhas e aliases NUNCA devem ser versionados no repositório. Armazene em gerenciador de senhas ou cofre seguro.

---

## 11. Comandos Operacionais

> Todos os comandos abaixo contêm placeholders. Substitua pelos valores reais sem versionar senhas.

### 11.1 Gerar Keystore

```bash
keytool -genkey -v -keystore {{KEYSTORE_FILENAME}}.jks -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 -alias {{KEY_ALIAS}}
```

### 11.2 Exportar Certificado PEM

```bash
keytool -export -rfc -alias {{KEY_ALIAS}} -file {{CERT_FILENAME}}.pem -keystore {{KEYSTORE_FILENAME}}.jks
```

### 11.3 Build AAB (Release)

```bash
flutter clean
flutter pub get
flutter analyze
flutter build appbundle --release
# Saída: build/app/outputs/bundle/release/app-release.aab
```

### 11.4 Verificar Assinatura do AAB

```bash
# Verificar se o AAB está assinado corretamente
 jarsigner -verify -verbose -certs build/app/outputs/bundle/release/app-release.aab
```

### 11.5 Validações Adicionais

```bash
# Verificar debuggable
# Descompacte o AAB e verifique o AndroidManifest.xml
# android:debuggable deve estar ausente ou false
```

### 11.6 Observações de Segurança

- `key.properties` deve estar em `.gitignore` desde o primeiro commit
- A keystore `.jks` ou `.p12` nunca deve entrar no repositório
- Prefira Play App Signing para gerenciamento de chaves pelo Google
- Faça backup da keystore em local seguro fora do repositório

---

## 12. Arquivos e Artefatos Necessários

| Artefato | Caminho / Local | Status |
|:---|:---|:---:|
| AAB (app-release.aab) | `build/app/outputs/bundle/release/app-release.aab` | ✅ / ❌ / pendente |
| Ícone 512x512 | `{{ICON_PATH}}` | ✅ / ❌ / pendente |
| Feature Graphic 1024x500 | `{{FEATURE_GRAPHIC_PATH}}` | ✅ / ❌ / pendente |
| Screenshots (mín. 4) | `{{SCREENSHOTS_PATH}}` | ✅ / ❌ / pendente |
| Política de privacidade | `{{PRIVACY_POLICY_PATH}}` (arquivo local) | ✅ / ❌ / pendente |
| Certificado PEM | `{{PEM_PATH}}` | ✅ / ❌ / pendente |
| Mapping.txt (ProGuard) | `{{MAPPING_PATH}}` | ✅ / ❌ / pendente |
| Release notes | `{{RELEASE_NOTES_PATH}}` | ✅ / ❌ / pendente |
| Dados do app preenchidos | `dados/google-play-dados.md` | ✅ / ❌ / pendente |
| Credenciais operacionais | Gerenciador de senhas / cofre (fora do repo) | ✅ / ❌ |

---

## 13. Instruções de Acesso e Revisão

| Campo | Valor |
|:---|:---|
| **App exige login?** | ✅ / ❌ |
| **Conta de teste fornecida?** | ✅ / ❌ |
| **E-mail da conta de teste** | `{{TEST_ACCOUNT_EMAIL}}` |
| **Senha da conta de teste** | `{{TEST_ACCOUNT_PASSWORD}}` (⚠️ não versionar — usar gerenciador de senhas) |
| **Instruções de acesso** | `{{ACCESS_INSTRUCTIONS}}` |
| **Fluxos a demonstrar** | `{{FLOWS_TO_DEMONSTRATE}}` |
| **Observações para aprovação** | `{{REVIEW_OBSERVATIONS}}` |

> ⚠️ **Crítico:** O formulário "App access" no Play Console deve estar preenchido antes do envio para revisão. Teste as credenciais antes de submeter.

---

## 14. Notas da Versão

| Versão | Data | Mudanças principais | Correções | Observações de rollout |
|:---|:---|:---|:---|:---|
| `{{VERSION_NAME}}` | `{{DATE}}` | `{{MAIN_CHANGES}}` | `{{FIXES}}` | `{{ROLLOUT_NOTES}}` |
| `{{VERSION_NAME}}` | `{{DATE}}` | `{{MAIN_CHANGES}}` | `{{FIXES}}` | `{{ROLLOUT_NOTES}}` |

### Template de Release Notes (Play Console)

```
Novidades da versão {{VERSION_NAME}}:

• {{CHANGE_1}}
• {{CHANGE_2}}
• {{CHANGE_3}}

Correções:
• {{FIX_1}}
• {{FIX_2}}
```

---

## 15. Riscos e Alertas

| Risco | Gravidade | Status | Observação |
|:---|:---:|:---:|:---|
| Dados sensíveis encontrados no repositório | Crítico | ✅ / ❌ / pendente | `{{OBSERVATION}}` |
| Permissões suspeitas ou excessivas | Alto | ✅ / ❌ / pendente | `{{OBSERVATION}}` |
| Inconsistência entre código e declaração Data Safety | Alto | ✅ / ❌ / pendente | `{{OBSERVATION}}` |
| Falta de política de privacidade ou URL inválida | Crítico | ✅ / ❌ / pendente | `{{OBSERVATION}}` |
| Problemas de assinatura (debug key no release) | Crítico | ✅ / ❌ / pendente | `{{OBSERVATION}}` |
| Pendências manuais no Play Console | Médio | ✅ / ❌ / pendente | `{{OBSERVATION}}` |
| Risco de rejeição por política de conteúdo | Alto | ✅ / ❌ / pendente | `{{OBSERVATION}}` |
| Login instructions ausentes no App Access | Alto | ✅ / ❌ / pendente | `{{OBSERVATION}}` |
| Ad ID não declarado no Data Safety | Médio | ✅ / ❌ / pendente | `{{OBSERVATION}}` |

---

## 16. Pendências

| Item | Responsável | Prioridade | Status | Observação |
|:---|:---|:---:|:---:|:---|
| `{{PENDING_ITEM}}` | `{{RESPONSIBLE}}` | Alta / Média / Baixa | 🔴 Aberto / 🟡 Em andamento / 🟢 Concluído | `{{OBSERVATION}}` |
| `{{PENDING_ITEM}}` | `{{RESPONSIBLE}}` | Alta / Média / Baixa | 🔴 Aberto / 🟡 Em andamento / 🟢 Concluído | `{{OBSERVATION}}` |

---

## 17. Aprovação

| Campo | Valor |
|:---|:---|
| **Task relacionada** | `{{TASK_REFERENCE}}` |
| **Plan relacionado** | `{{PLAN_REFERENCE}}` |
| **SDD relacionado** | `{{SDD_REFERENCE}}` |
| **Responsável pela revisão** | `{{REVIEWER}}` |
| **Status de aprovação** | ✅ Aprovado / ❌ Rejeitado / ⏳ Pendente |
| **Data de aprovação** | `{{APPROVAL_DATE}}` |
| **Observações finais** | `{{FINAL_OBSERVATIONS}}` |

---

## 18. Como Este Relatório Deve Ser Usado

1. **Preencher com base no código e documentação real** — extrair do manifesto, gradle, assets e código-fonte sempre que possível.
2. **Atualizar por versão/release** — cada nova versão deve gerar uma nova iteração deste relatório.
3. **Ser específico por aplicativo** — um relatório por app. Não misturar múltiplos aplicativos no mesmo documento.
4. **Separar dados institucionais de segredos** — dados institucionais (nome, e-mail, site) podem ficar no relatório; senhas, tokens e keystore nunca.
5. **Apoiar publicação real** — o relatório deve ser o documento guia durante todo o processo de publicação, não um artefato gerado a posteriori.

---

## 19. Como Este Relatório NÃO Deve Ser Usado

1. **Não deve conter segredo real** — senhas, keystore, tokens, service account JSON, private keys e secrets de CI/CD são proibidos.
2. **Não deve misturar múltiplos apps** — cada aplicativo tem seu próprio relatório.
3. **Não deve inventar respostas para o Play Console** — toda declaração de coleta de dados deve ter evidência no código.
4. **Não deve assumir permissões sem leitura do manifesto** — sempre validar no `AndroidManifest.xml`.
5. **Não deve ser só checklist sem contexto** — cada seção deve ter informações específicas do app, não apenas caixas vazias.
6. **Não deve ficar genérico demais** — preencher com dados reais do projeto; placeholders são temporários.

---

## 20. Anexos e Referências Internas

### Arquivos usados como base para este template

| Arquivo | Fonte |
|:---|:---|
| `modelos/skills/play-console-checklist.md` | Checklist de etapas do Play Console |
| `modelos/skills/privacy-disclosure-review.md` | Auditoria de política de privacidade e Data Safety |
| `modelos/skills/release-readiness.md` | Validação de assinatura e bundle |
| `modelos/skills/store-listing-optimization.md` | Metadados, ASO e limites de caracteres |
| `modelos/skills/android-policy-review.md` | Conformidade com políticas do Google Play |
| `modelos/skills/asset-compliance.md` | Dimensões e formatos de assets |
| `modelos/skills/security-mobile-review.md` | Segurança mobile e permissões |
| `modelos/docs/GOOGLE_PLAY_DEPLOY.template.md` | Guia de publicação Google Play |
| `modelos/docs/dados.template.md` | Template de dados do desenvolvedor |
| `modelos/docs/GUIA_DE_PREENCHIMENTO.md` | Guia de preenchimento e placeholders |
| `modelos/agentes/google-play-support.md` | Especificação do agente Google Play |
| `modelos/prompts/google-play-support.md` | Prompt do agente Google Play |
| `modelos/docs/SDD_UNIVERSAL.template.md` | Template SDD (checklist pre-release) |
| `modelos/docs/SECURITY.template.md` | Template de segurança |
| `modelos/docs/CHANGELOG.template.md` | Template de changelog/release notes |

### Documentos internos relacionados

| Documento | Local |
|:---|:---|
| Google Play Dados do app | `dados/google-play-dados.md` |
| Manual de publicação | `google_play/manual-publicacao.md` |
| Respostas Play Console | `google_play/respostas-play-console.md` |
| Permissões do app | `google_play/permissoes-app.md` |
| Política de privacidade | `google_play/politica-privacidade.md` |
| Versões e notas | `google_play/versoes-e-notas.md` |

---

## Lacunas Cobertas pelo Template

Itens que não estavam totalmente cobertos nos arquivos existentes e foram estruturados neste template:

| Item | Seção |
|:---|:---:|
| Tabela de Data Safety com colunas de confirmação (código, manual, validação humana, evidência) | 7 |
| Seção de riscos e alertas com gravidade e status | 15 |
| Tabela de pendências com responsável, prioridade e status | 16 |
| Seção de aprovação com referência a Task, Plan e SDD | 17 |
| Instruções de acesso e revisão com checklist de App Access | 13 |
| Tabela completa de permissões sensíveis com riscos | 8 |
| Seção de "Como deve ser" e "Como não deve ser" | 18, 19 |
| Anexos e referências internas | 20 |

---

> Template gerado em `{{GENERATION_DATE}}` | Versão `1.0.0`
