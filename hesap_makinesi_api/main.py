
from fastapi import FastAPI
from app.islemler import toplama, cikarma, carpma, bolme

app = FastAPI(title="Matematik API", description="Basit matematik işlemleri için API", version="1.0")
@app.get("/topla")
def topla_api(x: float, y: float):
    return {"sonuc": toplama(x, y)}

@app.get("/cikar")
def cikar_api(a: float, b: float):
   
    return {"sonuc": cikarma(a, b)}

@app.get("/carp")
def carp_api(a: float, b: float):
    return {"sonuc": carpma(a, b)}

@app.get("/bol")
def bol_api(a: float, b: float):
    return {"sonuc": bolme(a, b)}
