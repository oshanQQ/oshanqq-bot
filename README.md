# malcov-sample

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
docker-compose exec malcov-sample bash
```

anaconda 環境を停止させる

```
docker-compose down
```

環境リセットの滅びの呪文

```
docker-compose down --rmi all --volumes
```

# 参考

- [docker で簡易に python3 の環境を作ってみる - Qiita](https://qiita.com/reflet/items/4b3f91661a54ec70a7dc)
- [Docker で Python 実行環境を作ってみる - Qiita](https://qiita.com/jhorikawa_err/items/fb9c03c0982c29c5b6d5)
