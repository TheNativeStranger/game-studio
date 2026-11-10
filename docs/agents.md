# Ajanlar ve görevleri

[← README](../README.md)

Stüdyoda 20 rol vardır. Direktör ana oturumdur, diğerleri ihtiyaç olunca çağrılır. Boşta duran rol para harcamaz.

## Maliyetleri nasıl okumalı?

- **Tipik iş maliyeti** bir rolün gerçek bir işte harcayacağı tahmini tutardır, henüz ölçülmedi.
- **Ölçülen en küçük çağrı** basit bir deneme sorusunun gerçek maliyetidir; rolün açılış maliyetini gösterir.
- Tutarlar API fiyatıyladır. Claude aboneliğinde fatura yerine kullanım hakkından düşer.
- ElevenLabs ve Canva kredileri bu tutarlara dahil değildir.

## Özet

| Rol | Model | Görevi | Dış araç | Tipik iş (tahmin) | Ölçülen en küçük çağrı |
|---|---|---|---|---|---|
| Stüdyo Direktörü | Sonnet | İşi anlar, rolleri seçer, kararları sana getirir, sonucu denetler | Ana oturum | 2 $ üstü | 0,09 $ |
| Teknik Direktör | Opus | Motor seçimi, mimari, kare süresi ve bellek bütçesi | Engineering skill'leri | 2 $ üstü | Ölçülmedi |
| Creative Director | Sonnet | Sanat, ses ve ton bütünlüğü, özgünlük denetimi | Yok | 0,50-2 $ | Ölçülmedi |
| Game Designer | Sonnet | Çekirdek döngü, mekanikler, denge tabloları | Yok | 0,50-2 $ | Ölçülmedi |
| Level Designer | Sonnet | Bölüm akışı, zorluk eğrisi, karşılaşmalar | draw.io (yerel) | 0,50-2 $ | Ölçülmedi |
| Narrative Designer | Sonnet | Dünya, karakter, görev, diyalog tabloları | Yok | 0,50-2 $ | Ölçülmedi |
| UI/UX Designer | Sonnet | Menü akışı, HUD, kontroller, erişilebilirlik | Design skill'leri (varsa) | 0,50-2 $ | Ölçülmedi |
| Economy ve LiveOps | Sonnet | Ekonomi, ödül, satın alma, etkinlik, ölçümler | Unity skill'leri (varsa) | 0,50-2 $ | Ölçülmedi |
| Gameplay Programmer | Sonnet | Oyuncu kontrolü, mekanik, yapay zekâ, arayüz mantığı | Motor skill'leri | 2 $ üstü | Ölçülmedi |
| Engine Programmer | Sonnet | Render, fizik, bellek, kare süresi | Motor skill'leri | 2 $ üstü | Ölçülmedi |
| Network Programmer | Sonnet | Çok oyunculu, sunucu otoritesi, hile, kayıt verisi | Engineering skill'leri | 2 $ üstü | Ölçülmedi |
| Technical Artist | Sonnet | Shader, materyal, asset içe aktarma, draw call | Motor skill'leri | 0,50-2 $ | Ölçülmedi |
| 3D Artist ve Animator | Sonnet | Model, UV, rig, animasyon, dışa aktarma | Blender | 2 $ üstü | 0,07 $ |
| 2D Artist | Sonnet | İkon, arayüz görseli, kapak, 2B varlıklar | Canva (kredi) | 0,50-2 $ | 0,11 $ |
| Audio Director | Sonnet | Ses seçimi, seslendirme, ses efekti ve müzik planı | ElevenLabs (kredi) | 0,50-2 $ | 0,20 $ |
| Localization Specialist | Sonnet | Metin tabloları, çeviri, yazı tipi, kültür kontrolü | `check-loc` | 0,50-2 $ | Ölçülmedi |
| QA Engineer | Sonnet | Test planı, otomatik test, elle oynanacak liste, hata raporu | `check-game`, `check-media` | 0,50-2 $ | 0,07 $ |
| Build ve Release | Sonnet | Derleme hattı, platform paketi, mağaza kontrol listesi | Engineering skill'leri | 0,50-2 $ | Ölçülmedi |
| Marketing Producer | Sonnet | Mağaza sayfası, ekran görüntüsü, fragman, duyuru | Canva (kredi), Remotion | 0,50-2 $ | Ölçülmedi |
| Legal ve Compliance | Haiku | Lisans, yaş derecelendirmesi, veri, mağaza kuralları | `check-assets` | 0,50 $ altı | 0,003 $ |

