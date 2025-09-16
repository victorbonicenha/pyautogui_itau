from extracao_pyautogui import AutoClique
from time import sleep
import subprocess

if __name__ == "__main__":
    # 1. abre o aplicativo do Itaú direto (sem clicar no menu do Windows)
    caminho_app = r"C:\Users\tom\AppData\Local\Aplicativo Itau\itauaplicativo.exe"
    subprocess.Popen([caminho_app])

    sleep(20)
    bot = AutoClique(tempo_padrao=1)

    # 2. clica no campo agência e digita
    bot.clicar_e_digitar("itau_agencia_tentativa.PNG", "7243", confianca=0.5)

    # 3. clica no campo conta e digita
    bot.clicar_e_digitar("conta_itau.png", "40645-6", confianca=0.5)

    # 4. clica no botão acessar
    bot.clicar_imagem("botao_login_itau.png", confianca=0.5)

    print("Fluxo finalizado")
