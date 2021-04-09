# 간단한 소설 사이트 (NovelAPI)

### 핵심 Django 모듈

- Django==3.2

- django-allauth==0.44.0

- django-cors-headers==3.7.0

- django-rest-auth==0.9.5

- djangorestframework==3.12.4

  

### 기본 설정 방법

1. 파이썬 가상환경 생성(Window 기준)

   ```shell
   >> python -m venv env
   >> source env/scripts/activate
   ```

2. Django 의존성 설치

   ```shell
   >> cd NovelAPI
   >> pip install -r requirements.txt
   ```

3. media 폴더 생성

   ```shell
   >> mkdir media
   ```

4. Django DB 마이그레이션(sqlite3)

   ```shell
   >> python manage.py makemigrations
   >> python manage.py migrate
   ```

   간혹 마이그레이션이 되지 않을 경우에는 직접 애플리케이션을 입력해준다.

   ```shell
   >> python manage.py makemigrations author book
   >> python manage.py migrate
   ```

5. Django 서버 구동

   ```shell
   >> python manage.py runserver [port]
   ```

6. 해당 프로필 기본 사진 추가 : `media/profile/default.png`

   기본 사진명이나 확장자가 다른 경우에는 직접 코드 내에서 수정 필요 `author/models.py`, `author/serializers.py`



### 추가 설명

- ### [Database](./docs/Database.md)

- ### [Endpoint](./docs/Endpoint.md)