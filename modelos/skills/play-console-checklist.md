# Skill - play-console-checklist

| Campo | Valor |
|:---|:---|
| **Finalidade** | Checklist estruturado de etapas e formulários para o Google Play Console |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Ao preparar a submissão de um novo aplicativo ou atualização na Play Store.
- Ao revisar o andamento do processo de liberação (release checklist) no console de desenvolvedor.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] Todas as tarefas de inicialização da conta/app estão completadas (ex: Declaração de publicidade, classificação etária, público-alvo).
- [ ] O arquivo de mapeamento de símbolos de ofuscação (mapping.txt / ProGuard) está empacotado para o upload do AAB.
- [ ] Informações de contato e suporte (URL, e-mail) estão atualizadas na listagem da loja.

---

## 3. O que Analisa (Área de Investigação)

- Gaps operacionais que causam atrasos na aprovação do app pelo Google (ex: credenciais de teste para o revisor do Google ausentes).
- Configuração incompleta de países/regiões de distribuição do aplicativo.

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Ficha cadastral do app, credenciais da conta do Play Console, APK/AAB do projeto.
- **Saídas Esperadas:** Checklist de tarefas operacionais customizado para o tipo de aplicativo.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Sempre testar as credenciais da conta de teste fornecida ao revisor do Google antes de enviar para revisão.
- **Bloqueios Obrigatórios (Veto):** Bloquear envios que requeiram login no app sem que o formulário de "Instruções de acesso ao app" (App access) esteja totalmente preenchido.
