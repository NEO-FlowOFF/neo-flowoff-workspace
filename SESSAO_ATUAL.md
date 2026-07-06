<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->

# QUICKOFF SESSÃO: NEO-FlowOFF (neoflowoff-chat-ui)

```text
========================================
   NEO-FLOWOFF · ESTADO DA SESSÃO
========================================
Data: 2026-07-06
Workspace: neoflowoff-chat-ui
========================================
```

## Workspace Loaded

---

## 1. Git State

```text
| Item | Estado |
|---|---|
| **Branch** | `main` |
| **Upstream** | `origin/main` |
| **Ahead/Behind** | Ahead by 1 |
| **Modificações** | `SESSAO_ATUAL.md`, `neo-sdr-adapter` (untracked), `neoflowoff-chat-ui` (new commits), `pnpm-lock.yaml`, `servicos_neoflowoff_agency.json` |
| **Staged** | Nenhum |
| **Untracked** | Nenhum |
```

---

## 2. What I found

* **Projeto e Arquitetura:** O projeto `neoflowoff-chat-ui` é um Progressive Web App (PWA) de alta performance projetado para atuar como a interface de chat e primeiro ponto de contato conversacional do agente **NEØ:One** (agência NEO FlowOFF).
* **Stack Tecnológica:**
  * **Core / Framework:** [Astro v7.0.6](https://astro.build) rodando com adaptador Node.js (`@astrojs/node`) no runtime `>=22.12.0`, gerenciado via `pnpm@11.9.0`.
  * **Linguagem:** TypeScript (`^5.0.0`) rigorosamente tipado.
  * **Persistência de Dados & Ledger:** PostgreSQL (via pacote `pg` com pool de conexões e event handlers de erro) para armazenamento autoritativo de leads/CRM, e Redis (`ioredis`) para histórico conversacional com janela deslizante (sliding window) e memória de sessão.
  * **Integrações Externas:** Meta Conversions API (CAPI) (`src/lib/meta-capi.ts`), serviço de e-mail transacional/notificação Resend (`src/lib/emails.ts`) e integração com API LLM para completação de texto.
  * **Infraestrutura e Deploy:** Configuração para deploy no Railway (`railway.toml`, `Makefile`) e scripts de verificação de ambiente (`check_env.js`).
* **Arquitetura de Prompt e Atendimento:** O servidor orquestra os pedidos combinando o prompt base (`src/lib/system-prompt.md`), o contexto do ecossistema, os dados de atribuição de campanha (UTMs) e o estado operacional em tempo real do banco de dados antes de enviar as interações à LLM.

---

## 3. Documentation state

* **`README.md`:** Presente na raiz. Apresenta o diagrama arquitetural em formato gráfico (`graph TD`), política de segurança (Headers HSTS, CSP, Cloudflare AI Labyrinth, Robots.txt) e SEO. O arquivo está coerente com a stack real do projeto, com uma única observação menor: o cabeçalho do README indica `Version: v1.2.0`, enquanto o `package.json` já está na versão `1.2.1`.
* **`docs/SETUP.md`:** Presente no diretório `docs/`. O `README.md` direciona corretamente para este arquivo para orientações de setup, variáveis de ambiente e comandos de desenvolvimento.
* **`docs/SVG.md`:** Presente em `docs/`. Define o padrão e o uso de diagramas visuais e SVGs na documentação e no repositório.
* **`docs/MARKDOWN_STYLE_GUIDE.md`:** Presente em `docs/`. Define a padronização obrigatória e sintaxe para todas as documentações Markdown do repositório.
* **`CODEX.md` / `AGENTS.md` / `CLAUDE.md`:** Presentes no repositório (tanto na raiz quanto na pasta `agents/`), definindo a hierarquia da verdade, regras do NEØ Protocol (FlowOFF) e procedimentos de debugging e segurança.

---

## 4. O Que Entendi (Core Objective & Backend Authority)

* **Objetivo do Sistema:** Operar a interface conversacional autônoma do agente **NEØ:One**, entregando uma experiência consultiva humanizada que qualifica leads e executa o handoff comercial sem burocracia.
* **Princípio Core "Backend Authority beats interface assumptions":**
  * As modificações implementadas em `src/lib/leads.ts` e `src/pages/api/chat.ts` consolidam essa diretriz de segurança e conversão.
  * O servidor de chat (`chat.ts`) consulta o banco de dados operacional (PostgreSQL) a cada turno antes de enviar o histórico à LLM. 
  * Se o banco reportar que o lead já possui Nome, Telefone, Intenção Comercial (POI) ou se demonstra urgência, a IA é programaticamente proibida de repetir perguntas investigativas ("chatbot burro"), partindo diretamente para a coleta do dado restante ou liberação do link de handoff.
* **Protocolo de Captura Fluida de Contatos:**
  * Sob pressa ou detecção de intenção comercial (POI), o comercial exige apenas **Nome + WhatsApp** para iniciar o atendimento humano.
  * Caso falte algum dado, o LLM solicita o contato faltante de maneira hiper-humanizada em uma única frase e sem usar formatos rígidos de formulários (bullets ou listas). O e-mail é tratado estritamente como bônus (opcional) para o remarketing da Meta.

---

## 5. Current State

* **Implementado & Funcional:** PWA Astro configurado, controle de histórico de mensagens via Redis com janela deslizante de 10 interações, persistência de leads no PostgreSQL com proteção contra quedas de conexão, rastreamento via Meta CAPI e notificações de handoff pelo Resend.
* **Parcialmente Implementado / Em Validação (Local):** A injeção em tempo real de `LeadOperationalState` no prompt de sistema da rota `POST /api/chat` foi escrita localmente nos arquivos alterados, mas ainda não foi comitada nem submetida aos testes e lints de validação final.
* **Outdated (Desatualizado):** Pequena divergência textual na string de versão no `README.md` (`v1.2.0` vs `v1.2.1` no `package.json`).
* **Broken ou Dead Code (Quebrado/Morto):** Nenhum código quebrado ou inativo identificado na inspeção preliminar do fluxo principal.

---

## 6. Regras e Constraints Relevantes (AGENTS.md & README.md)

1. **Hierarchy of Truth:** *Runtime beats documentation. State beats narrative. Backend authority beats interface assumptions.* O comportamento e as respostas do chat devem derivar estritamente dos estados confirmados no banco de dados e ledger.
2. **NEØ Protocol (Zero-Invention & Fluid Capture):** É terminantemente proibido inventar dados, expor seletores técnicos, usar listas burocráticas numeradas no chat ("1. Nome: 2. Telefone:") ou criar barreiras quando o cliente demonstra pressa/urgência ou intenção comercial declarada (POI detectado).
3. **Current Documentation Rule:** Para qualquer alteração em bibliotecas (Astro, Prisma/pg, Tailwind, Resend, Vercel/Railway), deve-se validar a sintaxe nas documentações oficiais atualizadas antes da edição.
4. **Segurança e Tratamento de Erros:** Nunca expor credenciais, senhas, chaves de API ou variáveis do `.env` no front-end ou em logs de chat. Proibido usar blocos `catch` silenciosos sem log estruturado e fallback seguro.
5. **Estilo de Modificação e Documentação:** Modificações devem ser cirúrgicas, pequenas e reversíveis. Todo arquivo Markdown editado ou criado deve seguir o `MARKDOWN_STYLE_GUIDE.md` e o `SVG.md`.

---

## 7. Riscos e Pontos de Falha

1. **Latência de Banco no Request do Chat (`POST /api/chat`):** A função `getLeadBySessionId(sessionId)` faz uma query síncrona no pool do PostgreSQL em todo request em que houver um `sessionId`. Embora esteja protegida por um `try/catch` (evitando erro 500 no chat caso o banco caia ou demore), uma degradação na performance do banco pode impactar o tempo total de resposta (TTFB) percebido pelo usuário.
2. **Sincronia entre Sessões (Redis vs PostgreSQL):** Em cenários de alta concorrência ou falha temporária de rede, se o upsert do lead no PostgreSQL não tiver concluído quando a próxima mensagem chegar, o estado lido por `getLeadBySessionId` pode estar momentaneamente desatualizado, exigindo que o prompt lide com fluidez sem contradições.
3. **Limites de Provedores Externos (Resend & Meta CAPI):** Qualquer alteração no fluxo de qualificação e handoff deve garantir que falhas externas (ex: erro 422 na API do Resend) não interrompam a experiência conversacional no cliente.
4. **Logs e PII (Dados Pessoais):** Deve-se garantir que mensagens de erro ou logs de depuração não imprimam dados pessoais sensíveis de clientes (e-mails, telefones completos) em locais não seguros.

---

## 8. Plano de Validação e Handoff

1. **Correção de Divergência de Versão**: Atualizar o `README.md` do chat para constar a versão `v1.2.1` (sincronizado com o `package.json`).
2. **Execução de Lints e Builds**:
   - Rodar validação estática no subprojeto `neoflowoff-chat-ui` e certificar integridade.
3. **Commit e Handoff no Git**:
   - Subir os ponteiros atualizados no repositório pai após a validação.
