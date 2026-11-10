# Maliyet ve token mantığı

[← README](../README.md)

## Nerede para harcanır?

| Kaynak | Ödenen yer | Not |
|---|---|---|
| Rollerin okuması ve yazması | Claude hesabın | Abonelikte kullanım hakkından düşer, API'de faturalanır |
| Seslendirme | ElevenLabs kredisi | Üretimden önce onay alınır |
| Görsel tasarım | Canva hesabın | Hesabındaki kullanım haklarına bağlıdır |
| Betikler | Yok | Bilgisayarında çalışır, 0 token |
| Motor ve araç lisansları | İlgili firma | Unity'nin kendi planları vardır, Blender ücretsizdir |

## Token nasıl harcanır?

Bir rol çağrıldığında şunlar okunur: Claude Code'un sistem talimatı, rolün kartı, kullanabildiği araçların tanımı, Direktör'ün verdiği iş ve okuduğu dosyalar. Bu yüzden en kısa soru bile sıfır tutmaz: Sonnet'te ölçülen en düşük açılış 0,07 dolardır.

Her rol kendi ayrı bağlamında çalışır ve Direktör'e yalnızca kısa rapor döner. Sohbetin tamamı rollere aktarılmaz. Pahalı olan, uzun süren ana oturumdur; çünkü her turda biriken bağlam yeniden okunur.

## Ölçümler

Kasım 2026'da, boş klasörde, tek ve basit bir soruyla ölçüldü. Fiyatlar API karşılığıdır, önbellek durumu sonucu etkiler.

| Rol | Model | Yapılan | Maliyet |
|---|---|---|---|
| Audio Director, kısıtlama öncesi | Sonnet | İki araç araması, bütün araçlar açık | 0,43 $ |
| Audio Director, kısıtlama sonrası | Sonnet | Bir araç araması | 0,20 $ |
| 2D Artist | Sonnet | Bir araç araması | 0,11 $ |
| Stüdyo Direktörü | Sonnet | Basit cevap | 0,09 $ |
| 3D Artist | Sonnet | Bir araç araması | 0,07 $ |
| QA Engineer | Sonnet | Basit cevap | 0,07 $ |
| Legal ve Compliance | Haiku | Basit cevap | 0,003 $ |
| Ekip boşta | | Her oturumda açıklamaların yükü | Yaklaşık 900 token |

İlk iki satır birebir aynı deneme değildir: birinde iki arama, ötekinde bir arama vardır.

## Tahminler

Bunlar gerçek bir oyunda ölçülmedi. İlk iş kartlarından sonra güncellenmelidir.

| İş | Çalışan roller | Tahmini maliyet |
|---|---|---|
| Küçük hata | Programcı, QA | 0,50-2 $ |
| Orta özellik | Tasarım, kod, test | 3-8 $ |
| 20 rolün hepsi aynı işte | Tümü | 10-30 $ |

## Tasarruf kuralları

| Kural | Etkisi |
|---|---|
| Betiğin yapabildiği işi role yaptırma | 0 token |
| Yalnızca gereken rolü çağır | Her rol en az birkaç sent açılış maliyeti getirir |
| Bir işte dörtten fazla rol için onay iste | Kontrolsüz büyümeyi durdurur |
| Direktör Sonnet, Opus yalnızca mimaride | En uzun çalışan parça ucuzlar |
| Dış araç kullanan rollerin araçlarını sınırla | Kısıtlamadan sonra ölçülen çağrı yarıya yakın düştü |
| Skill'i yalnızca gerektiğinde yükle | draw.io skill'i gibi uzun belgeler her role binmez |
| İş kartı kullan | Roller sohbeti değil kısa kartı okur |
| Sonucu en fazla 15 satırla raporla | Direktör'ün bağlamı şişmez |
| Çeviriyi Haiku'ya verme | Yeniden yapılan işin maliyetinden kaçınılır; Haiku geçmişte çeviri hatası yaptı |

## Kendin ölçmek için

Tek bir rolün maliyetini komut satırından görebilirsin:

```bash
claude -p --agent game-studio:qa-engineer --output-format json "Rolünü üç kelimeyle yaz." | python3 -c "import json,sys; print(json.load(sys.stdin)['total_cost_usd'])"
```

Ölçümü yaptıktan sonra bu dosyadaki tabloyu güncelle.
