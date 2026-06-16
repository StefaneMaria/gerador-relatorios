import io

import matplotlib.pyplot as plt

from cores.paleta import CorHex, hex_para_rgb

def _configurar_eixos(ax, ocultar_bordas=("top", "right")):
    ax.spines[list(ocultar_bordas)].set_visible(False)
    ax.spines[["left", "bottom"]].set_color(CorHex.BORDA_SUAVE)
    ax.yaxis.grid(True, color=CorHex.GRADE_SUAVE, zorder=0)
    ax.set_axisbelow(True)
    
def _aplicar_fundo_branco(fig, ax):
    fig.patch.set_facecolor(CorHex.BRANCO)
    ax.set_facecolor(CorHex.BRANCO)

def _salvar_figura_em_buffer(fig) -> io.BytesIO:
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    buffer.seek(0)
    return buffer

def _classificar_cor_barra(valor: float, media_esperada: float) -> tuple:
    if valor >= media_esperada * 1.1:
        return hex_para_rgb(CorHex.AMARELO_SOLAR)
    if valor >= media_esperada * 0.7:
        return hex_para_rgb(CorHex.BARRA_PADRAO)
    return hex_para_rgb(CorHex.CINZA_MEDIO)
    