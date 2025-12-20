---

📺 Bölüm 2: Simple Bringup ve Launch Mekanizması

Bu aşamada, projenin modülerliğini artırmak için Launch dosyaları ve Remapping (Yeniden Adlandırma) teknikleri uygulanmıştır. `simple_bringup` paketi, birden fazla düğümü tek bir merkezden yönetmeyi sağlar.

📁 Klasör Yapısı ve Görevler
* **simple_bringup/**: Projenin fırlatıcı (launch) paketidir.
    * **launch/**: Launch dosyalarının bulunduğu dizin.
        * `television_app.launch.py`: Projenin ana fırlatıcı dosyasıdır.
    * **CMakeLists.txt**: Launch dosyalarının sisteme düzgün yüklenmesi (install) için yapılandırılmıştır.
    * **package.xml**: `simple_py_pkg` paketine olan bağımlılıklar tanımlanmıştır.

⚙️ Launch Dosyası Detayları (`television_app.launch.py`)
Dosyada şu teknik özellikler kullanılmıştır:
1. Düğüm Başlatma: `television_publisher_node` ve `remote_controller_node` aynı anda başlatılır.
2. Remapping (Yeniden Adlandırma): `channel_something` adlı topic ismi, çalışma anında `new_channel_something` olarak değiştirilmiştir. Bu sayede kodun içine müdahale etmeden haberleşme kanalları yönetilebilir.
3. Parametre Kullanımı: `parameter_1_int` (5) ve `parameter_2_string` ("GO") gibi değerler launch dosyası üzerinden düğümlere aktarılmıştır.

🚀 Çalıştırma Talimatları
Paketi derledikten sonra tüm sistemi tek komutla başlatabilirsiniz:

# Workspace derleme
colcon build --packages-select simple_bringup
source install/setup.bash

# Launch dosyasını çalıştırma
ros2 launch simple_bringup television_app.launch.py


Aşağıdaki videoda launch dosyamın çalıştırılması sonucu düğümlerin eş zamanlı olarak çalışma şekli gösterilmektedir:

<video src="https://github.com/user-attachments/assets/b8d5225c-1441-42e3-98df-41975b20a0c8" controls width="100%"></video>
