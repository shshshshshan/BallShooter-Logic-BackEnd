from main import getCOG
from flask import Flask, request, jsonify
from flask_cors import CORS
from time import sleep
import os

app = Flask(__name__);
CORS(app)

@app.route('/', methods=['POST'])
def root():
  data = request.get_json()

  required_payload = [
    'proximity',
    'height'
  ]

  for payload in required_payload:
     if payload not in data:
      return jsonify({ 'error' : 'Missing required payloads' }), 400
     
  print('Fuzzibellsication 🚀')


  try:
    result = getCOG(data['proximity'], data['height'])
  except:
    return jsonify({ 'error', 'Something went wrong with the solver'}), 400
  
  print('Done fuzzifying ❤️')

  return jsonify({ 'force': result }), 200

if __name__ == '__main__':
  #  os.system('cls' if os.name == 'nt' else 'clear')
   app.run(debug=True)