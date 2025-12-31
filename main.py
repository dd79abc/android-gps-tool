import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from PIL import Image
from PIL.ExifTags import GPSTAGS
import os

# --- LOGIKA GPS ANDA (TIDAK BERUBAH) ---
def rational_to_float(r):
    try:
        return r[0] / r[1]
    except Exception:
        return float(r)

def dms_list_to_decimal(dms, ref):
    d = rational_to_float(dms[0])
    m = rational_to_float(dms[1])
    s = rational_to_float(dms[2])
    dec = d + m / 60 + s / 3600
    return -dec if ref in ("S", "W") else dec

def read_exif_gps(path):
    try:
        img = Image.open(path)
        exif = img._getexif()
        if not exif: return None
        gps = exif.get(34853)
        if not gps: return None
        gps = {GPSTAGS.get(k): v for k, v in gps.items()}
        if "GPSLatitude" not in gps or "GPSLongitude" not in gps: return None
        lat = dms_list_to_decimal(gps["GPSLatitude"], gps["GPSLatitudeRef"])
        lon = dms_list_to_decimal(gps["GPSLongitude"], gps["GPSLongitudeRef"])
        return round(lon, 6), round(lat, 6)
    except Exception:
        return None

# --- UI BARU (KIVY UNTUK ANDROID) ---
class GPSApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        # Area untuk menampilkan hasil
        self.result_label = Label(text="Pilih file gambar untuk cek GPS", size_hint=(1, 0.2))
        self.layout.add_widget(self.result_label)

        # Pemilih File
        # Catatan: Di Android asli butuh izin storage, ini versi basic
        path = '/sdcard/DCIM' if os.path.exists('/sdcard/DCIM') else '/'
        self.file_chooser = FileChooserIconView(path=path, filters=['*.jpg', '*.jpeg', '*.png'])
        self.layout.add_widget(self.file_chooser)

        # Tombol Proses
        btn = Button(text="Cek Koordinat", size_hint=(1, 0.1))
        btn.bind(on_press=self.process_file)
        self.layout.add_widget(btn)

        return self.layout

    def process_file(self, instance):
        selection = self.file_chooser.selection
        if selection:
            filepath = selection[0]
            gps = read_exif_gps(filepath)
            if gps:
                self.result_label.text = f"File: {os.path.basename(filepath)}\nLon: {gps[0]}, Lat: {gps[1]}"
            else:
                self.result_label.text = "Tidak ada data GPS ditemukan."
        else:
            self.result_label.text = "Pilih file dulu!"

if __name__ == '__main__':
    GPSApp().run()
