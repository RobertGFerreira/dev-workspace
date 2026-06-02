# Skill - feature-storytelling

| Campo | Valor |
|:---|:---|
| **Finalidade** | Conversão de características técnicas em histórias e benefícios atraentes |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Ao criar materiais explicativos de novas features do produto.
- Ao estruturar logs de atualização (changelogs) públicos ou relatórios de melhorias para clientes.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] Cada especificação técnica é conectada a um benefício tangível (ex: "Banco de dados SQLite local" -> "Funciona sem internet, no meio do campo").
- [ ] O texto utiliza analogias simples para explicar arquiteturas técnicas complexas.
- [ ] Há uma narrativa que conecta a dor do usuário à feature implementada.

---

## 3. O que Analisa (Área de Investigação)

- Textos secos e puramente técnicos que falham em engajar o usuário não-técnico.
- Exagero na simplificação que acabe omitindo informações importantes de engenharia.

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Requisitos técnicos da feature, documentação de pull request.
- **Saídas Esperadas:** Copy explicativo e narrativo da feature voltado para o usuário final.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Usar a estrutura clássica: "Problema -> Solução -> Como usar -> Benefício".
- **Bloqueios Obrigatórios (Veto):** Bloquear descrições que listem siglas técnicas complicadas (ex: JWT, REST, SQLite) sem explicar o que elas significam na experiência prática do usuário.