## Kim, ne zaman çağrılır?

| Durum | Roller |
|---|---|
| Küçük hata | Programcı, QA |
| Yeni mekanik | Game Designer, Gameplay Programmer, QA |
| Yeni bölüm | Level Designer, 3D Artist, Gameplay Programmer, QA |
| Performans sorunu | Engine Programmer, Technical Artist |
| Çok oyunculu özellik | Teknik Direktör, Network Programmer, QA |
| Seslendirme | Narrative Designer, Audio Director |
| Çeviri | Localization Specialist |
| Mağaza hazırlığı | Marketing Producer, Build ve Release, Legal |
| Motor seçimi | Teknik Direktör |
| Stil belirleme | Creative Director |

## Roller

### Stüdyo Direktörü
<a id="studio-director"></a>

| | |
|---|---|
| **Ajan** | `game-studio:studio-director` |
| **Bölüm** | Yönetim |
| **Model** | Sonnet |
| **Görevi** | İşi anlar, rolleri seçer, kararları sana getirir, sonucu denetler |
| **Çıktısı** | İş kartı, özet rapor |
| **Dış araç** | Ana oturum |
| **Yetkileri** | Read, Grep, Glob, Write, Edit, Bash, Skill, Agent |
| **Tipik iş maliyeti (tahmin)** | 2 $ üstü |
| **Ölçülen en küçük çağrı** | 0,09 $ |

### Teknik Direktör
<a id="technical-director"></a>

| | |
|---|---|
| **Ajan** | `game-studio:technical-director` |
| **Bölüm** | Yönetim |
| **Model** | Opus |
| **Görevi** | Motor seçimi, mimari, kare süresi ve bellek bütçesi |
| **Çıktısı** | `docs/tech/` ADR ve teknik tasarım |
| **Dış araç** | Engineering skill'leri |
| **Yetkileri** | Read, Grep, Glob, Write, Skill |
| **Tipik iş maliyeti (tahmin)** | 2 $ üstü |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### Creative Director
<a id="creative-director"></a>

| | |
|---|---|
| **Ajan** | `game-studio:creative-director` |
| **Bölüm** | Yönetim |
| **Model** | Sonnet |
| **Görevi** | Sanat, ses ve ton bütünlüğü, özgünlük denetimi |
| **Çıktısı** | `docs/art/style-guide.md` |
| **Dış araç** | Yok |
| **Yetkileri** | Read, Grep, Glob, Write, Edit, Skill |
| **Tipik iş maliyeti (tahmin)** | 0,50-2 $ |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### Game Designer
<a id="game-designer"></a>

| | |
|---|---|
| **Ajan** | `game-studio:game-designer` |
| **Bölüm** | Tasarım |
| **Model** | Sonnet |
| **Görevi** | Çekirdek döngü, mekanikler, denge tabloları |
| **Çıktısı** | `docs/design/` |
| **Dış araç** | Yok |
| **Yetkileri** | Read, Grep, Glob, Write, Edit, Skill |
| **Tipik iş maliyeti (tahmin)** | 0,50-2 $ |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### Level Designer
<a id="level-designer"></a>

| | |
|---|---|
| **Ajan** | `game-studio:level-designer` |
| **Bölüm** | Tasarım |
| **Model** | Sonnet |
| **Görevi** | Bölüm akışı, zorluk eğrisi, karşılaşmalar |
| **Çıktısı** | `docs/design/levels/` |
| **Dış araç** | draw.io (yerel) |
| **Yetkileri** | Read, Grep, Glob, Write, Edit, Skill |
| **Tipik iş maliyeti (tahmin)** | 0,50-2 $ |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### Narrative Designer
<a id="narrative-designer"></a>

| | |
|---|---|
| **Ajan** | `game-studio:narrative-designer` |
| **Bölüm** | Tasarım |
| **Model** | Sonnet |
| **Görevi** | Dünya, karakter, görev, diyalog tabloları |
| **Çıktısı** | `docs/narrative/` |
| **Dış araç** | Yok |
| **Yetkileri** | Read, Grep, Glob, Write, Edit, Skill |
| **Tipik iş maliyeti (tahmin)** | 0,50-2 $ |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### UI/UX Designer
<a id="ui-ux-designer"></a>

