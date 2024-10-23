from app.db import db

class Firewall(db.Model):
    __tablename__ = 'firewall'
    
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(80), nullable=False)
    
    # Relation : un firewall peut avoir plusieurs politiques de filtrage
    policies: list[dict] = db.relationship('Policy', backref='firewall', cascade="all, delete", lazy=True)

    def __str__(self):
        return 'FirewallModel(id=%d,name=%s, policies=%s,)' % (self.id, self.name, self.policies)

    def json(self):
        return {'id':self.id,'name': self.name, 'policies': self.policies}

class Policy(db.Model):
    __tablename__ = 'policy'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    firewall_id = db.Column(db.Integer, db.ForeignKey('firewall.id'), nullable=False)
    
    # Relation : une politique de filtrage peut avoir plusieurs règles de firewall
    rules = db.relationship('Rule', backref='policy', cascade="all, delete", lazy=True)

    def __str__(self):
        return 'PolicyModel(id=%d,name=%s, firewall_id=%d, rules=%s,)' % (self.id, self.name, self.firewall_id, self.rules)

    def json(self):
        return {'id':self.id,'name': self.name, 'firewall_id': self.firewall_id, 'rules': self.rules}
    
class Rule(db.Model):
    __tablename__ = 'rule'
    
    id = db.Column(db.Integer, primary_key=True)
    rule_type = db.Column(db.String(50), nullable=False)
    source = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    policy_id = db.Column(db.Integer, db.ForeignKey('policy.id'), nullable=False)

    def __str__(self):
        return 'RuleModel(id=%d,rule_type=%s, source=%d, destination=%s, policy_id=%d)' % (self.id, self.rule_type, self.source, self.destination, self.policy_id)

    def json(self):
        return {'id':self.id,'rule_type': self.rule_type, 'source': self.source, 'destination': self.destination, "policy_id": self.policy_id}