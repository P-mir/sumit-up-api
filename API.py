# to load the app:  uvicorn API:app --reload
# Entry point  at http://127.0.0.1:8000 per default
# # to watch documentation http://127.0.0.1:8000/docs alternative doc : http://127.0.0.1:8000/redoc
# http://sumit-up-api.herokuapp.com/doc

## Put all elements together and package it into an API
import uvicorn
from typing import Optional
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import json
from sum_it_up import *

example = """In 1425, Dukes of Brabant created the University of Louvain[7] (Université de Louvain), which was suppressed under Joseph II, reopened in 1790, and was finally closed under the French Republic in 1797.[8]
In 1817, the State University of Louvain (Université de l'Etat de Louvain) was founded, which closed 15 August 1835. Université catholique de Louvain (also known as the Catholic University of Louvain, the English translation of its French name, and the University of Louvain, its official English name)[2] is Belgium's largest French-speaking university. It is located in Louvain-la-Neuve, which was expressly built to house the university, and Brussels, Charleroi, Mons, Tournai and Namur. Since September 2018, the university has used the branding UCLouvain, replacing the acronym UCL, following a merger with Saint-Louis University, Brussels."""

app = FastAPI()



class Document(BaseModel):
    document: str = Field(None, example = example)
    ratio: Optional[float] = Field(0.5, example = 0.5)
    nb_sentences: Optional[int] = Field(None, example = None)



@app.post("/summary")
async def sum_it_up_resume(data : Document):
    """Takes into input a document and return a summary""" 
    response = {"summary": resume(data.document,data.ratio, data.nb_sentences)}
    return response

# @app.post("/summary")
# async def sum_it_up_resume(data : Document):
#     """Takes into input a document and return a summary"""
#     document = data.document
#     nb_sentences =  data.nb_sentences
#     response = {"summary": resume(document, nb_sentences)}
#     return response

class Summary(BaseModel):   
    summary: str = Field(None)


@app.post("/pdf")
def sum_it_up_pdf(query : Summary):
    """Takes into input a summary and return a pdf document."""
    summary = query.summary
    return text_to_pdf(summary)



@app.post("/tts")
def sum_it_up_tts(query : Summary):
    """Takes into input a summary and return a mp3 file"""
    summary = query.summary
    return tts(summary)




if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0')