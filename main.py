from extracao_pyautogui import AutoClique

if __name__ == "__main__":
    bot = AutoClique(tempo_padrao=1)

    # 1. abre o app
    bot.clicar_imagem("icone_itau_vm.png", confianca=0.8, double=True)


    # 2. clica no campo agência e digita
    bot.clicar_e_digitar("itau_agencia.png", "7243", confianca=0.8)

    # 3. clica no campo conta e digita
    bot.clicar_e_digitar("conta_itau.png", "40645-6", confianca=0.8)

    # 4. clica no botão acessar
    bot.clicar_imagem("botao_login_itau.png", confianca=0.8)

    print("Fluxo finalizado")
