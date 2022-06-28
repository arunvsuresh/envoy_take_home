from flask import Flask, render_template, request, url_for, flash, redirect
import requests
from requests.auth import HTTPBasicAuth
from env_vars import client_id, client_secret, client_api_key, password
import base64
import basicauth
import json
import subprocess
import shlex


app = Flask(__name__)

def login():
	url = 'https://api.envoy.com/oauth2/token'

	data = {
		"username": "arunvsuresh@gmail.com",
		"password": password,
		"scope": "token.refresh,employees.read",
		"grant_type": "password"
	}

	res = requests.post(url, auth=(client_id, client_secret), data=data).json()
	return res

def token_refresh():
	url = 'https://api.envoy.com/oauth2/token'
	refresh_token = login()['refresh_token']
	data = {
		"client_id": client_id,
		"client_secret": client_secret,
		"refresh_token": refresh_token,
		"grant_type": "refresh_token"
	}

	res = requests.post(url, data=data)
	return res.json()

def get_employees():
	url = "https://api.envoy.com/v1/employees?page=1&perPage=10&sort=NAME&order=ASC"
	token = token_refresh()['access_token']

	headers = {
		"Accept": "application/json",
		"Authorization": "Bearer {0}".format(token)
	}

	res = requests.get(url, headers=headers)

	return res.text

@app.route('/', methods=('GET', 'POST'))
def validation_url():
	# https://arun-sample-app.herokuapp.com/
	duration = input()
	return duration








