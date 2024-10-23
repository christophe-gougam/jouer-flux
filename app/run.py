import connexion
from app.marshmallow import ma
from app.db import db

#Create the application instance
connex_app = connexion.App("__name__",specification_dir='./')
connex_app.add_api('app/static/swagger.yml', arguments={'title': 'API JouerFlux'}, swagger_ui=True)

app = connex_app.app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return "<h1>Welcome to JouerFlux API</h1><p>Go to <a href='/swagger-ui/'>Swagger UI</a></p>"

if __name__ == '__main__':    
    app.run(port=5000, debug=True)