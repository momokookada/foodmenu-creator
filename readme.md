## README.md

# 家族の1週間献立生成アプリ

このアプリは、冷蔵庫にある食材と栄養価情報から、家族の1週間分の献立を自動生成できるローカルWebアプリです。
FlaskとSQLiteを使用しており、インターネット接続なしでPC上で動作します。

---

## 主な機能

* **冷蔵庫の食材管理**
  追加・編集・削除が可能。食材の在庫状況を保存できます。
* **レシピ管理**
  材料・カロリー・PFC（タンパク質・炭水化物・脂質）を登録可能。
* **人数設定**
  家族の人数に合わせて献立を調整。
* **1週間の献立自動生成**
  登録されたレシピと冷蔵庫の食材をもとに、栄養バランスを考慮した献立を生成。
* **レシピ一覧表示**
  テーブル形式で登録済みレシピを閲覧。

---

## 技術スタック

* **バックエンド**: Python 3 + Flask
* **データベース**: SQLite3
* **フロントエンド**: HTML + Bootstrap 5
* **動作環境**: Windows / macOS / Linux（ローカル実行）

---

## セットアップ

1. **リポジトリをクローン**

```bash
git clone https://github.com/momokookada/foodmenu-creator.git
cd foodmenu-creator
```

2. **依存ライブラリのインストール**

```bash
pip install -r requirements.txt
```

※ `sqlite3` は多くのPython環境で標準搭載されています。

3. **アプリを起動**

```bash
python3 app.py
```

4. **ブラウザでアクセス**

```
http://127.0.0.1:5000/
```

---

## フォルダ構成

```
foodmenu-creator/
│ app.py                  # Flaskアプリ本体
│ database.db             # SQLiteデータベース
│ requirements.txt        # 必要ライブラリ
└ templates/
    ├ index.html           # トップページ（食材・レシピ管理）
    └ plan.html            # 1週間献立ページ
```

---

## 今後の改善予定

* 栄養バランスを自動最適化するアルゴリズム
* 献立のPDF出力
* 食材の使用期限管理
* 買い物リスト自動生成機能

---
