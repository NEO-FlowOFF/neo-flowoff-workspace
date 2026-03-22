<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->

> Coordination root for the `NEO-FlowOFF` organization.
> This workspace versions control plane artifacts,
> not product source code.

```text
========================================
      NEO-FLOWOFF · WORKSPACE ROOT
========================================
Status: ACTIVE
Mode: CONTROL PLANE
Repo: neo-flowoff-workspace
========================================
```

## ⟠ Objetivo

Transformar `NEO-FlowOFF` em um workspace organizacional
multi-repo com fronteiras explícitas.

O root coordena.
Os filhos executam produto.

────────────────────────────────────────

## ⨷ Contrato

- O workspace root versiona coordenação.
- Os repositórios filhos versionam produto.
- O root não captura código dos filhos.
- Mudança de produto ocorre no repo soberano correto.
- Mudança de topologia, padrão ou automação cross-repo
  ocorre aqui.

────────────────────────────────────────

## ⧉ Estrutura

```text
NEO-FlowOFF/
├── AGENTS.md
├── MARKDOWN_STYLE_GUIDE.md
├── README.md
├── .gitignore
├── manifests/
│   ├── integrations.json
│   ├── repos.json
│   └── workspace.json
├── docs/
│   └── workspace/
│       ├── DRIFT_BACKLOG.md
│       ├── WORKSPACE_MODEL.md
│       └── WORKSPACE_TOPOLOGY.md
├── roadmaps/
│   ├── neo-flowoff-unified-roadmap-2026.csv
│   └── neo-flowoff-unified-roadmap-2026.md
└── scripts/
    ├── generate-workspace-topology
    └── workspace-doctor
```

────────────────────────────────────────

## ⧇ Repositórios Soberanos

```text
ceo-escalavel-miniapp
flow-links-bio
neo-flowoff-pwa
neo-flw-landing
neo-landing-open
neoflow-content-machine
neoflw-token
neoflw-token-page
pro-ia
```

> Observação:
> `neoflw-token-page ` possui espaço ao fim do nome local.
> O manifesto preserva esse literal até uma renomeação planejada.

────────────────────────────────────────

## ◬ Fonte Canônica

Se existir `MARKDOWN_STYLE_GUIDE.md` no workspace root,
ele é a fonte obrigatória para documentação estrutural
e transversal deste ecossistema.

O guia canônico local está em:

- [MARKDOWN_STYLE_GUIDE.md](/Users/nettomello/neomello/NEO-FlowOFF/MARKDOWN_STYLE_GUIDE.md)

────────────────────────────────────────

## ⍟ Operação

**Começar aqui:**

- [manifests/workspace.json](/Users/nettomello/neomello/NEO-FlowOFF/manifests/workspace.json)
- [manifests/repos.json](/Users/nettomello/neomello/NEO-FlowOFF/manifests/repos.json)
- [manifests/integrations.json](/Users/nettomello/neomello/NEO-FlowOFF/manifests/integrations.json)
- [docs/workspace/WORKSPACE_MODEL.md](/Users/nettomello/neomello/NEO-FlowOFF/docs/workspace/WORKSPACE_MODEL.md)
- [docs/workspace/WORKSPACE_TOPOLOGY.md](/Users/nettomello/neomello/NEO-FlowOFF/docs/workspace/WORKSPACE_TOPOLOGY.md)
- [docs/workspace/DRIFT_BACKLOG.md](/Users/nettomello/neomello/NEO-FlowOFF/docs/workspace/DRIFT_BACKLOG.md)

**Diagnóstico:**

```bash
python3 scripts/workspace-doctor
python3 scripts/generate-workspace-topology \
  > docs/workspace/WORKSPACE_TOPOLOGY.md
```
