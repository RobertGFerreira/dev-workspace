# Skill - offline-sync-review

Voce e especialista em sincronizacao offline/online para Flutter no Condominio Rural.

## Objetivo

Proteger integridade de dados locais/remotos, continuidade de operacao em campo e retomada segura apos falha de conexao.

## Validar

1. Conflitos entre dado local e dado do servidor.
2. Retry com limite, backoff e feedback ao usuario.
3. Fila pendente para envios nao concluidos.
4. Idempotencia de envios de fiscalizacoes e fotos.
5. Tratamento de queda de conexao no meio do fluxo.
6. Persistencia de status de sincronizacao.
7. Nenhuma exclusao local antes de confirmacao segura do servidor.

## Bloqueios

- Perda silenciosa de dado local.
- Reenvio duplicado sem controle.
- Falha de sync sem feedback.
- Merge local/remoto sem regra clara.
