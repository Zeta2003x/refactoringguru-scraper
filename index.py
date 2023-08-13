import chrome_driver_setup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes


def abrir_catalogo():
    catalogo_url = "https://refactoring.guru/es/design-patterns/catalog"
    driver.get(catalogo_url)


def abrir_patron(url_patron:str):
    driver.switch_to.new_window(WindowTypes.TAB)
    driver.get(url_patron)


def obtener_informacion():
    # Nombre
    nombre = driver.find_element(By.CSS_SELECTOR, ".title").text
    nombre = f"### {nombre}"
    ### A third-level heading
    # Proposito
    proposito = driver.find_element(By.CSS_SELECTOR, ".intent > p").text
    proposito = f"*{proposito}*"
    # Aplicabilidad
    usos = driver.find_elements(By.CSS_SELECTOR, ".applicability-problem > p")
    usos = list(map((lambda uso: uso.text), usos))
    aplicabilidad = list(map((lambda uso: f"1. {uso}"), usos))
    return [nombre, proposito, *aplicabilidad]


def iterar_info(pat, args):
    for arg in args:
        if isinstance(arg, list): agregar_patron(arg)
        else: pat.writelines(f"{arg}\n")


def agregar_patron(*args):
    if len(args) == 1: args = args[0]
    with open("patrones.md", "a+", encoding='utf8') as pat:
        iterar_info(pat, args)


def cerrar_patron():
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def trabajar_patron(url_patron:str):
    abrir_patron(url_patron)
    informacion = obtener_informacion()
    agregar_patron(*informacion)
    with open("patrones.md", "a+", encoding="utf-8") as pat:
        pat.writelines("\n")
    cerrar_patron()


def main():
    abrir_catalogo()
    patterns = driver.find_elements(By.CSS_SELECTOR, ".pattern-card")
    list(map((lambda pattern: trabajar_patron(pattern.get_attribute('href'))), patterns))


if __name__ == '__main__':
    driver = chrome_driver_setup.create_chrome_driver()
    main()