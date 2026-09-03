import streamlit as st
import joblib
import pandas as pd

model = joblib.load("jakarta_house_price_predict.joblib")
data = pd.read_csv("jakarta_house_cleaning.csv")

st.title("Jakarta House Price Prediction App")

st.divider()

st.write("This app uses machine learning for predicting house price with given features of the house. For using this app you can enter the inputs from this UI and the use predict button")

st.divider()



city_district = {

    # =========================
    # JAKARTA PUSAT
    # =========================
    "Jakarta Pusat": [
        'Cempaka Putih', 'Kemayoran', 'Salemba', 'Menteng', 'Gambir',
       'Sawah Besar', 'Kramat', 'Johar Baru', 'Percetakan Negara',
       'Thamrin', 'Gunung Sahari', 'Bungur', 'Kebon Kacang',
       'Pangeran Jayakarta', 'Senen', 'Kartini', 'Bendungan Hilir',
       'Cideng', 'Karet Tengsin', 'Menteng Atas', 'Sumur Batu',
       'Tanah Abang', 'Kebon Sirih', 'Petojo', 'Wahid Hasyim', 'Cikini',
       'Roxy', 'Pejompongan', 'Karang Anyar', 'Gondangdia', 'Pasar Baru',
       'Gajah Mada', 'Pegangsaan'
    ],

    # =========================
    # JAKARTA TIMUR
    # =========================
    "Jakarta Timur": [
        'Pulo Asem', 'Pulo Gadung', 'Condet', 'Pulogebang', 'Duren Sawit',
       'Cipinang', 'Cibubur', 'Pondok Kelapa', 'Cakung',
       'Jakarta Garden City', 'Cipayung', 'Rawamangun', 'Ciracas',
       'Kota Wisata', 'Citra Grand', 'Matraman', 'Raffles Hills',
       'Jatiwaringin', 'Bambu Apus', 'Kalimalang', 'Metland Menteng',
       'Kayu Putih', 'Pasar Rebo', 'Lubang Buaya', 'Kalisari',
       'Utan Kayu', 'Cijantung', 'Ruko Rawa Lumbu', 'Kramat Jati',
       'Pondok Bambu', 'Makasar', 'Klender', 'Cilangkap', 'Jatinegara',
       'Pondok Ranggon', 'Cawang', 'Legenda Wisata', 'Pulomas',
       'Pondok Gede', 'Buaran', 'Pondok Kopi', 'Otista', 'Setu',
       'Kampung Rambutan', 'Cipinang Melayu', 'Penggilingan',
       'Kampung Ambon', 'Kayu Jati'
    ],

    # =========================
    # JAKARTA BARAT
    # =========================
    "Jakarta Barat": [
        'Citra Garden', 'Jelambar', 'Tanjung Duren', 'Permata Buana',
       'Cengkareng', 'Green Lake City', 'Metland Puri', 'Puri Indah',
       'Tomang', 'Taman Ratu', 'Tamansari', 'Mangga Besar', 'Kebon Jeruk',
       'Meruya', 'Intercon', 'Joglo', 'Duri Kepa', 'Kembangan',
       'Daan Mogot', 'Kedoya', 'Palmerah', 'Kalideres', 'Taman Kencana',
       'Kav DKI', 'Grogol', 'Green Ville', 'Tanjung Duren Selatan',
       'Green garden', 'Alfa Indah', 'Taman Palem', 'Pegadungan',
       'Puri Mansion', 'Kemanggisan', 'Kedoya Selatan', 'Srengseng',
       'Duri Kosambi', 'Rawa Buaya', 'Taman Surya', 'Jembatan Dua',
       'Tanjung Duren Utara', 'Rawa Belong', 'Sunrise Garden', 'Semanan',
       'Tawakal', 'Cengkareng Barat', 'Villa Meruya', 'Kepa Duri',
       'Puri Media', 'Jembatan Lima', 'Taman Meruya', 'Slipi',
       'Jalan Panjang', 'Green Mansion', 'Kembangan Selatan',
       'Grogol Petamburan', 'Mangga Dua', 'Bojong Indah', 'Taman Kota',
       'Tambora', 'Bandara', 'Kedoya Baru', 'Kota', 'Duta Garden',
       'Kelapa Dua', 'Metro permata', 'Angke', 'Jembatan Besi',
       'Duri Pulo', 'Kota Bambu Selatan', 'Central Park', 'Tubagus Angke',
       'Taman Cosmos', 'Gelong Baru'
    ],

    # =========================
    # JAKARTA UTARA
    # =========================
    "Jakarta Utara": [
        'Pantai Indah Kapuk 2', 'Pantai Indah Kapuk', 'Golf Island',
       'Kelapa Gading', 'Sunter', 'Ancol', 'Cilincing', 'Pluit',
       'Pantai Mutiara', 'Penjaringan', 'Muara Karang', 'Koja',
       'Kapuk Muara', 'Taman Grisenda', 'Pademangan', 'Pegangsaan',
       'Tanjung Priok', 'Rorotan', 'Bandengan', 'Teluk Gong', 'Marunda',
       'Semper', 'Kapuk', 'Rawa Badak', 'Kamal'
    ],

    # =========================
    # JAKARTA SELATAN
    # =========================
    "Jakarta Selatan": [
        'Kemang', 'Tebet', 'Pondok Indah', 'Jagakarsa', 'Kebayoran Baru',
       'Bintaro', 'Cilandak', 'Lebak Bulus', 'Cinere', 'Pondok Labu',
       'Kebayoran Lama', 'Ciganjur', 'Veteran', 'Jati Padang',
       'Permata Hijau', 'Kuningan', 'Pejaten', 'Pancoran', 'Gandaria',
       'Pasar Minggu', 'Kebagusan', 'Cipete', 'Fatmawati',
       'Sektor 2 - Bintaro', 'Simprug', 'Senopati', 'Pakubuwono',
       'Setiabudi', 'Radio Dalam', 'Kalibata', 'Pesanggrahan', 'Wijaya',
       'Duren Tiga', 'Pejaten Timur', 'Mega Kuningan', 'Antasari',
       'Sektor 1 - Bintaro', 'patra kuningan', 'Bangka', 'Pondok Pinang',
       'Blok M', 'Menteng Dalam', 'Cipulir', 'Panglima Polim', 'Cirendeu',
       'Ampera', 'Cipedak', 'Rempoa Ciputat Timur', 'Lenteng Agung',
       'Mampang', 'Mampang Prapatan', 'Warung Buncit', 'Patal Senayan',
       'Sektor 3 - Bintaro', 'Casablanca', 'Tanjung Barat', 'Senayan',
       'Manggarai', 'Petukangan', 'TB Simatupang', 'SCBD', 'Tanah Kusir',
       'Gatot Subroto', 'Ulujami', 'Ragunan', 'Guntur', 'Prapanca',
       'Karet', 'Graha Bintaro', 'Simprug Garden', 'Sultan Agung',
       'Pengadegan', 'Gudang Peluru', 'Jeruk Purut', 'Terogong'
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






