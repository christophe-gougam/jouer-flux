from app.model.repositories import FirewallRepo
from app.schemas import Firewall
from flask import request

firewallRepo = FirewallRepo()
firewallSchema = Firewall()
firewallListSchema = Firewall(many=True)
ITEM_NOT_FOUND = "Firewall not found for id: {}"


def get(id):
    firewall_data = firewallRepo.getById(id)
    if firewall_data:
        return firewallSchema.dump(firewall_data)
    return {'message': ITEM_NOT_FOUND.format(id)}, 404

def update(id):
    firewall_data = firewallRepo.getById(id)
    firewall_req_json = request.get_json()
    if firewall_data:
        firewall_data.name = firewall_req_json['name']
        firewall_data.policies = firewall_req_json['policies']
        firewallRepo.update(firewall_data)
        return firewallSchema.dump(firewall_data)
    return {'message': ITEM_NOT_FOUND.format(id)}, 404

def delete(id):
    firewall_data = firewallRepo.getById(id)
    if firewall_data:
        firewallRepo.delete(id)
        return {'message': 'Firewall deleted successfully'}, 200
    return {'message': ITEM_NOT_FOUND.format(id)}, 404

def create():
    firewall_req_json = request.get_json()
    firewall_data = firewallSchema.load(firewall_req_json)
    firewallRepo.create(firewall_data)
    return firewallSchema.dump(firewall_data),201

def getAll():
    return firewallListSchema.dump(firewallRepo.getAll()), 200
    