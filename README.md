# Python Görüntü İşleme Bitirme Projesi

## Projenin amacı:

**Canlı video akışında yüz tespiti ve gerçek zamanlı sansürleme**

## Kullanılan Teknikler:

- **Python (3.10.12)**
- **Opencv (cv2) kütüphanesi**                       (opencv-python)
- **Haar Cascade modeli (cv2.CascadeClassifier)**    (yüzü algılamak için)
- **Gaussian Blur tekniği (cv2.GaussianBlur)**       (blurlama işlemi için)
- **cv2.rectangle**                                  (Algılanan yüz bölgesini çerçevelemek için)

## Nasıl Çalıştırılır? 

1. Bilgisayarınızda **Python 3.10** ve opencv kütüphanesi **opencv-python** kurulu olduğundan emin olun.
2. `face_blur.py` dosyası ile `haarcascade_frontalface_default.xml` dosyası **aynı dizinde** bulunmalıdır.
3. Terminal veya herhangi bir IDE üzerinden aşağıdaki komutla çalıştırın:
   ```bash
   **python face_blur.py**
