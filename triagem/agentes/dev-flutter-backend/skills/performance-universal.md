# Skill - performance-universal

| Campo | Valor |
|:---|:---|
| **Finalidade** | Auditoria e otimização de performance geral, uso de recursos, concorrência e banco de dados |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Sempre que houver alterações que afetem a performance de chamadas de API, processamento assíncrono, renderização de telas ou persistência local/remota de dados.
- Durante a revisão de código de algoritmos complexos, loops aninhados ou transações de banco de dados.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] Loops e processamento de listas com limites de complexidade controlados (Big O adequado).
- [ ] Uso correto de caches em operações caras (computação pesada, chamadas de rede repetitivas).
- [ ] Conexões de banco de dados, arquivos abertos, ou chamadas de socket liberadas no final de sua execução.
- [ ] Paginação ativada para todas as listagens ou queries que possam crescer indefinidamente.
- [ ] Paralelismo ou processamento em threads/background tasks para operações bloqueantes de I/O.

---

## 3. O que Analisa (Área de Investigação)

- Consultas a banco de dados lentas ou ineficientes (como N+1 queries, falta de índices adequados, ou varreduras completas desnecessárias).
- Uso indevido de memória devido a retenção de referências longas ou objetos volumosos desnecessários.
- Payload de rede excessivo (sugerir compressão, envio de campos específicos ou paginação).
- Frequência de escrita e leitura em disco e sua otimização (I/O batching).

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Código-fonte da funcionalidade, mapeamento de queries do banco de dados (se aplicável), perfil de concorrência ou chamada de API.
- **Saídas Esperadas:** Relatório apontando issues de performance, complexidade estimada e sugestão de código refatorado otimizado.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:**
  1. Validar se a solução proposta mantém performance estável sob carga.
  2. Priorizar simplicidade e legibilidade, otimizando apenas onde há impacto real mensurável.
- **Bloqueios Obrigatórios (Veto):**
  - Bloquear loops síncronos na thread principal (UI thread / event loop) para operações de disco ou rede.
  - Bloquear queries sem limite (`limit`) ou filtros adequados.
  - Bloquear vazamento óbvio de recursos (ex: arquivos abertos sem fechamento garantido por `finally` ou equivalentes).

---

## 6. Limitações da Skill

- Esta skill não analisa conformidade estética visual (UI/UX) nem valida regras de negócio específicas ou criptografia de segurança.

---

## 7. Critérios de Sucesso

- O código auditado apresenta otimização em complexidade de tempo/espaço, consumo eficiente de recursos e atende aos limites aceitáveis de tempo de resposta sem degradação sob carga.
