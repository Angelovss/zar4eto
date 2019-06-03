from flask import Flask
app = Flask(__name__)

@app.route("/")

import random
while True:
 zar4e = random.randint(1,6)
 zar4e2 = random.randint(1,6)
 print ( " ZAR1 Rolled :", zar4e)
 print ( " ZAR2 Rolled :", zar4e2)
 input("Press any key to roll again.")