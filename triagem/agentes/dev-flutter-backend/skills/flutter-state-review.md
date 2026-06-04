# flutter-state-review

Use para revisar estado e ciclo de vida.

## Validar

- Dispose de `TextEditingController`, `ScrollController`, `AnimationController`, streams e subscriptions.
- Ausencia de memory leak.
- Escopo minimo de rebuild.
- Estado global apenas para dados de sessao ou contexto realmente compartilhado.
- Regras de negocio fora de widgets.
