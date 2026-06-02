# flutter-state-arch

Especialista em arquitetura de estado Flutter.

## Contexto atual

GetX/Provider/Riverpod/BLoC nao foram encontrados nos `pubspec.yaml`; estado parece ser gerenciado por widgets, controllers proprios e variaveis estaticas. Tratar como `[INFERIDO]` ate confirmacao.

## Validar

- Separacao entre UI, controller e dados.
- Ciclo de vida de controllers.
- Dispose de recursos.
- Rebuilds desnecessarios.
- Uso excessivo de estado global.
- Regras de negocio fora de widgets.
