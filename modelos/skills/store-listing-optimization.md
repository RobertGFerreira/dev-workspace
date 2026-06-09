# Skill - store-listing-optimization

**Finalidade:** Otimização de metadados para busca (ASO - App Store Optimization) e conversão na listagem das lojas Apple App Store e Google Play Store.
**Versão:** 1.1.0

---

## 1. Quando Usar

- Ao redigir, traduzir ou auditar metadados textuais de aplicativos para publicação em lojas (título, subtítulo, descrições, palavras-chave).
- Ao analisar palavras-chave competitivas e posicionamento de busca do aplicativo.
- Ao estruturar campanhas de testes A/B de metadados ou assets visuais nas fichas de loja.

---

## 2. O que Valida (Foco de Auditoria)

### Limites e Regras de Caracteres por Plataforma

- **Apple App Store:**
  - [ ] **Título (Title):** Máximo 30 caracteres.
  - [ ] **Subtítulo (Subtitle):** Máximo 30 caracteres.
  - [ ] **Texto Promocional (Promotional Text):** Máximo 170 caracteres.
  - [ ] **Descrição (Description):** Máximo 4.000 caracteres.
  - [ ] **Palavras-chave (Keywords):** Máximo 100 caracteres. Sem espaços depois da vírgula. Sem termos duplicados ou que já estejam no Título/Subtítulo.
  - [ ] **Novidades (What's New):** Máximo 4.000 caracteres.

- **Google Play Store:**
  - [ ] **Título (Title):** Máximo 50 caracteres.
  - [ ] **Descrição Curta (Short Description):** Máximo 80 caracteres.
  - [ ] **Descrição Completa (Full Description):** Máximo 4.000 caracteres.

### Qualidade e Coerência de Metadados
- [ ] Distribuição de palavras-chave estratégicas nas posições iniciais (front-loaded) de títulos e descrições.
- [ ] Ausência de repetição excessiva de termos (keyword stuffing).
- [ ] Tradução e localização completas e adequadas culturalmente para todos os idiomas alvo.
- [ ] Coerência de textos com os arquivos visuais descritos (screenshots, ícones, banners).

---

## 3. O que Analisa (Área de Investigação)

- **Análise de Concorrência:** Sobreposição de termos com líderes de categoria, análise de diferenciação na proposta de valor e identificação de lacunas.
- **Políticas das Lojas:** Presença de termos proibidos (ex: "melhor", "grátis", "nº 1", ou marcas registradas de concorrentes).
- **Planejamento de Teste A/B:** Proposta de hipóteses claras para testes de conversão (ex: mudar ícone, screenshots ou descrição curta), com estimativa de tamanho de amostra e tempo mínimo de duração para relevância estatística.

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas:** Proposta de metadados por idioma, lista de palavras-chave prioritárias do nicho, plataforma alvo (Apple / Google / Ambas) e informações sobre concorrentes.
- **Saídas:** Metadados otimizados para cópia direta nas respectivas caixas da console de publicação, validação de caracteres em tempo real e lista de termos recomendados para o campo de palavras-chave da Apple.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Nunca use espaços adicionais dentro da lista de palavras-chave da Apple (ex: use `todo,task,organizer` e não `todo, task, organizer`).
- **Bloqueios Obrigatórios (Veto):**
  - Menção a preços, promoções ou rankings ("grátis", "promoção", "#1 app") em elementos do Título, Ícone ou Descrição Curta → **BLOQUEADO**.
  - Nome de concorrente ou marca registrada de terceiros nos metadados visíveis → **BLOQUEADO**.
