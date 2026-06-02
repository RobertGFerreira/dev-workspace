# flutter-analyze-lint

Use como gate de qualidade Flutter.

## Exigir

- `flutter analyze` sem warnings antes de commit com codigo Flutter.
- Nenhum novo warning ignorado sem justificativa.
- Nenhum lint silenciado para esconder problema real.
- Se o comando nao puder rodar, registrar motivo e risco residual.
