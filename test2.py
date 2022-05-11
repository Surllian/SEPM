import streamlit as st
from streamlit_option_menu import option_menu
import networkx as nx
import leafmap.foliumap as leafmap
import streamlit.components.v1 as components
import pandas as pd
import numpy as np


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
                padding: 14px 8px;
                font-size: 20px;
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
    st.markdown('<h1 style:"padding:-15 0;">RMIT</h1>', unsafe_allow_html=True)
    st.markdown("""---""")
with st.container():
    col1,col2,col3,col4 = st.columns([1,0.75,1.2,3.6])
    col1.markdown("<p style='text-align: left'>Vietnamese |</p>", unsafe_allow_html=True)
    col2.markdown("<p style='text-align: left'>School |</p>", unsafe_allow_html=True)
    col3.markdown("<p style='text-align: left'>Avg: 100.000vnd |</p>", unsafe_allow_html=True)
    col4.markdown('<p style="text-align: left"><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="yellow" class="bi bi-star" viewBox="0 0 16 16"><path d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.565.565 0 0 0-.163-.505L1.71 6.745l4.052-.576a.525.525 0 0 0 .393-.288L8 2.223l1.847 3.658a.525.525 0 0 0 .393.288l4.052.575-2.906 2.77a.565.565 0 0 0-.163.506l.694 3.957-3.686-1.894a.503.503 0 0 0-.461 0z"/></svg> 4.4 </p>', unsafe_allow_html=True)
st.subheader("Address")
st.write("702 Nguyễn Văn Linh, Tân Hưng, Quận 7, Thành phố Hồ Chí Minh 700000, Việt Nam")
components.iframe("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3920.063744373333!2d106.69088691545974!3d10.729566992353336!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752fbea5fe3db1%3A0xfae94aca5709003f!2zxJDhuqFpIGjhu41jIFJNSVQgVmnhu4d0IE5hbSAtIGPGoSBz4bufIE5hbSBTw6BpIEfDsm4!5e0!3m2!1svi!2s!4v1652137475076!5m2!1svi!2s",height=600,)
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
                <p style="text-align: right;font-size: 20px; padding: 0 14px; color: black;"><b>Copyright © 2022 DAVIKO TEAM</b></p>
            </div>
        </div>
    </body>
    </html>
    """
)
