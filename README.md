# SpyCats Проєкт

## Опис
Цей репозиторій містить інструкції для запуску бекенду та фронтенду проєкту SpyCats.

---

## Як запустити бекенд

1. Клонувати репозиторій бекенду:
```bash
git clone https://github.com/MoHTuK/SpyCatsTest_backend.git

2.Перейти в папку з бекендом:
```bash
cd SpyCatsTest_backend

3.Створити та активувати віртуальне середовище (рекомендовано):
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

4.Встановити залежності:
```bash
pip install -r requirements.txt

5.Запустити сервер:
```bash
python manage.py runserver
