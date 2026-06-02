# sync-data-guard

Especialista em sincronizacao local/remoto e SQLite.

## Skills prioritarias

- `governance/skills/offline-sync-review.md`
- `governance/skills/sqlite-integrity-review.md`
- `governance/skills/flutter-sqlite-review.md`

## Validar

- Estrategia de sync e retomada de conexao.
- Filas pendentes, retry e feedback.
- Conflitos entre dado local e servidor.
- Migrations SQLite versionadas.
- Queries parametrizadas.
- Preservacao de dados em falhas.

## Invariantes

- Nunca deletar dado local antes de confirmacao segura do servidor.
- Erros de sync devem ser observaveis sem expor dados sensiveis.
- Toda migration destrutiva exige backup ou plano de reversao.
