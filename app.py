from flask import Flask, render_template, url_for, request, redirect, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'


@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/deploy/', methods=['POST', 'GET'])
def index():
    return render_template('deploy.html')

@app.route('/payToMint/<chainId>/<contract_address>', methods=['GET'])
def payToMintFunc(chainId, contract_address):
    return render_template('payToMint.html', contract_address=contract_address,chainId=chainId)

@app.route("/getOwned/<chainId>/<contract_address>",methods=["GET"])
def getOwned(chainId, contract_address):
    return render_template('getOwnedTokenList.html', contract_address=contract_address,chainId=chainId)

@app.route("/withdrawSale/<chainId>/<contract_address>",methods=["GET"])
def withdrawSell(chainId, contract_address):
    return render_template('withdrawSale.html', contract_address=contract_address, chainId=chainId)


@app.route("/redirect/<fn>", methods=["GET","POST"])
def getAddress(fn):
    if request.method == 'POST':
        address = request.form['address']
        chainId = request.form['chainId']
        fn = int(fn)
        if fn == 2:
            return redirect("/payToMint/"+chainId+"/"+address)
        elif fn == 3:
            return redirect("/getOwned/"+chainId+"/"+address)
        elif fn == 4:
            return redirect("/withdrawSale/"+chainId+"/"+address)
        else:
            return ("No Such Functiosn")
    else:
        return render_template('redirect.html', fn=fn)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
