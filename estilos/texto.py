"""
Fábrica de estilos para texto.
Centraliza a criação de ParagraphStyle, evitando repetição
"""
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

from cores.paleta import CorHex

def criar_estilo(
    nome: str,
    tamanho: float,
    negrito: bool = False,
    cor: str = CorHex.AZUL_ESCURO,
    alinhamento = TA_LEFT,
    entrelinha: float = None,
) -> ParagraphStyle: 
    """Cria e retorna um ParagraphStyle com os parâmetros fornecidos."""
    return ParagraphStyle(
        nome,
        fontSize=tamanho,
        fontName='Helvetica-Bold' if negrito else 'Helvetica',
        textColor=colors.HexColor(cor),
        alignment=alinhamento,
        leading=entrelinha or tamanho * 1.3,
        spaceAfter=0,
    )