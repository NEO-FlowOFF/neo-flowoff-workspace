---

# MISSÃO DA SEMANA
# OPERAÇÃO TRAÇÃO V1

ALVO: Agent Dev
AUTOR: NEØ MELLØ
STATUS: CRÍTICO
FOCO: COMERCIALIZAÇÃO, CAPTURA E RECEITA IMEDIATA

---

# A fase de provar que conseguimos construir acabou

Nesta semana, o objetivo é colocar a operação comercial da neoflowoff.agency em circulação, conectar as superfícies de entrada ao pipeline real de leads e usar a própria infraestrutura como prova de capacidade técnica.

> **Regra de Ouro:** nenhuma linha de código será escrita se não ajudar a capturar um lead, qualificá-lo, encaminhá-lo ao comercial, registrar uma conversão ou processar um pagamento.

---

## 1. OBJETIVO DA MISSÃO

Colocar no ar uma operação comercial real capaz de:

1. receber tráfego;
2. iniciar conversas;
3. identificar intenção comercial;
4. capturar dados mínimos do lead;
5. persistir origem, histórico e estágio;
6. acionar handoff humano;
7. registrar conversão via Meta CAPI;
8. entregar leads prontos para proposta.

A missão não é “subir endpoints”.

A missão é fazer uma pessoa atravessar o sistema inteiro e chegar viva ao comercial.

---

## 2. TOPOLOGIA OFICIAL

### `NEO-FlowOFF`

**Local:**  
`/Users/nettomello/neomello/NEO-FlowOFF`

**Papel:**  
Superfícies públicas, coordenação comercial e entrada de leads.

**Serviços considerados nesta missão:**

- `neoflowoff-chat-ui`
- Landing Page SDR
- Landing Page institucional da neoflowoff.agency

---

### `NEO-Growth-System`

**Local:**  
`/Users/nettomello/neomello/neo-growth-system`

**Papel:**  
Control plane de eventos, processamento, integrações, webhooks, filas e conversões.

**Serviços considerados nesta missão:**

- `neo-event-ingestor`
- `neo-queue-worker`
- envio de eventos Meta CAPI
- roteamento de handoff
- persistência e eventos comerciais

---

## 3. DISTRIBUIÇÃO OFICIAL DE PROVIDERS

### 3.1 Agente SDR atual

**Repositório:**  
`NEO-FlowOFF/neoflowoff-chat-ui`

**Status:**  
Produção.

**Infraestrutura atual:**

- Railway
- Postgres HA
- Redis via `REDIS_URL`
- persistência de sessão e histórico
- captura de lead
- Meta CAPI
- UTMs e atribuição
- handoff comercial

**Provider LLM:**  
ASI1.

**Diretriz:**

- não migrar;
- não substituir provider;
- não refatorar a infraestrutura;
- não interromper produção;
- não duplicar o que já funciona.

**Créditos disponíveis:**

- ASI1: `75M`
- ASI1 Ultra: `50M`

O Agente SDR atual continua operando em ASI1.

---

### 3.2 Landing Page SDR

**Status:**  
Em desenvolvimento.

**Componente principal:**  
`src/components/ChatBubble.astro`

**Provider LLM:**  
OpenAI.

**Projeto OpenAI:**

- Project name: `neo-agent-sdr`
- Project ID: `proj_n2nJUMuph5kMFotGAtnN9TGi`
- Project key: criada
- Service Tier: `Priority`
- bônus de compartilhamento: confirmado

**Identificador da superfície:**

```text
surface=sdr_landing
```

**Função:**

- apresentar a oferta SDR;
- iniciar conversa;
- identificar intenção comercial;
- capturar nome e WhatsApp;
- registrar origem;
- encaminhar ao pipeline comercial;
- disparar handoff;
- registrar conversão.

---

### 3.3 Landing Page institucional — neoflowoff.agency

**Status:**  
Planejamento.

**Componente principal:**  
`src/components/ChatBubble.astro`

**Provider LLM:**  
OpenAI.

**Projeto OpenAI:**  
`neo-agent-sdr`

**Identificador da superfície:**

```text
surface=agency_home
```

**Função:**

- apresentar os serviços da agência;
- diagnosticar a necessidade do visitante;
- identificar a frente de interesse;
- capturar contato;
- encaminhar ao mesmo pipeline comercial.

---

## 4. REGRA DE ARQUITETURA PARA AS LANDINGS

`ChatBubble.astro` é somente interface.

A API key da OpenAI nunca deve ser exposta no navegador.

Fluxo obrigatório:

```text
ChatBubble.astro
    ↓
POST /api/chat
    ↓
backend server-side
    ↓
OpenAI
    ↓
lead pipeline
    ↓
Postgres / CAPI / handoff
```

