import os
import shutil
import json

base_dir = r"c:\Users\Robert\Documents\GitHub"
workspace_dir = os.path.join(base_dir, "dev-workspace")

# Define exclude list for files and directories (to skip during markdown scanning and copying)
EXCLUDE_DIRS = {".git", "node_modules", ".venv", "env", "venv", ".idea", ".vscode", "__pycache__", "build", "ios", "android", "vendor", ".pytest_cache"}
ROOT_EXCLUDE = {"dev-workspace"}

# AI config markers and names
AI_MARKER_NAMES = [".antigravity", ".codex", ".opencode", ".continue", "antigravity.json", "codex.md", "AGENTS.md", "opencode.json"]

print("--- INICIANDO ORGANIZAÇÃO DO DEV-WORKSPACE ---")

# Step 1: Create basic directory structure
directories_to_create = [
    os.path.join(workspace_dir, "projetos"),
    os.path.join(workspace_dir, "auditoria"),
    os.path.join(workspace_dir, "modelos"),
    os.path.join(workspace_dir, "modelos", "agentes"),
    os.path.join(workspace_dir, "modelos", "prompts"),
    os.path.join(workspace_dir, "modelos", "skills"),
    os.path.join(workspace_dir, "modelos", "docs")
]

for d in directories_to_create:
    os.makedirs(d, exist_ok=True)
    print(f"Diretório garantido: {d}")

# Load subdirectories
subdirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
projects_data = []

