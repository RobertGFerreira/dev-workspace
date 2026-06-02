# Skill - game-ux-ui

| Campo | Valor |
|:---|:---|
| **Finalidade** | Princípios de UI/UX aplicados a games, layouts de HUD, feedback visual/sensorial |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Ao projetar interfaces do usuário de jogos (menus, inventários, HUD - Heads-Up Display).
- Ao definir a linguagem de feedback dinâmico para o jogador (sons de acerto, indicadores de dano).

---

## 2. O que Valida (Foco de Auditoria)

- [ ] Elementos essenciais do HUD (vida, energia, munição, minimapa) estão visíveis e organizados de forma não obstrutiva.
- [ ] A navegação pelos menus e inventários suporta atalhos físicos e gamepad quando aplicável.
- [ ] Informações críticas (ex: pouca vida, dano recebido) geram feedback sensorial (visual/sonoro/tátil) imediato.

---

## 3. O que Analisa (Área de Investigação)

- HUD poluído com informações irrelevantes ou de leitura lenta.
- Falta de contraste entre a interface e o cenário dinâmico do jogo.
- Acessibilidade visual (tamanho de textos de diálogos, modos para daltonismo).

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Mockups de telas, especificações de botões e mapa de fluxos.
- **Saídas Esperadas:** Protótipo estrutural da UI e checklist de acessibilidade visual do jogo.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Garantir que o HUD não obstrua o campo de visão central do gameplay.
- **Bloqueios Obrigatórios (Veto):** Bloquear textos de interface ou diálogos com fontes ilegíveis ou que não escalem para telas menores (mobile).
