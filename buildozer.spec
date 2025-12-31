[app]

# (str) Title of your application
title = GPS Extractor

# (str) Package name
package.name = gpstool

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (str) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
# INI YANG TADI HILANG DAN MENYEBABKAN ERROR
version = 0.1

# (list) Application requirements
# Kita tambahkan 'android' ke dalam requirements
requirements = python3,kivy==2.3.0,pillow,android

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# --- Bagian Icon (Saya matikan dulu pakai # agar tidak error jika file belum ada) ---
# presplash.filename = %(source.dir)s/data/presplash.png
# icon.filename = %(source.dir)s/data/icon.png

# (int) Android API to use
# Kita set ke versi stabil agar aman
android.api = 33
android.minapi = 21

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
