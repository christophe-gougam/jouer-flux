from app.db import db

class Firewall(db.Model):
    __tablename__ = 'firewall'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    
    # Relation : un firewall peut avoir plusieurs politiques de filtrage
    policies = db.relationship('Policy', backref='firewall', cascade="all, delete", lazy=True)

class Policy(db.Model):
    __tablename__ = 'policy'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    firewall_id = db.Column(db.Integer, db.ForeignKey('firewall.id'), nullable=False)
    
    # Relation : une politique de filtrage peut avoir plusieurs règles de firewall
    rules = db.relationship('Rule', backref='policy', cascade="all, delete", lazy=True)

class Rule(db.Model):
    __tablename__ = 'rule'
    
    id = db.Column(db.Integer, primary_key=True)
    rule_type = db.Column(db.String(50), nullable=False)  # Exemple : "ACCEPT", "DROP"
    source = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    policy_id = db.Column(db.Integer, db.ForeignKey('policy.id'), nullable=False)
