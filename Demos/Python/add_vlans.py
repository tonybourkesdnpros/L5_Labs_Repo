import yaml
import pyeapi

# Open VLANs file
file = open('vlans.yml', 'r')
pyeapi.load_config('eapi.conf')
vlan_dict = yaml.safe_load(file)

# Loop through the list of switches
for switch in vlan_dict['switches']:
    print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    vlan_api = connect.api('vlans')
    # Loop through the VLANs 
    for vlan in vlan_dict['vlans']:
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f"Adding VLAN {vlan_id} to {switch}")
        vlan_api.create(vlan_id)
        vlan_api.set_name(vlan_id, vlan_name)