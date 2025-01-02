import click

from src import create_app, db
from src.db.models.user import User

app = create_app()


@app.cli.command("create_admin")
def create_admin():
    with app.app_context():
        if User.query.filter_by(role="admin").first():
            click.echo("Администратор уже существует.")
            return

        admin = User()
        admin.username = "admin"
        admin.role = "admin"
        admin.set_password("admin")

        db.session.add(admin)
        db.session.commit()

        click.echo("Администратор создан.")
