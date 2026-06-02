# Skill - template-adherence

| Campo | Valor |
|:---|:---|
| **Finalidade** | Auditoria de correspondência perfeita com as diretrizes do template original |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Ao criar um novo arquivo a partir de um template universal (`README.template.md`, `ARCHITECTURE.template.md`, etc.).
- Ao auditar se um documento segue estritamente a hierarquia e as seções obrigatórias especificadas.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] Todas as seções obrigatórias declaradas no template existem no documento criado.
- [ ] A ordem de apresentação e a hierarquia dos títulos respeita o template mestre.
- [ ] Elementos de governança obrigatórios (tabelas de versão, data de atualização) estão devidamente preenchidos.

---

## 3. O que Analisa (Área de Investigação)

- Remoção ou alteração de títulos de seções importantes que quebram o padrão de busca automatizada.
- Inclusão de blocos explicativos ou pedagógicos que deveriam ter sido expurgados antes da entrega final.

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Arquivo de template original, arquivo implementado.
- **Saídas Esperadas:** Tabela comparativa de seções e status de conformidade do layout.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Em caso de seções intencionalmente vazias, exigir a indicação `[Não aplicável para este projeto]` em vez de apagar o título.
- **Bloqueios Obrigatórios (Veto):** Bloquear documentos que tenham alterado títulos de cabeçalhos de tabelas de metadados obrigatórias.
