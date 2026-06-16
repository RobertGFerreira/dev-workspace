# Google Play — Templates Padrão

> Estrutura base para o fluxo de publicação Android no Google Play.
> Estes templates são copiados pelo agente `google-play-support` para cada aplicativo.

## Conteúdo

| Arquivo | Propósito |
|:---|:---|
| `dados-aplicativo.template.md` | Dados institucionais do app (nome, package, contato, URLs) |
| `dados-sensiveis.template.md` | Placeholders para dados sensíveis (NUNCA versionar valores reais) |
| `tutorial-geracao-chave-e-configuracao.template.md` | Passo a passo de keystore, upload key e signing |
| `tutorial-cadastro-e-publicacao-google-play.template.md` | Fluxo completo de cadastro e publicação |
| `permissoes-e-politicas.template.md` | Análise de permissões e política de privacidade |
| `respostas-play-console.template.md` | Respostas prontas para copiar e colar no Play Console |
| `comandos/` | Comandos individuais para operações específicas |

## Fluxo de uso

1. O agente lê o projeto e extrai dados reais
2. Copia os templates para `google_play/` no app
3. Preenche com dados extraídos + placeholders para sensíveis
4. Gera comandos prontos para o desenvolvedor executar
5. Arquiteta Task, Plan e SDD em `google_play/arquivos/`

## ⚠️ Regra crítica

Dados sensíveis (senhas, keystore, tokens, service account JSON, private keys, secrets)
NUNCA devem ser versionados. Use apenas placeholders.
