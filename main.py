from fastapi import FastAPI

app = FastAPI()

pecas = {
    1: {"item": "shape", "preco_unitario": 300, "quantidade": 1},
    2: {"item": "lixa", "preco_unitario": 75, "quantidade": 1},
    3: {"item": "truck", "preco_unitario": 400, "quantidade": 2},
    3: {"item": "parafuso", "preco_unitario": 25, "quantidade": 1},
    5: {"item": "roda", "preco_unitario": 350, "quantidade": 4},
    6: {"item": "rolamento", "preco_unitario": 150, "quantidade": 8},
}

@app.get("/")
def home():
        return{"Vendas": len(pecas)}

@app.get("/pecas/{id_peca}")
def pegar_venda(id_peca: int):
    if id_peca in pecas:
        return pecas[id_peca]
    else:
         return {"Erro": "Chapelaram as tuas peças"}
