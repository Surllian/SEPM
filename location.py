import streamlit as st
from streamlit_folium import folium_static
import folium

with st.sidebar.subheader("Choose the district you want to view"):
    district_to_view = st.sidebar.selectbox("Choose a district",
                                            ("District 1", "District 2", "District 3", "District 4",
                                             "District 5", "District 6", "District 7", "District 8",
                                             "District 9", "District 10", "District 11", "District 12"))

if district_to_view == "District 1":
    m = folium.Map(location=[10.777902, 106.701996], titles="District 1", zoom_start=14)

    folium.Marker(
        [10.791346705102988, 106.68809704003041], popup="Monkey in Black Cafe\nRating: 7.5",
        tooltip="Monkey in Black Cafe"
    ).add_to(m)
    folium.Marker(
        [10.77313670640589, 106.6952868283908], popup="Sushi Tei\nRating: 8.9",
        tooltip="Sushi Tei"
    ).add_to(m)
    folium.Marker(
        [10.786963230851216, 106.69417918235844], popup="Oven Maru Chicken\nRating: 8.2",
        tooltip="Oven Maru Chicken"
    ).add_to(m)
    folium.Marker(
        [10.763500333995838, 106.69021299770246], popup="Beefsteak Ciao Vo Diep\nRating: 7.5",
        tooltip="Beefsteak Ciao Vo Diep"
    ).add_to(m)
    folium.Marker(
        [10.765265492565426, 106.69261458421042], popup="Japanit Matcha & Coffee house\nRating: 7.5",
        tooltip="Japanit Matcha & Coffee house"
    ).add_to(m)
    folium.Marker(
        [10.765531292561546, 106.68792048421041], popup="Sul Bingsu Korean Dessert & Coffee\nRating: 7.5",
        tooltip="Sul Bingsu Korean Dessert & Coffee"
    ).add_to(m)
    folium.Marker(
        [10.770744468500965, 106.70448175537447], popup="Don Chicken\nRating: 7.4",
        tooltip="Don Chicken"
    ).add_to(m)
    folium.Marker(
        [10.767906870687181, 106.68650808235839], popup="Xoi Che BTX\nRating: 6.3",
        tooltip="Xoi Che BTX"
    ).add_to(m)
    folium.Marker(
        [10.776613741371731, 106.70453720934222], popup="Kem Häagen Dazs\nRating: 7.7",
        tooltip="Kem Häagen Dazs"
    ).add_to(m)
    folium.Marker(
        [10.769702328780472, 106.69044896701412], popup="Sushi & BBQ Miya\nRating: 7.7",
        tooltip="Sushi & BBQ Miya"
    ).add_to(m)
    folium.Marker(
        [10.766695351843458, 106.69595966886641], popup="Kem Swensen's\nRating: 7.3",
        tooltip="Kem Swensen's"
    ).add_to(m)
    folium.Marker(
        [10.787519391038767, 106.70443112468634], popup="Ocean Palace\nRating: 7.3",
        tooltip="Ocean Place"
    ).add_to(m)
    folium.Marker(
        [10.773435448536972, 106.70081945537449], popup="Miyama Modern Tokyo\nRating: 8.1",
        tooltip="Miyama Modern Tokyo"
    ).add_to(m)
    folium.Marker(
        [10.771788326881113, 106.69182988235829], popup="Bistro Beefsteak & Mon Au\nRating: 7.1",
        tooltip="Bistro Beefsteak & Mon Au"
    ).add_to(m)
    folium.Marker(
        [10.763229754006604, 106.68825678235822], popup="Snow Bings Bingsu\nRating: 7.6",
        tooltip="Snow Bings Bingsu"
    ).add_to(m)
    folium.Marker(
        [10.766745631757198, 106.68789235352224], popup="Tra Sua Tien Huong\nRating: 7.2",
        tooltip="Tra Sua Tien Huong"
    ).add_to(m)
    folium.Marker(
        [10.794156589453662, 106.69325842653866], popup="Che Khuc Bach Thanh\nRating: 6.9",
        tooltip="Che Khuc Bach Thanh"
    ).add_to(m)
    folium.Marker(
        [10.765096432822542, 106.69119098421045], popup="Che Khuc Bach Thanh\nRating: 6.9",
        tooltip="Che Khuc Bach Thanh"
    ).add_to(m)
    folium.Marker(
        [10.765117512864617, 106.6911373400303], popup="Bun Dau Co Khan\nRating: 8",
        tooltip="Bun Dau Co Khan"
    ).add_to(m)
    folium.Marker(
        [10.763447114651818, 106.69070157442293], popup="Lau Bo Ti Chuot\nRating: 6.8",
        tooltip="Lau Bo Ti Chuot"
    ).add_to(m)
    folium.Marker(
        [10.76428821324609, 106.68712665537453], popup="Papaxot\nRating: 7.1",
        tooltip="Papaxot"
    ).add_to(m)

    folium_static(m, 1000, 714)

