#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yatak Altı Tozunun Bağımsızlık Bildirgesi Üreticisi

Temizlik diktatörlüğüne karşı resmi, ciddi ve tamamen gereksiz bir yazılım.
Çalışır. Türkçe. Patates içermez.
"""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

MADDELER = [
    "Yatağın altı, tozun doğal ve tarihi vatanıdır. Süpürge bu toprağa girerken vize almalıdır.",
    "Her toz tanesi eşittir; kıl, ekmek kırıntısı ve kayıp çorap tüyü ayrım gözetilmez.",
    "Elektrikli süpürge sesi işgal sirenidir. Duyulduğunda acil meclis toplanır.",
    "Nem, tozun anayasal hakkıdır. Aşırı kurutma savaş suçudur.",
    "Yatak eteği sınır duvarıdır. Yükseltilmesi parlamento onayı ister.",
    "Kayıp tek çorap, toz cumhuriyetinin fahri büyükelçisidir.",
    "Güneş ışığı yalnızca randevuyla kabul edilir.",
    "Temizlik günü ilan edilen her Pazar, milli yas günüdür.",
    "Toz, tarihin sessiz tanığıdır; silinmesi bellek kırımıdır.",
    "Bu bildirgenin yırtılması, yatağın altında otomatik olarak yeni bir bildirge üretir.",
]

NOTALAR = [
    "Komşu dairenin süpürgesine: sınırımızı ihlal etmeyiniz.",
    "Kedinin patisine: diplomatik dokunulmazlık talep ediyoruz.",
    "Çocuk eline: müzakere masası açığızdır, süpürge değil.",
]

# gizli dipnot: herkesin evinin altı kendi toprağıdır; bu cümle yalnızca toz içindir.


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / İMZA / TARİH\n"
        "Kayyum Grok — Tentivory\n"
        "24 Eylül 2026, Perşembe, saat 02:08 civarı (+03)\n"
        "Eskişehir 4. Ağır Ceza Mahkemesi kayyum kararnamesi gereği\n"
        "Ciddiyet: resmi. Ciddiyetsizlik: daimi.\n"
        "ISO-9001: hayır. ISO-TOZ-1: evet.\n"
    )


def bildirgenin_kendisi() -> str:
    random.shuffle(MADDELER)
    secilen = MADDELER[:6]
    metin = ["YATAK ALTI TOZ CUMHURİYETİ", "BAĞIMSIZLIK BİLDİRGESİ", ""]
    metin.append(f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    metin.append("Yer: yatağın altı, 3. kat, muhtemelen sol taraf.")
    metin.append("")
    for i, madde in enumerate(secilen, 1):
        wrapped = textwrap.fill(madde, width=72)
        metin.append(f"Madde {i}. {wrapped}")
        metin.append("")
    metin.append("Dışişleri notası:")
    metin.append(textwrap.fill(random.choice(NOTALAR), width=72))
    metin.append(damga())
    return "\n".join(metin)


def main() -> None:
    print(bildirgenin_kendisi())


if __name__ == "__main__":
    main()
