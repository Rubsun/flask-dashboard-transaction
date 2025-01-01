from flask import Flask

app: Flask


def setup_app(app_: Flask) -> None:
    global app
    app = app_


def get_app() -> Flask:
    global app
    return app
