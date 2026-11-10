---
name: asset-pipeline
description: "3B, 2B ve ses dosyalarının adlandırma, klasör, bütçe, varlık defteri ve motora aktarma kuralları. Asset üreten ya da projeye alan her rol kullanır."
---
# Asset hattı

## Klasörler
| İçerik | Kaynak | Oyuna giden |
|---|---|---|
| 3B | `art/source/*.blend` | Motorun model klasörü, FBX ya da glTF |
| 2B | Canva tasarımı, bağlantısı defterde | PNG |
| Ses | `audio/source/` | WAV, 48 kHz |

Adlandırma: `tur_ad_varyant`, küçük harf, Türkçe karaktersiz, boşluksuz (`chr_kahraman_a`, `vo_kahraman_0012`, `sfx_kapi_acilis`, `ui_ikon_altin`). Seslendirme dosyasının numarası diyalog tablosundaki satır kimliğidir.

## Varlık defteri
Her asset `docs/production/asset-ledger.csv` dosyasına bir satır olarak yazılır:

`path,source,tool,license,prompt_or_notes,approved_by`

- **source:** `original`, `generated`, `purchased`, `open-license`
- **tool:** `blender`, `canva`, `elevenlabs`, `human`
- **license:** Lisansın adı ya da aboneliğin ticari kullanım durumu. Belirsizse dosya oyuna girmez.

Kontrol: `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check-assets.py"`

## Kredi ve onay
ElevenLabs ve Canva üretiminden önce adet ve tahmini maliyet onaya sunulur. Önce tek örnek üretilir, stil onaylanınca toplu üretime geçilir. Başarısız üretim sormadan tekrarlanmaz.

## Yapay zekâ ve haklar
Gerçek bir kişinin sesi yazılı izin olmadan kopyalanmaz. Telifli karakter, logo ya da var olan bir oyuna ait içerik üretilmez. Mağazaların istediği yapay zekâ beyanı için `tool` sütunu kullanılır.

## Aktarma kontrolü
- **Model:** ölçek, pivot, üçgen sayısı, materyal adı
- **Doku:** boyut, saydamlık, sıkıştırma
- **Ses:** örnekleme hızı, ses yüksekliği, baştaki ve sondaki sessizlik
