swappa_router={
  "address" : "0xf35ed7156babf2541e032b3bb8625210316e2832",
  "abi": [
      {
        "anonymous": False,
        "inputs": [
          {
            "indexed": True,
            "internalType": "address",
            "name": "sender",
            "type": "address"
          },
          {
            "indexed": False,
            "internalType": "address",
            "name": "to",
            "type": "address"
          },
          {
            "indexed": True,
            "internalType": "address",
            "name": "input",
            "type": "address"
          },
          {
            "indexed": True,
            "internalType": "address",
            "name": "output",
            "type": "address"
          },
          {
            "indexed": False,
            "internalType": "uint256",
            "name": "inputAmount",
            "type": "uint256"
          },
          {
            "indexed": False,
            "internalType": "uint256",
            "name": "outputAmount",
            "type": "uint256"
          }
        ],
        "name": "Swap",
        "type": "event"
      },
      {
        "inputs": [
          {
            "internalType": "address[]",
            "name": "path",
            "type": "address[]"
          },
          {
            "internalType": "address[]",
            "name": "pairs",
            "type": "address[]"
          },
          {
            "internalType": "bytes[]",
            "name": "extras",
            "type": "bytes[]"
          },
          {
            "internalType": "uint256",
            "name": "inputAmount",
            "type": "uint256"
          }
        ],
        "name": "getOutputAmount",
        "outputs": [
          {
            "internalType": "uint256",
            "name": "outputAmount",
            "type": "uint256"
          }
        ],
        "stateMutability": "view",
        "type": "function"
      },
      {
        "inputs": [
          {
            "internalType": "address[]",
            "name": "path",
            "type": "address[]"
          },
          {
            "internalType": "address[]",
            "name": "pairs",
            "type": "address[]"
          },
          {
            "internalType": "bytes[]",
            "name": "extras",
            "type": "bytes[]"
          },
          {
            "internalType": "uint256",
            "name": "inputAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "minOutputAmount",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "to",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "deadline",
            "type": "uint256"
          }
        ],
        "name": "swapExactInputForOutput",
        "outputs": [
          {
            "internalType": "uint256",
            "name": "outputAmount",
            "type": "uint256"
          }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "inputs": [
          {
            "internalType": "address[]",
            "name": "path",
            "type": "address[]"
          },
          {
            "internalType": "address[]",
            "name": "pairs",
            "type": "address[]"
          },
          {
            "internalType": "bytes[]",
            "name": "extras",
            "type": "bytes[]"
          },
          {
            "internalType": "uint256",
            "name": "inputAmount",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "minOutputAmount",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "to",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "deadline",
            "type": "uint256"
          }
        ],
        "name": "swapExactInputForOutputWithPrecheck",
        "outputs": [
          {
            "internalType": "uint256",
            "name": "outputAmount",
            "type": "uint256"
          }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
      },
      {
        "stateMutability": "payable",
        "type": "receive"
      }
    ]
}
