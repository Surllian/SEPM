import streamlit as st
import streamlit.components.v1 as components
import requests

st.set_page_config(layout="wide")

chosen_district = []
chosen_name = []
chosen_cuisine = []
chosen_type = []
chosen_price = []
chosen_address = []
chosen_rating = []


# read file
@st.cache
def read_price(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split(",")
        array.append((words[-2]))
    my_file.close()
    return array


@st.cache
def read_rating(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split(",")
        array.append((words[-1]))
    my_file.close()
    return array


@st.cache
def read_district(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split(",")
        array.append((words[5]))
    my_file.close()
    return array


@st.cache
def read_name(filename):
    name = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split(",")
        name.append((words[1]))
    my_file.close()
    return name


@st.cache
def read_address(filename):
    address = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split(",")
        address.append((words[4]))
    my_file.close()
    return address


@st.cache
def read_type(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split(",")
        array.append((words[2]))
    my_file.close()
    return array


@st.cache
def read_cuisine(filename):
    array = []
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split(",")
        array.append((words[3]))
    my_file.close()
    return array


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def find_index(array1, array2, number_input):
    if number_input in array2:
        chosen_index = array2.index(number_input)
    else:
        array2.append(number_input)
        array2.sort()
        index = array2.index(number_input)
        if index == 0:
            chosen_index = 1
        elif index == (len(array2) - 1):
            chosen_index = index - 1
        else:
            result_1 = abs(number_input - array2[index - 1])
            result_2 = abs(array2[index + 1] - number_input)
            if result_1 < result_2:
                chosen_index = index - 1
            elif result_1 > result_2:
                chosen_index = index + 1
            else:
                chosen_index = index - 1
    chosen_value = array2[chosen_index]
    final_index = array1.index(chosen_value)
    print(final_index)
    return final_index


def getGeoCoord(geo_address, API_KEY):
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
        components.html(map_illustration, height=2000)
    else:
        st.title("Error")


# Read file
my_price = read_price("All_dis_workbook.csv")
my_name = read_name("All_dis_workbook.csv")
my_address = read_address("All_dis_workbook.csv")
my_type = read_type("All_dis_workbook.csv")
my_cuisine = read_cuisine("All_dis_workbook.csv")
my_district = read_district("All_dis_workbook.csv")
my_rating = read_rating("All_dis_workbook.csv")


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
    """, width=None, height=None, scrolling=False,
)

district = st.selectbox("Choose your district", ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
                                                 "Binh_Chanh", "Binh_Tan", "Binh_Thanh", "Go_Vap", "Hoc_Mon",
                                                 "Nha_Be", "Phu_Nhuan", "Tan_Binh", "Thu_Duc_city", "Tan_Phu"))

type = st.selectbox("Choose your type", ("Bakery", "Bar", "Bistro", "Buffet", "Cafe", "Coffee", "Restaurant"))
cuisine = st.selectbox("Choose your cuisine", ("Vietnamese", "American", "Arabian", "Asian", "Australian", "Brazilian",
                                               "Cambodia", "Canadian", "Chinese", "Czech", "European", "French",
                                               "German", "Germany", "Indian", "Italian", "Italy", "Japanese", "Korean",
                                               "Malaysia", "Malaysian", "Mexican", "Philippines", "Singapore", "South",
                                               "Southeast", "Spanish", "Taiwanese", "Thailand", "USA"))
num = st.slider("Choose your approximately price", 10000, 450000, value=0)

search = st.button("Search", key="option")

if search:
    # filering data to match the input, finding the index
    index_keep_type = [i for i, x in enumerate(my_type) if x == type]
    index_keep_cusine = [i for i, x in enumerate(my_cuisine) if x == cuisine]
    index_keep_district = [i for i, x in enumerate(my_district) if x == district]
    index_keep_temp = intersection(index_keep_cusine, index_keep_type)
    final_index_keep = intersection(index_keep_temp, index_keep_district)
    if len(final_index_keep) > 0:
        for i in final_index_keep:
            chosen_name.append(my_name[i])
            chosen_cuisine.append(my_cuisine[i])
            chosen_type.append(my_type[i])
            chosen_price.append(my_price[i])
            chosen_address.append(my_address[i])
            chosen_district.append(my_district[i])
            chosen_rating.append(my_rating[i])

        # finding final result
        price = [int(x) for x in chosen_price]
        price_array = [int(x) for x in chosen_price]
        find_data = find_index(price, price_array, num)

        # Output
        final_name = chosen_name[find_data]
        final_address = chosen_address[find_data]
        final_rating = chosen_rating[find_data]
        final_district = chosen_district[find_data]

        API_KEY = 'AIzaSyAcMOBy56peJHN9pjTwALVLYQBuQycgr2U'
        longtitude = ''
        latitude = ''
        location_html = '<iframe src="https://maps.google.com/maps?q='
        location_html_3 = '&z=18&output=embed&" width="2000" height="1000" loading="lazy" ></iframe>'
        location_html_2 = ', '
        map_illustration = ''

        st.write("You should eat at {name} at {address}, district {district}, with rating of {rating}".format(
            name=final_name, address=final_address, district=final_district, rating=final_rating))

        getGeoCoord(final_address, API_KEY)
    else:
        st.write("There is no data of your search, please try again")

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
