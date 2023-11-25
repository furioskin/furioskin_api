# furioskin_api

---
### 실행 방법
```shell
pip install poetry
poetry install
poetry run alembic upgrade head
poetry run python main.py --env dev
```

### mysql 실행
```shell
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=password -d -p 3306:3306 mysql:latest
```