if district_to_view == "District 2":
    m = folium.Map(location=[10.80561845047513, 106.73656241119451], titles="District 2", zoom_start=14)

    folium.Marker(
        [10.806403195310855, 106.74622624003068], popup="The Deck Saigon\nRating: 7.1",
        tooltip="The Deck Saigon"
    ).add_to(m)
    folium.Marker(
        [10.801807544531568, 106.74714972653862], popup="D'Maris Buffet\nRating: 7.6",
        tooltip="D'Maris Buffet"
    ).add_to(m)
    folium.Marker(
        [10.80283453082987, 106.7325397958505], popup="Cheesecake\nRating: 7.6",
        tooltip="Cheesecake"
    ).add_to(m)
    folium.Marker(
        [10.78892369770348, 106.74280782653862], popup="Cocorico Ga Nuong Phap Rotisserie\nRating: 7.8",
        tooltip="Cocorico Ga Nuong Phap Rotisserie"
    ).add_to(m)
    folium.Marker(
        [10.81205723660755, 106.73135446886677], popup="Chickita Ga Nuong Lua Hong\nRating: 7.9",
        tooltip="Chickita Ga Nuong Lua Hong"
    ).add_to(m)
    folium.Marker(
        [10.803598497872612, 106.74189792468651], popup="Sumo BBQ\nRating: 8.9",
        tooltip="Sumo BBQ"
    ).add_to(m)
    folium.Marker(
        [10.797560220068913, 106.7389315130468], popup="Hana BBQ & Hot Pot Buffet\nRating: 7.1",
        tooltip="Hana BBQ & Hot Pot Buffet"
    ).add_to(m)
    folium.Marker(
        [10.800178039798086, 106.73710831119463], popup="Mr Kiss\nRating: 7.1",
        tooltip="Mr Kiss"
    ).add_to(m)
    folium.Marker(
        [10.793707250788598, 106.7398533977027], popup="Pho Thin Ha Noi Pho Nho\nRating: 6.9",
        tooltip="Pho Thin Ha Noi Pho Nho"
    ).add_to(m)
    folium.Marker(
        [10.806414865391279, 106.73520562468651], popup="The Loop\nRating: 7.7",
        tooltip="The Loop"
    ).add_to(m)
    folium.Marker(
        [10.799525601591506, 106.7356820246865], popup="Banh 9 Sach Banh Sau Rieng\nRating: 10",
        tooltip="Banh 9 Sach Banh Sau Rieng"
    ).add_to(m)
    folium.Marker(
        [10.804020381487389, 106.73630375722703], popup="Union Jack's Fish & Chips\nRating: 9",
        tooltip="Union Jack's Fish & Chips"
    ).add_to(m)
    folium.Marker(
        [10.804390271975395, 106.73554716886663], popup="Al Fresco's Pizza, My Y, Suon, Steak Bo Bit Tet\nRating: 7.3",
        tooltip="Al Fresco's Pizza, My Y, Suon, Steak Bo Bit Tet"
    ).add_to(m)
    folium.Marker(
        [10.805938779937192, 106.75015691119472], popup="Poke\nRating: 7.4",
        tooltip="Poke"
    ).add_to(m)
    folium.Marker(
        [10.80401375216606, 106.73570794003065], popup="Kim Thao Hot Vit Lon\nRating: 6.1",
        tooltip="Kim Thao Hot Vit Lon"
    ).add_to(m)
    folium.Marker(
        [10.788452433269486, 106.75309081304671], popup="HIA Corner\nRating: 9.4",
        tooltip="HIA Corner"
    ).add_to(m)
    folium.Marker(
        [10.802125766821957, 106.7287459977027], popup="River View\nRating: 8.6",
        tooltip="River View"
    ).add_to(m)
    folium.Marker(
        [10.804261649353323, 106.73752518421081], popup="Popeyes\nRating: 7.5",
        tooltip="Popeyes"
    ).add_to(m)
    folium.Marker(
        [10.80561845047513, 106.73656241119451], popup="Boat House\nRating: 6.6",
        tooltip="Boat House"
    ).add_to(m)

    folium_static(m, 1000, 714)

