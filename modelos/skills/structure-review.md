# Skill - structure-review

| Campo | Valor |
|:---|:---|
| **Finalidade** | Validação estrutural de documentos, hierarquia de cabeçalhos e índices |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Ao auditar a formatação técnica de documentos extensos (SDD, Artigo de Arquitetura).
- Ao realizar lints de estrutura de documentação antes de fechamento de milestones de design de software.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] A hierarquia de cabeçalhos H1 a H6 é lógica e sequencial (sem pular de `#` para `###` diretamente).
- [ ] O índice analítico (Table of Contents - TOC) do documento corresponde exatamente aos títulos reais existentes.
- [ ] Tabelas estão formatadas corretamente, com alinhamento explícito nas colunas.

---

## 3. O que Analisa (Área de Investigação)

- Cabeçalhos redundantes ou com grafia inconsistente.
- Páginas excessivamente longas sem quebras temáticas adequadas por separadores (`---`).

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Arquivo markdown para análise.
- **Saídas Esperadas:** Árvore de hierarquia de títulos e apontamento de quebras de sequencialidade lógica.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Exigir o uso de uma única tag `#` (H1) por arquivo de documentação.
- **Bloqueios Obrigatórios (Veto):** Bloquear documentos com quebra severa de renderização markdown (como tags de tabelas desalinhadas ou links com sintaxe incorreta).
