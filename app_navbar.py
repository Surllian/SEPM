import streamlit as st
import pandas as pd

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

#Footer
st.markdown("""
<nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #FFFFFF; border-top-style: solid; height: 120px">
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
