# QA OOP Allure Project

Пример автотестов на Java с демонстрацией принципов ООП, использованием JUnit 5 и генерацией Allure отчётов.

---

##  Структура проекта

- `BasePage.java` – абстрактный базовый класс страницы (инкапсуляция, абстракция)
- `LoginPage.java`, `MainPage.java` – реализации страниц (наследование, полиморфизм)
- `PageTest.java` – JUnit тесты, покрывающие поведение

---

##  Используемые технологии

| Компонент | Версия |
|-----------|--------|
| Java      | 17     |
| Maven     | 3.8+   |
| JUnit     | 5.10.0 |
| Allure    | 2.24.0 |
| SLF4J     | 1.7.36 |

---

##  Как запустить

### 1. Клонировать проект

```bash
git clone https://github.com/your-username/qa-oop-allure.git
cd qa-oop-allure
```

### 2. Запустить тесты
```bash
mvn clean test
```

### 3. Открыть отчет 
```bash
allure serve target/allure-results
```
<img width="1352" height="759" alt="Снимок экрана 2025-07-21 в 12 12 11" src="https://github.com/user-attachments/assets/ed6edba5-c4a8-4541-a656-c5b527da7ebc" />
<img width="1352" height="762" alt="Снимок экрана 2025-07-21 в 12 12 59" src="https://github.com/user-attachments/assets/59eeff45-05dc-44f8-93a7-3d3a69925daf" />
<img width="1352" height="760" alt="Снимок экрана 2025-07-21 в 12 13 11" src="https://github.com/user-attachments/assets/3312021e-9983-4ca3-9c50-9382bc981a3c" />


