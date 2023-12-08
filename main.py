import streamlit as st
from items import morning_items, night_items
from datetime import datetime

current_time = datetime.now().time()
hour = current_time.hour  

st.set_page_config(menu_items=None,page_title="JASHMIN's MENU")
c1,c2,c3,c4,c5 = st.columns(5,gap = "small")
with c3:
        st.title("MENU")

st.title(" ")

cx1,cx2,cx3,cx4,cx5 = st.columns(5,gap = "small")
with cx1:
    st.title("ITEM")
    st.title("")
    for item in morning_items.keys():
        st.header(item)
        st.title("")
with cx2:
    st.title("PRICE")
    st.title("")
    for price in morning_items.values():
          st.header(f"{price} Rs")
          st.title("")   

with cx4:
    st.title("ITEM")
    st.title("")
    for item in morning_items.keys():
        st.header(item)
        st.title("")
with cx5:
    st.title("PRICE")
    st.title("")
    for price in morning_items.values():
          st.header(f"{price} Rs")
          st.title("")

# for item, price in morning_items.items():
#     with st.container(border=True):
#         c1, c2 = st.columns(2, gap='large')
#         with c1:
#             st.header(item)
#         with c2:
#             st.header(f"{price} Rs")  

# if hour >= 15:
#     tab1, tab2 = st.tabs(["NIGHT MENU","MORNING MENU"])
#     with tab1:
#         with st.container():
#             for item, price in morning_items.items():
#                 st.header(f"{item} - {price} Rs")
#     with tab2:
#         with st.container():
#             for item, price in morning_items.items():
#                 st.header(f"{item} - {price} Rs")            
# elif hour<15:
#     flag = "morning"      
#     tab1, tab2 = st.tabs(["MORNING MENU", "NIGHT MENU"])

#     with tab1:
#         with st.container():
#             for item, price in morning_items.items():
#                 st.header(f"{item} - {price} Rs")
#     with tab2:
#         with st.container():
#             for item, price in morning_items.items():
#                 st.header(f"{item} - {price} Rs")            