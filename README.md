## Discord Bot
(編集中)

```
cp .env.template .env
```

dockerの立ち上げ
```
cd docker
docker compose up -d  --build
docker exec -it main bash
```

botの実行
```
python main.py
```
