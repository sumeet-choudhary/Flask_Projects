from username_pass.views import views_file
from restfull import app

app.register_blueprint(views_file)


if __name__ == '__main__':
    app.run(debug=True)




