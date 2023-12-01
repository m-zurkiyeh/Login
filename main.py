from flask import Flask, request, jsonify
import json
from db_manager import db_manager
from connector import connector


if __name__ == '__main__':
    conn = connector()
    dbm = db_manager()