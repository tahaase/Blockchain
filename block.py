#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:21:44 2018

@author: Thomas
"""

from datetime import datetime
from hashlib import sha256

class Block:
  def __init__(self, transactions, previous_hash, nonce = 0):
    self.timestamp = datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.hash = self.generate_hash()
    
  def print_block(self):
    # prints block contents
    print("Timestamp:", self.timestamp)
    print("Transactions:", self.transactions)
    print("Current hash:", self.generate_hash())
    print("Previous hash:", self.previous_hash())
    
  def generate_hash(self):
    block_contents = str(self.timestamp) + str(self.transactions) +  str(self.nonce) + str(self.previous_hash)
    block_hash = sha256(block_contents.encode())
    return block_hash.hexdigest()

