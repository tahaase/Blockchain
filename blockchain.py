#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:28:30 2018

@author: Thomas
"""
from block import Block

class Blockchain:
    def __init__(self):
      self.chain = []
      self.all_transactions = []
      #Create genesis block
      self.genesis_block()

    
    def genesis_block(self):
      transactions = {}
      genesis_block = Block(transactions, "0")
      self.chain.append(genesis_block)
      return self.chain
  
    def print_blocks(self):
        for ii in range(len(self.chain)):
            current_block = self.chain[ii]
            print("Block {} {}".format(ii, current_block))
            current_block.print_block()    
            
    def add_block(self, transactions):
        previous_block_hash = self.chain[len(self.chain)-1].hash
        new_block = Block(transactions,previous_block_hash)
        self.chain.append(new_block)
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return proof, new_block
    
    def validate_chain(self):
        for ii in range(1, len(self.chain)):
            current = self.chain[ii]
            previous = self.chain[ii-1]
      
            if(current.hash != current.generate_hash()):
                print("The current hash and generated hash of the block are not equal. Block:",ii)
                return False
      
            if(current.previous_hash != previous.generate_hash()):
                print("The previous block's hash is not equal to the value stored in the current block. Block:",ii)
                return False
    
        return True
    
    def proof_of_work(self,block, difficulty=2):
        proof = block.generate_hash()
        while ( proof[0:difficulty] != '0' * difficulty):
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof