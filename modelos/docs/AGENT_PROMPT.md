# AGENT_PROMPT - Documentacao Modelo

## Escopo

Trabalhar somente dentro de `Documentacao_modelo/`. Nunca sobrescrever arquivos originais dos repositorios analisados sem solicitacao explicita.

## Ordem de leitura

1. `project.config.json`, `project.config.yaml`, `project.meta.json` ou `project.meta.yaml`.
2. `AGENT_PROMPT.md` ou `prompt.md`.
3. Arquivos raiz: `README.md`, `ROADMAP.md`, `CHANGELOG.md`, `ARCHITECTURE.md`, `CONTRIBUTING.md`, `SECURITY.md`.
4. Manifestos tecnicos: `pubspec.yaml`, `package.json`, `requirements.txt`, `pyproject.toml`, `Dockerfile`, `docker-compose.yml`.
5. `docs/*.md` apenas quando necessario para preencher lacunas.
6. Historico git dos arquivos de documentacao relevantes.

## Sanitizacao obrigatoria

- Substituir tokens por `{{TOKEN}}`.
- Substituir emails privados por `{{EMAIL}}`.
- Substituir telefones por `{{TELEFONE}}`.
- Substituir caminhos locais absolutos por `{{CAMINHO_LOCAL}}`.
- Remover usuario/senha/token embutido em URL remota.
- Nunca copiar valores reais de `.env`, logs, screenshots, vaults ou arquivos privados.

## Ordem de geracao

1. Criar ou atualizar `project.config.json`.
2. Criar ou atualizar `AGENT_PROMPT.md`.
3. Gerar `_PADRAO_UNIVERSAL/*.template.md`.
4. Gerar `README.md`, `ROADMAP.md`, `CHANGELOG.md`, `ARCHITECTURE.md`, `CONTRIBUTING.md` e `SECURITY.md` em `Documentacao_modelo/<Projeto>/`.
5. Gerar `_PADRAO_UNIVERSAL/RELATORIO_ANALISE.md`.
6. Validar que nao ha segredos, caminhos locais ou remotes com credencial.

## Criterios de qualidade

- Nao inventar dados; usar placeholders quando a informacao nao for confirmada.
- Manter idioma original predominante do projeto.
- Preferir clareza, estrutura e manutencao a excesso de conteudo.
- Incluir Mermaid valido em arquitetura.
- Changelog deve seguir categorias do Keep a Changelog.

## Recuperacao por historico

Consultar diffs anteriores quando o arquivo atual estiver incompleto, tiver grande reducao de conteudo, perder secoes criticas ou quando commits recentes indicarem restauracao/reorganizacao de documentacao. Se houver duvida entre completude e privacidade, privacidade vence.
