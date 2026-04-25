<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->

# NEOFLW  

```text
========================================
   NEO-FLOWOFF · CHILD · neoflw-token-page
========================================
Status: ACTIVE
Type: child repository (product)
Workspace: NEO-FlowOFF
Updated: 2026-04-18
========================================
```

> **Local:** `/Users/nettomello/neomello/NEO-FlowOFF/neoflw-token-page`
> **Remote:** `https://github.com/NEO-FlowOFF/neoflw-token-page.git`
> **Coordination contract:** segue `WORKSPACE_MODEL.md` deste workspace.

────────────────────────────────────────

## ⟠ Objetivo

Fingerprint canônico do child repository `neoflw-token-page`
para consumo pelo workspace NEO-FlowOFF e pelo orchestrator.

Este arquivo é coordination, não product.
Source-of-truth executável vive no próprio repo:
`neoflw-token-page/AGENTS.md` + `CHANGELOG.md`.

────────────────────────────────────────

## ⨷ Identidade

```text
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ ITEM            VALOR
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ Tipo            landing page + mint app (estática)
┃ Framework       Astro 5 (output: 'static')
┃ Islands         React 19 (apenas em src/components/web3/)
┃ Web3            OnchainKit + Wagmi v2 + Viem
┃ Wallets         Coinbase Smart Wallet + injected ('all')
┃ Gas             CDP Paymaster (gasless mint)
┃ Chain           Base Mainnet (8453)
┃ Contract        0x41F4ff3d45DED9C1332e4908F637B75fe83F5d6B
┃ Deploy          Vercel (4 páginas estáticas)
┃ i18n            EN (default) + PT-BR (rotas /pt)
┃ Analytics       Turso (libsql) via /api/track
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

────────────────────────────────────────

## ⧉ Arquivos Canônicos no Child

```text
neoflw-token-page/
├── AGENTS.md            contexto operacional p/ agentes
├── CHANGELOG.md         histórico cronológico de sessões
├── README.md            entry point público (badges, quick start)
├── DEPLOYMENT.md        deploy Vercel + ENS
├── BASE_BUILD_INFO.md   info Builder Rewards
├── NEXTSTEPS.md         backlog operacional do agente
├── .env.example         template completo
├── .agents/skills/      skills locais (gitignored)
└── .vscode/settings.json  webhint OFF p/ JSX
```

────────────────────────────────────────

## ⨂ Skills Ativas no Child

Instaladas via `npx skills` em `.agents/skills/` (symlinks).
Lidas por todos agentes (Cursor, Claude Code, Codex, Gemini, Copilot).

```text
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ SKILL                          ORIGEM         CATEGORIA
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ astro                          astrolicious   framework
┃ vercel-react-best-practices    vercel-labs    framework
┃ setup-solidity-contracts       openzeppelin   contract
┃ adding-builder-codes           base/skills    onchain ops
┃ building-with-base-account     base/skills    wallet
┃ deploying-contracts-on-base    base/skills    deploy
┃ migrating-an-onchainkit-app    base/skills    integration
┃ registering-agent-base-dev     base/skills    onchain ops
┃ skill-creator                  base/skills    meta
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Padrão de governance segue:
[../../../docs/AGENT_SKILLS_REGISTRY.md](../../../../docs/AGENT_SKILLS_REGISTRY.md)
(global do workspace `~/neomello`).

────────────────────────────────────────

## ⧇ Integração com NEO-FlowOFF

Posição no manifest:

```text
manifests/repos.json
└─ id: "neoflw-token-page"
   localPath: ./neoflw-token-page
   remote: github.com/NEO-FlowOFF/neoflw-token-page
```

Posição no orchestrator:

```text
NEO-PROTOCOL/neobot-orchestrator/
└─ projects/neoflw-token-page/manifest.json
└─ projects/neoflw-token-page/README.md
```

Cross-repo deps:

- contrato canônico: `NEO-FlowOFF/neoflw-token` (sibling repo)
- coordenação ecosystem: `NEO-PROTOCOL/neobot-orchestrator/config/ecosystem.json`

────────────────────────────────────────

## ⧖ Convenções Herdadas

- `MARKDOWN_STYLE_GUIDE.md` (workspace root) — canônico
- `WORKSPACE_MODEL.md` — coordination vs product
- Hard rules do workspace AGENTS.md
- Sem product code no workspace root
- Sem versionar child dirs no coordination repo

────────────────────────────────────────

## ◬ Hard Rules do Child

- Nunca commitar `.env`, `.env.local`, `.npmrc`
- Nunca commitar `.agents/`, `.claude/skills/`
- Nunca trocar `output: 'static'` sem aprovação
- Nunca trocar `coinbaseWallet({ preference: 'all' })`
  para `smartWalletOnly` sem decisão de produto
- Nunca remover `pnpm.overrides` (axios CVE patch)
- Nunca editar contratos sem rodar skill `solidity-security`

────────────────────────────────────────

## ◮ Histórico

Mudanças por sessão: ver `neoflw-token-page/CHANGELOG.md`.
Próximos passos: ver `neoflw-token-page/NEXTSTEPS.md`.

────────────────────────────────────────

## ⍟ Fechamento

```text
▓▓▓ NEO-FLOWOFF · neoflw-token-page
────────────────────────────────────────
Static onchain landing · Base Mainnet
Coordination fingerprint · do not duplicate
────────────────────────────────────────
```
