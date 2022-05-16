import streamlit as st
import streamlit.components.v1 as components
import requests

st.set_page_config(layout="wide")

# Navigation_bar
# Hide menu
hide_menu = """
<style>
#MainMenu { visibility: hidden;
}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

#Header
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #FFFFFF; border-bottom-style: solid;">
  <img src="https://scontent.xx.fbcdn.net/v/t1.15752-9/277445185_695956418275236_1324434635958245909_n.png?stp=dst-png_p206x206&_nc_cat=108&ccb=1-5&_nc_sid=aee45a&_nc_ohc=HJhaOg0gRMMAX-Bjzjx&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVIVfpGRprjvJVO3UZSSaT0ygvyDOXCUffjGu-9qD9BCKA&oe=627D7229" 
            class="rounded float-left" alt="MAFOOD" width="50" height="50">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank" style="color: #000000;">MAFOOD</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse " id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#" style="color: #000000;"> Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank" style="color: #000000;">Cuisine</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank" style="color: #000000;">Category</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:8502" target="_blank" style="color: #000000;">Location</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank" style="color: #000000;">Reccomendation</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

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

# Footer
st.markdown("""
<nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #FFFFFF; border-top-style: solid; height: 80px">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse " id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank" style="color: #000000;">About Us</a>
      </li>
    </ul>
  </div>
  <div style="padding: 100px 80px 50px">Copyright ©2022 TEAM DAVIKO</div>
</nav>
""", unsafe_allow_html=True)