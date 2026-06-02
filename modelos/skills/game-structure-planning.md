# Skill - game-structure-planning

| Campo | Valor |
|:---|:---|
| **Finalidade** | Planejamento de fluxos, cenas, fases e estruturas gerais de jogos |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Ao modelar a arquitetura lógica de um jogo (divisão de fases, telas de menu, transições de estado de jogo).
- Durante a criação de fluxogramas de navegação do jogador entre as cenas do jogo.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] Todas as cenas básicas (splash screen, main menu, gameplay, pause, game over, settings) estão listadas.
- [ ] O fluxo de navegação permite ao jogador transitar entre todas as cenas sem loops infinitos ou telas órfãs.
- [ ] O estado de jogo é salvo ou limpo corretamente ao trocar de cena.

---

## 3. O que Analisa (Área de Investigação)

- Gargalos na transição de fases (ex: carregamento assíncrono).
- Complexidade da estrutura do jogo e acoplamento entre cenas.

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Proposta de jogo, lista de fases/cenas planejadas.
- **Saídas Esperadas:** Grafo ou tabela detalhada do fluxo de transição entre cenas.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Sempre garantir que haja um caminho claro para o jogador retornar ao menu principal ou sair do jogo.
- **Bloqueios Obrigatórios (Veto):** Bloquear fluxos em que o jogador fique preso (soft-lock) em menus sem botão de retorno.
