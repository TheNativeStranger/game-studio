# Kullanım kılavuzu

[← README](../README.md)

## 1. Gerekenler

| Gereken | Neden |
|---|---|
| Claude Code ya da Claude masaüstü uygulaması | Ekip burada çalışır |
| Python 3 ve Node.js | Betikler için |
| Unity, Godot ya da Unreal | Oyun motoru; web oyunu için gerekmez |
| Blender 5.1 veya üstü ve resmî MCP eklentisi | 3D Artist için |
| Canva ve ElevenLabs bağlantıları | 2D, tanıtım ve ses için |
| ffmpeg | Ses dönüştürme için, isteğe bağlı |

Blender'ın MCP eklentisi üretilen kodu Blender içinde denetimsiz çalıştırır. Önemli dosyalarından ayrı bir kullanıcı hesabında ya da ayrı bir makinede kullanman önerilir.

ElevenLabs'in mevcut bağlantısı yalnızca konuşma üretir. Ses efekti ve müzik için Ayarlar → Bağlayıcılar'dan tam bağlantıyı ekle: `https://api.elevenlabs.io/v1/mcp`

## 2. Kurulum

```bash
git clone https://github.com/TheNativeStranger/game-studio.git ~/Desktop/projects/game-studio
```

```bash
claude plugin marketplace add ~/Desktop/projects/game-studio
```

```bash
claude plugin install game-studio@game-studio-local
```

Claude'u yeniden aç.

## 3. Güncelleme

Depoda değişiklik yaptıktan sonra `.claude-plugin/plugin.json` ve `.claude-plugin/marketplace.json` içindeki sürümü artır, ardından:

```bash
claude plugin marketplace update game-studio-local
```

```bash
claude plugin update game-studio@game-studio-local
```

## 4. İlk iş

Claude'u oyun projesinin klasöründe aç ve yaz:

```text
/game-studio:studio Oyuncu kapıyı anahtarla açabilsin, anahtar yoksa uyarı çıksın
```

Direktör şu sırayla ilerler:

1. Projeyi okur, motoru ve aşamayı belirler.
2. İş kartını açar: `docs/production/tasks/001-kapi-anahtari.md`
3. Yeni mekanikse tasarımı onayına sunar.
4. Gereken uzmanları çağırır.
5. Betikleri ve testleri çalıştırır.
6. Sana yapılanları, gerçek sonuçları, elle oynaman gerekenleri, riskleri ve beklenen kararı raporlar.

## 5. Örnek komutlar

```text
/game-studio:studio Yeni proje: tek parmakla oynanan özgün bir mobil bulmaca. Motor öner, karar bana kalsın
/game-studio:studio Yapım aşamasındaki sahnede kare süresi düştü, ölç ve sebebini bul
/game-studio:studio Ana karakterin 20 satırlık diyaloğunu seslendir, önce tek örnek ve maliyet göster
/game-studio:studio Mağaza sayfası için kapak, 5 ekran görüntüsü planı ve metin hazırla
/game-studio:studio Beta öncesi lisans, yaş derecelendirmesi ve veri kontrolü yap
```

Tek bir uzmanı doğrudan çağırmak istersen: `@game-studio:qa-engineer` yaz ya da Direktör'e o rolle çalışmasını söyle.

## 6. Onay noktaları

| Ekip senden ne zaman onay ister? |
|---|
| Motor, mimari ve yeni mekanik kararlarında |
| Stil rehberi ve oyunun tonunda |
| Bir işte dörtten fazla rol gerektiğinde |
| ElevenLabs ve Canva'da kredi harcamadan önce |
| Commit, push, mağazaya gönderme ve yayında |
| Aynı hata iki kez döndüğünde |

## 7. Üretim düzeni

| Aşama | Soru |
|---|---|
| Prototip | Çekirdek döngü eğlenceli mi? |
| Vertical Slice | Bir bölüm son kalitede ve bütçede yapılabiliyor mu? |
| Alpha | Bütün özellikler var mı? |
| Beta | İçerik tamam mı, yalnızca hata mı düzeltiliyor? |
| Release Candidate | Kritik hata yok, platform gereksinimleri tamam mı? |

Bir işin **bitmiş** sayılması için: her kabul ölçütünün testi ya da oynanış adımı olmalı, betik çıktısı kayıtta olmalı, performansı etkileyen işte önce ve sonra ölçümü bulunmalı, yeni uyarı çıkmamalı, eski kayıtlar açılmalı, yeni asset'in lisansı belli olmalı.

## 8. Oyun projesinde oluşan klasörler

```text
docs/
├── production/tasks/        İş kartları
├── production/asset-ledger.csv  Varlık defteri
├── design/                  Tasarım ve bölüm planları
├── tech/                    Mimari kararlar
├── art/style-guide.md       Stil rehberi
├── narrative/               Diyalog tabloları
├── audio/                   Ses listeleri
├── ui/                      Arayüz belirtimleri
└── marketing/               Mağaza ve tanıtım
art/source/                  Blender kaynakları
audio/source/                Ses kaynakları
```

## 9. Asset üretimi

**Adlandırma:** `tur_ad_varyant`, küçük harf, Türkçe karaktersiz: `chr_kahraman_a`, `vo_kahraman_0012`, `sfx_kapi_acilis`, `ui_ikon_altin`.

**3B (Blender):** Kaynak `.blend` dosyası `art/source/` altında kalır, oyuna FBX ya da glTF gider. Ölçek 1 birim 1 metredir.

**2B (Canva):** Adaylar üretilir, seçim sende. Oyun içi görseller PNG olarak dışa aktarılır.

**Ses (ElevenLabs):** Önce maliyet tahmini ve tek örnek, sonra toplu üretim. Dosyalar WAV, 48 kHz.

**Varlık defteri:** Her dosya `docs/production/asset-ledger.csv` içinde kaynağı, aracı ve lisansıyla kayıtlıdır. Lisansı belirsiz dosya oyuna girmez.

## 10. Sorun giderme

| Sorun | Çözüm |
|---|---|
| `/game-studio:studio` görünmüyor | Claude'u yeniden aç, `claude plugin list` ile eklentiye bak |
| "Blender bağlı değil" | Blender'ı ve MCP eklentisini kur |
| Canva ya da ElevenLabs bulunamıyor | Ayarlar → Bağlayıcılar'da bağlantıya bak |
| `NO_RUNNER: Unity ... not found` | Projedeki Unity sürümünü Unity Hub'dan kur |
| `NO_RUNNER: set UE_EDITOR_CMD` | `UE_EDITOR_CMD` değişkenine UnrealEditor-Cmd yolunu ver |
| Ses efekti üretilmiyor | Tam ElevenLabs bağlantısını ekle |
| Kullanım hakkı hızlı bitiyor | [Maliyet rehberindeki](costs.md) kuralları uygula |

## 11. Kapatma ve kaldırma

Geçici kapatmak için Claude'da Özelleştirme → Eklentiler sayfasındaki düğmeyi kullan ya da:

```bash
claude plugin disable game-studio@game-studio-local
```

Tamamen kaldırmak için:

```bash
claude plugin uninstall game-studio@game-studio-local
```
