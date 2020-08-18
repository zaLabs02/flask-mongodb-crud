
<p align="right">
بِسْــــــــــــــمِ اللَّهِ الرَّحْمَنِ الرَّحِيم 
</p>

# flask mongodb crud

CRUD simpel menggunakan MongoDb.

## Installation

<h3>Paling gampang pake Docker</h3>
Download repo ini, lalu jalankan perintah

```bash
docker-compose up
```

<h3>Kalo manual</h3>
Buat virtualenv terlebih dahulu

```bash
virtualenv {nama_virtual}
virtualenv -p python3 {nama_virtual} (untuk python3, ubuntu biasanya menggunakan ini)
```

Masuk kedalam virtual
```bash
source {nama_virtual}/Scripts/activate

kalo pake Ubuntu
cd {nama_virtual}
source bin/activate
```
Install packages menggunakan [pip](https://pip.pypa.io/en/stable/).
```bash
pip install -r requirements.txt

kalo pake python3 (biasanya dipakeubuntu)
pip3 install -r requirements.txt
```
Jalankan dengan perintah
```bash
python main.py

kalo pake python3 (biasanya dipakeubuntu)
python3 main.py
```
<h3>Jangan lupa setting dbnya sesuai customi masing2</h3>

