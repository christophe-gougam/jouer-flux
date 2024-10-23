from app.model.repositories import RuleRepo
from app.schemas import Rule
from flask import request

ruleRepo = RuleRepo()
ruleSchema = Rule()
ruleListSchema = Rule(many=True)
ITEM_NOT_FOUND = "Rule not found for id: {}"


def get(id):
    rule_data = ruleRepo.getById(id)
    if rule_data:
        return ruleSchema.dump(rule_data)
    return {'message': ITEM_NOT_FOUND.format(id)}, 404

def update(id):
    rule_data = ruleRepo.getById(id)
    rule_req_json = request.get_json()
    if rule_data:
        rule_data.rule_type = rule_req_json['rule_type']
        rule_data.source = rule_req_json['source']
        rule_data.destination = rule_req_json['destination']
        rule_data.policy_id = rule_req_json['policy_id']
        ruleRepo.update(rule_data)
        return ruleSchema.dump(rule_data)
    return {'message': ITEM_NOT_FOUND.format(id)}, 404

def delete(id):
    rule_data = ruleRepo.getById(id)
    if rule_data:
        ruleRepo.delete(id)
        return {'message': 'Rule deleted successfully'}, 200
    return {'message': ITEM_NOT_FOUND.format(id)}, 404

def create():
    rule_req_json = request.get_json()
    rule_data = ruleSchema.load(rule_req_json)
    ruleRepo.create(rule_data)
    return ruleSchema.dump(rule_data),201

def getAll():
    return ruleListSchema.dump(ruleRepo.getAll()), 200
    