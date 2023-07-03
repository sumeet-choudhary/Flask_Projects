from username_pass.views import username_pass_blueprint
from restfull import app

app.register_blueprint(username_pass_blueprint)

if __name__ == '__main__':
    app.run(debug=True)




