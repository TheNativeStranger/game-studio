# Betikler

[← README](../README.md)

Betikler bilgisayarında çalışır ve token harcamaz. Oyun projesinin klasöründen çalıştırılır.

**Çıkış kodları:** `0` sorun yok, `1` sorun bulundu, `2` denenecek bir şey ya da gereken araç yok.

## Özet

| Betik | İş |
|---|---|
| `new-task` | İş kartını ve varlık defterini açar |
| `check-game` | Motoru bulur, testleri çalıştırır, yalnızca özeti verir |
| `check-media` | Doku boyutu, üçgen sayısı, ses biçimi |
| `check-loc` | Eksik çeviri, aşırı uzun metin, tekrar eden anahtar |
| `check-assets` | Her dosya varlık defterinde ve lisansı belli mi? |
| `check-drawio` | Çizim dosyası geçerli mi? |

## new-task

```bash
python3 scripts/new-task.py "Kapı anahtarı"
```

Sıradaki numarayla `docs/production/tasks/001-kapi-anahtari.md` dosyasını açar. Varlık defteri yoksa onu da oluşturur.

## check-game

```bash
bash scripts/check-game.sh
```

| Proje | Nasıl tanınır | Ne çalışır |
|---|---|---|
| Godot | `project.godot` | GUT eklentisi varsa testler, yoksa başsız açılış |
| Unity | `ProjectSettings/ProjectVersion.txt` | Projedeki sürümle EditMode testleri |
| Unreal | `*.uproject` | `UE_EDITOR_CMD` tanımlıysa otomasyon testleri |
| Web | `package.json` | `npm test` |

Örnek çıktı: `NO_RUNNER: godot not found`

## check-media

```bash
python3 scripts/check-media.py --max-texture 2048 --max-tris 50000 --rate 48000
```

`art`, `audio`, `assets`, `Assets`, `Content` klasörlerini tarar. PNG boyutunu, WAV örnekleme hızını ve glTF ya da GLB üçgen sayısını denetler.

Örnek çıktı:

```text
TEXTURE_TOO_BIG 4096x4096: art/big.png
TOO_MANY_TRIS 100000: art/m.gltf
WRONG_RATE 44100: audio/a.wav
SUMMARY: 4 files checked, 3 problems
```

## check-loc

```bash
python3 scripts/check-loc.py localization/strings.csv
```

CSV'nin ilk sütunu anahtar, ikincisi kaynak dil, kalanı çevirilerdir.

| Çıktı | Anlamı |
|---|---|
| `MISSING` | Çeviri boş |
| `BROKEN_SLOT` | `{n}` ya da `%s` gibi bir değişken kaybolmuş |
| `TOO_LONG` | Çeviri kaynağın 1,4 katından uzun |
| `DUPLICATE_KEY` | Aynı anahtar iki kez var |

## check-assets

```bash
python3 scripts/check-assets.py
```

Sanat ve ses dosyalarını `docs/production/asset-ledger.csv` ile karşılaştırır.

| Çıktı | Anlamı |
|---|---|
| `NOT_IN_LEDGER` | Dosya defterde yok |
| `NO_LICENSE` | Lisans boş ya da belirsiz |
| `FILE_MISSING` | Defterde var, diskte yok |

## check-drawio

```bash
python3 scripts/check-drawio.py docs/design/akis.drawio
```

XML'in geçerliliğini, yinelenen kimlikleri ve ok bağlantılarını denetler.