# Step 2 & 3: Iterate through projects and copy files
for d in subdirs:
    if d in ROOT_EXCLUDE or d.startswith("."):
        continue
    
    proj_path = os.path.join(base_dir, d)
    print(f"\n[Projeto: {d}]")
    
    proj_dest_docs = os.path.join(workspace_dir, "projetos", d, "docs")
    proj_dest_ai = os.path.join(workspace_dir, "projetos", d, "ai-configs")
    
    os.makedirs(proj_dest_docs, exist_ok=True)
    os.makedirs(proj_dest_ai, exist_ok=True)
    
    all_md_files = []
    found_ai_configs = []
    found_ai_tools = set()
    
    # Run scan walk
    for root, dirs, files in os.walk(proj_path):
        # prune directory search tree in-place
        dirs[:] = [sub for sub in dirs if sub not in EXCLUDE_DIRS and not sub.startswith(".venv") and not sub.startswith("node_modules")]
        
        # Check files
        for f in files:
            file_path = os.path.join(root, f)
            rel_path = os.path.relpath(file_path, proj_path)
            
            # Copy valid .md files
            if f.endswith(".md"):
                all_md_files.append(rel_path)
                dest_file_path = os.path.join(proj_dest_docs, rel_path)
                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                try:
                    shutil.copy2(file_path, dest_file_path)
                except Exception as e:
                    print(f"Erro ao copiar MD {rel_path}: {e}")
            
            # Check for specific AI files and copy them
            is_ai_file = False
            if f.endswith(".prompt.md"):
                found_ai_tools.add("Prompt.md")
                is_ai_file = True
            elif f.endswith(".skill.ai"):
                found_ai_tools.add("Skill.ai")
                is_ai_file = True
            elif f == "antigravity.json":
                found_ai_tools.add("Antigravity")
                is_ai_file = True
            elif f == "codex.md" or f == "AGENTS.md":
                found_ai_tools.add("Codex")
                is_ai_file = True
            elif f == "opencode.json":
                found_ai_tools.add("Open Code")
                is_ai_file = True
            elif f == "config.json" and (".continue" in root or "continue" in root.lower()):
                found_ai_tools.add("Continue")
                is_ai_file = True
                
            if is_ai_file:
                found_ai_configs.append(rel_path)
                dest_file_path = os.path.join(proj_dest_ai, rel_path)
                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                try:
                    shutil.copy2(file_path, dest_file_path)
                except Exception as e:
                    print(f"Erro ao copiar config IA {rel_path}: {e}")
                    
        # Check directories for AI markers
        for dir_name in list(dirs):
            dir_path = os.path.join(root, dir_name)
            rel_path = os.path.relpath(dir_path, proj_path)
            
            is_ai_dir = False
            if dir_name == ".antigravity":
                found_ai_tools.add("Antigravity")
                is_ai_dir = True
            elif dir_name == ".codex":
                found_ai_tools.add("Codex")
                is_ai_dir = True
            elif dir_name == ".opencode":
                found_ai_tools.add("Open Code")
                is_ai_dir = True
            elif dir_name == ".continue":
                found_ai_tools.add("Continue")
                is_ai_dir = True
            elif dir_name in ["agents", "skills", "prompts", "rules"]:
                is_ai_dir = True
                if dir_name == "agents":
                    found_ai_tools.add("Agents folder")
                elif dir_name == "skills":
                    found_ai_tools.add("Skills folder")
                elif dir_name in ["prompts", "rules"]:
                    found_ai_tools.add("Continue/General prompts")
                    
            if is_ai_dir:
                found_ai_configs.append(rel_path)
                dest_dir_path = os.path.join(proj_dest_ai, rel_path)
                os.makedirs(dest_dir_path, exist_ok=True)
                # Copy recursively everything in this AI folder
                try:
                    for sub_root, sub_dirs, sub_files in os.walk(dir_path):
                        for sub_f in sub_files:
                            src_f = os.path.join(sub_root, sub_f)
                            if os.path.isfile(src_f):
                                sub_rel = os.path.relpath(src_f, dir_path)
                                dst_f = os.path.join(dest_dir_path, sub_rel)
                                os.makedirs(os.path.dirname(dst_f), exist_ok=True)
                                shutil.copy2(src_f, dst_f)
                except Exception as e:
                    print(f"Erro ao copiar pasta de config IA {rel_path}: {e}")
                
                # Prune this directory from the outer search tree to avoid walking into it again
                if dir_name in dirs:
                    dirs.remove(dir_name)
                    
    # Analysis & classification
    has_readme = "Sim" if any(f.lower() == "readme.md" for f in all_md_files) else "Não"
    
    # Classify project type
    d_lower = d.lower()
    if "site" in d_lower or "landing" in d_lower or "portfolio" in d_lower:
        proj_type = "Site"
    elif "showcase" in d_lower or "demo" in d_lower or "exemplo" in d_lower:
        proj_type = "Showcase"
    else:
        proj_type = "Privado"
        
    # Generate observations
    observations = []
    try:
        root_files = os.listdir(proj_path)
    except Exception as e:
        root_files = []
        
    if "pubspec.yaml" in root_files:
        observations.append("Flutter/Dart")
    if "package.json" in root_files:
        observations.append("Node.js/JS/TS")
    if "requirements.txt" in root_files or "setup.py" in root_files or any(f.endswith(".py") for f in root_files):
        observations.append("Python")
    if "pom.xml" in root_files:
        observations.append("Java (Maven)")
    if any(f.endswith(".sln") for f in root_files):
        observations.append("C#/.NET")
        
    if len(all_md_files) > 0:
        observations.append(f"{len(all_md_files)} arquivos .md")
    if len(found_ai_configs) > 0:
        observations.append(f"{len(found_ai_configs)} itens de IA")
        
    # Save project data for report
    projects_data.append({
        "name": d,
        "type": proj_type,
        "has_readme": has_readme,
        "has_ai_config": "Sim" if len(found_ai_configs) > 0 else "Não",
        "ai_tools": ", ".join(sorted(list(found_ai_tools))) if found_ai_tools else "Nenhuma",
        "observations": "; ".join(observations) if observations else "Nenhuma"
    })
    
    print(f" -> {len(all_md_files)} MDs e {len(found_ai_configs)} itens de IA catalogados e copiados.")

# Step 4: Selection and copying of "Melhores Modelos"
print("\n--- COPIANDO OS MELHORES MODELOS E TEMPLATES ---")

# 1. Copy Document Templates (docs)
source_universal_docs = os.path.join(base_dir, "Documentacao_modelo", "Documentacao_modelo", "_PADRAO_UNIVERSAL")
dest_modelos_docs = os.path.join(workspace_dir, "modelos", "docs")
if os.path.exists(source_universal_docs):
    for f in os.listdir(source_universal_docs):
        src_f = os.path.join(source_universal_docs, f)
        if os.path.isfile(src_f):
            shutil.copy2(src_f, os.path.join(dest_modelos_docs, f))
            print(f"Modelo de doc copiado: {f}")
            
