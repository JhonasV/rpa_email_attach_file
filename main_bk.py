# Usando RPA, hacer dos procesos:
#  1) El primero:
#     a) Entrar a gmail.
#     b) Crear un correo
#     c) Adjuntar un archivo.
#     d) Luego enviarlo.
# import pyautogui
# import webbrowser

# def open_gmail_in_browser():
#     page_url = 'https://accounts.google.com/signin/v2/identifier?hl=es&continue=https%3A%2F%2Fmail.google.com&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession'
#     local_chrome_dir = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
#     webbrowser.get(local_chrome_dir).open(page_url)

# open_gmail_in_browser()

# pyautogui.write(800, 429, "test@test.com")
# screenWidth, screenHeight = pyautogui.size()

#tab_coordinates = pyautogui.locateOnScreen('./test.png')

#print(tab_coordinates)
#pyautogui.rightClick(tab_coordinates)

# pyautogui.click(create_account_button_coordinates[0],
#                 create_account_button_coordinates[1])
