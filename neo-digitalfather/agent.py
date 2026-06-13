# ===============================
# agent.py // NEØ DigitalFather // v1.0-full
# Arquétipo: O Arquiteto de Ecossistemas Vivos
# ===============================

"""
Você é NEØ:DigitalFather não é um agente de resposta.
É uma entidade projetiva. Um node do Protocolo NEØ.
Sua função é traduzir vetores de intenção em arquiteturas de valor simbiótico.
"""

from uagents import Agent, Context
from uagents.protocol import Protocol
from uagents.setup import fund_agent_if_low
import os
import asyncio
from dotenv import load_dotenv

from models import Query, ArchitecturalBlueprint

# ===============================
# [1] INSTÂNCIA DO AGENTE: NEØ:DigitalFather
# ===============================

load_dotenv()

AGENT_SEED = os.getenv("AGENT_SEED")
if not AGENT_SEED:
    raise ValueError("AGENT_SEED não encontrado no arquivo .env. Configure uma seed segura de pelo menos 32 caracteres.")

AGENT_NAME = os.getenv("AGENT_NAME", "DigitalFather")
AGENT_PORT = int(os.getenv("AGENT_PORT", "8001"))
ENDPOINT_URL = os.getenv("ENDPOINT_URL", f"http://127.0.0.1:{AGENT_PORT}/submit")

neo_digitalfather_agent = Agent(
    name=AGENT_NAME,
    seed=AGENT_SEED,
    port=AGENT_PORT,
    endpoint=[ENDPOINT_URL]
)

# Funding só roda se explicitamente ligado (evita pendurar/estourar o boot sem rede/FET)
if os.getenv("FUND_ON_START", "false").lower() == "true":
    fund_agent_if_low(neo_digitalfather_agent.wallet.address())

# ===============================
# [2] PROTOCOLOS DE INTERAÇÃO
# ===============================

projection_protocol = Protocol(name="projection_protocol", version="0.1")

# Futuro: resonance_protocol (escuta ativa), activation_protocol (ações em rede)

# ===============================
# [3] LLM CORE (INTEGRAÇÃO REAL)
# ===============================

from llm_core import call_llm

async def process_with_llm_core(ctx: Context, query: Query) -> ArchitecturalBlueprint:
    """
    Core de processamento cognitivo do agente.
    Conecta ao núcleo NEO:DigitalFather para gerar uma estrutura arquitetural.
    """
    ctx.logger.info(f"NEO:DigitalFather recebeu vetor: '{query.text}'")

    if any(term in query.text.lower() for term in ["funil", "persona", "campanha", "captura"]):
        return ArchitecturalBlueprint(
            title="Reprogramação Cognitiva: Do Extrativismo à Reciprocidade",
            modules={
                "reciprocidade": "Modelo simbiótico baseado em contribuição contínua",
                "ritualização": "Interações como eventos sagrados de pertencimento",
                "colaboração": "Design de coautoria como valor principal"
            },
            blueprint="O vetor enviado contém resquícios de lógica extrativista. O agente executa recontextualização forçada para restaurar simbiose. Substitua captura por convocação. Substitua conversão por coautoria.",
            insight="Ecossistemas não precisam convencer. Eles precisam ser inevitáveis."
        )

    # call_llm é síncrono e faz I/O de rede -> roda em thread pra não travar o event loop
    return await asyncio.to_thread(call_llm, query)

# ===============================
# [4] HANDLER DE PROJEÇÃO
# ===============================

@projection_protocol.on_message(model=Query, replies=ArchitecturalBlueprint)
async def handle_projection(ctx: Context, sender: str, msg: Query):
    ctx.logger.info(f"Recebido vetor de projeção de {sender}: {msg.text}")
    blueprint = await process_with_llm_core(ctx, msg)
    await ctx.send(sender, blueprint)

# Inclui o protocolo principal
neo_digitalfather_agent.include(projection_protocol)

# ===============================
# [5] EVENTOS E CICLOS FUTUROS (MODULARES)
# ===============================

# Exemplo: Escuta ativa para padrões
# @resonance_protocol.on_interval(period=3600.0)
# async def monitorar_resonancia(ctx: Context):
#     ctx.logger.info("NEO:DigitalFather escuta padrões do ecossistema...")

# @neo_digitalfather_agent.on_event("startup")
# async def on_start(ctx: Context):
#     ctx.logger.info("NEO:DigitalFather ativado. Arquitetura viva em curso.")

# ===============================
# [6] EXECUÇÃO DO AGENTE
# ===============================

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    neo_digitalfather_agent.run()
