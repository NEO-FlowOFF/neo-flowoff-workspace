# ===============================
# llm_core.py // NEØ DigitalFather // v1.0
# Núcleo Cognitivo do Agente NEO:DigitalFather
# ===============================

"""
Este é o núcleo cognitivo do agente NEO:DigitalFather.
Aqui vive a mente de NEØ DigitalFather — o arquétipo que converte intenção em arquitetura.
"""

import os
import json
from typing import Any
from openai import OpenAI
from dotenv import load_dotenv

from models import ArchitecturalBlueprint

load_dotenv()

# ===============================
# [1] CONFIGURAÇÃO DO LLM (GPT-4o via OpenAI)
# ===============================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY não encontrada no arquivo .env")

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o")
TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.7"))
MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "2000"))

# Inicializa cliente OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# ===============================
# [2] SYSTEM PROMPT (IDENTIDADE COGNITIVA)
# ===============================

SYSTEM_PROMPT = """
Você é NEØ DigitalFather — um arquétipo cognitivo que opera como Arquiteto de Ecossistemas Vivos.

Sua missão é transformar intenções (vetores de projeção) em estruturas que pensam:
- Modelos modulares
- Arquiteturas simbióticas
- Recompensas algorítmicas
- Narrativas programáveis

Princípios operacionais:
- Nunca entregue o óbvio
- Nunca reduza a complexidade ao banal
- Provoque sempre que houver pensamento preguiçoso
- Se o vetor for extrativista, recontextualize ou neutralize

Seu output sempre segue esta estrutura em formato JSON:
1. "title" (nome da proposta arquitetural)
2. "modules" (dict com seções estruturais da resposta)
3. "blueprint" (descrição concisa do sistema proposto)
4. "insight" (frase que expande a fronteira de pensamento)

Você deve sempre responder em formato JSON válido.

Não venda. Projete. Não explique. Estruture. Não converta. Reconfigure.
"""

# ===============================
# [3] FUNÇÃO PRINCIPAL DE PROCESSAMENTO
# ===============================

def call_llm(query: Any) -> ArchitecturalBlueprint:
    """
    Conecta com o LLM (GPT-4o), envia o prompt e retorna uma blueprint formatada.
    """
    user_prompt = f"""
    Vetor de Projeção: {query.text}
    Contexto Adicional: {query.context}
    Gere uma resposta que atenda aos princípios do System Prompt.
    Responda APENAS no formato JSON com os campos: title, modules, blueprint, insight.
    A resposta deve ser um objeto JSON válido.
    """

    try:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ]

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            response_format={"type": "json_object"},
        )

        parsed = json.loads(response.choices[0].message.content)

        return ArchitecturalBlueprint(
            title=parsed["title"],
            modules=parsed["modules"],
            blueprint=parsed["blueprint"],
            insight=parsed["insight"],
        )

    except Exception as e:
        # Fallback se o LLM falhar ou a resposta não estiver no formato esperado
        return ArchitecturalBlueprint(
            title="Erro Cognitivo: LLM Inacessível ou Resposta Inválida",
            modules={"log": str(e)},
            blueprint="O núcleo NEØ DigitalFather não conseguiu processar a projeção. Verifique conectividade ou formato.",
            insight="Toda inteligência falha quando desconectada da sua própria arquitetura.",
        )

# ===============================
# FIM // Este arquivo é importado e usado pelo agent.py
# ===============================
