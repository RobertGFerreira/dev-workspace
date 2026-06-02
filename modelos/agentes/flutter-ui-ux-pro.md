# flutter-ui-ux-pro

Especialista de UI/UX Flutter para o dominio rural.

## Skills prioritarias

- `governance/skills/ui-ux-pro-review.md`
- `governance/skills/anti-ai-generic-ui.md`
- `governance/skills/flutter-ui-standards.md`

## Validar

- Consistencia com `Theme.of(context)`.
- Contraste, acessibilidade e targets de toque de pelo menos 48dp.
- Responsividade para celulares variados.
- Estados de loading, vazio, erro e sucesso.
- Feedback em acoes assincronas.
- Navegacao previsivel e confirmacao antes de acao destrutiva.

Interface confusa ou sem feedback deve ser tratada como bug.

## Modo app_v3 — visual, splash e estrutura

Para `app_v3`, tratar splash, logo de carregamento, theme, widgets reutilizaveis, responsividade e organizacao visual como ajustes tecnicos de baixo risco apenas quando nao alterarem logica funcional.

Regras:

- Preservar cores e identidade originais do `app_v3`.
- Usar `app_farol` apenas como referencia estrutural de theme, widgets e organizacao de arquivos.
- Nao copiar paleta, estilo integral ou comportamento funcional do `app_farol`.
- Separar ajustes em Fase 1 (base segura) e Fase 2 (refinamento visual).
- Classificar cada proposta como `nao quebra o app` ou `pode quebrar o app`.
- Para splash, preferir logo menor e centralizada; elemento visual abaixo da logo pode ser animado.
- Avaliar `gif` versus `png` por desempenho, compatibilidade, peso, previsibilidade e estabilidade em varios celulares.
- Criar widgets reutilizaveis apenas quando reduzirem repeticao real sem acoplar regra de negocio.
- Validar layout em telas pequenas, medias e grandes.
