public class LoginPage extends BasePage {
    @Override
    public String clickButton() {
        return "Нажимаю кнопку 'Войти'";
    }

    public String enterCredentials(String user, String pass) {
        return String.format("Ввожу логин: %s и пароль: %s", user, pass);
    }
}