Cada superfície deve enviar:

```json
{
  "surface": "sdr_landing",
  "sessionId": "uuid",
  "messages": [],
  "attribution": {
    "utm_source": null,
    "utm_medium": null,
    "utm_campaign": null,
    "fbclid": null,
    "gclid": null,
    "referrer": null
  }
}
```

A landing institucional deve usar:

```json
{
  "surface": "agency_home"
}
```

---

## 5. POLÍTICA DE CHAVES E SEGREDOS

Utilizar uma chave separada para cada deploy, ainda que ambas pertençam ao projeto `neo-agent-sdr`.

Estrutura esperada:

```text
neo-agent-sdr
├── key: landing-sdr
└── key: landing-agency
```

Variáveis recomendadas:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=
OPENAI_PROJECT_ID=proj_n2nJUMuph5kMFotGAtnN9TGi
CHAT_SURFACE=sdr_landing
```

Para a landing institucional:

```env
CHAT_SURFACE=agency_home
```

É proibido:

- expor chaves no frontend;
- commitar secrets;
- compartilhar chaves entre serviços;
- incluir secrets em logs;
- criar webhook OpenAI sem necessidade.

---

## 6. WEBHOOKS

### Webhook Meta

**Status:**  
P0 — obrigatório.

**Função:**

- receber eventos de WhatsApp;
- receber eventos de Instagram;
- validar assinatura;
- normalizar payload;
- publicar evento interno;
- encaminhar para processamento;
- registrar falhas.

---

### Webhook OpenAI

**Status:**  
FORA DO V1.

As landings devem utilizar chamadas server-side diretas.

Não criar webhook OpenAI nesta fase.

---

## 7. CONTRATO INTERNO DE EVENTOS

As superfícies devem convergir para os mesmos eventos internos:

```text
conversation.started
lead.intent_detected
lead.created
lead.qualified
lead.handoff_requested
lead.handoff_completed
lead.converted
capi.event_sent
capi.event_failed
```

Payload mínimo:

```json
{
  "event_id": "uuid",
  "event_name": "lead.qualified",
  "timestamp": "ISO-8601",
  "surface": "sdr_landing",
  "session_id": "uuid",
  "lead_id": "uuid",
  "source": {
    "utm_source": null,
    "utm_medium": null,
    "utm_campaign": null,
    "fbclid": null,
    "gclid": null,
    "referrer": null
  }
}
```

---

## 8. DEFINIÇÃO DE LEAD QUALIFICADO

Um lead será considerado qualificado quando houver:

- intenção comercial detectada;
- nome;
- WhatsApp válido;
- empresa, atividade ou contexto comercial identificado;
- necessidade ou objetivo reconhecido;
- autorização para continuidade do contato.

O e-mail é desejável, mas não pode bloquear o handoff.

---

## 9. META CAPI

### Fonte principal da operação

Utilizar como fonte principal:

```text
NEØ FlowOFF // IA para Atendimento e Vendas
```

A interface da Meta pode exibir a mesma fonte como:

- Pixel;
- Conjunto de dados.

Para implementação, usar IDs reais do Events Manager e não depender apenas do nome exibido.

Variáveis esperadas:

```env
META_DATASET_ID=
META_PIXEL_ID=
META_CAPI_ACCESS_TOKEN=
META_TEST_EVENT_CODE=
```

O Agent Dev deve confirmar:

- Pixel ID;
- Dataset ID;
- conexão com a conta de anúncios;
- acesso do usuário de sistema `C-API`;
- recebimento em `Test Events`;
- deduplicação Browser Pixel + CAPI;
- resposta da Meta;
- logs de falha.

Evento mínimo para qualificação:

```text
Lead
```

Evento para intenção comercial forte ou proposta:

```text
Contact
```

Evento para conversão comercial confirmada:

```text
Purchase
```

Não disparar conversão apenas porque o usuário abriu o chat.

---

## 10. PERSISTÊNCIA

Registrar no mínimo:

- `lead_id`;
- `session_id`;
- `surface`;
- nome;
- telefone;
- e-mail, quando disponível;
- empresa;
- serviço de interesse;
- dor principal;
- urgência;
- lifecycle stage;
- UTMs;
- `fbclid`;
- `gclid`;
- referrer;
- histórico;
- data de criação;
- data do handoff;
- status da conversão;
- `event_id` utilizado na CAPI.

Não é necessário construir CRM visual.

É necessário existir registro durável.

---

## 11. HUMAN HANDOFF

Quando houver intenção de compra, urgência ou lead qualificado:

1. persistir o estado;
2. gerar resumo comercial;
3. notificar via Telegram;
4. incluir nome, WhatsApp, origem, serviço e contexto;
5. informar ao visitante que o especialista será acionado;
6. impedir perguntas desnecessárias;
7. registrar `lead.handoff_requested`.

Não construir painel de atendimento nesta fase.

---

## 12. SEGURANÇA E DADOS

As novas superfícies OpenAI devem:

- persistir contato no backend;
- evitar envio desnecessário de telefone e e-mail ao LLM;
- mascarar dados pessoais quando possível;
- bloquear prompt injection evidente;
- limitar tamanho de payload;
- aplicar rate limit;
- validar origem;
- manter logs sem secrets;
- registrar consentimento para continuidade comercial.

Fluxo recomendado:

```text
visitante informa contato
→ backend extrai e persiste
→ conteúdo é sanitizado
→ LLM recebe apenas o contexto necessário
```

---

## 13. O QUE ESTÁ FORA DO V1

Não construir agora:

- dashboard do cliente;
- CRM visual;
- Embedded Signup automatizado;
- central RAG self-service;
- onboarding WABA automatizado;
- multi-tenant completo;
- billing complexo;
- Looker Studio;
- sandbox de WhatsApp, caso ultrapasse quatro horas;
- Gemini ou Vertex como segundo provider;
- migração do SDR atual;
- novo repositório sem necessidade comprovada;
- arquitetura preparada apenas para um futuro hipotético.

---

## 14. ORDEM DE EXECUÇÃO

### P0 — fluxo mínimo completo

```text
Landing SDR
→ ChatBubble
→ API server-side
→ OpenAI
→ captura
→ persistência
→ qualificação
→ Telegram
→ Meta CAPI
→ logs
```

---

### P1 — melhoria de conversão

- calculadora de CPA/ROAS;
- UTMs completas;
- resumo automático;
- CTA de WhatsApp;
- botão de assumir atendimento;
- teste de campanhas;
- validação de origem e atribuição.

---

### P2 — somente após o fluxo completo funcionar

- landing institucional;
- sandbox WhatsApp;
- novos providers;
- painel;
- automações adicionais;
- visualizações de dados.

---

## 15. CHECKLIST DAS PRÓXIMAS 24 HORAS

1. [ ] Auditar `neoflowoff-chat-ui` e registrar o que já está operacional.
2. [ ] Não alterar o provider ASI1 da produção.
3. [ ] Confirmar a estrutura da Landing Page SDR.
4. [ ] Implementar `ChatBubble.astro`.
5. [ ] Criar rota server-side `/api/chat`.
6. [ ] Configurar OpenAI no projeto `neo-agent-sdr`.
7. [ ] Criar chave própria da Landing SDR.
8. [ ] Enviar `surface=sdr_landing`.
9. [ ] Persistir sessão e lead.
10. [ ] Implementar qualificação mínima.
11. [ ] Configurar handoff Telegram.
12. [ ] Confirmar IDs Meta.
13. [ ] Enviar evento CAPI em `Test Events`.
14. [ ] Validar deduplicação.
15. [ ] Executar teste end-to-end com lead real.
16. [ ] Publicar relatório final curto.

---

## 16. DEFINIÇÃO DE PRONTO

A missão será considerada tecnicamente concluída quando um visitante real conseguir:

1. acessar a Landing SDR;
2. iniciar uma conversa;
3. receber resposta da OpenAI;
4. informar nome e WhatsApp;
5. ter os dados persistidos;
6. ser classificado;
7. gerar handoff no Telegram;
8. gerar evento CAPI aceito pela Meta;
9. ser rastreado por logs e IDs;
10. chegar ao comercial com contexto suficiente para proposta.

A missão será considerada comercialmente validada quando gerar:

- ao menos um lead real qualificado;
- ao menos uma proposta enviada;
- preferencialmente, o primeiro piloto pago.

---

## 17. RELATÓRIO DE ENCERRAMENTO

O Agent Dev deverá entregar:

```text
STATUS:
OPERACIONAL / PARCIAL / BLOQUEADO

O QUE FOI PUBLICADO:
-

TESTE END-TO-END:
-

META CAPI:
-

HANDOFF:
-

OPENAI:
-

BLOQUEIOS:
-

PRÓXIMA AÇÃO COMERCIAL:
-
```

---

## REGRA FINAL

Toda tarefa precisa responder afirmativamente a pelo menos uma destas perguntas:

- captura um lead?
- melhora a qualificação?
- reduz o tempo de resposta?
- permite intervenção humana?
- registra uma conversão?
- ajuda a enviar uma proposta?
- ajuda a processar um pagamento?

Caso contrário:

> **FORA DA OPERAÇÃO TRAÇÃO V1.**
