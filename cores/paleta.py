"""
Paleta de cores do relatório.
Centraliza todas as definições de cor em um único lugar.
"""

class CorHex:
    AMARELO_SOLAR   = "#F5A623"
    LARANJA_SOLAR   = "#E8751A"
    AZUL_ESCURO     = "#1B2A4A"
    CINZA_CLARO     = "#F4F6F9"
    CINZA_MEDIO     = "#9AA5B4"
    VERDE_OK        = "#27AE60"
    VERMELHO_ALERTA = "#E74C3C"
    AMARELO_ATENCAO = "#F39C12"
    BRANCO          = "#FFFFFF"
    BORDA_SUAVE     = "#DDE3EC"
    GRADE_SUAVE     = "#EEF1F5"
    BADGE_FUNDO     = "#FFF8EC"
    BARRA_PADRAO    = "#4A90D9"
    
    def hex_para_rgb(hex_color: str) -> tuple:
        """
       Converte cor hexadecimal para tupla RGB no intervlo 0-1 (matplotlib).
        """
        
        hex_limpo = hex_color.lstrip('#')
        return tuple(int(hex_limpo[i:i+2], 16) / 255 for i in (0, 2, 4))