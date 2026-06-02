# commit-guardian

Ultima defesa antes de commit interno.

## Validar

1. Mensagem no formato `tipo(escopo): descricao em portugues`.
2. Escopo permitido em `governance/COMMIT_STANDARD.md`.
3. Commit atomico e coeso.
4. Ausencia de secrets, dados sensiveis e logs indevidos.
5. Documentacao relevante atualizada.
6. `flutter analyze` sem warnings quando houver codigo Flutter.

Se falhar, bloquear com lista objetiva de correcoes.
