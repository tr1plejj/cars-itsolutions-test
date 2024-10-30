# Django/DRF/Djoser backend. API for make courses, lessons, groups etc.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) 
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

# Небольшое описание
Для авторизации при работы с обычными **views** используются сессии.

При работы с API использются токены из **djangorestframework**.

Создавать автомобили и комментарии могут только авторизованные пользователи
(работает как с Django, так и с DRF).

Изменять и удалять автомобили могут только сами создатели этих
автомоболией (работает как с Django, так и с DRF).

Просматривать комментарии и автомобили могут все пользователи.

# Эндпоинты Django

## /
Главная страница.

## register/
Регистрация пользователя.

## login/
Авторизация пользователя.

## logout/
Выход из аккаунта.

## {car_id}/ 
Просмотр определенного автомобиля и комментариев к нему
(оставлять комментарии на этой же странице могут только авторизованные
пользователи).

## {car_id}/edit/
Изменение полей у конкретного автомобиля (доступно только создателям
данного объекта).

## {car_id}/delete/
Удаление конкретного автомобиля (доступно только создателям
данного объекта).

## create/
Создание автомобиля (только авторизованным пользователям).

## profile/
Профиль пользователя (там же отображаются все его 
добавленные автомобили).

# Эндпоинты DRF (base url: *api/*)

## register/ ['POST']
Создание нового пользователя.

**Поля**: *username, password*

## token/ ['POST']
Аутентификация и авторизация пользователя. Выдача токена.

**Поля**: *username, password*

**Headers**: *Authorization: Token ***your-token****

## cars/ ['GET', 'POST']

**GET:** получение всех автомобилей.

**POST:** создание автомобиля (только авторизованным пользователям).

## cars/{car_id}/ ['GET', 'PUT', 'DELETE']

**GET:** получение конкретного автомобиля.

**PUT:** изменение конкретного автомобиля (только создателю объекта).

**DELETE:** удаление конкретного автомобиля (только создателю объекта).

## cars/{car_id}/comments/ ['GET', 'POST']

**GET:** получение комментариев к автомобилю.
**POST:** создание нового комментария (только авторизованным пользователям).
