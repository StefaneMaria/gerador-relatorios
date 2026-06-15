"""
Enums para status e classificações do sistema.
"""

from enum import Enum

class StatusSistema(str, Enum):
    NORMAL = "Normal"
    ATENCAO = "Atenção"
    CRITICO = "Crítico"
    
class ClassificacaoGeracao(Enum):
    ACIMA_DA_MEDIA = "acima"
    DENTRO_DA_MEDIA = "dentro"
    ABAIXO_DA_MEDIA = "abaixo"