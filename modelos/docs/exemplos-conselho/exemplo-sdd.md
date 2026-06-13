# Exemplo — Apoio do Conselho à Criação de SDD

## Cenário

Feature: "Sistema de notificações push para usuários do aplicativo"

## Entrada (Requisitos Preliminares)

- RF001: Usuário recebe notificação quando há nova mensagem
- RF002: Usuário pode configurar quais notificações receber
- RNF001: Notificações devem chegar em até 30s
- RNF002: Deve funcionar offline — notificações pendentes na reconexão
- Restrição: App Android e iOS

## Parecer do Conselho

### Conselheiros acionados

**caminho-correto**
- Alinhamento: OK, requisitos cobertos
- Observação: Ausência de especificação de permissões (Android 13+)

**caca-falhas**
- Risco: Notificação sem permissão do usuário gera rejeição na loja
- Edge case: Dispositivo sem conectividade por mais de 7 dias
- Teste sugerido: Notificação recebida com app em background vs. killed

**fora-da-caixa**
- Alternativa: Usar FCM + WebSocket como fallback para baixa latência
- Expansão: Notificações agrupadas por tipo (mensagem, alerta, promoção)

**leigo-radical**
- Premissa questionada: "Precisa de notificação push ou um badge local resolve?"
- Simplificação: Para MVP, notificação local com polling a cada 60s reduz complexidade

### Consolidação

- **Aprovado:** Condicional (tratar permissões e cenário offline)
- **Lacunas:** Permissões Android 13+, fallback offline, agrupamento
- **Recomendação:** Iniciar com polling + notificação local, evoluir para push
