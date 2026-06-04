# Skill - scope-control

| Campo | Valor |
|:---|:---|
| **Finalidade** | Controle de escopo, autoridade e fronteiras entre agentes |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Ao criar, revisar ou consolidar agentes com responsabilidades próximas.
- Ao validar se uma tag concede escopo sem ampliar autoridade.
- Ao verificar se um especialista invadiu papel de orquestrador.

---

## 2. O que Valida

- [ ] O agente declara o que faz e o que não faz.
- [ ] Arquivos permitidos e proibidos estão explícitos.
- [ ] Tags reconhecidas não concedem autoridade extra.
- [ ] Existe validador definido para mudanças do agente.
- [ ] Não há sobreposição injustificada com outro agente ativo.

---

## 3. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** definição do agente, README do catálogo e tags relevantes.
- **Saídas Esperadas:** diagnóstico de conflito, recomendação de consolidação ou ajuste de escopo.

---

## 4. Bloqueios Obrigatórios

- Bloquear agente sem prompt, skill ou documentação.
- Bloquear mudança estrutural sem validação do guardião.
- Bloquear especialização que substitua a camada universal.
