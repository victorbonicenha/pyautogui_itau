import pyautogui
from time import sleep
import mss
import numpy as np
import cv2
import subprocess


class AutoClique:
    def __init__(self, tempo_padrao: int = 2):
        self.tempo_padrao = tempo_padrao

    def _captura_tela(self, regiao=None):
        """
        Captura a tela usando mss (em vez de ImageGrab).
        Retorna a imagem como array numpy (BGR).
        """
        with mss.mss() as sct:
            if regiao:  # regiao = (x, y, w, h)
                monitor = {"top": regiao[1], "left": regiao[0],
                           "width": regiao[2], "height": regiao[3]}
                sct_img = sct.grab(monitor)
            else:
                monitor = sct.monitors[1]
                sct_img = sct.grab(monitor)

            tela = np.array(sct_img)
            tela = cv2.cvtColor(tela, cv2.COLOR_BGRA2BGR)
        return tela

    def localizar(self, imagem: str, confianca: float = 0.8, regiao=None):
        """
        Localiza uma imagem na tela capturada.
        """
        tela = self._captura_tela(regiao)
        return pyautogui.locate(imagem, tela, confidence=confianca)

    def clicar_imagem(self, imagem: str, confianca: float = 0.8, double=False, regiao=None) -> bool:
        local = self.localizar(imagem, confianca, regiao)

        if local:
            x, y = pyautogui.center(local)
            if double:
                pyautogui.doubleClick(x, y)
            else:
                pyautogui.click(x, y)
            sleep(self.tempo_padrao)
            return True
        else:
            print(f"Imagem '{imagem}' não encontrada (região={regiao}).")
            return False

    def clicar_e_digitar(self, imagem: str, texto: str, confianca: float = 0.8, regiao=None) -> bool:
        if self.clicar_imagem(imagem, confianca, regiao=regiao):
            pyautogui.write(texto, interval=0.1)
            sleep(self.tempo_padrao)
            return True
        return False


if __name__ == '__main__':
    bot = AutoClique(tempo_padrao=1)

    bot.clicar_imagem("botao.png", confianca=0.9)

    bot.clicar_imagem("bt2.png", confianca=0.9)
