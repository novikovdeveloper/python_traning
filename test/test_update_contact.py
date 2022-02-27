

def test_update_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_contact()
    app.session.logout()