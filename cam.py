from flask import Flask
from flask import make_response
import camelot
import os
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello():
    directory = os.path.dirname(os.path.realpath(__file__))
    tables = camelot.read_pdf(f'{directory}/Direct Bill Commission Statement.pdf',pages='all',flavor='stream')
    df = tables[0].df
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=output.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

if __name__ == "__main__":
    app.run()    
