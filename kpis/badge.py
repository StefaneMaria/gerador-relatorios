"""
Lógica de geração da mensagem de contexto (badge) do relatório.
"""

from typing import List

LIMITE_INFERIOR_PERFORMANCE = 0.7
LIMITE_SUPERIOR_PERFORMANCE = 1.1

def cacular_ratio_performance(geracao_diaria: List[float], media_esperada_diaria: float) -> float:
    dias = len(geracao_diaria)
    if not dias or not media_esperada_diaria:
        return 1.0
    media_real = sum(geracao_diaria) / dias
    return media_real / media_esperada_diaria

def gerar_mensagem_badge(geracao_diaria: List[float], media_esperada_diaria: float) -> str:
    ratio = cacular_ratio_performance(geracao_diaria, media_esperada_diaria)
    
    if ratio < LIMITE_INFERIOR_PERFORMANCE:
        return "🌧️  Período chuvoso — comportamento esperado, fique tranquilo!"
    if ratio > LIMITE_SUPERIOR_PERFORMANCE:
        return "🚀  Geração de vento e popa! Sistema acima da média."
    return "✅  Geração dentro do esperado — tudo certo!"