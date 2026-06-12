<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->
#
> Documento gerado a partir dos manifests do workspace.
> Fonte: `manifests/repos.json`, `manifests/integrations.json`
> e `manifests/workspace.json`.

```text
========================================
    NEO-FLOWOFF · WORKSPACE TOPOLOGY
========================================
Status: GENERATED
Schema: 2026-03-22
========================================
```

## ⟠ Objetivo

Mapear a topologia real do workspace
a partir dos manifests canonicos.

────────────────────────────────────────

## ⨷ Resumo

```text
workspace  | neo-flowoff-workspace
org        | NEO-FlowOFF
mode       | control-plane
repos      | 8
integracoes| 13
guia-md    | ./MARKDOWN_STYLE_GUIDE.md
```

────────────────────────────────────────

## ⧉ Repos

```text
repo                    | deploy                         | local | public
------------------------|--------------------------------|-------|------------------------------
ceo-escalavel-miniapp   | vercel                         | 4173  | agente.neoflowoff.agency
flow-links-bio          | cloudflare-pages-inferred      | -     | flow-links-bio.pages.dev +1
neo-flowoff-pwa         | unpublished-static-pwa         | 3000  | -
neo-flw-landing         | vercel                         | -     | neoflowoff.agency +2
neo-landing-open        | vercel-inferred                | -     | neo-landing-open.vercel.app
neoflow-content-machine | fly-io                         | 3001  | -
neoflw-token-page       | vercel                         | -     | neoflowoff.eth.limo +2
pro-ia                  | vercel / netlify-docs-still-pr | 3001  | proia.netlify.app +1
```

────────────────────────────────────────

## ◬ Papéis

```text
ceo-escalavel-miniapp | miniapp de aquisicao, referral, wallet utility e monetizacao Telegram
flow-links-bio | hub publico de distribuicao e roteamento para propriedades do ecossistema
neo-flowoff-pwa | pwa principal com wallet, mcp-router, identidade e modulos de operacao
neo-flw-landing | landing principal com proxy de pagamento, webhooks e tracking server-side
neo-landing-open | landing publica aberta com captura de leads e prova de stack
neoflow-content-machine | engine de criacao, aprovacao, assets e distribuicao multicanal
neoflw-token-page | microsite soberano do token com presenca ENS e links on-chain
pro-ia | produto de monetizacao com checkout PIX, leads e area protegida
```

────────────────────────────────────────

## ⧇ Webhooks

```text
ceo-escalavel-miniapp | /api/webhook
neo-flowoff-pwa | /webhook, /api/webhook/instagram
neo-flw-landing | /api/payment-webhook, /api/webhook
pro-ia | /api/webhook
```

────────────────────────────────────────

## ◯ Integrações

```text
token-base-canonical-to-miniapp | observed | workspace-root -> ceo-escalavel-miniapp
token-canonical-path-to-pwa | partially-aligned | workspace-root -> neo-flowoff-pwa
flow-links-routing-to-owned-surfaces | observed | flow-links-bio -> neo-flw-landing,neoflw-token-page
landing-flowpay-charge-proxy | observed | neo-flw-landing -> FlowPay
landing-payment-webhook-confirmation | observed | FlowPay or Woovi -> neo-flw-landing
landing-meta-tracking-stack | observed | neo-flw-landing -> Meta Ads stack
proia-payment-webhook-and-lead-upsert | observed | FlowPay or Woovi -> pro-ia
miniapp-telegram-bot-and-stars | observed | ceo-escalavel-miniapp -> Telegram Bot API
pwa-whatsapp-bot-webhook | observed | Meta WhatsApp Cloud API -> neo-flowoff-pwa
pwa-flowpay-client | observed-mock | neo-flowoff-pwa -> FlowPay
content-machine-distribution-channels | observed | neoflow-content-machine -> Instagram,LinkedIn,Farcaster,IPFS
content-launch-assets-to-landing | roadmap-mapped | neoflow-content-machine -> neo-flw-landing
landing-open-lead-capture | observed | neo-landing-open -> Web3Forms
```

────────────────────────────────────────

## ⍟ Drifts

```text
token-canonical-path-to-pwa | partially-aligned | Frontend publico e token client ja convergem para Base, mas ainda existem configuracoes e docs legadas com Polygon no repo.
pwa-flowpay-client | observed-mock | Cliente aponta para FlowPay, mas fluxo de checkout e status ainda esta simulado no codigo.
neo-flowoff-pwa | port-collision | Portas locais duplicadas entre superficies do mesmo repo.
pro-ia | deploy-drift | Documentacao ou superficie publica ainda aponta legado.
```

────────────────────────────────────────

## ⨀ Governança Local

```text
approved-on-2026-06-01 | root-pnpm-control-plane | legitimo
approved-on-2026-06-01 | child-repo-npmrc-store-dir | legitimo
pending-structural     | root-gitlinks-without-gitmodules | neo-flowoff-agency, neoflowoff-chat-ui
pending-doc-consistency| neoflow-content-machine | prompts removidos ainda citados na documentacao
```

────────────────────────────────────────

## ◯ Geração

```bash
python3 scripts/generate-workspace-topology \
  > docs/workspace/WORKSPACE_TOPOLOGY.md
```
