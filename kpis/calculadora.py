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