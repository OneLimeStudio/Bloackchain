import hashlib
import json
from time import time
from uuid import uuid4


from flask import Flask, jsonify, request


class Blockchain(object):
    def __init__(self):
        self.current_transaction = []
        self.chain = []

    def proof_of_work(self, last_proof):


        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def newBlock(self,proof,previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.newTransaction,
            'proof': proof,
            'previous_hash':self.createHash(self.chain[-1])
        }
        self.current_transaction = []
        self.chain.append(block)

        return block

    def newTransaction(self,sender,recepient,amount):
        self.current_transaction.append({
            'sender':sender,
            'recepient':recepient,
            'amount': amount
        })
        return self.lastBlock['index'] + 1
        


    def createHash(block):
        block_string = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    def lastBlock():
        pass
        
    