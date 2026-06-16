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
    
class EstilosRelatorio:
    """
    Agrupa todos os estilos usados no relatório.
    Instanciar uma vez e reutlizar em todo o documento.
    """
    
    def __init__(self):
        self.titulo     = criar_estilo("titulo",       18, negrito=True,  cor=CorHex.BRANCO,      alinhamento=TA_LEFT)
        self.subtitulo  = criar_estilo("subtitulo",     9, negrito=False, cor=CorHex.BRANCO,      alinhamento=TA_LEFT)
        self.secao      = criar_estilo("secao",         9, negrito=True,  cor=CorHex.AZUL_ESCURO)
        self.kpi_valor  = criar_estilo("kpival",       20, negrito=True,  cor=CorHex.AZUL_ESCURO, alinhamento=TA_CENTER)
        self.kpi_label  = criar_estilo("kpilabel",      7, negrito=False, cor=CorHex.CINZA_MEDIO, alinhamento=TA_CENTER)
        self.badge      = criar_estilo("badge",         8, negrito=False, cor=CorHex.AZUL_ESCURO, alinhamento=TA_CENTER)
        self.normal     = criar_estilo("normal",        8, negrito=False, cor=CorHex.AZUL_ESCURO)
        self.pequeno    = criar_estilo("small",         7, negrito=False, cor=CorHex.CINZA_MEDIO)
        self.ocorrencia = criar_estilo("ocorrencia",  7.5, negrito=False, cor=CorHex.AZUL_ESCURO, entrelinha=11)
        self.rodape     = criar_estilo("rodape",      6.5, negrito=False, cor=CorHex.CINZA_MEDIO, alinhamento=TA_CENTER)
 