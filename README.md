Трекер полезных привычек - habit_project.
Для использования проекта [.env.sample](.env.sample) и [requirements.txt](requirements.txt).
Перед использованием проекта выполните все миграции.
Выполните команду [csu.py](users%2Fmanagement%2Fcommands%2Fcsu.py) для создания суперпользователя.
Для регистрации пользователя используйте UserRegisterAPIView.
Для изменения профиля пользователя используйте UserProfileAPIView.
Для удаления пользователя используйте UserDestroyAPIView.
Для создания, просмотра, изменения и удаления привычек реализован CRUD, смотри habits.views.
Что бы мользователь мог использовать приложение используй JWTAuthentication.

В проекте реализовано подключение к telegram.bot.
В проекте настроен redis и celery для выполенния периодической задачи send_message_habit_telegram.
Настроен CORS.
Настроен drf_yasg.

В проекте созданы [Dockerfile](Dockerfile) и [docker-compose.yaml](docker-compose.yaml).
Перед запуском комад docker-compose build docker-compose up, настройте файл [.env](.env).
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=

CACHE_ENABLED=
CACHE_LOCATION=

CELERY_BROKER_URL=
CELERY_RESULT_BACKEND=



