# Skill - game-monetization-strategy

| Campo | Valor |
|:---|:---|
| **Finalidade** | Arquitetura de economia in-game, passes, anúncios e compras integradas |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Ao modelar a loja do jogo, fluxos de compras in-app (IAP), passes de temporada ou passes de batalha.
- Ao planejar a inserção e frequência de anúncios (Ads).

---

## 2. O que Valida (Foco de Auditoria)

- [ ] A moeda virtual do jogo tem uma paridade estável e inflação controlada.
- [ ] Itens pagos não destroem o balanceamento do modo competitivo (sem mecânicas pay-to-win descaradas).
- [ ] Anúncios são integrados de forma opcional ou pouco intrusiva (ex: anúncios premiados / rewarded ads).

---

## 3. O que Analisa (Área de Investigação)

- Risco de frustração do jogador devido a barreiras de pagamento abusivas (paywalls agressivos).
- Falta de valor percebido nas ofertas da loja do jogo.

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Estrutura da economia interna do jogo, catálogo de itens virtuais e política de monetização.
- **Saídas Esperadas:** Proposta comercial e tabela de precificação da loja do jogo.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Manter uma distinção clara entre itens puramente cosméticos e itens que afetam o gameplay.
- **Bloqueios Obrigatórios (Veto):** Bloquear qualquer mecânica que induza compras por cliques acidentais ou simule jogos de azar sem a devida classificação etária.
