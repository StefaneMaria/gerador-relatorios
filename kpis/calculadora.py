"""
Modelo de domínio para os KPIs do relatório.
Separa a lógica de cálculo da camada de apresentação.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class KpisGeracao:
    geracao_total: float
    perfomance_percentual: float
    melhor_dia_kwh: float
    melhor_dia_numero: int
    pior_dia_kwh: float
    pior_dia_numero: int
    
def calcular_kpis(geracao_diaria: List[float], meta_mensal: float) -> KpisGeracao:
    """Calcula os KPIs a partir da geração diária e da meta mensal."""
    geracao_total = sum(geracao_diaria)
    perfomance_percentual = (geracao_total / meta_mensal) * 100 if meta_mensal else 0

    melhor_dia_kwh = max(geracao_diaria)
    melhor_dia_numero = geracao_diaria.index(melhor_dia_kwh) + 1

    pior_dia_kwh = min(geracao_diaria)
    pior_dia_numero = geracao_diaria.index(pior_dia_kwh) + 1

    return KpisGeracao(
        geracao_total=geracao_total,
        perfomance_percentual=perfomance_percentual,
        melhor_dia_kwh=melhor_dia_kwh,
        melhor_dia_numero=melhor_dia_numero,
        pior_dia_kwh=pior_dia_kwh,
        pior_dia_numero=pior_dia_numero
    )