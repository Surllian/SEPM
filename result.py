import streamlit as st
import streamlit.components.v1 as components
import requests
import recommend



st.set_page_config(layout="wide")

components.html(
    """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="aUTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <style>
            * {
                box-sizing: border-box;
            }
            body {
                margin: 0;
            }
            .myNav {
                display: block;
                height: 75px;
                width: 100%;
                line-height: 50px;
                background-color: rgb(255, 255, 255);
                box-shadow: 0 0 10px 0;
                position: fixed;
            }
            /* Remove bullets, margin and padding */
            .myNav ul {
                list-style: none;
                margin: 0;
                text-align: right;
            }
            .myNav li {
                display: inline;
                /* Or you can use display: inline; */
            }
            /* Define the block styling for the links */
            .myNav li a {
                display: inline-block;
                text-align: right;
                padding: 14px 14px;
                font-size: 30px;
                font-family: Arial;
            }
            .myNav a:link { text-decoration: none; 
                color: #000000;
            }


            .myNav a:visited { 
                text-decoration: none;
                font-weight: bold;
                color: #000000;
            }


            .myNav a:hover { text-decoration: none; }


            .myNav li a.active {
                text-align: none;
                color: #000000;
                font-weight: bold;
            }

            .column {
                border-top: 4px groove rgba(255, 247, 247, 0.596);
                float: left;
                background-color:rgb(255, 255, 255);
                height: 50px;
                width: 70%;
            }
            .column1 {
                border-top: 4px groove rgba(255, 247, 247, 0.596);
                float: left;
                background-color:rgb(255, 255, 255);
                height: 50px;
                width: 30%;
            }
            .column2 {
                float: left;
                background-color:rgb(255, 255, 255);
                height: 50px;
                width: 100%;
            }

            .column_body_side {
                float: left;
                width: 20%;
                padding:75px 16px;
                background-color:rgb(255, 255, 255);
                height: 500px;
            }  

            .column_body_main {
                float: left;
                padding-top: 75px;
                width: 60%;
                background-color:rgb(255, 255, 255);
                height: 500px;
            }  
            
            .row:after {
                content: "";
                display: table;
                clear: both;
            }
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: rgb(0, 0, 0);
                color: white;
                text-align: left;
            }


            .column ul {
                list-style: none;
                margin: 0;
                text-align: left;
            }
            .column li {
                display: inline;
                /* Or you can use display: inline; */
            }
            /* Define the block styling for the links */
            .column li a {
                display: inline-block;
                text-align: left;
                padding: 14px 16px;
                font-size: 18px;
                font-family: Arial;
            }
            .column a:link { text-decoration: none; 
                color: #000000;
            }


            .column a:visited { 
                text-decoration: none;
                font-weight: bold;
                color: #000000;
            }


            .column a:hover { text-decoration: none; }

            .footer li a.active {
                text-decoration: none;
                color: #000000;
                font-weight: bold;
            }

            .column1 a {
                display: block;
                text-align: right;
                padding: 14px 16px;
                font-size: 18px;
                font-family: Arial;
            }

            .column1 a:link { text-decoration: none; 
                color: #000000;
            }


            .column1 a:visited { 
                text-decoration: none;
                font-weight: bold;
                color: #000000;
            }


            .column1 a:hover { text-decoration: none; }
        </style>
        <body>
            <nav class="myNav">                           
                <ul>    
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">Cuisine</a></li>
                    <li><a href="contact.html">Category</a></li>
                    <li><a href="contact.html">Location</a></li>
                    <li><a href="Result.html"><b>Recommendation<b></a></li>
                </ul>
            </nav>
        </body>
    </html>
    """,width=None, height=None,scrolling=False,
)


with st.container():
    st.title(recommend.final_name)
    st.markdown("""---""")



with st.container():
    col1,col2,col3,col4,col5 = st.columns([1,2,2,1,8])
    col1.subheader(recommend.final_type)
    col2.subheader(recommend.final_cuisine)
    col3.subheader(recommend.final_price)
    col4.markdown('<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="yellow" class="bi bi-star-fill" viewBox="0 0 16 16"><path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/></svg>', unsafe_allow_html=True)
    col5.subheader(recommend.final_rating)

