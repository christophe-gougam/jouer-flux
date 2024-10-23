from app.model.repositories import PolicyRepo
from app.schemas import Policy
from flask import request

policyRepo = PolicyRepo()
policySchema = Policy()
policyListSchema = Policy(many=True)
ITEM_NOT_FOUND = "Policy not found for id: {}"


def get(id):
    policy_data = policyRepo.getById(id)
    if policy_data:
        return policySchema.dump(policy_data)
    return {'message': ITEM_NOT_FOUND.format(id)}, 404

def update(id):
    policy_data = policyRepo.getById(id)
    policy_req_json = request.get_json()
    if policy_data:
        policy_data.name = policy_req_json['name']
        policy_data.firewall_id = policy_req_json['firewall_id']
        policy_data.rules - policy_req_json['rules']
        policyRepo.update(policy_data)
        return policySchema.dump(policy_data)
    return {'message': ITEM_NOT_FOUND.format(id)}, 404

def delete(id):
    policy_data = policyRepo.getById(id)
    if policy_data:
        policyRepo.delete(id)
        return {'message': 'Policy deleted successfully'}, 200
    return {'message': ITEM_NOT_FOUND.format(id)}, 404

def create():
    policy_req_json = request.get_json()
    policy_data = policySchema.load(policy_req_json)
    policyRepo.create(policy_data)
    return policySchema.dump(policy_data),201

def getAll():
    return policyListSchema.dump(policyRepo.getAll()), 200
    