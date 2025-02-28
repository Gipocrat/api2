# Сокращение ссылок с помощью ВК
## Описание
Этот проект был создан для сокращения или подсчета кликов по ссылке. Для получения сокращенной ссылки необходимо передать программе ссылку для сокращения.В ином случае, если вы хотите узнать сколько раз переходили по вашей ссылке, необходимо передать сокращенную ссылку
## Установка
Скачайте необходимые файлы, затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей и установить зависимости. Зависимости можно установить командой, представленной ниже 

Установите зависимости командой: 
```python
pip install -r requirements.txt
```
## Пример запуска скрипта 
Для запуска скрипта у вас должен быть установлен Python 3

Для получания сокращенной ссылки, необходимо написать команду в таком формате
```python
python main.py --url https://translate.google.ru
```
После аргумента --url необходимо указать ссылку для работы кода, документацию можно найти на сайте [Сократить ссылку Bitly](https://gist.github.com/dvmn-tasks/5dd3bd3dd0e54a9c0a66613fe5f3318d)

Для получения количества кликов, необходимо вписать команду в такой форме:
```python
python main.py --url bit.ly/3uujaRS
```
## Переменные окружения
Часть настроек проекта берется из переменных окружений. Переменные окружения - это переменные, значение которых присваиваются программе Python извне. Чтобы их определить, создайте файл .env рядом с main.py и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Примеры содержания файла .env:
```python 
VK_TOKEN=e521a9de4921a9de4921a9d00e7671c4ee492e4921a9d89ab346486d24c03301a49
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/modules/)