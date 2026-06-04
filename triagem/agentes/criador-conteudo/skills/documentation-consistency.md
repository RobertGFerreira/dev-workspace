# Skill - documentation-consistency

| Campo | Valor |
|:---|:---|
| **Finalidade** | Validação de consistência cruzada entre múltiplos arquivos de documentação |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Ao auditar um conjunto de documentações técnicas de um repositório (README, SDD, Arquitetura, APIs).
- Após grandes refatorações de código para validar se os guias e manuais continuam condizentes com as implementações.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] Referências de arquivos em guias correspondem a caminhos físicos reais no repositório.
- [ ] Siglas, termos técnicos e conceitos de negócio são uniformes em todos os arquivos.
- [ ] O passo a passo de guias de setup de ambiente funciona perfeitamente nas versões declaradas.

---

## 3. O que Analisa (Área de Investigação)

- Informações contraditórias entre documentos (ex: README lista versão 3.0 de biblioteca, Contributing diz 2.5).
- Links relativos quebrados.

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Todos os arquivos de documentação (`.md`), estrutura de diretórios do repositório.
- **Saídas Esperadas:** Diagnóstico de links e consistência de caminhos, com lista de issues encontradas.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Sempre rastrear links relativos até o destino físico para garantir validade.
- **Bloqueios Obrigatórios (Veto):** Bloquear qualquer documentação que cite comandos ou caminhos inexistentes ou desatualizados.
