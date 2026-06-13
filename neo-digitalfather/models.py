# ===============================
# models.py // NEØ DigitalFather
# Modelos compartilhados (evita import circular entre agent.py e llm_core.py)
# ===============================

from uagents import Model


class Query(Model):
    """Vetor de intenção enviado a NEØ:DigitalFather."""
    text: str
    context: str = ""


class ArchitecturalBlueprint(Model):
    """Estrutura de resposta do agente."""
    title: str
    modules: dict
    blueprint: str
    insight: str
