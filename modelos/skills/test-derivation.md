# Skill: test-derivation

| Campo | Valor |
|:---|:---|
| **Versão** | `1.0.0` |
| **Domínio** | `Derivação de Cenários de Teste` |
| **Tipo** | `Análise` |
| **Reutilizável** | `Sim` |
| **Atualizado em** | `2026-06-12` |

---

## Propósito

Derivar sistematicamente cenários de teste a partir de features, decisões ou requisitos — cobrindo testes positivos, negativos, edge cases e comportamentos proibidos.

---

## Quando usar

- Durante elaboração de SDD para derivar critérios de aceite
- Após definição de feature para planejar testes
- Ao revisar decisão para identificar cenários de falha
- Antes de implementação para validar entendimento do requisito

---

## Entrada

```markdown
## Feature / Decisão para Derivação

**Descrição:**
[descrição da feature ou decisão]

**Comportamento Esperado:**
[o que deve acontecer em condições normais]

**Contexto de Uso:**
[como usuários vão interagir com isso]

**Restrições Conhecidas:**
[limitações técnicas ou de negócio]
```

---

## Processo

### 1. Identificar Happy Paths (Testes Positivos)

- [ ] Qual é o fluxo principal/feliz?
- [ ] Quais são os fluxos alternativos válidos?
- [ ] Quais entradas válidas devem ser testadas?

### 2. Identificar Falhas Esperadas (Testes Negativos)

- [ ] Quais entradas inválidas devem ser rejeitadas?
- [ ] Quais estados inválidos devem ser tratados?
- [ ] Quais erros esperados podem ocorrer?

### 3. Identificar Edge Cases

- [ ] Valores limite (mínimo, máximo, zero, vazio)?
- [ ] Condições de corrida ou concorrência?
- [ ] Estados de transição?

### 4. Identificar Comportamentos Proibidos

- [ ] O que NUNCA deve acontecer?
- [ ] Quais violações de segurança devem ser bloqueadas?
- [ ] Quais comportamentos violariam regras de negócio?

### 5. Derivar Critérios de Aceite

Para cada cenário acima:
- [ ] Critério é mensurável?
- [ ] Critério é testável automaticamente?
- [ ] Critério é independente de outros critérios?

---

## Saída

```markdown
## Derivação de Testes: {{FEATURE}}

### Critérios de Aceite

| ID | Critério | Tipo | Prioridade |
|:---|:---|:---:|:---:|
| CA01 | [critério 1] | Must/Should/Could | Alta/Média/Baixa |
| CA02 | [critério 2] | Must/Should/Could | Alta/Média/Baixa |

### Testes Positivos (Happy Path)

| ID | Cenário | Entradas | Saída Esperada |
|:---|:---|:---|:---|
| TP01 | [cenário 1] | [dados de entrada] | [resultado esperado] |
| TP02 | [cenário 2] | [dados de entrada] | [resultado esperado] |

### Testes Negativos (Falhas Esperadas)

| ID | Cenário | Entradas | Comportamento Esperado |
|:---|:---|:---|:---|
| TN01 | [cenário 1] | [dado inválido] | [erro específico retornado] |
| TN02 | [cenário 2] | [estado inválido] | [tratamento adequado] |

### Edge Cases

| ID | Cenário | Condição Especial | Validação Necessária |
|:---|:---|:---|:---|
| EC01 | [cenário] | [valor limite/condição] | [o que validar] |
| EC02 | [cenário] | [concorrência/timing] | [o que validar] |

### Comportamentos Proibidos

| ID | Comportamento | Por que é proibido? | Como prevenir? |
|:---|:---|:---|:---|
| CP01 | [o que nunca fazer] | [razão: segurança/negócio/etc.] | [mecanismo de prevenção] |
| CP02 | [o que nunca fazer] | [razão] | [mecanismo] |

### Matriz de Cobertura

| Funcionalidade | TP | TN | EC | CP | Cobertura % |
|:---|:---:|:---:|:---:|:---:|:---:|
| [func 1] | 3 | 2 | 2 | 1 | 80% |
| [func 2] | 2 | 1 | 1 | 1 | 70% |

### Handoff para Agente de Testes

**Implementar:**
- [ ] Testes unitários: [quais cenários]
- [ ] Testes de integração: [quais fronteiras]
- [ ] Testes E2E: [quais fluxos críticos]

**Ferramentas recomendadas:**
- [framework/tool sugerido]

**Prioridade:**
- [alta/média/baixa - justificar]
```

---

## Critérios de Qualidade

- [ ] Todos os happy paths cobertos
- [ ] Falhas esperadas identificadas
- [ ] Edge cases considerados (valores limite, concorrência)
- [ ] Comportamentos proibidos explícitos
- [ ] Critérios de aceite mensuráveis e testáveis
- [ ] Matriz de cobertura preenchida
- [ ] Handoff claro para implementação

---

## Exemplo de Uso

**Entrada:**
```
Feature: Upload de arquivos

Descrição: Usuários podem upload de fotos de perfil até 5MB

Comportamento Esperado: Foto salva e exibida no perfil

Restrições: Máximo 5MB, formatos JPG/PNG
```

**Saída:**
```markdown
## Derivação de Testes: Upload de Fotos

### Critérios de Aceite
| ID | Critério | Tipo | Prioridade |
|:---|:---|:---:|:---:|
| CA01 | Upload JPG ≤5MB funciona | Must | Alta |
| CA02 | Upload PNG ≤5MB funciona | Must | Alta |
| CA03 | Arquivo >5MB é rejeitado | Must | Alta |

### Testes Positivos
| ID | Cenário | Entradas | Saída Esperada |
|:---|:---|:---|:---|
| TP01 | Upload JPG 2MB | file.jpg (2MB) | Foto salva e URL retornada |
| TP02 | Upload PNG 4MB | file.png (4MB) | Foto salva e URL retornada |

### Testes Negativos
| ID | Cenário | Entradas | Comportamento Esperado |
|:---|:---|:---|:---|
| TN01 | Upload 6MB | file.jpg (6MB) | Erro "Arquivo excede 5MB" |
| TN02 | Upload GIF | file.gif (2MB) | Erro "Formato não suportado" |

### Edge Cases
| ID | Cenário | Condição | Validação |
|:---|:---|:---|:---|
| EC01 | Upload 5MB exato | file.jpg (5.0MB) | Deve aceitar |
| EC02 | Upload 0 bytes | empty.jpg (0B) | Deve rejeitar |
| EC03 | Upload concorrente | 2 uploads simultâneos | Ambos devem funcionar |

### Comportamentos Proibidos
| ID | Comportamento | Por que | Prevenção |
|:---|:---|:---|:---|
| CP01 | Executar código no arquivo | Segurança | Validar metadados, sanitizar |
| CP02 | Acessar arquivos de outros usuários | Privacidade | Isolar por user_id |

### Handoff
**Implementar:**
- Unitários: Validação de tamanho, formato
- Integração: Upload → storage → CDN
- E2E: Fluxo completo no UI
```

---

## Agentes que usam esta skill

- `conselho-decisao` (orquestrador)
- `agente-testes`
- `spec-agent`