if district_to_view == "District 3":
    m = folium.Map(location=[10.782157096303273, 106.68476118398186], titles="District 3", zoom_start=14)

    folium.Marker(
        [10.786414434985035, 106.68697018213413], popup="Oromia Coffee\nRating: 7.7",
        tooltip="Oromia Coffee"
    ).add_to(m)
    folium.Marker(
        [10.785368396545092, 106.69426835329888], popup="The Sushi Bar\nRating: 7.5",
        tooltip="The sushi bar"
    ).add_to(m)
    folium.Marker(
        [10.788043856171592, 106.69141287972673], popup="El Sol Meat & Wine\nRating: 8.2",
        tooltip="El Sol Meat & Wine"
    ).add_to(m)
    folium.Marker(
        [10.78470001511687, 106.67336478398194], popup="Ga Co Bap\nRating: 7.8",
        tooltip="Ga Co Bap"
    ).add_to(m)
    folium.Marker(
        [10.782331541290851, 106.68818538398189], popup="Fly Cupcake\nRating: 7.0",
        tooltip="Fly Cupcake"
    ).add_to(m)
    folium.Marker(
        [10.771373346694851, 106.68602046864025], popup="Banh trang tron\nRating: 6.5",
        tooltip="Banh trang tron"
    ).add_to(m)
    folium.Marker(
        [10.789079593551131, 106.67794155329888], popup="Chao Restaurant\nRating: 7.3",
        tooltip="Chao Restaurant"
    ).add_to(m)
    folium.Marker(
        [10.774547024368704, 106.68979591281722], popup="Pasta Paradise\nRating: 7.1",
        tooltip="Pasta Paradise"
    ).add_to(m)
    folium.Marker(
        [10.77077286763831, 106.6831972128171], popup="Hem Spaghetti\nRating: 7.2",
        tooltip="Hem Spaghetti"
    ).add_to(m)
    folium.Marker(
        [10.76913326918847, 106.68354369562789], popup="Beefsteak titi\nRating: 6.3",
        tooltip="Beefsteak titi"
    ).add_to(m)

    folium_static(m, 1000, 714)

if district_to_view == "District 4":
    m = folium.Map(location=[10.760012095298249, 106.70226718400649], titles="District 4", zoom_start=14)

    folium.Marker(
        [10.760642635176273, 106.70706832815857], popup="Chill lau nuong tu chon\nRating: 6.9",
        tooltip="Chill lau nuong tu chon"
    ).add_to(m)
    folium.Marker(
        [10.754196838785264, 106.71409432631096], popup="Waffle place\nRating: 7.4",
        tooltip="Waffle place"
    ).add_to(m)
    folium.Marker(
        [10.757147617744565, 106.70280691281712], popup="Ba Bac Banh Trang Cuon Tron\nRating: 6.7",
        tooltip="Ba Bac Banh Trang Cuon Tron"
    ).add_to(m)
    folium.Marker(
        [10.754480421424525, 106.70821189562781], popup="Oc To\nRating: 6.6",
        tooltip="Oc To"
    ).add_to(m)
    folium.Marker(
        [10.756634880997339, 106.6937754109695], popup="Ning Cha\nRating: 7.6",
        tooltip="Ning Cha"
    ).add_to(m)
    folium.Marker(
        [10.762382995316239, 106.71036799562779], popup="Mi oc hen Di Lan\nRating: 6.5",
        tooltip="Mi oc hen Di Lan"
    ).add_to(m)
    folium.Marker(
        [10.754702042427732, 106.69944772631096], popup="Banh trang kep Di Hoa\nRating: 6.7",
        tooltip="Banh trang kep Di Hoa"
    ).add_to(m)
    folium.Marker(
        [10.760877494870021, 106.70327573980468], popup="Oc Oanh 1\nRating: 8.9",
        tooltip="Oc Oanh 1"
    ).add_to(m)
    folium.Marker(
        [10.757982839444498, 106.70059965329872], popup="Uchi Sushi\nRating: 7.9",
        tooltip="Uchi Sushi"
    ).add_to(m)
    folium.Marker(
        [10.75968539767589, 106.69745545514627], popup="Bun Bo Hue\nRating: 8.4",
        tooltip="Bun Bo Hue"
    ).add_to(m)

    folium_static(m, 1000, 714)

