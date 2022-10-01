# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 01:23:21 2022

@author: Ahmed Tarek """

import cohere 
co = cohere.Client('rB5QMCCPPu9FfOLvTIA8dErKKReLCYWchcWVKYQz')
response = co.generate( 
  model='xlarge', 
  prompt='shark', 
  max_tokens=50, 
  temperature=0.9, 
  k=0, 
  p=0.75, 
  frequency_penalty=0, 
  presence_penalty=0, 
  stop_sequences=[], 
  return_likelihoods='NONE') 
print('Prediction: {}'.format(response.generations[0].text)) 