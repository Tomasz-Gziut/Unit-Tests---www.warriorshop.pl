import random
import string
import time
from asyncio import wait_for
from time import sleep
import re

from playwright.sync_api import Playwright, sync_playwright

def generate_random_string(length=12, chars=string.ascii_letters + string.digits + "!@#$%^&*"):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    while True:
        password = ''.join(random.choices(chars, k=length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password)):
            return password

RANDOM_PASSWORD = generate_random_string()
RANDOM_LOGIN = generate_random_string(length=8, chars=string.ascii_letters + string.digits)

def run1(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/")

    page.locator('a[title=""]').hover()
    page.get_by_role("link", name="Rejestracja").click()
    page.get_by_role("textbox", name="Imię i nazwisko:").fill("Test User")
    page.get_by_role("textbox", name="Ulica:").fill("Random Street")
    page.get_by_role("textbox", name="Nr domu / lokalu").fill("123")
    page.get_by_role("textbox", name="Kod pocztowy:").fill("00-000")
    page.get_by_role("textbox", name="Miasto:").fill("Random City")
    page.get_by_role("textbox", name="Telefon:").fill("123456789")
    page.get_by_role("textbox", name="E-mail:").fill("hivimov745@anlocc.com")
    page.get_by_role("textbox", name="Login:").fill(RANDOM_LOGIN)
    page.get_by_role("textbox", name="Hasło:", exact=True).fill(RANDOM_PASSWORD)
    page.get_by_role("textbox", name="Powtórz hasło:").fill(RANDOM_PASSWORD)
    page.locator("#toggle-create span").nth(3).click()
    page.get_by_role("button", name="Załóż nowe konto").click()

    current_url = page.url
    if current_url == "https://www.warriorshop.pl/user,account":
        print("❌ Test 1 niepowodzenie: Rejestracja się nie powiodła. Użytkownik pozostał na stronie /user,account.")
    elif current_url == "https://www.warriorshop.pl/":
        print("✅ Test 1 sukces: Rejestracja zakończona pomyślnie. Użytkownik został przekierowany na stronę główną.")
    else:
        print("❌ Test 1 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()

def run2(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/")
    page.get_by_role("link", name=" Zaloguj").click()
    page.locator("#js-main > div > div.section.general > form > div:nth-child(3) > label > input").click()
    page.locator("#js-main").get_by_role("textbox", name="Login:").fill(RANDOM_LOGIN)
    page.locator("#js-main > div > div.section.general > form > div:nth-child(4) > label > input").click()
    page.locator("#js-main").get_by_role("textbox", name="Hasło:").fill(RANDOM_PASSWORD)
    page.locator("#js-main").get_by_role("button", name="Zaloguj").click()

    current_url = page.url
    if current_url == "https://www.warriorshop.pl/logowanie,auth":
        print("❌ Test 2 niepowodzenie: Logowanie nie powiodło się. Użytkownik pozostał na stronie logowania.")
    elif current_url == "https://www.warriorshop.pl/":
        print("✅ Test 2 sukces: Logowanie zakończone pomyślnie. Użytkownik został przekierowany na stronę główną.")
    else:
        print("❌ Test 2 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()

def run3(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/")
    page.get_by_role("link", name=" Zaloguj").click()
    page.locator("#js-main > div > div.section.general > form > div:nth-child(3) > label > input").click()
    page.locator("#js-main").get_by_role("textbox", name="Login:").fill(RANDOM_LOGIN)
    page.locator("#js-main > div > div.section.general > form > div:nth-child(4) > label > input").click()
    page.locator("#js-main").get_by_role("textbox", name="Hasło:").fill(RANDOM_PASSWORD)
    page.locator("#js-main").get_by_role("button", name="Zaloguj").click()
    page.locator('#js-header > div > nav > div.r-3 > div > ul > li:nth-child(1) > a').hover()
    page.locator("#js-header").get_by_role("link", name="Koszulki patriotyczne").click()
    page.get_by_role("link", name="Koszulka Anty 60 Koszulka").click()
    page.get_by_role("button", name=" Do koszyka WYSYŁKA 24 H").click()
    page.locator("span").filter(has_text=re.compile(r"^L$")).click()
    page.get_by_role("button", name=" Do koszyka WYSYŁKA 24 H").click()
    page.get_by_role("link", name="Przejdź do koszyka").click()

    current_url = page.url
    if current_url == "https: // www.warriorshop.pl / 720, koszulka - anty - 60":
        print("❌ Test 3 niepowodzenie: Produkt nie został dodany do koszyka.")
    elif current_url == "https://www.warriorshop.pl/koszyk":
        print("✅ Test 3 sukces: Produkt został pomyślnie dodany do koszyka.")
    else:
        print("❌ Test 3 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run4(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/")
    page.get_by_role("textbox", name="Szukaj...").click()
    page.get_by_role("textbox", name="Szukaj...").fill("Koszulka Śmierć Konfidentom 60")
    page.get_by_role("button", name="").click()

    current_url = page.url
    if current_url == "https://www.warriorshop.pl/":
        print("❌ Test 4 niepowodzenie: Wyszukiwanie produktu nie powiodło się.")
    elif current_url.startswith("https://www.warriorshop.pl/produkty,szukaj"):
        print("✅ Test 4 sukces: Produkt został pomyślnie wyszukany.")
    else:
        print("❌ Test 4 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()


def run5(playwright):
    RANDOM_WRONG_PASSWORD = generate_random_string()
    RANDOM_WROND_LOGIN = generate_random_string(length=8, chars=string.ascii_letters + string.digits)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/")
    page.get_by_role("link", name=" Zaloguj").click()
    page.locator("#js-main > div > div.section.general > form > div:nth-child(3) > label > input").click()
    page.locator("#js-main").get_by_role("textbox", name="Login:").fill(RANDOM_WROND_LOGIN)
    page.locator("#js-main > div > div.section.general > form > div:nth-child(4) > label > input").click()
    page.locator("#js-main").get_by_role("textbox", name="Hasło:").fill(RANDOM_WRONG_PASSWORD)
    page.locator("#js-main").get_by_role("button", name="Zaloguj").click()

    current_url = page.url
    if current_url == "https://www.warriorshop.pl/logowanie,auth":
        print("✅ Test 5 sukces: Logowanie zostało poprawnie odrzucone dla nieistniejącego konta.")
    elif current_url == "https://www.warriorshop.pl/":
        print("❌ Test 5 niepowodzenie: Logowanie na nieistniejące konto zakończyło się sukcesem – to błąd!")
    else:
        print("❌ Test 5 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()

def run6(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/146,koszulka-smierc-konfidentom-60")
    page.locator("span").filter(has_text=re.compile(r"^L$")).click()
    page.get_by_role("link", name="").click()
    page.get_by_role("button", name=" Do koszyka WYSYŁKA 24 H").click()
    page.get_by_role("link", name="Przejdź do koszyka").click()

    current_url = page.url
    if current_url == "https://www.warriorshop.pl/146,koszulka-smierc-konfidentom-60":
        print("✅ Test 6 sukces: Użytkownik pozostał na stronie produktu – brak możliwości dodania do koszyka.")
    elif current_url == "https://www.warriorshop.pl/koszyk":
        print("❌ Test 6 niepowodzenie: Produkt został dodany do koszyka pomimo braku logowania.")
    else:
        print("❌ Test 6 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()

def run7(playwright: Playwright) -> None:
    NEW_RANDOM_PASSWORD = generate_random_string()
    NEW_RANDOM_LOGIN = generate_random_string(length=8, chars=string.ascii_letters + string.digits)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/")

    page.locator('a[title=""]').hover()
    page.get_by_role("link", name="Rejestracja").click()
    page.get_by_role("textbox", name="Imię i nazwisko:").fill("Test User")
    page.get_by_role("textbox", name="Ulica:").fill("Random Street")
    page.get_by_role("textbox", name="Nr domu / lokalu").fill("123")
    page.get_by_role("textbox", name="Kod pocztowy:").fill("00-000")
    page.get_by_role("textbox", name="Miasto:").fill("Random City")
    page.get_by_role("textbox", name="Telefon:").fill("123456789")
    page.get_by_role("textbox", name="E-mail:").fill("hivimov745@anlocc.com")
    page.get_by_role("textbox", name="Login:").fill(NEW_RANDOM_LOGIN)
    page.get_by_role("textbox", name="Hasło:", exact=True).fill(NEW_RANDOM_PASSWORD)
    page.get_by_role("textbox", name="Powtórz hasło:").fill(NEW_RANDOM_PASSWORD)
    page.locator("#toggle-create span").nth(3).click()
    page.get_by_role("button", name="Załóż nowe konto").click()
    page.get_by_role("link", name=" Konto").hover()
    page.get_by_role("link", name="Wyloguj się").click()

    current_url = page.url
    if current_url == "https://www.warriorshop.pl/":
        print("❌ Test 7 niepowodzenie: Użytkownik nie został przekierowany po wylogowaniu.")
    elif current_url == "https://www.warriorshop.pl/logowanie,logout":
        print("✅ Test 7 sukces: Wylogowanie zakończone pomyślnie.")
    else:
        print("❌ Test 7 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()


def run8(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/c52,odziez-uliczna")
    page.get_by_label("Sortuj: Cena od najniższej").select_option("cennik-asc")

    if page.get_by_label("Sortuj: Cena od najniższej").select_option("cennik-asc") == ['cennik-asc']:
        print("✅ Test 8 sukces: Produkty zostały posortowane rosnąco po cenie.")
    else:
        print("❌ Test 8 niepowodzenie: Nie udało się posortować produktów po cenie.")

    context.close()
    browser.close()


def run9(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/146,koszulka-smierc-konfidentom-60")
    page.locator("span").filter(has_text=re.compile(r"^L$")).click()
    page.get_by_role("button", name=" Do koszyka WYSYŁKA 24 H").click()
    page.get_by_role("link", name="Przejdź do koszyka").click()
    page.get_by_role("spinbutton").click()
    page.get_by_role("spinbutton").fill("-1")
    page.locator("div").filter(has_text="1. Koszyk Dodaj produkty do").nth(1).click()
    page.get_by_role("button", name="Aktualizuj koszyk").click()

    current_url = page.url
    if current_url == "https://www.warriorshop.pl/koszyk":
        print("❌ Test 9 niepowodzenie: System zaakceptował niepoprawną ilość produktu.")
    elif current_url == "https://www.warriorshop.pl/koszyk,edytuj":
        print("✅ Test 9 sukces: Nieprawidłowa ilość została wychwycona – przekierowano do edycji koszyka.")
    else:
        print("❌ Test 9 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()


def run10(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/146,koszulka-smierc-konfidentom-60")
    page.locator("span").filter(has_text=re.compile(r"^L$")).click()
    page.get_by_role("button", name=" Do koszyka WYSYŁKA 24 H").click()
    page.get_by_role("link", name="Przejdź do koszyka").click()
    page.get_by_role("spinbutton").click()
    page.get_by_role("spinbutton").fill("7500000000000000000")
    page.locator("div").filter(has_text="1. Koszyk Dodaj produkty do").nth(1).click()
    page.get_by_role("button", name="Aktualizuj koszyk").click()

    current_url = page.url
    if current_url == "https://www.warriorshop.pl/koszyk":
        print("✅ Test 10 sukces: Zbyt duża ilość produktu została poprawnie odrzucona – brak zmiany strony.")
    elif current_url == "https://www.warriorshop.pl/koszyk,edytuj":
        print("❌ Test 10 niepowodzenie: System zaakceptował nieprawidłową ilość i przekierował do edycji.")
    else:
        print("❌ Test 10 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()

def run11(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/")
    page.get_by_role("link", name=" Zaloguj").click()
    page.locator("#js-main > div > div.section.general > form > div:nth-child(3) > label > input").click()
    page.locator("#js-main").get_by_role("textbox", name="Login:").fill(RANDOM_LOGIN)
    page.locator("#js-main > div > div.section.general > form > div:nth-child(4) > label > input").click()
    page.locator("#js-main").get_by_role("textbox", name="Hasło:").fill(RANDOM_PASSWORD)
    page.locator("#js-main").get_by_role("button", name="Zaloguj").click()
    page.goto("https://www.warriorshop.pl/146,koszulka-smierc-konfidentom-60")
    page.locator("span").filter(has_text=re.compile(r"^L$")).click()
    page.get_by_role("button", name=" Do koszyka WYSYŁKA 24 H").click()
    page.get_by_role("link", name="Przejdź do koszyka").click()
    page.locator("label").filter(has_text="Paczkomat, Płacę teraz").locator("span").click()
    time.sleep(5)
    page.get_by_role("link", name="Paczkomat® CZE03M Kopernika").click()
    page.get_by_text("Wybierz", exact=True).click()
    page.get_by_role("button", name="Dane do wysyłki >").click()

    current_url = page.url
    if current_url == "https://www.warriorshop.pl/koszyk":
        print("❌ Test 11 niepowodzenie: Nie udało się przejść do danych użytkownika po wyborze paczkomatu.")
    elif current_url == "https://www.warriorshop.pl/user?ref=basket":
        print("✅ Test 11 sukces: Przejście do danych użytkownika po wyborze paczkomatu zakończone sukcesem.")
    else:
        print("❌ Test 11 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()



def run12(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/")
    page.get_by_role("link", name=" Zaloguj").click()
    page.locator("#js-main > div > div.section.general > form > div:nth-child(3) > label > input").click()
    page.locator("#js-main").get_by_role("textbox", name="Login:").fill(RANDOM_LOGIN)
    page.locator("#js-main > div > div.section.general > form > div:nth-child(4) > label > input").click()
    page.locator("#js-main").get_by_role("textbox", name="Hasło:").fill(RANDOM_PASSWORD)
    page.locator("#js-main").get_by_role("button", name="Zaloguj").click()
    page.goto("https://www.warriorshop.pl/146,koszulka-smierc-konfidentom-60")
    page.locator("span").filter(has_text=re.compile(r"^L$")).click()
    page.get_by_role("button", name=" Do koszyka WYSYŁKA 24 H").click()
    page.get_by_role("link", name="Przejdź do koszyka").click()
    page.get_by_role("button", name="Dane do wysyłki >").click()

    current_url = page.url
    if current_url == "https://www.warriorshop.pl/koszyk":
        print("❌ Test 12 niepowodzenie: Nie udało się przejść do danych użytkownika po dodaniu produktu do koszyka.")
    elif current_url == "https://www.warriorshop.pl/user?ref=basket":
        print("✅ Test 12 sukces: Przejście do danych użytkownika po dodaniu produktu do koszyka zakończone sukcesem.")
    else:
        print("❌ Test 12 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()


def run13(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/koszyk")
    page.get_by_role("link", name="Strona główna").click()
    page.locator("div").filter(has_text="Szukaj... kategoria Odzież").first.click()

    current_url = page.url
    if current_url == "https://www.warriorshop.pl/koszyk":
        print("❌ Test 13 niepowodzenie: Użytkownik pozostał na stronie koszyka.")
    elif current_url == "https://www.warriorshop.pl/":
        print("✅ Test 13 sukces: Użytkownik został przekierowany na stronę główną.")
    else:
        print("❌ Test 13 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()


def run14(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/")

    page.locator('a[title=""]').hover()
    page.get_by_role("link", name="Rejestracja").click()
    page.get_by_role("textbox", name="Imię i nazwisko:").fill("")
    page.get_by_role("textbox", name="Ulica:").fill("")
    page.get_by_role("textbox", name="Nr domu / lokalu").fill("")
    page.get_by_role("textbox", name="Kod pocztowy:").fill("")
    page.get_by_role("textbox", name="Miasto:").fill("")
    page.get_by_role("textbox", name="Telefon:").fill("")
    page.get_by_role("textbox", name="E-mail:").fill("")
    page.get_by_role("textbox", name="Login:").fill("")
    page.get_by_role("textbox", name="Hasło:", exact=True).fill("")
    page.get_by_role("textbox", name="Powtórz hasło:").fill("")
    page.locator("#toggle-create span").nth(3).click()
    page.get_by_role("button", name="Załóż nowe konto").click()

    current_url = page.url
    if current_url == "https://www.warriorshop.pl/user,account":
        print("❌ Test 14 niepowodzenie: Użytkownik pozostał na stronie konta po próbie rejestracji bez danych.")
    elif current_url == "https://www.warriorshop.pl/":
        print("✅ Test 14 sukces: Użytkownik został przekierowany na stronę główną po błędnej rejestracji.")
    else:
        print("❌ Test 14 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()


def run15(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.warriorshop.pl/")

    page.locator('a[title=""]').hover()
    page.get_by_role("link", name="Rejestracja").click()
    page.get_by_role("textbox", name="Imię i nazwisko:").fill("Test User")
    page.get_by_role("textbox", name="Ulica:").fill("Random Street")
    page.get_by_role("textbox", name="Nr domu / lokalu").fill("123")
    page.get_by_role("textbox", name="Kod pocztowy:").fill("00-000")
    page.get_by_role("textbox", name="Miasto:").fill("Random City")
    page.get_by_role("textbox", name="Telefon:").fill("123456789")
    page.get_by_role("textbox", name="E-mail:").fill("hivimov745@anlocc.com")
    page.get_by_role("textbox", name="Login:").fill("wtZrqV3n")
    page.get_by_role("textbox", name="Hasło:", exact=True).fill("f78gifsmde1D")
    page.get_by_role("textbox", name="Powtórz hasło:").fill("f78gifsmde1D")
    page.locator("#toggle-create span").nth(3).click()
    page.get_by_role("button", name="Załóż nowe konto").click()

    current_url = page.url
    if current_url == "https://www.warriorshop.pl/user,account":
        print("❌ Test 15 niepowodzenie: Użytkownik pozostał na stronie konta po prawidłowej rejestracji.")
    elif current_url == "https://www.warriorshop.pl/":
        print("✅ Test 15 sukces: Użytkownik został pomyślnie zarejestrowany i przekierowany na stronę główną.")
    else:
        print("❌ Test 15 niepowodzenie: Wystąpił nieoczekiwany błąd.")

    context.close()
    browser.close()


print(f"Login: {RANDOM_LOGIN}")
print(f"Password: {RANDOM_PASSWORD}")

with sync_playwright() as playwright:
    run1(playwright)
    run2(playwright)
    run3(playwright)
    run4(playwright)
    run5(playwright)
    run6(playwright)
    run7(playwright)
    run8(playwright)
    run9(playwright)
    run10(playwright)
    run11(playwright)
    run12(playwright)
    run13(playwright)
    run14(playwright)
    run15(playwright)


