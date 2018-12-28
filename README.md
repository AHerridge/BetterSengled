![Demo Image](https://lh3.googleusercontent.com/WPIb4nTBzjEhDMZC1NBjdnjixULmED59ishlprCHGziMi4afBRQRPda1RvhRYVcP0EBojxmnPk8uoNo-oPrArPxy-3nobfid0CJfXlAOACEMSVeIa-epRcnZ91KMG-X4iRjmA3vcSizVgccgWHUgboatxEMVjTBisLktPNSPOKX5iRUsrHAODnbrTsigwQopjOzyq5NR230unH9RNPnAvHojN660NPnEs7VwLVZSxebSa5UZi77F_2MS9euv-DKslwo0-acB8KQqzVZBZFp1efv0Re7d6ZlBpsQgZkg2jDa5B4BKmTULzOBL0eQheMt26nkP6hCVqHFWUb4X5guXs_b0sj_wxYQJR9RYXLT03HW7Au7-3Jfv3ornvg4-pEEx5KM4cL_dqaKYNcbJoaTcXiykCBMHOcNAPHDmqLrwdFiJafeHyGsjOUzY1xHfunH1K4uCr8pe-24ga4aohfAWxHUWuqGblO0UddH7iDL7RbrfVa_mQeENCsYR7ELiN0JIxxBV0MzD_LsiUZgP3l4EmZq9EEpIAPkWSrbVPNtleCksFMHCzu4Qpqclq4KmxbPHudv_j73nSnUc5_ZyGtyPFJA0v_egGJff2goKc6B56VMqNhoX3S39O-nGSFX8frwfiRoR02uAz-2NQA0vaxVQHZBp_A=w1667-h912-no)

# Flask-based Sengled Interface
[flask](http://flask.pocoo.org/): to provide web endpoints for easy automation using IFTTT etc.

[sengled-python](https://github.com/sroehl/sengled-python): to interface with the Sengled Element api

## Devices Tested
* [Element Classic](https://us.sengled.com/products/element-classic-bulb) (Dimmable)
* [Element Plus](https://us.sengled.com/products/element-plus-bulb) (Dimmable, Tunable White)

## Getting Started
**You must change the "username" and "password" in setup.py**

In console type:

```sh
export FLASK_APP=setup.py
export FLASK_ENVIRONMENT=development
flask run
```

Open in web browser - default: [localhost:5000/home](http://localhost:5000/home)

**See actions for advanced examples of how to use the library to control Sengled Element bulbs.**

## API Endpoints
- /devices -> get all devices as json list
- /devices/<device_id> -> get data for device identified by device_id as json
- /devices/<device_id>/<trait_name>/<new_value> -> set device trait to value and return "Success" or "Failure"
- /actions/<action_name> -> executes action

Device traits are defined in devices.py
