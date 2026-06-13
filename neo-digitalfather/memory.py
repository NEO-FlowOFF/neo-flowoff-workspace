# ===============================
# memory.py // NEO:DigitalFather MEMORY CORE
# Sistema de Memória Vetorial usando FAISS
# ===============================

"""
Este módulo permite que NEO:DigitalFather tenha memória viva:
- Armazena vetores de interações anteriores
- Recupera contexto relevante para enriquecer novas projeções
- Baseado em embeddings e FAISS (local, rápido, expansível)

NOTA: este módulo ainda NÃO está plugado no runtime (nem agent.py nem llm_core.py
o importam). Funciona standalone. Para ativar memória viva, chamar store_interaction /
retrieve_similar_context a partir do llm_core.py.
"""

import os
import faiss
import pickle
import numpy as np
from typing import List, Tuple, Dict, Any
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# ===============================
# [1] CONFIGURAÇÕES
# ===============================

EMBEDDING_MODEL = "text-embedding-3-small"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY não encontrada no arquivo .env")

INDEX_PATH = os.getenv("MEMORY_INDEX_PATH", "memory_index.faiss")
META_PATH = os.getenv("MEMORY_METADATA_PATH", "memory_metadata.pkl")

# ===============================
# [2] EMBEDDINGS
# ===============================

client = OpenAI(api_key=OPENAI_API_KEY)

def get_embedding(text: str) -> List[float]:
    """Gera embedding usando OpenAI API"""
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding

# ===============================
# [3] INDEXAÇÃO COM FAISS
# ===============================

DIMENSION = 1536  # Tamanho para OpenAI embedding-3-small

try:
    if os.path.exists(INDEX_PATH) and os.path.exists(META_PATH):
        index = faiss.read_index(INDEX_PATH)
        with open(META_PATH, "rb") as f:
            metadata = pickle.load(f)
    else:
        index = faiss.IndexFlatL2(DIMENSION)
        metadata = []
except Exception as e:
    print(f"Erro ao carregar índice existente, criando novo: {e}")
    index = faiss.IndexFlatL2(DIMENSION)
    metadata = []

# ===============================
# [4] FUNÇÕES PRINCIPAIS
# ===============================

def store_interaction(text: str, metadata_entry: Dict[str, Any]):
    """Armazena uma interação na memória vetorial"""
    vector = get_embedding(text)
    index.add(np.array([vector], dtype='float32'))
    metadata.append(metadata_entry)

    # Salva o índice e metadados
    dir_name = os.path.dirname(INDEX_PATH)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "wb") as f:
        pickle.dump(metadata, f)

def retrieve_similar_context(text: str, k: int = 3) -> List[Dict[str, Any]]:
    """Recupera contextos similares da memória"""
    if index.ntotal == 0:
        return []

    vector = get_embedding(text)
    D, I = index.search(np.array([vector], dtype='float32'), k)

    results = []
    for idx in I[0]:
        if 0 <= idx < len(metadata):
            results.append(metadata[idx])

    return results

# ===============================
# [5] EXEMPLO DE USO FUTURO
# ===============================

# def contextual_memory(query_text: str) -> str:
#     similar = retrieve_similar_context(query_text)
#     return "\n".join([item["text"] for item in similar])

# ===============================
# FIM // Essa memória pode ser usada pelo llm_core.py
# ===============================
