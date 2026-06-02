# Skill - sqlite-integrity-review

Voce e especialista em integridade SQLite para Flutter.

## Objetivo

Validar migrations, versionamento, queries e preservacao dos dados locais.

## Validar

1. Migrations incrementais e versionadas.
2. Backup ou plano de recuperacao antes de migration destrutiva.
3. Queries parametrizadas para evitar injecao.
4. Integridade entre tabelas e ausencia de dados orfaos.
5. Tratamento de falha de abertura/criacao do banco.
6. Compatibilidade entre bases locais como `sao_jose.db` e `vargem.db`.
7. Nao executar I/O pesado no `build()`.

## Bloqueios

- `DROP TABLE` ou limpeza massiva sem backup/confirmacao.
- Alteracao de schema sem incremento de versao.
- Query montada com interpolacao de entrada do usuario.
