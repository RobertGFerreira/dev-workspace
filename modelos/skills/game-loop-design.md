# Skill - game-loop-design

| Campo | Valor |
|:---|:---|
| **Finalidade** | Modelagem do loop de jogabilidade central (core loop) e ciclos de retenção |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Ao definir a sequência fundamental de ações do jogador (ex: Matar -> Ganhar Ouro -> Comprar Equipamento -> Enfrentar Inimigo Mais Forte).
- Ao projetar mecânicas de retenção secundárias e diárias do jogo.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] O core loop é claro, satisfatório e incentiva a repetição de forma orgânica.
- [ ] As ações do loop geram recompensas e feedback imediatos ao jogador.
- [ ] Existe um loop secundário (metagame) que sustenta o progresso de longo prazo.

---

## 3. O que Analisa (Área de Investigação)

- Pontos de atrito onde o loop se torna repetitivo de forma cansativa (grinding excessivo).
- Falta de incentivo claro para o jogador retornar ao core loop.

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Proposta de jogo, descrição das ações básicas do jogador.
- **Saídas Esperadas:** Diagrama do fluxo do core loop e metagame.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Garantir que cada ação do jogador tenha um feedback sensorial claro (visual/sonoro).
- **Bloqueios Obrigatórios (Veto):** Bloquear loops em que o progresso seja impossível sem o uso de compras reais (paywalls intransponíveis).
