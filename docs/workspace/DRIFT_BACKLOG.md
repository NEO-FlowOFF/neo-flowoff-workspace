<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->

#
/ > Handoff de governança derivado dos drifts observados no workspace.
/ > Este arquivo não substitui a ferramenta real de execução.
/ > Ele existe para empacotar contexto acionável por repositório.
/

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
WF-006 | workspace-root  | Publicar e estabilizar manifesto canonico do token Base
WF-008 | workspace-root  | Registrar governanca local do control plane pnpm
```

────────────────────────────────────────

## ◬ Itens

### WF-001 · neo-flowoff-pwa (PARCIALMENTE RESOLVIDO)

**Drift**

- frontend publico e token client ja apontam para Base Mainnet
- configs e docs legadas ainda preservam referencias a Polygon

**Ação**

- unificar `config/neo-protocol.config.js`,
  `src/modules/neoflw-token/` e o manifesto canônico
  `manifests/tokens/base-neoflow.json`
- remover ou arquivar referencias legadas a Polygon
- reescrever docs internas que ainda afirmam Polygon como default

**Saída esperada**

- PWA consome um único manifesto canônico
- endereço Base e chain id 8453 viram fonte única
- nenhuma doc ativa contradiz a camada publica atual

**Aceite*
- wallet, token UI e token client usam o mesmo contrato Base
- nenhum documento operacional do repo afirma Polygon como verdade corrente
- configs legadas ficam claramente marcadas como históricas ou são removidas

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

**Drift*
- coexistem múltiplas superfícies de webhook PIX

**Ação*
- decidir endpoint canônico externo
- manter compatibilidade apenas se documentada
- normalizar headers, segredos e fluxo de confirmação

**Saída esperada*
- webhook público inequívoco
- contrato de pagamento sem duplicidade ambígua

**Aceite*
- docs e código apontam para a mesma rota canônica
- assinatura e fallback ficam explicitados

────────────────────────────────────────

### WF-005 · pro-ia

**Drift*
- runtime atual aponta Vercel
- documentação e URLs públicas ainda apontam Netlify

**Ação*
- escolher a verdade operacional
- alinhar `README`, docs, links públicos e deploy config

**Saída esperada*
- uma única narrativa de deploy

**Aceite*
- docs, domínio principal e plataforma configurada convergem
- manifesto deixa de registrar `deploy-drift`

────────────────────────────────────────

### WF-006 · workspace-root (RESOLVIDO)

**Drift*
- o manifesto canônico do token existia,
  mas ainda carregava o contrato antigo no control plane

**Ação*
- manter `manifests/tokens/base-neoflow.json`
  como contrato soberano do token Base
- apontar consumidores para o manifesto do root
- sincronizar o endereço real com `neoflw-token-page`

**Saída esperada**

- workspace-root passa a ser o plano de controle do token
- consumidores leem a mesma verdade canônica

**Aceite**

- manifesto do root aponta para `0x41f4ff3d45ded9c1332e4908f637b75fe83f5d6b`
- miniapp, PWA e microsite convergem para o mesmo endereço

────────────────────────────────────────

### WF-007 · workspace-root (RESOLVIDO)

**Drift*
- diretório local `neoflw-token-page` estava com nome inconsistente em manifests e docs

**Ação*
- normalizar `manifests/repos.json` e referências documentais para `./neoflw-token-page`

**Saída esperada*
- o plano de controle aponta para o path real

**Aceite*
- `manifests/repos.json` usa `./neoflw-token-page`
- `workspace.registry.json` não acusa repo faltando

────────────────────────────────────────

### WF-008 · workspace-root

**Drift*
- o workspace passou a operar com control plane local em `pnpm`
- parte da topologia local aprovada ainda nao esta refletida de forma limpa
  no root

**Ação*
- registrar a camada local `pnpm` como governanca aprovada
- documentar que `neo-flowoff-agency` e `neoflowoff-chat-ui`
  seguem com pendencia estrutural no root
- registrar que `neoflow-content-machine`
  tem inconsistencia entre docs e arquivos removidos

**Saída esperada*
- o root descreve a verdade atual sem romantizar o estado do workspace

**Aceite*
- topologia explicita a aprovacao local de `pnpm`
- pendencias estruturais continuam visiveis
- a documentacao deixa claro o que foi aprovado
  e o que ainda exige correção tecnica

────────────────────────────────────────

## ⍟ Handoff

**Destino recomendado*
- backlog oficial da organização
- roadmap unificado em [roadmaps/neo-flowoff-unified-roadmap-2026.md](/Users/nettomello/neomello/NEO-FlowOFF/roadmaps/neo-flowoff-unified-roadmap-2026.md)

**Ritmo de governança*
- abrir item no backlog real
- executar no repo soberano
- refletir mudança no manifesto do workspace
