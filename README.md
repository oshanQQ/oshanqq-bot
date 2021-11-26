# oshanqq-bot

## 概要
@oshanqq のツイートっぽい文章を生成します。マルコフ連鎖を使っています。

## 開発に必要なコマンド

`Dockerfile`からイメージを差作成する

```bash
docker-compose build
```

python 環境を立ち上げる

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
