from app.model.objects import Firewall, Rule, Policy
from app.marshmallow import ma

class Firewall(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Firewall
        load_instance = True

class Policy(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Policy
        load_instance = True

class Rule(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rule
        load_instance = True