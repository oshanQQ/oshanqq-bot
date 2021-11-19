# oshanqq-bot

anaconda 環境を立ち上げる

```bash
docker-compose up
```

anaconda 環境をバックグラウンドで立ち上げる

```bash
docker-compose up -d
```

ターミナルからコンテナに入る

```bash
docker-compose exec oshanqq-bot bash
```

anaconda 環境を停止させる

```
docker-compose down
```

環境リセットの滅びの呪文

```
docker-compose down --rmi all --volumes
```
