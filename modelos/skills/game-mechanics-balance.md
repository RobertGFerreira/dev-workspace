# Skill - game-mechanics-balance

| Campo | Valor |
|:---|:---|
| **Finalidade** | Balanceamento matemático de mecânicas de jogo, regras e curvas de progressão |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Ao calibrar variáveis numéricas (dano, vida, velocidade, taxas de drop, custo de itens).
- Ao definir curvas de experiência (XP), progressão de níveis e recompensas.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] A relação de força entre diferentes elementos do jogo (armas, personagens) está equilibrada.
- [ ] O tempo estimado para passar de nível (XP curve) escala de forma justa.
- [ ] As chances de drop de itens raros estão estatisticamente balanceadas.

---

## 3. O que Analisa (Área de Investigação)

- Elementos "dominantes" que tornam outras estratégias ou itens obsoletos (estratégias dominantes/metagame quebrado).
- Saltos de dificuldade abruptos na progressão (difficulty spikes).

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Tabelas de atributos, fórmulas de dano/XP, dados de simulação.
- **Saídas Esperadas:** Gráficos ou matrizes matemáticas demonstrando o equilíbrio numérico e progressão de itens.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Sempre simular cenários extremos (ex: personagem com o máximo de defesa) para evitar quebras de lógica.
- **Bloqueios Obrigatórios (Veto):** Bloquear qualquer mecânica que resulte em um item ou habilidade com vantagem desproporcional intransponível (overpowered - OP) sem contrapartida.
