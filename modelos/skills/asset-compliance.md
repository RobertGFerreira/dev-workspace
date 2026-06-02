# Skill - asset-compliance

| Campo | Valor |
|:---|:---|
| **Finalidade** | Auditoria de formatos, resoluções e conformidade de imagens exigidas pelas lojas |
| **Versão** | `1.0.0` |

---

## 1. Quando Usar

- Ao criar ou revisar o pacote de assets gráficos (ícone, banner de destaque, screenshots de tablet/celular) do app.
- Durante a preparação do kit de mídia (Media Kit) para a publicação do aplicativo.

---

## 2. O que Valida (Foco de Auditoria)

- [ ] Ícone do aplicativo tem resolução de exatamente 512x512 pixels, formato PNG de 32 bits e tamanho máximo de 1MB.
- [ ] Banner de destaque (Feature Graphic) tem exatamente 1024x500 pixels, proporção correta e formato PNG ou JPG.
- [ ] Screenshots de dispositivos atendem às proporções exigidas (mínimo 4 capturas, formato PNG/JPG, proporção 16:9 ou 9:16).

---

## 3. O que Analisa (Área de Investigação)

- Distorções ou problemas de escala nas screenshots devido a alongamento incorreto.
- Imagens que contenham elementos de interface de outros sistemas operacionais (ex: barra de status do iOS em screenshots da Play Store).
- Textos em screenshots ilegíveis em telas de celulares pequenos.

---

## 4. Entradas Necessárias e Saídas Esperadas

- **Entradas Necessárias:** Arquivos de imagem dos assets propostos.
- **Saídas Esperadas:** Relatório de conformidade dimensional e de formato das imagens.

---

## 5. Regras de Execução e Bloqueios

- **Regras Operacionais:** Verificar a legibilidade do texto e a qualidade visual em múltiplos tamanhos.
- **Bloqueios Obrigatórios (Veto):** Bloquear imagens com resoluções diferentes dos valores absolutos definidos pelo Google, ou que exibam marcas d'água de ferramentas de mockup.
