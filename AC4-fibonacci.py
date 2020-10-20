import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')

def fibonacci():
    anterior = 0
    proximo = 0
    fibo = []
    cont = 0
    saida = "Fibonacci: "

    for i in range(50):
        fibo.append(proximo)
        proximo = proximo + anterior
        anterior = proximo - anterior
        if(proximo == 0):
            proximo = proximo + 1

    for j in fibo:
        cont += 1
        j = str(j)
        saida += j
        if cont < 50:
            saida +=  ", "
            
    saida += "."
    return saida

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port=port)

