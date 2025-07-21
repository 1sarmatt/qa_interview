import io.qameta.allure.*;
import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.*;

@Epic("OOP Demo")
@Feature("Page Actions")
public class PageTest {

    @Test
    @Story("Login flow")
    @Severity(SeverityLevel.CRITICAL)
    @DisplayName("Проверка логина")
    void testLoginPageFlow() {
        BasePage page = new LoginPage();
        assertEquals("Открываю страницу", page.openPage());
        assertEquals("Ввожу логин: user и пароль: 1234", ((LoginPage) page).enterCredentials("user", "1234"));
        assertEquals("Нажимаю кнопку 'Войти'", page.clickButton());
    }

    @Test
    @Story("Logout flow")
    @Severity(SeverityLevel.NORMAL)
    @DisplayName("Проверка выхода")
    void testMainPageFlow() {
        BasePage page = new MainPage();
        assertEquals("Открываю страницу", page.openPage());
        assertEquals("Нажимаю кнопку 'Выйти'", page.clickButton());
    }
}
