from flask import Flask
from app.blockchain import Blockchain
from uuid import uuid4

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()