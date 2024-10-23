from app.db import db
from app.model.objects import Firewall, Policy, Rule
from typing import List


class FirewallRepo:
    
 def create(self,firewall):
    db.session.add(firewall)
    db.session.commit()
    
 def getById(self,_id)-> 'Firewall':
     return db.session.query(Firewall).filter_by(id=_id).first()
 
 def getAll(self) -> List['Firewall']:
     return db.session.query(Firewall).all()
 
 def delete(self,_id) -> None:
     firewall= db.session.query(Firewall).filter_by(id=_id).first()
     db.session.delete(firewall)
     db.session.commit()
     
 def update(self,firewall_data):
    db.session.merge(firewall_data)
    db.session.commit()

class PolicyRepo:
    
 def create(self,policy):
    db.session.add(policy)
    db.session.commit()
    
 def getById(self,_id)-> 'Policy':
     return db.session.query(Policy).filter_by(id=_id).first()
 
 def getAll(self) -> List['Policy']:
     return db.session.query(Policy).all()
 
 def delete(self,_id) -> None:
     policy= db.session.query(Policy).filter_by(id=_id).first()
     db.session.delete(policy)
     db.session.commit()
     
 def update(self,policy_data):
    db.session.merge(policy_data)
    db.session.commit()

class RuleRepo:
    
 def create(self,rule):
    db.session.add(rule)
    db.session.commit()
    
 def getById(self,_id)-> 'Rule':
     return db.session.query(Rule).filter_by(id=_id).first()
 
 def getAll(self) -> List['Rule']:
     return db.session.query(Rule).all()
 
 def delete(self,_id) -> None:
     rule= db.session.query(Rule).filter_by(id=_id).first()
     db.session.delete(rule)
     db.session.commit()
     
 def update(self,rule_data):
    db.session.merge(rule_data)
    db.session.commit()