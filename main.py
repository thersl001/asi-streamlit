import streamlit as st
import pandas as pd

st.title("📊 Annual Survey of Industries")

powerbi = "https://app.powerbi.com/view?r=eyJrIjoiMzgwMjAwZDUtNmEyZC00MWM4LThhMmYtZDgwYTZjODhmODMxIiwidCI6ImUxNGU3M2ViLTUyNTEtNDM4OC04ZDY3LThmOWYyZTJkNWE0NiIsImMiOjEwfQ%3D%3D"

st.markdown(f"""
    <iframe title="Power BI Report"
            width="800" height="500"
            src="{powerbi}"
            frameborder="0" allowFullScreen="true">
    </iframe>
""", unsafe_allow_html=True)

st.markdown('---')

st.header('🔍 Findings')
st.subheader('🏆 Top 10 States by Number of Factories in 2023')

data1 = {
    'States': ['Tamilnadu','Gujarat','Maharashtra','Uttar Pradesh','Andhra Pradesh','Karnataka','Punjab','Telangana','Haryana','Rajasthan'],
    'Factories': [39665,31033,26447,19103,16484,14512,13230,13065,10603,10529]}

df1 = pd.DataFrame(data=data1)

df1.index = range(1, len(df1)+1)

st.dataframe(df1)

data4 = {
    'Industry':[
                'Manufacture of Food Products',
                'Manufacture of Other Non-Metallic Mineral Products',
                'Manufacture of Textiles',
                'Manufacture of Fabricated Metal Products, Except Machinery and Equipment',
                'Manufacture of Rubber and Plastics Products',
                'Other',
                'Manufacture of Chemicals and Chemical Products',
                'Manufacture of Machinery and Equipment N.E.C',
                'Manufacture of Wearing Apparel',
                'Manufacture of Basic Metals'],
    'Factories':[
                40510,
                29321,
                18122,
                17196,
                15375,
                14856,
                13974,
                13827,
                12544,
                12457]}

st.subheader('🏆 Top 10 Industries in 2023')

df4 = pd.DataFrame(data=data4)

df4.index = range(1, len(df4)+1)

st.dataframe(df4)

data2 = {
    'Industry':['Crop and Animal Production, Hunting and Related Service Activities',
                'Other Mining and Quarrying',
                'Manufacture of Food Products',
                'Manufacture of Beverages',
                'Manufacture of Tobacco Products',
                'Manufacture of Textiles',
                'Manufacture of Wearing Apparel',
                'Manufacture of Leather and Related Products',        
                'Manufacture of Wood and Products of Wood and Cork Except Furniture, Manufacture of Articles of Straw and Plaiting Materials',
                'Manufacture of Paper and Paper Products',
                'Printing and Reproduction of Recorded Media',
                'Manufacture of Coke and Refined Petroleum Products',
                'Manufacture of Chemicals and Chemical Products',
                'Manufacture of Pharmaceuticals, Medicinal Chemical and Botanical Products',
                'Manufacture of Rubber and Plastics Products',
                'Manufacture of Other Non-Metallic Mineral Products',
                'Manufacture of Basic Metals',
                'Manufacture of Fabricated Metal Products, Except Machinery and Equipment',
                'Manufacture of Computer, Electronic and Optical Products',
                'Manufacture of Electrical Equipment',
                'Manufacture of Machinery and Equipment N.E.C',
                'Manufacture of Motor Vehicles, Trailers and Semi Trailers',
                'Manufacture of Other Transport Equipment',
                'Manufacture of Furniture',
                'Other Manufacturing',
                'Repair and Installation of Machinery and Equipment',
                'Waste Collection,treatment and Disposal Activities; Materials Recovery',
                'Publishing Activities',
                'Other'],
    'State':['Telangana',
             'Gujarat',
             'Andhra Pradesh',
             'Tamil Nadu',
             'Tamil Nadu',
             'Tamil Nadu',
             'Tamil Nadu',
             'Tamil Nadu',
             'Kerala',
             'Gujarat',
             'Tamil Nadu',
             'Jharkhand',
             'Gujarat',
             'Gujarat',
             'Gujarat',
             'Andhra Pradesh',
             'Gujarat',
             'Maharashtra',
             'Maharashtra',
             'Maharashtra',
             'Gujarat',
             'Tamil Nadu',
             'Punjab',
             'Rajasthan',
             'Maharashtra',
             'Maharashtra',
             'Gujarat',
             'Andhra Pradesh',
             'Tamil Nadu']}

st.subheader('🏭 Industries and States with Highest Number of Factories')

df2 = pd.DataFrame(data=data2)

df2.index = range(1, len(df2)+1)

st.dataframe(df2)