if district_to_view == "District 5":
    m = folium.Map(location=[10.754596042524117, 106.66844908213399], titles="District 5", zoom_start=14)

    folium.Marker(
        [10.752398142152446, 106.66982599562775], popup="Osaka Com Tho Nhat Ban\nRating: 6.8",
        tooltip="Osaka Com Tho Nhat Ban"
    ).add_to(m)
    folium.Marker(
        [10.753400881854256, 106.6740656974755], popup="Thien Du & Sky Sushi\nRating: 7.1",
        tooltip="Thien Du & Sky Sushi"
    ).add_to(m)
    folium.Marker(
        [10.762025854132931, 106.68276688213408], popup="Texas Chicken\nRating: 7.0",
        tooltip="Texas Chicken"
    ).add_to(m)
    folium.Marker(
        [10.754808242331166, 106.66636471096943], popup="Tokori BBQ\nRating: 8.3",
        tooltip="Tokori BBQ"
    ).add_to(m)
    folium.Marker(
        [10.754557663758872, 106.67130303980476], popup="Tra sua Momo\nRating: 7.0",
        tooltip="Tra sua Momo"
    ).add_to(m)

    folium_static(m, 1000, 714)

if district_to_view == "District 6":
    m = folium.Map(location=[10.74661967180491, 106.6364900821339], zoom_start=14)

    folium.Marker(
        [10.75129778091749, 106.64897002446311], popup="Steak Zone\nRating: 4.2",
        tooltip="Steak Zone"
    ).add_to(m)


# District 7
if district_to_view == "District 7":
    m = folium.Map(location=[10.7375815,106.6933228], titles="District 7", zoom_start=14)

    folium.Marker(
        [10.7283101,106.7162159], popup="Morico Contemporary Japanese Lifestyle Crescent Mall\nRating=3.95",
        tooltip="Morico Contemporary Japanese Lifestyle Crescent Mall"
    ).add_to(m)

    folium.Marker(
        [10.7307273,106.7065185], popup="Papa's Chicken Phu My Hung\nRating=3.5",
        tooltip="Papa's Chicken Phu My Hung"
    ).add_to(m)

    folium.Marker(
        [10.7298577,106.7010969], popup="Sumo BBQ SC VivoCity Buffet Nuong & Lau\nRating=4.2",
        tooltip="Sumo BBQ SC VivoCity Buffet Nuong & Lau"
    ).add_to(m)

    folium.Marker(
        [10.7234184,106.6811206], popup="Mr.BBQ Am Thuc Han Quoc\nRating=3.6",
        tooltip="Mr.BBQ Am Thuc Han Quoc"
    ).add_to(m)

    folium.Marker(
        [10.7315855,106.7134245], popup="Pizza 4P’s Pizza Kieu Nhat Nguyen Van Linh\nRating=4.05",
        tooltip="Pizza 4P’s Pizza Kieu Nhat Nguyen Van Linh"
    ).add_to(m)

    folium_static(m, 1000, 714)

# District 8
if district_to_view == "District 8":
    m = folium.Map(location=[10.722881,106.6103573], titles="District 8", zoom_start=14)

    folium.Marker(
        [10.7452085,106.681053], popup="Shinsen Sushi Au Duong Lan\nRating=3.4",
        tooltip="Shinsen Sushi Au Duong Lan"
    ).add_to(m)

    folium.Marker(
        [10.7476124,106.6648761], popup="Com Ga Xoi Mo 142 Ba Dinh\nRating=3.45",
        tooltip="Com Ga Xoi Mo 142 Ba Dinh"
    ).add_to(m)

    folium.Marker(
        [10.7380838,106.6746301], popup="Pha Lau Dong Dieu\nRating=5",
        tooltip="Pha Lau Dong Dieu"
    ).add_to(m)

    folium.Marker(
        [10.742032,106.6879954], popup="Oc Tuyet Duong Ba Trac\nRating=3.35",
        tooltip="Oc Tuyet Duong Ba Trac"
    ).add_to(m)

    folium.Marker(
        [10.7391938,106.6512863], popup="Oc 10 Gio\nRating=3.4",
        tooltip="Oc 10 Gio"
    ).add_to(m)

    folium_static(m, 1000, 714)

# District 9
if district_to_view == "District 9":
    m = folium.Map(location=[10.8295542, 106.7487347], titles="District 9", zoom_start=14)

    folium.Marker(
        [10.8451593,106.7767245], popup="Gogi House Quan Nuong Han Quoc Vincom Le Van Viet\nRating=4.05",
        tooltip="Gogi House Quan Nuong Han Quoc Vincom Le Van Viet"
    ).add_to(m)

    folium.Marker(
        [10.8463401,106.79514], popup="Tra Sua Wait Tea Vietnam Le Van Viet\nRating=4.65",
        tooltip="Tra Sua Wait Tea Vietnam Le Van Viet"
    ).add_to(m)

    folium.Marker(
        [10.843911,106.7800816], popup="Domino’s Pizza Le Van Viet\nRating=3.7",
        tooltip="Domino’s Pizza Le Van Viet"
    ).add_to(m)

    folium.Marker(
        [10.8472532,106.7740567], popup="King BBQ Vua Nuong Han Quoc Vincom Le Van Viet\nRating=3.8",
        tooltip="King BBQ Vua Nuong Han Quoc Vincom Le Van Viet"
    ).add_to(m)

    folium.Marker(
        [10.8270673,106.7675027], popup="Buffet Beo 99k\nRating=3.7",
        tooltip="Buffet Beo 99k"
    ).add_to(m)

    folium_static(m, 1000, 714)

