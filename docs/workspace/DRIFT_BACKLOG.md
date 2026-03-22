<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->

> Handoff de governança derivado dos drifts observados no workspace.
> Este arquivo não substitui a ferramenta real de execução.
> Ele existe para empacotar contexto acionável por repositório.

```text
========================================
      NEO-FLOWOFF · DRIFT BACKLOG
========================================
Status: ACTIVE
Mode: HANDOFF
========================================
```

## ⟠ Objetivo

Transformar sinais de deriva em trabalho executável
por repositório soberano.

O backlog real continua na ferramenta de execução
da organização.

Este documento é pacote de handoff.

────────────────────────────────────────

## ⨷ Contrato

- Cada item abaixo deve existir como issue ou card
  na ferramenta oficial da organização.
- O workspace root registra contexto e padrão.
- A execução de produto ocorre no repo correto.
- Ao concluir um item, atualizar o manifesto
  correspondente no root.

────────────────────────────────────────

## ⧉ Fila Executável

```text
WF-001 | neo-flowoff-pwa | Canonicalizar token path para Base Mainnet
WF-002 | neo-flowoff-pwa | Separar portas locais entre frontend e bot
WF-003 | neo-flowoff-pwa | Remover simulacao silenciosa do cliente FlowPay
WF-004 | neo-flw-landing | Canonicalizar superficie publica de webhook PIX
WF-005 | pro-ia          | Alinhar verdade de deploy entre runtime e docs
WF-006 | neoflw-token    | Publicar manifesto canonico de deploy consumivel
WF-007 | workspace-root  | Sanear path local de neoflw-token-page
```

────────────────────────────────────────

## ◬ Itens

### WF-001 · neo-flowoff-pwa

**Drift**
- config global aponta Base Mainnet
- modulo de token ainda opera com Polygon hardcode

**Ação**
- unificar `config/neo-protocol.config.js`,
  `src/modules/neoflw-token/` e integrações Thirdweb
  sob um contrato canônico de rede
- remover endereços hardcode fora do contrato central

**Saída esperada**
- PWA consome um único manifesto canônico
- endereço Base e chain id 8453 viram fonte única

**Aceite**
- nenhum endereço Polygon permanece como default
- wallet, token UI e integrações usam o mesmo contrato

────────────────────────────────────────

### WF-002 · neo-flowoff-pwa

**Drift**
- frontend Vite e bot WhatsApp usam porta 3000

**Ação**
- reservar portas distintas por superfície local
- documentar convenção no repo e refletir no manifesto

**Saída esperada**
- desenvolvimento local sem colisão de porta

**Aceite**
- frontend sobe isolado
- bot WhatsApp sobe isolado
- docs e manifesto apontam para a convenção final

────────────────────────────────────────

### WF-003 · neo-flowoff-pwa

**Drift**
- cliente FlowPay aponta para API externa
  mas checkout e status ainda são mockados

**Ação**
- integrar endpoints reais
  ou introduzir `mockMode` explícito e visível
- impedir falsa sensação de produção

**Saída esperada**
- contrato de pagamento verificável

**Aceite**
- código diferencia claramente `real` de `mock`
- manifesto deixa de marcar `observed-mock`

────────────────────────────────────────

### WF-004 · neo-flw-landing

**Drift**
- coexistem múltiplas superfícies de webhook PIX

**Ação**
- decidir endpoint canônico externo
- manter compatibilidade apenas se documentada
- normalizar headers, segredos e fluxo de confirmação

**Saída esperada**
- webhook público inequívoco
- contrato de pagamento sem duplicidade ambígua

**Aceite**
- docs e código apontam para a mesma rota canônica
- assinatura e fallback ficam explicitados

────────────────────────────────────────

### WF-005 · pro-ia

**Drift**
- runtime atual aponta Vercel
- documentação e URLs públicas ainda apontam Netlify

**Ação**
- escolher a verdade operacional
- alinhar `README`, docs, links públicos e deploy config

**Saída esperada**
- uma única narrativa de deploy

**Aceite**
- docs, domínio principal e plataforma configurada convergem
- manifesto deixa de registrar `deploy-drift`

────────────────────────────────────────

### WF-006 · neoflw-token

**Drift**
- consumidores dependem de contratos e redes
  mas não existe artefato canônico simples para consumo

**Ação**
- publicar manifesto de deploy com rede,
  chain id, token, vault, claim e status por ambiente
- versionar esse artefato no repo soberano do token

**Saída esperada**
- PWA, miniapp e microsite leem a mesma fonte

**Aceite**
- artefato de deploy existe e é referenciado
- consumidores substituem hardcodes dispersos

────────────────────────────────────────

### WF-007 · workspace-root

**Drift**
- diretório local `neoflw-token-page ` possui espaço final

**Ação**
- planejar renomeação segura do diretório local
- atualizar manifesto, scripts e referências do root

**Saída esperada**
- higiene operacional do workspace

**Aceite**
- path local saneado
- `workspace-doctor` e `.gitignore` seguem válidos

────────────────────────────────────────

## ⍟ Handoff

**Destino recomendado**
- backlog oficial da organização
- roadmap unificado em [roadmaps/neo-flowoff-unified-roadmap-2026.md](/Users/nettomello/neomello/NEO-FlowOFF/roadmaps/neo-flowoff-unified-roadmap-2026.md)

**Ritmo de governança**
- abrir item no backlog real
- executar no repo soberano
- refletir mudança no manifesto do workspace
