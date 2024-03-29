
from configs.globalconfig import default_region


## Devops Account
devops_account = { "account": 'xxxxxx', "region": default_region }

## CI/CD managed Accounts
managed_accounts = {
    "dev" : {

            "enabled": True,
            "account": 'xxxxxx', 
            "region": default_region, 
            "vpc_id": "vpc-c50f3bbf",
            "private_subnets": [ "subnet-8de942c0", "subnet-465ebb19" ],
  },
    "prod" : {

            "enabled": True,
            "account": 'xxxxxx', 
            "region": default_region, 
            "vpc_id": "vpc-c50f3bbf",
            "private_subnets": [ "subnet-8de942c0", "subnet-465ebb19" ],

    },
}