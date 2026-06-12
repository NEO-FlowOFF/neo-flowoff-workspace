# Handoff — Remediação de vulnerabilidades (pnpm audit) no monorepo NEO-FlowOFF

> Prompt para delegar a um agent dev. Auto-contido: contém todo o contexto necessário.

## Contexto

Monorepo pnpm (raiz: `/Users/nettomello/neomello/NEO-FlowOFF`, pnpm 10.33, branch `main`),
com 11 pacotes em `pnpm-workspace.yaml`.

Acabou de ser corrigido um bug de governança (commit `767233a`): o pnpm 10.33 parou de ler
o campo `pnpm` do `package.json`, então as `overrides` de segurança estavam sendo ignoradas.
Elas foram migradas para `pnpm-workspace.yaml` (chaves `overrides` + `onlyBuiltDependencies`).
**Os overrides já cobrem** estas transitivas: `path-to-regexp`, `undici`, `axios`, `lodash`,
`brace-expansion`, `picomatch`, `tar`, `ajv`, `minimatch`, `rollup`, `vite`, `yaml`,
`socket.io-parser`, `flatted`. NÃO mexer nesses — já estão pinados.

O `pnpm audit` ainda reporta **34 vulnerabilidades** (7 low / 17 moderate / 10 high). Todas
são **dependências diretas** dos apps abaixo — não dá para resolver por override transitivo;
exigem upgrade real da versão da dependência direta. **O app `neoflowoff-chat-ui` está limpo**
(nenhuma vuln) e NÃO deve ser tocado neste trabalho.

## Tarefa

Para cada app abaixo, subir as dependências diretas indicadas até a versão corrigida (ou
acima), rodar `pnpm install` na raiz, validar que o app builda/checa, e confirmar com
`pnpm audit` que a vuln saiu. Trabalhar **um app por vez**, em branch separada, commitando por app.
Priorizar `high` → `moderate` → `low`. Onde houver breaking change de major (ex.: `next`,
`astro`, `vercel`), ler o changelog/migração antes e sinalizar regressões em vez de forçar.

### pro-ia  ⚠️ prioridade máxima (14 vulns, quase todas em `next`)

- [high/moderate/low] `next` (atual `>=12.x–15.4.x` → **`>=15.5.18`**) — múltiplos: DoS,
  SSRF em App Router, middleware/proxy bypass (App+Pages Router), XSS, cache poisoning,
  Image Optimization DoS. Subir para `next@>=15.5.18` resolve TODOS de uma vez.
  ⚠️ Possível breaking change (12/13/14 → 15). Validar build + rotas + middleware.
- [moderate] `postcss` (`<8.5.10` → **`>=8.5.10`**) — XSS via `</style>` não escapado.
  Costuma vir transitivo do next; pode resolver junto após o upgrade do next.

### neoflw-token  (7 vulns — tooling Hardhat/blockchain, dev-only mas corrigir)

- [high] `serialize-javascript` (`<=7.0.2` → **`>=7.0.5`**) — RCE via `RegExp.flags` + CPU DoS.
- [high] `tmp` (`<0.2.6` → **`>=0.2.6`**) — path traversal via prefix/postfix.
- [moderate] `bn.js` (`<4.12.3` → **`>=4.12.3`**) — loop infinito.
- [low] `cookie` (`<0.7.0` → **`>=0.7.0`**).
- Cadeia via `hardhat`/`solc`/`@nomicfoundation/hardhat-*`. Se forem transitivas presas a
  versões antigas do hardhat, considerar bump do hardhat ou `overrides` no `pnpm-workspace.yaml`
  (seguir o padrão de overrides já existente).

### neo-flw-landing  (4 vulns — Vercel CLI)

- [moderate] `vercel` (`>=50.16.0 <=52.0.0` → **`>=52.0.1`**) — args expostos em modo não-interativo.
- [moderate] `smol-toml` (`<1.6.1` → **`>=1.6.1`**) — DoS (transitivo de `vercel`).
- [moderate] `srvx` (`<0.11.13` → **`>=0.11.13`**) — middleware bypass via URL absoluta (transitivo de `vercel`).
- [low] `@tootallnate/once` (`<2.0.1` → **`>=2.0.1`**) (transitivo de `vercel`).
- Subir `vercel` para `>=52.0.1` deve arrastar as 3 transitivas. Se não, adicionar overrides.

### neo-landing-open  (2 vulns — Astro)

- [moderate] `astro` (`<6.1.6` → **`>=6.1.10`**) — XSS em `define:vars`.
- [low] `astro` (`<6.1.10` → **`>=6.1.10`**) — server island encrypted params.
- Subir `astro@>=6.1.10` resolve ambas.

### neo-flowoff-pwa  (2 vulns)

- [high] `ws` (`>=8.0.0 <8.17.1` → **`>=8.20.1`**) — DoS (transitivo de `@ceramicnetwork/http-*`).
- [low] `elliptic` (`<=6.6.1`) — sem patch upstream ainda; documentar como risco aceito/monitorar.
- `ws` é transitivo de ceramic; se preso, adicionar `overrides: { ws: '^8.20.1' }` no workspace.

### ceo-escalavel-miniapp  (1 vuln)

- [moderate] `ws` (`>=8.0.0 <8.20.1` → **`>=8.20.1`**) — uninitialized memory disclosure
  (transitivo de `@reown/appkit-adapter-*`). Resolver via override de `ws` se preso.

### neoflw-token-page  (1 vuln)

- [moderate] `uuid` (`<11.1.1` → **`>=11.1.1`**) — buffer bounds check em v3/v5/v6.

## Critério de pronto

- `pnpm audit` na raiz com 0 high e 0 moderate (low residuais só se sem patch upstream, documentados).
- Cada app afetado builda/checa sem regressão.
- Um commit por app, mensagens no padrão `fix(security/<app>): bump <pkg> to <ver>`.
- Não tocar em `neoflowoff-chat-ui` nem nos overrides já existentes no `pnpm-workspace.yaml`.
