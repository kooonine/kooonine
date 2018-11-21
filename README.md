# DAO vote

It's a simple SCORE to vote

## Purpose
dao_vote is a simple vote SCORE. You can add or remove users by voting, Proportional to the number of users
The number of votes will change.
## Structure
```
dao_vote
├── README.md
├── dao_vote
│   ├── __init__.py
│   ├── dao_vote.py
│   └── package.json
├── tests
│   ├── keystore_test1
│   └── test.py
├── deploy.json
├── call.json
└── send.json
```

## How To Use
### Available people
Users registered with dao_vote SCORE(The first user is deployee)

### SCORE deployment
    tbears deploy -k <keystore_file> -c deploy.json ./dao_vote

The deploy.json option is not required when deploying.

## Specification
### Methods

#### add_user
Suggests a new user to SCORE

    @external
    def add_user(self, contents: Address) -> None:
 
#### Example
    
    {
      "jsonrpc": "2.0",
      "method": "icx_sendTransaction",
      "params": {
        "version": "0x3",
        "stepLimit": "0x300000000000000000000000000",
        "timestamp": "0x573117f1d6568",
        "nid": "0x3",
        "to": "cxa9bd7bae66565016f5515866d794c4ae5d692a1d",
        "dataType": "call",
        "data": {
          "method": "add_user",
          "params": {"contents":"hx485c66c60229f31ab3f130753caf6822078714f1"

          }
        }
      },
      "id": 1
    }
    
#### Sendtx result
  
    Transaction result: {
        "jsonrpc": "2.0",
        "result": {
            "txHash": "0xf9cd30152af278924a7302186923449d26e94d33e8d9c785cccb75789b7c358d",
            "blockHeight": "0xd4b3",
            "blockHash": "0x531b64d2588b7ec8849adff43084c41f68da73b2c2b6a0101dcbbc24c5b67b86",
            "txIndex": "0x0",
            "to": "cxa9bd7bae66565016f5515866d794c4ae5d692a1d",
            "stepUsed": "0x1045a0",
            "stepPrice": "0x0",
            "cumulativeStepUsed": "0x1045a0",
            "eventLogs": [],
            "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "status": "0x1"
        },
        "id": 1
    }

#### remove_user
Suggest removal of existing users to SCORE

    @external
    def remove_user(self, contents: Address) -> None:
 
#### Example

    {
      "jsonrpc": "2.0",
      "method": "icx_sendTransaction",
      "params": {
        "version": "0x3",
        "stepLimit": "0x300000000000000000000000000",
        "timestamp": "0x573117f1d6568",
        "nid": "0x3",
        "to": "cxa9bd7bae66565016f5515866d794c4ae5d692a1d",
        "dataType": "call",
        "data": {
          "method": "remove_user",
          "params": {"contents":"hx485c66c60229f31ab3f130753caf6822078714f1"
    
          }
        }
      },
      "id": 1
    }
    
#### Sendtx result

    Transaction result: {
        "jsonrpc": "2.0",
        "result": {
            "txHash": "0x8d2213f2270faafe76614438d15cf59fa8e26f015e0eea7bd57f87b0015a8d90",
            "blockHeight": "0xd52d",
            "blockHash": "0x90723b7bdba446434c86672d1d5f0bc7f0fc826e8f4cf56c573f8431d7a51e33",
            "txIndex": "0x0",
            "to": "cxa9bd7bae66565016f5515866d794c4ae5d692a1d",
            "stepUsed": "0x104762",
            "stepPrice": "0x0",
            "cumulativeStepUsed": "0x104762",
            "eventLogs": [],
            "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "status": "0x1"
        },
        "id": 1
    }

#### ox
Propose Opposition vote

    @external
    def ox(self, contents: str) -> None:

#### Example

    {
      "jsonrpc": "2.0",
      "method": "icx_sendTransaction",
      "params": {
        "version": "0x3",
        "stepLimit": "0x300000000000000000000000000",
        "timestamp": "0x573117f1d6568",
        "nid": "0x3",
        "to": "cxa9bd7bae66565016f5515866d794c4ae5d692a1d",
        "dataType": "call",
        "data": {
          "method": "ox",
          "params": {"contents":"hello_world"
    
          }
        }
      },
      "id": 1
    }

#### Sendtx result

    Transaction result: {
        "jsonrpc": "2.0",
        "result": {
            "txHash": "0x580a29348cab67b77f79fc3a2f7c26961949183a94bd552177a752f203ff2eff",
            "blockHeight": "0xd53d",
            "blockHash": "0x698b3d77a037fe32e0f8349f92a81242473a303b424d65d9c8edc3f078e7fbe6",
            "txIndex": "0x0",
            "to": "cxa9bd7bae66565016f5515866d794c4ae5d692a1d",
            "stepUsed": "0x100fea",
            "stepPrice": "0x0",
            "cumulativeStepUsed": "0x100fea",
            "eventLogs": [],
            "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "status": "0x1"
        },
        "id": 1
    }

#### vote
I vote for the agenda I want
    
    @external
    def vote(self, code: str, vote_res: int) -> None:

