---
name: production
description: "Oyun işlerinin iş kartı, kilometre taşı ve bitti tanımı kuralları."
---
# Oyun üretim düzeni

Her iş için `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/new-task.py" "<kısa ad>"` ile `docs/production/tasks/NNN-kisa-ad.md` iş kartı aç. Roller sohbeti değil bu kartı okur.

## İş kartı
- **Hedef:** Oyuncu ne yapabilecek ya da ne hissedecek
- **Kabul ölçütleri:** Test edilebilir ya da oynanarak görülebilir maddeler
- **Bütçe:** Hedef platform, kare süresi, bellek
- **Etkilenenler:** Sistemler, sahneler, asset'ler, kayıt verisi, ağ
- **Görevler:** Rol, iş, durum
- **Sonuçlar:** Her rolün kısa çıktısı ve kanıtı

## Kilometre taşları
| Aşama | Soru |
|---|---|
| Prototip | Çekirdek döngü eğlenceli mi? Kod atılabilir |
| Vertical Slice | Bir bölüm son kalitede yapılabiliyor mu, bütçeye sığıyor mu? |
| Alpha | Bütün özellikler var mı? |
| Beta | İçerik tamam mı, yalnızca hata mı düzeltiliyor? |
| Release Candidate | Kritik hata yok, platform gereksinimleri karşılandı mı? |

Aşamaya uymayan işi Stüdyo Direktörü işaretler: prototipte optimizasyon, Beta'da yeni özellik gibi.

## Rol sırası
1. Stüdyo Direktörü kapsamı ve bütçeyi yazar; mimari gerekiyorsa `technical-director`, görsel ya da ses yönü gerekiyorsa `creative-director` çağrılır.
2. Tasarım: `game-designer`, gerekiyorsa `level-designer`, `narrative-designer`, `ui-ux-designer`, `economy-liveops-designer`. Onay alınır.
3. Yazılım: `gameplay-programmer`, `engine-programmer`, `network-programmer`, gerekiyorsa `technical-artist`.
4. İçerik: `3d-artist`, `2d-artist`, `audio-director`, `localization-specialist`. `creative-director` rehbere göre inceler.
5. `qa-engineer` test eder, elle oynanacak listeyi çıkarır.
6. Sürüm çıkacaksa `legal-compliance`, `build-release-engineer` ve `marketing-producer`.

Küçük hatada 1 ve 2 atlanır. Aynı hata iki kez dönerse Stüdyo Direktörü bana sorar.

## Bitti tanımı
- Her kabul ölçütünün karşılığı olan bir test ya da oynanış adımı var
- `check-game.sh` gerçek çıktısı kayıtta
- Performansı etkileyen işte önce ve sonra ölçümü var
- Yeni uyarı ve hata yok
- Kayıt biçimi değiştiyse eski kayıt açılıyor
- Yeni asset varlık defterinde, kaynağı ve lisansı belli (`check-assets.py` geçti)

Kalıplar: `templates/gdd.md`, `templates/tech-design.md`.
