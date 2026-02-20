# ToDo REST API

[![Python](https://img.shields.io/badge/Python-3.12-green)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.x-orange)](https://djangoproject.com)

## 機能一覧

| Method | Endpoint | 機能 | レスポンス例 |
|--------|----------|------|-------------|
| `GET` | `/api/tasks/` | タスクリスト取得 | `[{id:1, title:"買い物", completed:false}]` |
| `POST` | `/api/tasks/` | タスク作成 | `{id:2, title:"新タスク", completed:false}` |
| `PATCH` | `/api/tasks/1/` | タスク編集 | `{id:1, completed:true}` |
| `DELETE` | `/api/tasks/1/` | タスク削除 | `204 No Content` |

## 技術スタック

Backend: Django 5.x + DRF  
Database: SQLite
