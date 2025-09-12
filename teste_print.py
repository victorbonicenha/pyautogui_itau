import pyautogui
import time
import mss

def capturar_regiao(nome_arquivo="print_regiao.png"):
    print("Posicione o mouse no CANTO SUPERIOR ESQUERDO da região e espere 5 segundos...")
    time.sleep(5)
    x1, y1 = pyautogui.position()
    print(f"Canto superior esquerdo: {x1}, {y1}")

    print("Agora posicione o mouse no CANTO INFERIOR DIREITO da região e espere 5 segundos...")
    time.sleep(5)
    x2, y2 = pyautogui.position()
    print(f"Canto inferior direito: {x2}, {y2}")

    largura = x2 - x1
    altura = y2 - y1

    with mss.mss() as sct:
        monitor = {"top": y1, "left": x1, "width": largura, "height": altura}
        img = sct.grab(monitor)
        mss.tools.to_png(img.rgb, img.size, output=nome_arquivo)

    print(f"Print salvo como '{nome_arquivo}'")

if __name__ == "__main__":
    capturar_regiao("meu_campo.png")
