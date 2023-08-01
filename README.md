# **Task 1** 

## **Subtask 1** 

Hej :wave: Mam na imię Justyna. Zadecydowałam się wziąć udział w tym szalonym Dare IT Challenge, ponieważ brałam już udział w Challengu testowaniu manualnym i poczułam, że teraz nadszedł czas, aby rozkręcić się i spróbować swoich sił w świecie testów automatycznych! 🚀
Chcę zyskać wiedzę, która pozwoli mi przyczynić się do tworzenia produktów świetnej jakości i sprawić, że proces testowania będzie szybszy i bardziej efektywny!
Jestem wniebowzięta na myśl o Dare IT Challenge na ścieżce QA: Wstęp do Testów Automatycznych! To będzie niezapomniana przygoda pełna nauki i ogromnej satysfakcji. 

Przygotujcie się, bo nadchodzi testowa superbohaterka! 💪😄

## **Subtask 4** 
Wynik testu ze strony [GET ISTQB](http://getistqb.com/quiz-purpurowy/) o nazwie *PURPUROWY*

**11/14** 
Almost ... :construction_worker:

# **Task 2** 

## **Subtask 2** Wypisz wszystkie elementy znajdujące się na stronie, a następnie, pod każdym elementem znalezionym na stronie, wymień 3 działające selektory.
 **Elementy znajdujące się na stronie logowania: [Scouts-test](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true)**

:white_square_button: Pole wprowadzania nazwy użytkownika  
  
* //*[text()="Login"]

* input[name="login"]

* input[type="text"]

* //*[@id="login"]

* //child::div/label

* label#login-label

* input#login

:white_square_button: Pole wprowadzania hasła 
  
* //*[text()="Password"]

* input[name="password"]

* input#password

* //*[@id="password"]

* //child::div/label

* label#password-label
  
:white_square_button: Przycisk "Zaloguj się" 

* //*[text()="Sign in"]

* //button[@type="submit"]

* form button

* //*[@id="__next"]/form/div/div[2]/button/span[1]

:white_square_button: Link do odzyskiwania hasła  
  
* //*[@id="__next"]/form/div/div[1]/a

* //*[text()="Remind password"]

* //child::div/a

* form a

:white_square_button: Zmiana języka strony  
  
* //*[text()="English"]

* //*[text()="Polish"]

* div[role="button"][aria-haspopup="listbox"]

* //*[@id="__next"]/form/div/div[2]/div
  
:white_square_button: Nazwa strony 

* //*[text()="Scouts Panel"]

* //child::div/h5

* h5.MuiTypography-h5

* //*[@id="__next"]/form/div/div[1]/h5

# **Task 3** 
**Pierszy test automatyczny**

To zadanie miało na celu:

:white_square_button: zapoznanie się z biblioteką Selenium,

:white_square_button: klikanie w elementy na stronie,

:white_square_button: wypełnianie pól tekstem,

:white_square_button: wykorzystanie asercji assert title,

:white_square_button: uruchomienie testu.

*Zapraszam do zapoznania się z plikami z kodem* 😄

# **Task 4** 
**Testy automatyczne dla strony: [Scouts-test](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true)**

[Link do google dysk](https://drive.google.com/drive/folders/1WIPPOjHHXA0GYEZqHe42WV6CEb4Lzg5A)

# **Task 5**

**Robot framework dla strony: [Scouts-test](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true)**

[Link do repozytorium](https://github.com/JustynaJac/challenge_portfolio_robotframework)

# **Task 6**
**Zgłaszanie błędów i raport z testów dla strony: [Scouts-dareit](https://dareit.futbolkolektyw.pl/)**

[Link do raportu z testów](https://docs.google.com/document/d/1LW4kRAuhuM7b5l5VOYgGKjpQa5ktohEgNtEOkG-Quwc)
