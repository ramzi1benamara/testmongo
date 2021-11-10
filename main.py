import streamlit as st
import pymongo
from pymongo import MongoClient
import pandas as pd


client = pymongo.MongoClient("mongodb+srv://ramziadmin:ramziadmin@cluster1.e6ban.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('sample_training')
routes = db['routes']
cursor = routes.find({"dst_airport": "KZN"}, {"_id": 0, "src_airport": 1})
b = pd.DataFrame(cursor)
st.write(b)
