# Skill - markdown-quality

| Campo | Valor |
|:---|:---|
| **Finalidade** | Qualidade geral de formatação Markdown, tratamento de caracteres e quebra de linhas |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Sempre que arquivos `.md` forem submetidos ao repositório para auditoria ou commit.
- Ao revisar a legibilidade estática do código-fonte markdown em editores de texto.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] Ausência de linhas em branco consecutivas em excesso (máximo 1).
- [ ] Uso correto de aspas, traços e espaços ao redor de listas ordenadas e não-ordenadas.
- [ ] Fenced code blocks (` ``` `) têm a indicação correta da linguagem de programação usada no bloco.

---

## 3. O que Analisa (Área de Investigação)

- Erros de indentação em listas aninhadas.
- Caracteres especiais mal interpretados (problemas de codificação UTF-8).
- Linhas excessivamente longas sem quebras que prejudicam a visualização lado a lado.

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Arquivo markdown para validação de lint.
- **Saídas Esperadas:** Lista de warnings de formatação markdown e arquivo limpo automatizado (se aplicável).

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Manter consistência na sintaxe de formatação (ex: preferir sempre `**` para negrito, em vez de `__`).
- **Bloqueios Obrigatórios (Veto):** Bloquear blocos de código sem declaração de linguagem ou com delimitadores abertos e não fechados.
