# Exemplo — Derivação de Testes com o Conselho

## Cenário

Decisão técnica: "Implementar cache SQLite local com sincronização offline-first"

## Parecer de Derivação de Testes

### Casos Positivos

- [CT001] Dados salvos localmente são sincronizados quando conectividade é restaurada
- [CT002] Cache retorna dados corretos quando dispositivo está offline

### Casos Negativos

- [CT003] Falha de sincronização não corrompe cache local
- [CT004] Conflito de dados (local vs. servidor) não resulta em perda de dados

### Casos de Borda

- [CT005] Cache com 0 registros — sincronização não falha
- [CT006] Cache com 10.000+ registros — performance aceitável
- [CT007] Dispositivo fica offline durante sincronização — rollback parcial

### Comportamentos Proibidos

- [CT008] Dados do servidor NUNCA sobrescrevem dados locais mais recentes sem merge
- [CT009] Cache NUNCA expõe dados de outro usuário em dispositivos compartilhados

### Riscos não cobertos

- Concorrência: duas escritas simultâneas no cache podem causar race condition
- Migração: versão antiga do cache deve ser migrada sem perda