# Copy AGENT_PROMPT.md template
agent_prompt_src = os.path.join(base_dir, "Documentacao_modelo", "Documentacao_modelo", "AGENT_PROMPT.md")
if os.path.exists(agent_prompt_src):
    shutil.copy2(agent_prompt_src, os.path.join(dest_modelos_docs, "AGENT_PROMPT.md"))
    print("Modelo de doc copiado: AGENT_PROMPT.md")

# 2. Copy Agent Architectures (agentes)
source_agents = os.path.join(base_dir, "condominio-rural", "governance", "agents")
dest_modelos_agents = os.path.join(workspace_dir, "modelos", "agentes")
if os.path.exists(source_agents):
    for f in os.listdir(source_agents):
        src_f = os.path.join(source_agents, f)
        if os.path.isfile(src_f):
            shutil.copy2(src_f, os.path.join(dest_modelos_agents, f))
            print(f"Modelo de agente copiado: {f}")

# 3. Copy Specialized Prompts (prompts)
source_prompts = os.path.join(base_dir, "Projeto_rual_web", "prompts")
dest_modelos_prompts = os.path.join(workspace_dir, "modelos", "prompts")
if os.path.exists(source_prompts):
    for f in os.listdir(source_prompts):
        src_f = os.path.join(source_prompts, f)
        if os.path.isfile(src_f):
            shutil.copy2(src_f, os.path.join(dest_modelos_prompts, f))
            print(f"Modelo de prompt copiado: {f}")

# 4. Copy Skills definitions (skills)
source_skills = os.path.join(base_dir, "condominio-rural", "governance", "skills")
dest_modelos_skills = os.path.join(workspace_dir, "modelos", "skills")
if os.path.exists(source_skills):
    for f in os.listdir(source_skills):
        src_f = os.path.join(source_skills, f)
        if os.path.isfile(src_f):
            shutil.copy2(src_f, os.path.join(dest_modelos_skills, f))
            print(f"Modelo de skill copiado: {f}")

# Step 5: Generate Auditoria (relatorio-geral.md)
print("\n--- GERANDO RELATÓRIO DE AUDITORIA ---")
report_path = os.path.join(workspace_dir, "auditoria", "relatorio-geral.md")

report_content = """# Relatório Geral de Auditoria dos Projetos

Este relatório apresenta um inventário completo dos projetos de desenvolvimento encontrados na pasta de trabalho, catalogando suas documentações e mapeando a adoção de configurações e ferramentas de Inteligência Artificial.

## Tabela Comparativa de Projetos

| Projeto | Tipo | Tem README | Tem Config IA | Ferramentas IA | Observações |
| :--- | :--- | :--- | :--- | :--- | :--- |
"""

for p in sorted(projects_data, key=lambda x: x["name"].lower()):
    report_content += f"| {p['name']} | {p['type']} | {p['has_readme']} | {p['has_ai_config']} | {p['ai_tools']} | {p['observations']} |\n"

report_content += """
## Métricas de Adoção de IA e Documentação

- **Total de Projetos Analisados:** {total_projetos}
- **Projetos com README:** {total_readme} ({pct_readme:.1f}%)
- **Projetos com Configuração de IA:** {total_ai} ({pct_ai:.1f}%)

### Legenda dos Tipos de Projetos
1. **Privado:** Produto real ou repositório de uso pessoal.
2. **Showcase:** Repositório público configurado para portfólio.
3. **Site:** Aplicação focada exclusivamente no front-end ou landing page.

---
*Gerado automaticamente pelo assistente de IA Antigravity em 2026.*
"""

total_proj = len(projects_data)
total_read = sum(1 for p in projects_data if p["has_readme"] == "Sim")
total_ai_c = sum(1 for p in projects_data if p["has_ai_config"] == "Sim")

report_content = report_content.format(
    total_projetos=total_proj,
    total_readme=total_read,
    pct_readme=(total_read / total_proj * 100) if total_proj > 0 else 0,
    total_ai=total_ai_c,
    pct_ai=(total_ai_c / total_proj * 100) if total_proj > 0 else 0
)

with open(report_path, "w", encoding="utf-8") as rf:
    rf.write(report_content)

print(f"Relatório gravado com sucesso em: {report_path}")
print("\n--- PROCESSO DE ORGANIZAÇÃO CONCLUÍDO ---")
