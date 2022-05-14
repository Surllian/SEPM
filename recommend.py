import streamlit as st

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

        st.write("You should eat at {name} at {address}, district {district}, with rating of {rating}".format(
            name=final_name, address=final_address, district=final_district, rating=final_rating))
    else:
        st.write("There is no data of your search, please try again")
