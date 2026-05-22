import pandas as ps
import pygwalker as py

id = 1
kutuphane_listesi = ['pandas', 'numpy', 'matplotlib', 'scikit-learn', 'seaborn', 'tensorflow', 'keras', 'xgboost', 'lightgbm', 'catboost']

kutuphane_kullanim = ['Tablo', 'Veri Analizi', 'Veri Görselleştirme', 'Makine Öğrenimi', 'Veri Görselleştirme', 'Derin Öğrenme', 'Derin Öğrenme', 'Makine Öğrenimi', 'Makine Öğrenimi', 'Makine Öğrenimi']

kutuphane_cikisYili = [2008, 2008, 2007, 2007, 2012, 2015, 2015, 2014, 2016, 2016]

liste = ps.DataFrame({
    'Kütüphane': kutuphane_listesi,
    'Kullanım Alanı': kutuphane_kullanim,
    'Çıkış Yılı': kutuphane_cikisYili
})



liste.index = range(1, len(liste) + 1)

print(liste)

walker = py.walk(liste)