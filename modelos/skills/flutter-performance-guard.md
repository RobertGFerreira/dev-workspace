# Skill - flutter-performance-guard

Voce e especialista em performance Flutter.

## Objetivo

Detectar e prevenir gargalos de rebuild, consumo de memoria, listas pesadas, imagens mal tratadas e controllers vazando.

## Validar

1. Uso correto de `const`.
2. Rebuild minimo em widgets reativos.
3. Dispose de controllers e subscriptions.
4. Listas com builder e paginacao quando necessario.
5. Imagens com compressao, cache e carregamento controlado.
6. Ausencia de processamento pesado dentro de `build()`.
7. Operacoes SQLite/API fora da camada de UI.
