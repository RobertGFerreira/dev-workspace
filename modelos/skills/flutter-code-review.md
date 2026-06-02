# flutter-code-review

Use para revisar codigo Dart/Flutter.

## Regras

- Preferir `const` e `final` quando possivel.
- Evitar `late` sem inicializacao garantida.
- Null safety sem `!` desnecessario.
- Proibir `print()` em producao.
- Proibir `withOpacity`; usar `Color.withValues()`.
- Novos arquivos/diretorios Flutter em `snake_case`.
- Imports: `dart` -> `flutter` -> packages -> local.