data3 = {
    "State": [
        "Dadra & Nagar Haveli and Daman & Diu",
        "Ladakh",
        "Telangana",
        "Andaman & Nicobar Islands",
        "Puducherry",
        "Tamil Nadu",
        "Kerala",
        "Goa",
        "Karnataka",
        "Andhra Pradesh",
        "Maharashtra",
        "Gujarat",
        "Madhya Pradesh",
        "Chhattisgarh",
        "Odisha",
        "Jharkhand",
        "West Bengal",
        "Assam",
        "Meghalaya",
        "Tripura",
        "Mizoram",
        "Manipur",
        "Nagaland",
        "Arunachal Pradesh",
        "Sikkim",
        "Bihar",
        "Uttar Pradesh",
        "Rajasthan",
        "Delhi",
        "Haryana",
        "Uttarakhand",
        "Chandigarh",
        "Punjab"],
    "Industry with Highest Factories": [
        "Manufacture of Rubber and Plastics Products",
        "Manufacture of Other Non-Metallic Mineral Products",
        "Manufacture of Food Products",
        "Other",
        "Manufacture of Rubber and Plastics Products",
        "Manufacture of Textiles",
        "Manufacture of Food Products",
        "Manufacture of Other Non-Metallic Mineral Products",
        "Manufacture of Food Products",
        "Manufacture of Food Products",
        "Manufacture of Fabricated Metal Products, Except Machinery and Equipment",
        "Manufacture of Chemicals and Chemical Products",
        "Manufacture of Food Products",
        "Manufacture of Food Products",
        "Manufacture of Food Products",
        "Manufacture of Other Non-metallic Mineral Products",
        "Manufacture of Food Products",
        "Manufacture of Other Non-Metallic Mineral Products",
        "Manufacture of Other Non-Metallic Mineral Products",
        "Manufacture of Other Non-Metallic Mineral Products",
        "Manufacture of Other Non-Metallic Mineral Products",
        "Manufacture of Other Non-Metallic Mineral Products",
        "Manufacture of Other Non-Metallic Mineral Products",
        "Manufacture of Wood and Products of Wood and Cork Except Furniture; Manufacture of Articles of Straw and Plaiting Materials",
        "Manufacture of Pharmaceuticals, Medicinal Chemical and Botanical Products",
        "Manufacture of Other Non-Metallic Mineral Products",
        "Manufacture of Food Products",
        "Manufacture of Other Non-Metallic Mineral Products",
        "Other",
        "Manufacture of Other Non-Metallic Mineral Products",
        "Manufacture of Pharmaceuticals, Medicinal Chemical and Botanical Products",
        "Other",
        "Manufacture of Food Products",
    ]}

st.subheader('🗺️ State and Industry with Highest Number of Total Factories')

df3 = pd.DataFrame(data=data3)

df3.index = range(1, len(df3)+1)

st.dataframe(df3)

# data4 = {
#     'Industry':[
#                 'Crop and Animal Production, Hunting and Related Service Activities',
#                 'Other Mining and Quarrying',
#                 'Manufacture of Food Products',
#                 'Manufacture of Beverages',
#                 'Manufacture of Tobacco Products',
#                 'Manufacture of Textiles',
#                 'Manufacture of Wearing Apparel',
#                 'Manufacture of Leather and Related Products',        
#                 'Manufacture of Wood and Products of Wood and Cork Except Furniture, Manufacture of Articles of Straw and Plaiting Materials',
#                 'Manufacture of Paper and Paper Products',
#                 'Printing and Reproduction of Recorded Media',
#                 'Manufacture of Coke and Refined Petroleum Products',
#                 'Manufacture of Chemicals and Chemical Products',
#                 'Manufacture of Pharmaceuticals, Medicinal Chemical and Botanical Products',
#                 'Manufacture of Rubber and Plastics Products',
#                 'Manufacture of Other Non-metallic Mineral Products',
#                 'Manufacture of Basic Metals',
#                 'Manufacture of Fabricated Metal Products, Except Machinery and Equipment',
#                 'Manufacture of Computer, Electronic and Optical Products',
#                 'Manufacture of Electrical Equipment',
#                 'Manufacture of Machinery and Equipment N.E.C',
#                 'Manufacture of Motor Vehicles, Trailers and Semi Trailers',
#                 'Manufacture of Other Transport Equipment',
#                 'Manufacture of Furniture',
#                 'Other Manufacturing',
#                 'Repair and Installation of Machinery and Equipment',
#                 'Waste Collection,treatment and Disposal Activities; Materials Recovery',
#                 'Publishing Activities',
#                 'Other'],
#     'Factories':[
#                 3221,
#                 131,
#                 40510,
#                 2293,
#                 3307,
#                 18122,
#                 12544,
#                 4922,
#                 4707,
#                 7619,
#                 4271,
#                 1887,
#                 13974,
#                 5499,
#                 15375,
#                 29321,
#                 12457,
#                 17196,
#                 2394,
#                 7994,
#                 13827,
#                 6468,
#                 2208,
#                 2407,
#                 4258,
#                 603,
#                 698,
#                 299,
#                 14856]}

# st.subheader('🏭 Industry-Wise Factory Count')

# df4 = pd.DataFrame(data=data4)

# df4.index = range(1, len(df4)+1)

# st.dataframe(df4)