import streamlit as st
import streamlit.components.v1 as components

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
    st.markdown("<p style='text-align: left; font-size:60px; font-family: Arial;'><b>RMIT - Ho Chi Minh brand</b></p>", unsafe_allow_html=True)
    st.markdown("""---""")
with st.container():
    col1,col2,col3,col4 = st.columns([1,1,1.1,9])
    col1.markdown("<p style='text-align: left; font-size:30px;'>Vietnamese |</p>", unsafe_allow_html=True)
    col2.markdown("<p style='text-align: left; font-size:30px;'>School |</p>", unsafe_allow_html=True)
    col3.markdown("<p style='text-align: left; font-size:30px;'>Avg: 100.000vnd |</p>", unsafe_allow_html=True)
    col4.markdown('<p style="text-align: left; font-size:30px;"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="yellow" class="bi bi-star-fill" viewBox="0 0 16 16"><path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/></svg> 4.4 </p>', unsafe_allow_html=True)
st.header("Address")
st.markdown("<p style='text-align: left; font-size:25px;'>702 Nguyễn Văn Linh, Tân Hưng, Quận 7, Thành phố Hồ Chí Minh 700000, Việt Nam</p>", unsafe_allow_html=True)
components.iframe("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.063744373334!2d106.69088691533346!3d10.729566992353291!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752fbea5fe3db1%3A0xfae94aca5709003f!2zxJDhuqFpIGjhu41jIFJNSVQgVmnhu4d0IE5hbSAtIGPGoSBz4bufIE5hbSBTw6BpIEfDsm4!5e0!3m2!1svi!2s!4v1652287432698!5m2!1svi!2s",height=1000,)
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
