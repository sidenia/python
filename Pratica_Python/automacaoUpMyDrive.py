import pyautogui
import time

#antes de começar a rodar abrir o seu Google Drive e logar. Atualizar os atributos dos métodos MoveTo com as coordenadas do arquivo de acordo com sua tela.

pyautogui.alert("Não mecha mais no computador. A automação vai começar!")
pyautogui.PAUSE = 0.5  #esperar meio segundo para cada comando

#abrir o google drive
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1) #pausa + 1 segundo
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

#entrar na area de trabalho
pyautogui.hotkey('winleft','d')

#clicar no arquivo e arrastar pro drive
pyautogui.moveTo(1303,39)  #atualizar coodenada do local do arquivo na tela
pyautogui.mouseDown()
pyautogui.moveTo(369,556) #atualizar coodenada do local onde deve soltar para iniciar o upload

#mudar para a pagina do google drive
pyautogui.hotkey('alt', 'tab')
time.sleep(2)

#soltar o arquivo no google drive
pyautogui.mouseUp()

#esperar o upload
time.sleep(5)

pyautogui.alert("Sua aplicação concluiu o upload no drive!")