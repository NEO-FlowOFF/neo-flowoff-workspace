<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->
#
/> Modelo estrutural do workspace organizacional `NEO-FlowOFF`.
/> Este documento descreve fronteiras, responsabilidades
/> e o contrato de operacao do control plane.

```text
========================================
     NEO-FLOWOFF · WORKSPACE MODEL
========================================
Status: ACTIVE
Version: v1.0.0
========================================
```

## ⟠ Objetivo

Definir `NEO-FlowOFF` como um workspace organizacional
multi-repo com plano de controle explícito.

O root coordena.
Os filhos entregam produto.

────────────────────────────────────────

## ⨷ Princípio Central

- O workspace root versiona coordenação.
- Os repositórios filhos versionam produto.
- O root não é monorepo de produto.
- O root não deve capturar código dos filhos.
- O root funciona como control plane da organização.
- O workspace pode ser descoberto pelo control-plane pessoal
  `neomello-control-plane`, mas mantém soberania própria.

────────────────────────────────────────

## ⧉ Fronteiras

**Workspace root:**

- manifests de repositórios
- manifests de integrações
- padrões operacionais
- documentação transversal
- scripts de bootstrap
- scripts de diagnóstico
- mapas de ambientes, portas, domínios e dependências
  quando fizer sentido

**Repos filhos:**

- source code
- runtime
- testes
- dependências de produto
- documentação específica
- histórico soberano de entrega

────────────────────────────────────────

## ◬ Regras Duras

- Nunca tratar a pasta agregadora como pseudo-monorepo.
- Nunca mover código dos filhos para o root.
- Nunca versionar diretórios dos filhos no repo-raiz.
- Nunca criar backlog paralelo desconectado da execução.
- Toda mudança de produto ocorre no repo filho correto.
- Toda mudança de topologia, coordenação, padrão ou
  automação cross-repo ocorre no root.

────────────────────────────────────────

## ⧇ Estrutura Mínima

```text
NEO-FlowOFF/
├── AGENTS.md
├── MARKDOWN_STYLE_GUIDE.md
├── README.md
├── .gitignore
├── manifests/
│   ├── repos.json
│   ├── integrations.json
│   ├── tokens/
│   │   └── base-neoflow.json
│   └── workspace.json
├── docs/
│   └── workspace/
│       ├── DRIFT_BACKLOG.md
│       ├── WORKSPACE_MODEL.md
│       └── WORKSPACE_TOPOLOGY.md
├── roadmaps/
└── scripts/
    ├── generate-workspace-topology
    └── workspace-doctor
```

────────────────────────────────────────

## ⍟ Contrato de Operação

1. Descobrir primeiro se a tarefa pertence ao workspace root
   ou a um repositório filho.
2. Se for coordenação, operar no workspace root.
3. Se for produto, operar no repositório filho correto.
4. Se tocar vários repositórios, registrar contexto e padrão
   no root e aplicar mudanças de produto em cada repo soberano.
5. Nunca confundir control plane com camada de execução.
6. Relações transversais com outras organizações podem ser
   registradas em `/Users/nettomello/neomello`, sem mover código
   nem substituir os manifests deste workspace.

────────────────────────────────────────

## ◯ Manifestos

**`manifests/repos.json`**

- nome do repo
- path local
- remoto
- papel no ecossistema

**`manifests/integrations.json`**

- integração cross-repo
- produtor
- consumidor
- contrato
- evidência

**`manifests/workspace.json`**

- nome do workspace
- organização
- modo operacional
- o que rastreia
- o que não rastreia

────────────────────────────────────────

## ⨀ Documentação

Se existir `MARKDOWN_STYLE_GUIDE.md` no root,
ele é fonte canônica obrigatória para documentos
estruturais deste ecossistema.

Documentação estratégica deve traduzir
execução real.
Não deve inventar segunda realidade.
