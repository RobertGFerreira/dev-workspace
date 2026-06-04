# Skill - game-release-readiness

| Campo | Valor |
|:---|:---|
| **Finalidade** | Validação final de builds de jogos, conformidade de assets e readiness para publicação |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Nas etapas finais que precedem a geração da build de produção do jogo.
- Ao revisar pacotes de assets, texturas, áudios e dependências antes do empacotamento (build final).

---

## 2. O que Valida (Foco de Auditoria)

- [ ] A taxa de quadros (FPS) está estável nas plataformas alvo sob cenários de estresse.
- [ ] O tamanho da build final de distribuição está otimizado (compressão de áudio, texturas e modelos).
- [ ] O arquivo de save-game funciona corretamente ao reiniciar a build ou atualizar a versão.

---

## 3. O que Analisa (Área de Investigação)

- Vazamentos de memória em execuções prolongadas do motor de jogo.
- Bugs impeditivos de progressão (game-breaking bugs) nas fases finais de teste.
- Conformidade com as diretrizes das lojas de distribuição (Steam, Epic, Consoles).

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Relatórios de performance, logs de QA, especificações da build.
- **Saídas Esperadas:** Relatório de homologação da build e checklist de readiness de publicação.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Testar exaustivamente o comportamento do jogo sob interrupções (ex: perda de conexão, suspensão do app).
- **Bloqueios Obrigatórios (Veto):** Bloquear builds com travamentos crônicos (crashes) na tela de carregamento ou com corrupção de save-games.
