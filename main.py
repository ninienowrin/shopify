from fastapi import FastAPI, UploadFile, File
import pandas as pd
import csv, re
from utils import create_dataframe, modified_dataframe, get_frequency_of_purchase, get_customer_order_count
    
app = FastAPI()

@app.post("/")
async def root(file: UploadFile = File(...)):
    orig = await file.read()

    data = orig.decode('utf-8').splitlines()

    df = create_dataframe(data)
    df = modified_dataframe(df,['order_id','customer\.id',])

    return get_customer_order_count(df)