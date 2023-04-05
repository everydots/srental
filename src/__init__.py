from flask import Flask


def create_app(config_class='config.ProductionConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .controllers import spaceship
    app.register_blueprint(spaceship.bp)

    return app
