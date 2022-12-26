from app import create_app  # Основной файл для запуска приложения

app = create_app()  # Собираем приложение из функции

if __name__ == '__main__':
    app.run(port=25000)