#### Example

    {
      "jsonrpc": "2.0",
      "method": "icx_sendTransaction",
      "params": {
        "version": "0x3",
        "stepLimit": "0x300000000000000000000000000",
        "timestamp": "0x573117f1d6568",
        "nid": "0x3",
        "to": "cxa9bd7bae66565016f5515866d794c4ae5d692a1d",
        "dataType": "call",
        "data": {
          "method": "vote",
          "params": {"code":"A0", "vote_res":"1"
    
          }
        }
      },
      "id": 1
    }

#### Sendtx result

    Transaction result: {
        "jsonrpc": "2.0",
        "result": {
            "txHash": "0x1adc819108b2b9757c2f75abaa3f8a0ee04e48d5b08d781ae9a309e7899e2b8b",
            "blockHeight": "0xd521",
            "blockHash": "0x3912546e610a4112025beb4e820b6f92414f155e386b292860a71af1ab462e50",
            "txIndex": "0x0",
            "to": "cxa9bd7bae66565016f5515866d794c4ae5d692a1d",
            "stepUsed": "0xfb3ba",
            "stepPrice": "0x0",
            "cumulativeStepUsed": "0xfb3ba",
            "eventLogs": [],
            "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "status": "0x1"
        },
        "id": 1
    }

#### vote_list_delete
Delete voting list

    @external
    def vote_list_delete(self,code: str) -> None:
    
#### Example

    {
      "jsonrpc": "2.0",
      "method": "icx_sendTransaction",
      "params": {
        "version": "0x3",
        "stepLimit": "0x300000000000000000000000000",
        "timestamp": "0x573117f1d6568",
        "nid": "0x3",
        "to": "cxa9bd7bae66565016f5515866d794c4ae5d692a1d",
        "dataType": "call",
        "data": {
          "method": "vote_list_delete",
          "params": {"code":"O2"
    
          }
        }
      },
      "id": 1
    }
    
#### Sendtx result

    Transaction result: {
        "jsonrpc": "2.0",
        "result": {
            "txHash": "0x452c2383047e3b6b507c678fd1c2d97899e8803e375fb1ff746a408240adcdbe",
            "blockHeight": "0xd557",
            "blockHash": "0xbcd218a00208e74b6218779dfe1e7bd1cd4a97c842c362be6d633d4cfbb05479",
            "txIndex": "0x0",
            "to": "cxa9bd7bae66565016f5515866d794c4ae5d692a1d",
            "stepUsed": "0xfb068",
            "stepPrice": "0x0",
            "cumulativeStepUsed": "0xfb068",
            "eventLogs": [],
            "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "status": "0x1"
        },
        "id": 1
    }

#### vote_list
Check the voting list

    @external(readonly=True)
    def vote_list(self) -> str:
    
#### Example

    {
      "jsonrpc": "2.0",
      "method": "icx_call",
      "params": {
        "from": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
        "to": "cxa9bd7bae66565016f5515866d794c4ae5d692a1d",
        "dataType": "call",
        "data": {
          "method": "vote_list",
          "params": {
    
          }
        }
      },
      "id": 1
    }
    
#### Call result

    response : {
        "jsonrpc": "2.0",
        "result": [
            "CODE : A0 info : {\"contents\": \"hx485c66c60229f31ab3f130753caf6822078714f1\", \"date\": \"1542761884077347\", \"total_num\": \"1\", \"agree_num\": 0, \"opposition_num\": \"0\", \"proposer\": \"hxe7af5fcfd8dfc67530a01a0e403882687528dfcb\", \"result\": \"Allow\"} vote check : 1",
            "CODE : R1 info : {\"contents\":\"hx485c66c60229f31ab3f130753caf6822078714f1\",\"date\":\"1542763104672933\",\"total_num\":\"2\",\"agree_num\":\"2\",\"opposition_num\":\"1\",\"proposer\":\"hxe7af5fcfd8dfc67530a01a0e403882687528dfcb\",\"result\":\"\"} vote check : 0",
            "CODE : O2 info : {\"contents\": \"hello_world\", \"date\": \"1542763264738575\", \"total_num\": \"2\", \"agree_num\": \"2\", \"opposition_num\": \"1\", \"proposer\": \"hxe7af5fcfd8dfc67530a01a0e403882687528dfcb\", \"result\": \"Delete\"} vote check : 0"
        ],
        "id": 1
    }




## Run test

Testcase uses python sdk. You need to install python sdk to run the test.
    
    pip3 install iconsdk
    
The value can be changed depending on the environment

    node_uri = "http://localhost:9000/api/v3"
    network_id = 3
    vote_dao_address = "cx3f9f66cd7478d8dfa85cdf977965000e97bedcba"
    basic_step_limit = 3000000000000000000000
    basic_timestamp = 0x573117f1d6568
    keystore_path = "./keystore_test1"
    keystore_pw = "test1_Account"


- Run the test.

```bash
$ python3 test.py
....
----------------------------------------------------------------------
Ran 4 tests in 30.483s

OK
```