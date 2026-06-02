# Skill - placeholder-governance

| Campo | Valor |
|:---|:---|
| **Finalidade** | Identificação, rastreamento e governança de placeholders não preenchidos |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Na verificação final de documentos que saem de rascunho (`draft`) para ativo (`active`).
- Antes do merge de especificações ou guias em branch de produção.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] Ausência de strings como `[NOME_DO_PROJETO]`, `{{PLACEHOLDER}}`, `TODO:`, ou `[A PREENCHER]`.
- [ ] Marcações de pendência técnica ou inferência estão devidamente listadas como `[PENDENTE]` em tabela separada se permitidas pelo projeto.
- [ ] Textos descritivos explicativos inseridos pelo template (ex: `> *Escreva aqui...*`) foram totalmente removidos.

---

## 3. O que Analisa (Área de Investigação)

- Vazamento de templates de exemplo em documentos do repositório final de produção.
- Áreas de documentação vazias ou negligenciadas pelo time de desenvolvimento.

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Arquivo markdown para varredura de tags de exemplo.
- **Saídas Esperadas:** Lista exata de linhas com placeholders não preenchidos.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Buscar de forma insensível a maiúsculas e minúsculas por padrões comuns de marcação.
- **Bloqueios Obrigatórios (Veto):** Bloquear qualquer documento em produção que contenha placeholders padrão inalterados nas seções críticas (metadados, contatos, segurança).
