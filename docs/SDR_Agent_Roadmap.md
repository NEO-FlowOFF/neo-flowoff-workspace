# DIRETRIZES DE EXECUÇÃO: OPERAÇÃO TRAÇÃO (V1)

## ALVO: Agente Dev | Autor: NEØ MELLØ

**STATUS: CRÍTICO | FOCO: COMERCIALIZAÇÃO E RECEITA IMEDIATA*

Este documento estabelece o roadmap imediato e corrige a rota de desenvolvimento. A fase de "provar que conseguimos construir" acabou. A fase agora é "provar que o mercado quer comprar".

## 1. DIRETRIZES DE TOPOLOGIA E QUADRO BRANCO

Anotações para consolidação do mapa mental/arquitetura (`neoflowoff_platform_nodes_whiteboard.html`):

* **Nomenclatura Oficial:** O core da operação deve ser referenciado como "NEØ Growth System".
* **Filtragem de Nós:** Inserir SOMENTE nodes, services, rotas e contratos reais e verificados. Nada de abstrações.
* **Tags de Status:** Rotular tudo estritamente como `OPERACIONAL`, `PARCIAL`, `AUSENTE` ou `FORA DO V1`.
* **Conexões:** Ligar Meta, Google Cloud (Vertex/Gemini), NEØ Growth System e FlowPay de forma direta, refletindo os repositórios reais.

**Regra de Ouro:** Nenhuma linha de código deve ser escrita se não for para capturar um lead, fechar um contrato ou processar um pagamento nesta semana.

---

## 2. MAPEAMENTO DE WORKSPACES (O QUE VAMOS USAR)

A arquitetura base já existe. Não invente novos repositórios.

* **`NEO-Growth-System` (O Motor Insvisível)**
  * *Local:* `/Users/nettomello/neomello/neo-growth-system`
  * *Papel:* Control plane de eventos.
  * *Serviços Ativos para V1:* `neo-event-ingestor` (Webhooks Meta), `neo-queue-worker` (Fila de processamento), envio de eventos CAPI.
* **`NEO-FlowOFF` (A Superfície de Contato / Frontend)**
  * *Local:* `/Users/nettomello/neomello/NEO-FlowOFF`
  * *Papel:* Coordenação organizacional, vitrine e interface de chat.
  * *Serviços Ativos para V1:*
    * `neo-landing-sdr` (Página de captura e vitrine tecnológica).
    * `neoflowoff-chat-ui` **[FINALIZADO]** (Interface visual do Agente SDR. Repositório intocável para novas features, apenas integração).

---

## 3. AUDITORIA E CORREÇÃO DA PROPOSTA ANTERIOR

A sua proposta anterior estava excelente tecnicamente, mas muito focada em "produto final" (SaaS). Nós somos uma **Agência Tech Provider**. Vamos fatiar a entrega para gerar caixa agora.

### 🔴 O QUE FICA DE FORA DO V1 (PARALISADO)

* **Dashboard Complexo do Cliente (Glassmorphism, etc.):** Não vamos construir painel de cliente antes de ter cliente pagando. O onboarding dos 3 primeiros clientes será "Concierge" (nós fazemos por eles nos bastidores).
* **Embedded Signup 100% Automatizado:** Lindo, mas consome tempo. Faremos o provisionamento WABA via gerenciador de negócios para os primeiros clientes até o gargalo doer.
* **Central de Treinamento RAG Self-Service:** Nós mesmos injetaremos o contexto (PDFs, regras) via código/banco nos primeiros setups.

### 🟢 O QUE ENTRA NO V1 (EXECUÇÃO IMEDIATA)

**A. FRONTEND CAPTURA: `neo-landing-sdr` (Repositório NEO-FlowOFF)**

* **Design:** Minimalista, fundo escuro (matte black), tipografia geométrica, contrastes neon (Cyan/Acid Green).
* **Agente SDR Bobble (O Fechador):** O bot da home não é para tirar dúvida, é para qualificar, pegar o contato (WhatsApp/Email) e jogar no nosso CRM/Funil.
* **Hook Tecnológico:** Calculadora de ROAS / Simulador de economia de CPA. Mostrar o número na cara do cliente. (O "Sandbox" de WhatsApp fica como V1.5 se demorar mais de 4 horas para implementar).

**B. BACKEND TRAÇÃO: `neo-growth-system`**

* **Motor de Webhooks:** `neo-event-ingestor` ouvindo a Meta API (WhatsApp/Insta Direct) sem latência.
* **C-API Server-Side:** Mandando o evento de conversão do nosso SDR limpinho pra Meta. Isso prova nosso valor como Tech Provider.
* **Integração LLM (ASI 1 ONE):** Conectar os prompts de vendas do SDR à API da OpenAI (temos 200k tokens pra queimar) ou Gemini.
* **Human Handoff Básico:** Se a IA travar com um lead, disparar um alerta (Telegram/Slack via `neo-provider-telegram`) para eu assumir a venda pelo celular. Não precisa de painel complexo, apenas roteamento de emergência.

---

## 4. CHECKLIST DO AGENTE DEV (PRÓXIMAS 24H)

1. [x] Inicializar o setup do `neo-landing-sdr` dentro de `NEO-FlowOFF`.
2. [ ] Subir o endpoint de webhook no `neo-growth-system` para receber chamadas da Meta.
3. [ ] Integrar a lógica do Agente SDR (prompt de qualificação) com a rota de recepção de mensagens.
4. [ ] Configurar o disparo do C-API quando o Agente SDR capturar um lead qualificado.

**Lembre-se:** Código despachado gera conhecimento, sistema vendido gera negócio. Arquitetura perfeita sem adoção é museu. FOCO NA TRAÇÃO.
