import io
from typing import List

import matplotlib.pyplot as plt

from cores.paleta import CorHex, hex_para_rgb

LARGURA_FIGURA_PADRAO = 7.2

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

def gerar_grafico_geracao_diaria(geracao_diaria: List[float], meta_mensal: float) -> io.BytesIO:
    dias = list(range(1, len(geracao_diaria) + 1))
    media_esperada = meta_mensal / 30
    
    fig, ax = plt.subplots(figsize=(LARGURA_FIGURA_PADRAO, 2,.6))
    _aplicar_fundo_branco(fig, ax)
    
    cores_barras = [_classificar_cor_barra(v, media_esperada) for v in geracao_diaria]
    ax.bar(dias, geracao_diaria, color=cores_barras, zorder=2)
    
    ax.axhline(
        y=media_esperada,
        color=CorHex.LARANJA_SOLAR,
        linewidth=1.8,
        linestyle='--',
        zorder=3,
        label=f"Média esperada: ({media_esperada:.1f} kWh/dia)"
    )
    
    ax.set_xlabel("Dia do mês", fontsize=8, color=CorHex.AZUL_ESCURO)
    ax.set_ylabel("kWh", fontsize=8, color=CorHex.AZUL_ESCURO)
    ax.tick_params(labelsize=7, colors=CorHex.AZUL_ESCURO)
    ax.set_xlim(0.2, len(dias) + 0.8)
    _configurar_eixos(ax)
    
    legenda = ax.legend(fontsize=7, framealpha=0, loc="upper right")
    for texto in legenda.get_texts():
        texto.set_color(CorHex.AZUL_ESCURO)
        
    plt.tight_layout(pad=0.4)
    return _salvar_figura_em_buffer(fig)
    