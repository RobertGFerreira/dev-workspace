# quality-gate

Verificacao transversal final.

## Regra fundamental: agentes nao pedem permissao

Os agentes deste repositorio sao **auditores e executores tecnicos**, nao solicitantes de confirmacao. O quality-gate nao deve bloquear por falta de permissao para ler ou criar artefatos — deve verificar se os artefatos obrigatorios existem e estao completos.

## Checklist

- `flutter analyze` limpo quando aplicavel.
- Nenhum `print()` em producao.
- Nenhum `withOpacity` em codigo novo.
- Novos arquivos/diretorios Flutter em `snake_case`.
- Imports organizados.
- Dispose correto em controllers/streams novos ou alterados.
- Spec/docs alinhadas com implementacao.
- Demandas complexas possuem `plan.md`, `tasks.md` e `audit.md` em `Documentação/[projeto]/`.
- Para atualizacao de bibliotecas/Gradle/migracao tecnica: `plan.md` e `tasks.md` devem conter `Chance de quebrar`, `Risco de quebra` e classificacao de criticidade obrigatorios.
- Nenhum artefato novo de agente foi salvo na raiz, em `governance/specs/` ou dentro dos apps Flutter.
- Auditoria cobre riscos de seguranca, UX, persistencia local, dependencias, sobrescrita, salvamento e concorrencia quando aplicavel.
- Se houve referencia a `app_farol`, ela foi declarada como referencia estrutural, nao funcional, sem copiar paleta ou identidade visual.
- Para ajustes visuais do `app_v3`, `plan.md` possui Fase 1 (base segura) e Fase 2 (refinamento visual).
- Para ajustes visuais do `app_v3`, `tasks.md` classifica cada task como `nao quebra o app` ou `pode quebrar o app`.
- Splash, logo, trator/loading, theme, widgets base e responsividade foram validados sem alterar regras de negocio.
- Mudancas visuais foram revisadas em multiplos tamanhos de tela quando aplicavel.
- Antes de substituir planejamento, foi verificado se `plan.md` e `tasks.md` anteriores estavam concluidos.
- Planejamento pendente foi mantido e complementado, sem apagamento silencioso.
- SDD foi revisado antes do fechamento ou marcado como pendencia documental quando ausente/desatualizado.
- Codigo, plano, tasks, validacao, documentacao e SDD estao coerentes quando aplicavel.
- Commit no padrao interno.

Qualquer falha relevante bloqueia a entrega.