| | |
|---|---|
| **Ajan** | `game-studio:ui-ux-designer` |
| **Bölüm** | Tasarım |
| **Model** | Sonnet |
| **Görevi** | Menü akışı, HUD, kontroller, erişilebilirlik |
| **Çıktısı** | `docs/ui/` |
| **Dış araç** | Design skill'leri (varsa) |
| **Yetkileri** | Read, Grep, Glob, Write, Edit, Skill |
| **Tipik iş maliyeti (tahmin)** | 0,50-2 $ |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### Economy ve LiveOps
<a id="economy-liveops-designer"></a>

| | |
|---|---|
| **Ajan** | `game-studio:economy-liveops-designer` |
| **Bölüm** | Tasarım |
| **Model** | Sonnet |
| **Görevi** | Ekonomi, ödül, satın alma, etkinlik, ölçümler |
| **Çıktısı** | Ekonomi tabloları |
| **Dış araç** | Unity skill'leri (varsa) |
| **Yetkileri** | Read, Grep, Glob, Write, Edit, Skill |
| **Tipik iş maliyeti (tahmin)** | 0,50-2 $ |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### Gameplay Programmer
<a id="gameplay-programmer"></a>

| | |
|---|---|
| **Ajan** | `game-studio:gameplay-programmer` |
| **Bölüm** | Yazılım |
| **Model** | Sonnet |
| **Görevi** | Oyuncu kontrolü, mekanik, yapay zekâ, arayüz mantığı |
| **Çıktısı** | Oyun kodu |
| **Dış araç** | Motor skill'leri |
| **Yetkileri** | Read, Grep, Glob, Edit, Write, Bash, Skill |
| **Tipik iş maliyeti (tahmin)** | 2 $ üstü |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### Engine Programmer
<a id="engine-programmer"></a>

| | |
|---|---|
| **Ajan** | `game-studio:engine-programmer` |
| **Bölüm** | Yazılım |
| **Model** | Sonnet |
| **Görevi** | Render, fizik, bellek, kare süresi |
| **Çıktısı** | Ölçüm raporu, sistem kodu |
| **Dış araç** | Motor skill'leri |
| **Yetkileri** | Read, Grep, Glob, Edit, Write, Bash, Skill |
| **Tipik iş maliyeti (tahmin)** | 2 $ üstü |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### Network Programmer
<a id="network-programmer"></a>

| | |
|---|---|
| **Ajan** | `game-studio:network-programmer` |
| **Bölüm** | Yazılım |
| **Model** | Sonnet |
| **Görevi** | Çok oyunculu, sunucu otoritesi, hile, kayıt verisi |
| **Çıktısı** | Ağ ve sunucu kodu |
| **Dış araç** | Engineering skill'leri |
| **Yetkileri** | Read, Grep, Glob, Edit, Write, Bash, Skill |
| **Tipik iş maliyeti (tahmin)** | 2 $ üstü |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### Technical Artist
<a id="technical-artist"></a>

| | |
|---|---|
| **Ajan** | `game-studio:technical-artist` |
| **Bölüm** | Yazılım |
| **Model** | Sonnet |
| **Görevi** | Shader, materyal, asset içe aktarma, draw call |
| **Çıktısı** | Asset hattı ayarları |
| **Dış araç** | Motor skill'leri |
| **Yetkileri** | Read, Grep, Glob, Edit, Write, Bash, Skill |
| **Tipik iş maliyeti (tahmin)** | 0,50-2 $ |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### 3D Artist ve Animator
<a id="3d-artist"></a>

| | |
|---|---|
| **Ajan** | `game-studio:3d-artist` |
| **Bölüm** | İçerik |
| **Model** | Sonnet |
| **Görevi** | Model, UV, rig, animasyon, dışa aktarma |
| **Çıktısı** | `art/source/*.blend`, FBX, glTF |
| **Dış araç** | Blender |
| **Yetkileri** | Read, Grep, Glob, Write, Edit, Bash, Skill, ToolSearch, Blender bağlantısı |
| **Tipik iş maliyeti (tahmin)** | 2 $ üstü |
| **Ölçülen en küçük çağrı** | 0,07 $ |

### 2D Artist
<a id="2d-artist"></a>

