<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->

# QUICKOFF SESSÃO: NEO-FlowOFF

```text
========================================
   NEO-FLOWOFF · ESTADO DA SESSÃO
========================================
Data: 2026-06-14
Workspace: Control Plane (neo-flowoff-workspace)
========================================
```

## Workspace Loaded

---

## 1. Git State

| Item | Estado |
|---|---|
| **Branch** | `main` |
| **Upstream** | `origin/main` |
| **Ahead/Behind** | **Ahead by 3** / Behind 0 (3 commits locais não pushados) |
| **Modificações** | `neo-sdr-adapter` (M) e `neo-flowoff-agency` (m) |
| **Staged** | Nenhum |
| **Untracked** | Nenhum reportado no root |
| **Merge/rebase** | Nenhum |

**⚠️ Atenção:** O branch está com 3 commits na frente do remote. Além disso, há modificações listadas em `neo-sdr-adapter` e `neo-flowoff-agency` — como são repositórios filhos/gitlinks, isso indica que os ponteiros locais de commit mudaram ou há trabalho sujo dentro deles.

---

## 2. O Que Encontrei

O diretório `/Users/nettomello/neomello/NEO-FlowOFF` é o **workspace root de coordenação** (control plane) da organização `NEO-FlowOFF`.

Ele **não é um monorepo de produto**. Ele hospeda 8 repositórios soberanos como subdiretórios (ex: `ceo-escalavel-miniapp`, `neo-flw-landing`, `neo-flowoff-pwa`), além de diretórios de coordenação (`manifests/`, `docs/`, `scripts/`, `roadmaps/`).
A stack de scripts de coordenação usa Python 3.

---

## 3. Estado da Documentação

| Arquivo | Status |
|---|---|
| **README.md** | ✅ Existe e está perfeitamente coerente com o paradigma de Control Plane. |
| **AGENTS.md** | ✅ Existe, é rigoroso e define claramente as fronteiras (Root = coordenação, Filhos = produto). |
| **MARKDOWN_STYLE_GUIDE.md** | ✅ Existe (`markdown_style_guide.md` em minúsculas). |
| **docs/workspace/** | ✅ Existe e contém a topologia e modelo (`WORKSPACE_TOPOLOGY.md`, etc). |
| **SVG.md / CODEX.md / CLAUDE.md** | ❌ Não existem na raiz (não obrigatórios pelo README atual). |

---

## 4. O Que Entendi

Este workspace funciona como um "mapa" e "orquestrador estrutural" para a organização NEO-FlowOFF. O objetivo principal deste repositório raiz é gerenciar manifests (`workspace.json`, `repos.json`), topologias, integrações e scripts de diagnóstico transversais.

Se a tarefa for mexer em regras de negócio ou frontend, devo descer para o repositório filho correto. Se for mapear uma nova arquitetura, atualizar padrões, ou criar scripts cross-repo, trabalho aqui na raiz.

---

## 5. Current State

- **Já implementado:** Todo o sistema de manifests e topologia está funcional. O script de topologia documenta 8 repos e 13 integrações ativas.
- **Drifts mapeados (Broken/Unclear):** O `WORKSPACE_TOPOLOGY.md` reporta pendências estruturais ("gitlinks-without-gitmodules" em `neo-flowoff-agency` e `neoflowoff-chat-ui`) e inconsistências de documentação ("prompts removidos ainda citados" em `neoflow-content-machine`).

---

## 6. Regras e Constraints Relevantes (AGENTS.md & README.md)

1. **Root coordena, filhos executam.** Nenhuma mudança de código de produto deve ocorrer na raiz.
2. **Sem vazamento de código.** Nunca mover código de um repo filho para a raiz do workspace.
3. **Scripts root = Python 3.** Não usar `npm` ou `node` para ferramentas de coordenação do workspace.
4. **Git Routing:** Se o trabalho envolver um repo filho, devo entrar na pasta dele para operar.

---

## 7. Riscos e Pontos de Falha

| Risco                                   | Severidade | Notas |
|---                                      | ---|---|
| Commits root não pushados               | 🟡 Médio | `main` tem 3 commits na frente. Pode causar descompasso se houver colaboração externa. |
| Submódulos sujos / desatualizados       | 🟡 Médio | `neo-sdr-adapter` e `neo-flowoff-agency` mostram modificações. Fazer commit na raiz sem pushar/sanitizar os filhos pode quebrar referências no remote. |
| Gitlinks vs Gitmodules                  | 🟢 Baixo | A topologia aponta que faltam `.gitmodules` formais para alguns repositórios (estão apenas como pastas ignoradas ou gitlinks frouxos). |

---

## 8. Assumptions

- Assumo que os 3 commits locais em `main` são seus e estão prontos para push, ou você está ciente deles.
- Assumo que as alterações marcadas em `neo-sdr-adapter` indicam trabalho ativo dentro daquele repositório.

---

## 9. Perguntas antes da Execução

1. **Qual é o alvo da sessão de hoje?** Estamos fazendo manutenção no Control Plane (ex: corrigindo os gitlinks/drifts) ou vamos atuar dentro de algum dos repositórios filhos (ex: `neo-flowoff-pwa` ou `neo-flw-landing`)?

---

## 10. Plano Proposto

**Metas Imediatas Definidas:**
1. **Refatoração Frontend:** Alterar completamente o frontend de `https://lp.neoflowoff.agency/` (repositório soberano `neo-flw-landing`).
2. **Correção de Rota/Deploy:** Corrigir `https://agente.neoflowoff.agency/` que atualmente não leva para lugar nenhum (repositório soberano `ceo-escalavel-miniapp`).

**Possíveis caminhos de coordenação:**
- Consertar os gitlinks apontados no Drift Backlog, atualizar topologia e fazer o push dos 3 commits retidos na raiz.

---

## 11. Arquivos que devem ser tocados

- Repositório `neo-flw-landing` (arquivos de interface / UI).
- Repositório `ceo-escalavel-miniapp` (roteamento, config de deploy ou código do mini-app).

---

## 12. Waiting for approval

I will not change files until you approve the plan.