st.header("Address")

st.subheader(recommend.final_address)

API_KEY = 'AIzaSyAcMOBy56peJHN9pjTwALVLYQBuQycgr2U'
geo_address = "Nha tho Duc Ba"
longtitude = ''
latitude = ''
location_html = '<iframe src="https://maps.google.com/maps?q='
location_html_3 = '&z=18&output=embed&" width="2000" height="1000" loading="lazy" ></iframe>'
location_html_2 = ', '
map_illustration = ''


def getGeoCoord(geo_address):
    params = {
        'key': API_KEY,
        'address': geo_address.replace(' ', '+')
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        result = data['results'][0]
        location = result['geometry']['location']
        longtitude = str(location['lng'])
        latitude = str(location['lat'])
        map_illustration = location_html + latitude + location_html_2 + longtitude + location_html_3
        components.html(map_illustration,height=2000)
    else:
        st.title("Error")


getGeoCoord(geo_address)



components.html(
    """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <style>
            * {
                box-sizing: border-box;
            }
            body {
                margin: 0;
            }
            .column {
                border-top: 4px groove rgba(255, 247, 247, 0.596);
                float: left;
                background-color:rgb(255, 255, 255);
                height: 50px;
                width: 70%;
            }
            .column1 {
                border-top: 4px groove rgba(255, 247, 247, 0.596);
                float: left;
                background-color:rgb(255, 255, 255);
                height: 50px;
                width: 30%;
            }
            .column2 {
                float: left;
                background-color:rgb(255, 255, 255);
                height: 75px;
                width: 100%;
            }

            .column_body_side {
                float: left;
                width: 20%;
                padding:75px 16px;
                background-color:rgb(255, 255, 255);
                height: 500px;
            }  

            .column_body_main {
                float: left;
                padding-top: 75px;
                width: 60%;
                background-color:rgb(255, 255, 255);
                height: 500px;
            }  
            
            .row:after {
                content: "";
                display: table;
                clear: both;
            }
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                heitht: 100%;
                background-color: rgb(0, 0, 0);
                color: white;
                text-align: left;
            }


            .column ul {
                list-style: none;
                margin: 0;
                text-align: left;
            }
            .column li {
                display: inline;
                /* Or you can use display: inline; */
            }
            /* Define the block styling for the links */
            .column li a {
                display: inline-block;
                text-align: left;
                padding: 14px 16px;
                font-size: 25px;
                font-family: Arial;
            }
            .column a:link { text-decoration: none; 
                color: #000000;
            }


            .column a:visited { 
                text-decoration: none;
                font-weight: bold;
                color: #000000;
            }


            .column a:hover { text-decoration: none; }

            .footer li a.active {
                text-decoration: none;
                color: #000000;
                font-weight: bold;
            }

            .column1 a {
                display: block;
                text-align: right;
                padding: 14px 16px;
                font-size: 25px;
                font-family: Arial;
            }

            .column1 a:link { text-decoration: none; 
                color: #000000;
            }


            .column1 a:visited { 
                text-decoration: none;
                font-weight: bold;
                color: #000000;
            }


            .column1 a:hover { text-decoration: none; }

        </style>
    <body>
        <div class="footer">
            <div class= "row">
                <div class="column">
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">Cuisine</a></li>
                        <li><a href="contact.html">Category</a></li>
                        <li><a href="contact.html">Location</a></li>
                        <li><a href="Result.html">Recommendation</a></li>
                    </ul>
                </div>
                <div class="column1">
                    <a href="Null", style="display: right;">About Us</a>
                </div>
            </div>
            <div class="column2">
                <p style="text-align: right;font-size: 30px; padding: 0 14px; color: black;"><b>Copyright © 2022 DAVIKO TEAM</b></p>
            </div>
        </div>
    </body>
    </html>
    """
)
