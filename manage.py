from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    admin = User(username='admin', password='admin', is_admin=True)
    db.session.add(admin)
    db.session.commit()
    print("Admin uživatel vytvořen: admin / admin")