from fastapi import HTTPException

def toplama(a, b):
    return a + b   

def cikarma(a,b):
    return a-b
def carpma(a, b):
    return a*b

def bolme(a,b):
    if b==0:
        raise HTTPException(status_code=400, detail="Sıfıra bölme hatası Şerif abeeeeeee!")
    else:
        return a/b
    
    

