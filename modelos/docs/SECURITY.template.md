# Security Policy — {{NOME_DO_PROJETO}}

> **Versão da política:** `{{VERSAO_DA_POLITICA}}`
> **Atualizado em:** `{{DATA}}`

---

## Versões com suporte

<!-- Liste apenas as versões ativamente mantidas com patches de segurança -->

| Versão | Suportada |
|:---|:---:|
| `{{VERSAO}}` | ✅ |
| `{{VERSAO_ANTIGA}}` | ❌ |

---

## Reporte de vulnerabilidades

**Não abra issues públicas** com detalhes de vulnerabilidades exploráveis.

Reporte exclusivamente por canal privado:

| Canal | Endereço |
|:---|:---|
| E-mail | `{{EMAIL_DE_SEGURANCA}}` <!-- ex: security@dominio.com --> |
| PGP <!-- OPCIONAL --> | `{{FINGERPRINT_PGP}}` |

### SLA de resposta

| Criticidade | Tempo de confirmação | Tempo de resolução |
|:---|:---:|:---:|
| Crítica (CVSS ≥ 9.0) | 24h | 7 dias |
| Alta (CVSS 7.0–8.9) | 48h | 30 dias |
| Média / Baixa | 72h | 90 dias |

### O que incluir no reporte

1. Descrição da vulnerabilidade
2. Passos para reprodução
3. Impacto esperado
4. Versão afetada
5. Sugestão de correção (se disponível)

---

## Política de segredos

**Nunca versionar:**
- Arquivos `.env` reais
- Tokens de API, chaves privadas (SSH, TLS, PGP)
- Strings de conexão com credenciais
- Cookies de sessão ou JWTs ativos

**Sempre fornecer:**
- `.env.example` com placeholders e descrição funcional de cada variável
- Documentação das variáveis sem valores reais

---

## Variáveis de ambiente

- Manter `.env.example` com valores completamente fictícios.
- Documentar nome, tipo e finalidade de cada variável.
- Nunca incluir caminhos locais absolutos ou dados pessoais em exemplos.

---

## Procedimento em caso de exposição acidental

1. **Revogar** imediatamente o segredo afetado (token, chave, senha).
2. **Remover** a exposição do código e da documentação.
3. **Limpar** o histórico git com `git filter-repo` se o segredo foi commitado.
4. **Auditar** logs, releases, forks e pipelines que possam ter capturado o segredo.
5. **Registrar** a correção no CHANGELOG sem reproduzir o conteúdo exposto.

---

## Projetos públicos

Antes de tornar um repositório público:

- [ ] Substituir `.env` real por `.env.example` com placeholders
- [ ] Executar verificação de segredos no histórico git
- [ ] Remover TODOs e comentários com informações sensíveis
- [ ] Auditar metadados de assets e imagens (EXIF)
- [ ] Executar `npm audit`, `pip-audit` ou equivalente nas dependências