| | |
|---|---|
| **Ajan** | `game-studio:2d-artist` |
| **Bölüm** | İçerik |
| **Model** | Sonnet |
| **Görevi** | İkon, arayüz görseli, kapak, 2B varlıklar |
| **Çıktısı** | PNG, Canva tasarımı |
| **Dış araç** | Canva (kredi) |
| **Yetkileri** | Read, Grep, Glob, Write, Edit, Bash, Skill, ToolSearch, Canva bağlantısı |
| **Tipik iş maliyeti (tahmin)** | 0,50-2 $ |
| **Ölçülen en küçük çağrı** | 0,11 $ |

### Audio Director
<a id="audio-director"></a>

| | |
|---|---|
| **Ajan** | `game-studio:audio-director` |
| **Bölüm** | İçerik |
| **Model** | Sonnet |
| **Görevi** | Ses seçimi, seslendirme, ses efekti ve müzik planı |
| **Çıktısı** | `docs/audio/`, WAV |
| **Dış araç** | ElevenLabs (kredi) |
| **Yetkileri** | Read, Grep, Glob, Write, Edit, Bash, Skill, ToolSearch, ElevenLabs bağlantısı |
| **Tipik iş maliyeti (tahmin)** | 0,50-2 $ |
| **Ölçülen en küçük çağrı** | 0,20 $ |

### Localization Specialist
<a id="localization-specialist"></a>

| | |
|---|---|
| **Ajan** | `game-studio:localization-specialist` |
| **Bölüm** | İçerik |
| **Model** | Sonnet |
| **Görevi** | Metin tabloları, çeviri, yazı tipi, kültür kontrolü |
| **Çıktısı** | Çeviri tabloları |
| **Dış araç** | `check-loc` |
| **Yetkileri** | Read, Grep, Glob, Write, Edit, Skill |
| **Tipik iş maliyeti (tahmin)** | 0,50-2 $ |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### QA Engineer
<a id="qa-engineer"></a>

| | |
|---|---|
| **Ajan** | `game-studio:qa-engineer` |
| **Bölüm** | Kalite ve yayın |
| **Model** | Sonnet |
| **Görevi** | Test planı, otomatik test, elle oynanacak liste, hata raporu |
| **Çıktısı** | Test kodu, hata raporu |
| **Dış araç** | `check-game`, `check-media` |
| **Yetkileri** | Read, Grep, Glob, Edit, Write, Bash, Skill |
| **Tipik iş maliyeti (tahmin)** | 0,50-2 $ |
| **Ölçülen en küçük çağrı** | 0,07 $ |

### Build ve Release
<a id="build-release-engineer"></a>

| | |
|---|---|
| **Ajan** | `game-studio:build-release-engineer` |
| **Bölüm** | Kalite ve yayın |
| **Model** | Sonnet |
| **Görevi** | Derleme hattı, platform paketi, mağaza kontrol listesi |
| **Çıktısı** | Sürüm listesi |
| **Dış araç** | Engineering skill'leri |
| **Yetkileri** | Read, Grep, Glob, Edit, Write, Bash, Skill |
| **Tipik iş maliyeti (tahmin)** | 0,50-2 $ |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### Marketing Producer
<a id="marketing-producer"></a>

| | |
|---|---|
| **Ajan** | `game-studio:marketing-producer` |
| **Bölüm** | Kalite ve yayın |
| **Model** | Sonnet |
| **Görevi** | Mağaza sayfası, ekran görüntüsü, fragman, duyuru |
| **Çıktısı** | `docs/marketing/` |
| **Dış araç** | Canva (kredi), Remotion |
| **Yetkileri** | Read, Grep, Glob, Write, Edit, Bash, Skill, ToolSearch, Canva bağlantısı |
| **Tipik iş maliyeti (tahmin)** | 0,50-2 $ |
| **Ölçülen en küçük çağrı** | Ölçülmedi |

### Legal ve Compliance
<a id="legal-compliance"></a>

| | |
|---|---|
| **Ajan** | `game-studio:legal-compliance` |
| **Bölüm** | Kalite ve yayın |
| **Model** | Haiku |
| **Görevi** | Lisans, yaş derecelendirmesi, veri, mağaza kuralları |
| **Çıktısı** | Kontrol raporu |
| **Dış araç** | `check-assets` |
| **Yetkileri** | Read, Grep, Glob, Write, Skill |
| **Tipik iş maliyeti (tahmin)** | 0,50 $ altı |
| **Ölçülen en küçük çağrı** | 0,003 $ |