if district_to_view == "District 10":
    m = folium.Map(location=[10.773360326744879, 106.66750772631107], titles="District 10", zoom_start=16)

    folium.Marker(
        [10.77228846734884, 106.66966379803287], popup="Hanuri\nRating: 3.5", tooltip="Hanuri"
    ).add_to(m)

    folium.Marker(
        [10.771541467924596, 106.67005998083548], popup="Monkey in black\nRating: 3.8", tooltip="Monkey in black"
    ).add_to(m)

    folium.Marker(
        [10.77263474778628, 106.66946864221367], popup="Say coffee\nRating: 3.45", tooltip="Say coffee"
    ).add_to(m)

    folium.Marker(
        [10.773503265094195, 106.66870619803296], popup="Cow Express\nRating: 3.85", tooltip="Cow Express"
    ).add_to(m)

    folium.Marker(
        [10.766473054466099, 106.67419933239366], popup="Lau tom cang xien Tran Nhan Ton\nRating: 3.5", tooltip="Lau tom cang xien Tran Nhan Ton"
    ).add_to(m)

    folium_static(m, 1000, 714)

if district_to_view == "District 11":
    m = folium.Map(location=[10.76467025304849, 106.6468291839818], zoom_start=16)

    folium.Marker(
        [10.761315796287489, 106.65085612872197], popup="Tra sua bon bon\nRating: 3.95", tooltip="Tra sua bon bon"
    ).add_to(m)

    folium.Marker(
        [10.767839050977939, 106.65317056919677], popup="Ha cao pha lau Marie Curie\nRating: 3.7", tooltip="Ha cao pha lau Marie Curie"
    ).add_to(m)

    folium.Marker(
        [10.853792561353314, 106.62554689803358], popup="Moda House coffee\nRating: 4", tooltip="Moda House coffee"
    ).add_to(m)

    folium.Marker(
        [10.758153797690815, 106.65266498454126], popup="Sui cao Ngoc Y\nRating: 3.35", tooltip="Sui cao Ngoc Y"
    ).add_to(m)

    folium.Marker(
        [10.757928475625025, 106.64483885570515], popup="Sapinkie\nRating: 3.15", tooltip="Sapinkie"
    ).add_to(m)

    folium_static(m, 1000, 714)

if district_to_view == "District 12":
    m = folium.Map(location=[10.87273471705438, 106.6517924551472], zoom_start=14)

    folium.Marker(
        [10.872409787197864, 106.67221737421346], popup="LongBuri\nRating: 4.15", tooltip="LongBuri"
    ).add_to(m)

    folium.Marker(
        [10.82910187231742, 106.62703009803333], popup="Nha hang Dai Phu\nRating: 3.85", tooltip="Nha hang Dai Phu"
    ).add_to(m)

    folium.Marker(
        [10.853792561353314, 106.62554689803358], popup="Moda House coffee\nRating: 4", tooltip="Moda House coffee"
    ).add_to(m)

    folium.Marker(
        [10.84642257284936, 106.63345351337806], popup="Met Quan\nRating: 3.3", tooltip="Met Quan"
    ).add_to(m)

    folium.Marker(
        [10.827551497626137, 106.61912037105027], popup="Kimbab tuoi\nRating: 3.7", tooltip="Kimbab Tuoi"
    ).add_to(m)

    folium.Marker(
        [10.853237846203227, 106.6779545422142], popup="Khu du lich Ben Xua\nRating: 3.3", tooltip="Khu du lich Ben Xua"
    ).add_to(m)

    folium.Marker(
        [10.828876061419255, 106.62999652501651], popup="Quan an Han Quoc\nRating: 3.35", tooltip="Quan An Han Quoc"
    ).add_to(m)

    folium.Marker(
        [10.830181673603828, 106.62308541152491], popup="Sky 17 cafe\nRating: 3.2", tooltip="Sky 17 cafe"
    ).add_to(m)

    folium.Marker(
        [10.8694406466983, 106.64863164036132], popup="Meo beo tiramisu\nRating: 4.4", tooltip="Meo beo tiramisu"
    ).add_to(m)

    folium_static(m, 1000, 714)






















