import pyautogui
from time import sleep

class AutoClique:
    def __init__(self, tempo_padrao: int = 2):
        self.tempo_padrao = tempo_padrao

    def clicar_imagem(self, imagem: str, confianca: float = 0.8, double=False) -> bool:
        local = pyautogui.locateOnScreen(imagem, confidence=confianca)

        if local:
            x, y = pyautogui.center(local)
            if double:
                pyautogui.doubleClick(x, y)   
            else:
                pyautogui.click(x, y)         
            sleep(self.tempo_padrao)
            return True
        else:
            print(f"Imagem '{imagem}' não encontrada na tela.")
            return False

    def clicar_e_digitar(self, imagem: str, texto: str, confianca: float = 0.8) -> bool:
        """
        Clica na imagem e digita o texto informado.
        """
        if self.clicar_imagem(imagem, confianca):
            pyautogui.write(texto, interval=0.1) 
            sleep(self.tempo_padrao)
            return True
        return False

if __name__ == '__main__':
    bot = AutoClique(tempo_padrao=1)

    bot.clicar_imagem("botao.png", confianca=0.9)

    bot.clicar_imagem("bt2.png", confianca=0.9)
