import streamlit as st
import joblib
import pandas as pd

model = joblib.load("jakarta_house_price_predict.joblib")
data = pd.read_csv("jakarta_house.csv")

st.title("Jakarta House Price Prediction App")

st.divider()

st.write("This app uses machine learning for predicting house price with given features of the house. For using this app you can enter the inputs from this UI and the use predict button")

st.divider()


city_district = {

    # =========================
    # JAKARTA PUSAT
    # =========================
    "Jakarta Pusat": [
        "Cempaka Putih",
        "Kemayoran",
        "Salemba",
        "Menteng",
        "Gambir",
        "Kuningan",
        "Thamrin",
        "Johar Baru",
        "Gunung Sahari",
        "Bungur",
        "Kebon Kacang",
        "Pangeran Jayakarta",
        "Senen",
        "Kartini",
        "Bendungan Hilir",
        "Cideng",
        "Tanah Abang",
        "Karet Tengsin",
        "Pejompongan",
        "Kebon Sirih",
        "Petojo",
        "Pasar Baru",
        "Gondangdia",
        "Sultan Agung",
        "Duri Pulo",
        "Wahid Hasyim",
        "Kota",
        "Kampung Ambon"
    ],

    # =========================
    # JAKARTA TIMUR
    # =========================
    "Jakarta Timur": [
        "Pulo Asem",
        "Pulo Gadung",
        "Condet",
        "Pulogebang",
        "Duren Sawit",
        "Cipinang",
        "Cibubur",
        "Pondok Kelapa",
        "Cakung",
        "Rawamangun",
        "Cipayung",
        "Ciracas",
        "Rawa Belong",
        "Jatiwaringin",
        "Kalimalang",
        "Pasar Rebo",
        "Kayu Putih",
        "Lubang Buaya",
        "Kalisari",
        "Utan Kayu",
        "Cijantung",
        "Pejaten Timur",
        "Duren Tiga",
        "Bambu Apus",
        "Pondok Bambu",
        "Makasar",
        "Klender",
        "Cilangkap",
        "Jatinegara",
        "Pondok Ranggon",
        "Cawang",
        "Buaran",
        "Pondok Kopi",
        "Otista",
        "Setu",
        "Kampung Rambutan",
        "Cipinang Melayu",
        "Penggilingan",
        "Ruko Rawa Lumbu",
        "Kayu Jati",
        "Kramat Jati",
        "Gudang Peluru",
        "Duren Sawit"
    ],

    # =========================
    # JAKARTA BARAT
    # =========================
    "Jakarta Barat": [
        "Citra Garden",
        "Jelambar",
        "Tanjung Duren",
        "Permata Buana",
        "Green Lake City",
        "Metland Puri",
        "Cengkareng",
        "Puri Indah",
        "Citra Grand",
        "Tomang",
        "Kebon Jeruk",
        "Meruya",
        "Intercon",
        "Joglo",
        "Duri Kepa",
        "Kembangan",
        "Daan Mogot",
        "Taman Ratu",
        "Kedoya",
        "Taman Kencana",
        "Green Ville",
        "Kapuk Muara",
        "Tanjung Duren Selatan",
        "Green garden",
        "Palmerah",
        "Kalideres",
        "Taman Palem",
        "Pegadungan",
        "Kemanggisan",
        "Srengseng",
        "Duri Kosambi",
        "Taman Meruya",
        "Cengkareng Barat",
        "Puri Mansion",
        "Villa Meruya",
        "Taman Surya",
        "Rawa Buaya",
        "Grogol",
        "Grogol Petamburan",
        "Kota Bambu Selatan",
        "Central Park",
        "Slipi",
        "Jalan Panjang",
        "Kembangan Selatan",
        "Karang Anyar",
        "Tambora",
        "Bandengan",
        "Teluk Gong",
        "Angke",
        "Jembatan Besi",
        "Taman Kota",
        "Duri Pulo",
        "Tawakal"
    ],

    # =========================
    # JAKARTA UTARA
    # =========================
    "Jakarta Utara": [
        "Pantai Indah Kapuk 2",
        "Pantai Indah Kapuk",
        "Golf Island",
        "Kelapa Gading",
        "Sunter",
        "Ancol",
        "Cilincing",
        "Penjaringan",
        "Pluit",
        "Pantai Mutiara",
        "Muara Karang",
        "Jembatan Dua",
        "Pademangan",
        "Tanjung Priok",
        "Koja",
        "Kapuk Muara",
        "Rorotan",
        "Bandara",
        "Semper",
        "Marunda",
        "Rawa Badak",
        "Kamal",
        "Kapuk",
        "Pangeran Jayakarta",
        "Mangga Dua",
        "Jembatan Lima",
        "Pademangan"
    ],

    # =========================
    # JAKARTA SELATAN
    # =========================
    "Jakarta Selatan": [
        "Kemang",
        "Tebet",
        "Pondok Indah",
        "Jagakarsa",
        "Kebayoran Baru",
        "Cilandak",
        "Lebak Bulus",
        "Kota Wisata",
        "Cinere",
        "Pondok Labu",
        "Kebayoran Lama",
        "Ciganjur",
        "Veteran",
        "Jati Padang",
        "Permata Hijau",
        "Pejaten",
        "Pancoran",
        "Kebagusan",
        "Cipete",
        "Fatmawati",
        "Simprug",
        "Senopati",
        "Pakubuwono",
        "Setiabudi",
        "Radio Dalam",
        "Kalibata",
        "Pesanggrahan",
        "Wijaya",
        "Duren Tiga",
        "Antasari",
        "Kuningan",
        "Mega Kuningan",
        "Pondok Pinang",
        "Patal Senayan",
        "Senayan",
        "Menteng Dalam",
        "Menteng Atas",
        "Mampang",
        "Mampang Prapatan",
        "Pondok Gede",
        "TB Simatupang",
        "Prapanca",
        "Gandaria",
        "Panglima Polim",
        "Ampera",
        "Tanjung Barat",
        "Ragunan",
        "Cipedak",
        "Lenteng Agung",
        "Ulujami",
        "Petukangan",
        "Tanah Kusir",
        "Jeruk Purut",
        "Terogong",
        "Cirendeu",
        "Rempoa Ciputat Timur",
        "Pengadegan",
        "Karet",
        "Casablanca",
        "Warung Buncit",
        "Bangka",
        "patra kuningan"
    ]
}

city = st.selectbox("Name of city",list(city_district.keys()))
district = st.selectbox("Name of district",city_district[city])
bed_rooms = st.number_input("Number of bedrooms", min_value = 0, value = 0)
bath_rooms = st.number_input("Number of bathrooms", min_value = 0, value = 0)
land_area = st.number_input("Land area (meter squared)", min_value = 0, value = 60)
building_area = st.number_input("Building area (meter squared)", min_value = 0, value = 60)
carport = st.number_input("Number of carport", min_value = 0, value = 0)

st.divider()


if st.button("Predict"):
    input_data = pd.DataFrame([{
        "city" : city,
        "district" : district,
        "bed_rooms" : bed_rooms,
        "bath_rooms" : bath_rooms,
        "land_area" : land_area,
        "building_area" : building_area,
        "carport" : carport
    }])

    prediction = model.predict(input_data)[0]

    st.write(f"Price prediction is Rp {prediction:,.0f}".replace(",", "."))






