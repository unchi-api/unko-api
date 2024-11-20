# うんこ API 仕様書

## エンドポイント一覧

| メソッド | エンドポイント | 概要                       |
| -------- | -------------- | -------------------------- |
| GET      | `/unko`        | すべてのうんこを取得       |
| GET      | `/unko/{id}`   | 指定した ID のうんこを取得 |
| POST     | `/unko`        | 新しいうんこを作成         |

---

## GET `/unkos`

### 概要

すべてのうんこのデータを取得します。

### リクエスト例

```
GET /api/unkos
```

### レスポンス例

```json
[
  {
    "id": 1,
    "name": "黄金のうんこ",
    "color_id": 1,
    "color": {
      "id": 1,
      "name": "gold"
    },
    "size_id": 1,
    "size": {
      "id": 1,
      "name": "large"
    }
  },
  {
    "id": 2,
    "name": "虹色のうんこ",
    "color_id": 2,
    "color": {
      "id": 2,
      "name": "rainbow"
    },
    "size_id": 2,
    "size": {
      "id": 2,
      "name": "medium"
    }
  }
]
```

---

## GET `/unko/{id}`

### 概要

指定した ID のうんこデータを取得します。

### リクエスト例

```
GET /api/unko/1
```

### レスポンス例

```json
{
  "id": 1,
  "name": "黄金のうんこ",
  "color_id": 1,
  "color": {
    "id": 1,
    "name": "gold"
  },
  "size_id": 1,
  "size": {
    "id": 1,
    "name": "large"
  }
}
```

### エラーレスポンス

- 404 Not Found  
  指定された ID のうんこが存在しない場合。

```json
{
  "error": "Unko not found"
}
```

---

## POST `/unko`

### 概要

新しいうんこのデータを作成します。

### リクエスト例

```
POST /api/unko
Content-Type: application/json
```

### リクエストボディ

```json
{
  "name": "銀色のうんこ",
  "color_id": 3,
  "size_id": 3
}
```

### レスポンス例

- 201 Created  
  新しく作成されたうんこのデータを返します。

```json
{
  "id": 3,
  "name": "銀色のうんこ",
  "color_id": 3,
  "color": {
    "id": 3,
    "name": "silver"
  },
  "size_id": 3,
  "size": {
    "id": 3,
    "name": "small"
  }
}
```

### エラーレスポンス

- 400 Bad Request  
  必要なデータが不足している場合。

```json
{
  "error": "Invalid input data"
}
```

---

## データ仕様

| フィールド名 | 型      | 必須 | 説明                     |
| ------------ | ------- | ---- | ------------------------ |
| `id`         | Integer | N/A  | うんこの一意な ID        |
| `name`       | String  | Yes  | うんこの名前             |
| `color_id`   | Integer | Yes  | うんこの色 ID            |
| `size_id`    | Integer | Yes  | うんこのサイズ ID        |
| `color`      | Object  | Yes  | うんこの色 (id,name)     |
| `size`       | Object  | Yes  | うんこのサイズ (id,name) |

---

## ステータスコード一覧

| ステータスコード | 説明                   |
| ---------------- | ---------------------- |
| 200              | 成功                   |
| 201              | リソースが作成された   |
| 400              | リクエストが無効       |
| 404              | リソースが見つからない |
