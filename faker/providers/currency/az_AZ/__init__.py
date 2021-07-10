from .. import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    # Format: (code, name)
    # Source: https://az.wikipedia.org/wiki/M%C3%B6vcud_valyutalar%C4%B1n_siyah%C4%B1s%C4%B1
    currencies = (
        ('USD', 'ABŞ dolları'), ('ALL', 'Albaniya leki'), ('AOA', 'Anqola kvanzası'), ('ARS', 'Argentina pesosu'),
        ('AWG', 'Aruba florini'), ('EUR', 'Avro'), ('AUD', 'Avstraliya dolları'), ('AZN', 'Azərbaycan manatı'),
        ('BSD', 'Baham dolları'), ('BDT', 'Banqladeş takası'), ('BBD', 'Barbados dolları'), ('BZD', 'Beliz dolları'),
        ('BMD', 'Bermud dolları'), ('MMK', 'Birma kyatı'), ('BOB', 'Boliviya bolivianosu'), ('BGN', 'Bolqarıstan levi'),
        ('BAM', 'Bosniya və Herseqovina konvertasiya olunan markası'), ('BWP', 'Botsvana pulası'),
        ('BRL', 'Braziliya realı'), ('GBP', 'Britaniya funtu'), ('GBP', 'Britaniya funtu[C]'),
        ('BND', 'Bruney dolları'), ('BIF', 'Burundi frankı'), ('BTN', 'Butan nqultrumu'), ('AED', 'BƏƏ dirhəmi'),
        ('BHD', 'Bəhreyn dinarı'), ('XPF', 'CFP frankı'), ('JEP', 'Cersi funtu'), ('DJF', 'Cibuti frankı'),
        ('GIP', 'Cəbəllütariq funtu'), ('ZAR', 'Cənubi Afrika randı'), ('KRW', 'Cənubi Koreya vonası'),
        ('SSP', 'Cənubi Sudan funtu'), ('DKK', 'Danimarka kronu'), ('PRB', 'Dnestryanı rublu'),
        ('DOP', 'Dominikan pesosu'), ('ETB', 'Efiopiya birri'), ('ERN', 'Eritreya nakfası'),
        ('AMD', 'Ermənistan dramı'), ('SZL', 'Esvatini lilangenisi'), ('FJD', 'Fici dolları'),
        ('PHP', 'Filippin pesosu'), ('FKP', 'Folklend adaları funtu'), ('(yoxdur)', 'Gernsi funtu'),
        ('GGP', 'Gernsi funtu'), ('GEL', 'Gürcüstan larisi'), ('HTG', 'Haiti qurdu'), ('INR', 'Hindistan rupisi'),
        ('HNL', 'Honduras lempirası'), ('HKD', 'Honkonq dolları'), ('CVE', 'Kabo-Verde eskudosu'),
        ('KHR', 'Kamboca rieli'), ('CAD', 'Kanada dolları'), ('KYD', 'Kayman adaları dolları'),
        ('KES', 'Keniya şillinqi'), ('COP', 'Kolumbiya pesosu'), ('KMF', 'Komor frankı'), ('CDF', 'Konqo frankı'),
        ('CRC', 'Kosta-Rika kolonu'), ('CUC', 'Kuba konvertasiya olunan pesosu'), ('CUP', 'Kuba pesosu'),
        ('BYN', 'Köhnə Belarus rublu'), ('KWD', 'Küveyt dinarı'), ('LAK', 'Laos kipi'), ('LSL', 'Lesoto lotisi'),
        ('LRD', 'Liberiya dolları'), ('LBP', 'Livan funtu'), ('LYD', 'Liviya dinarı'), ('HUF', 'Macarıstan forinti'),
        ('MOP', 'Makao patakası'), ('MKD', 'Makedoniya denarı'), ('MGA', 'Malaqasi ariarisi'),
        ('MWK', 'Malavi kvaçası'), ('MYR', 'Malayziya ringgiti'), ('MVR', 'Maldiv rufiyası'), ('MUR', 'Mavriki rupisi'),
        ('MRO', 'Mavritaniya ugiya'), ('MRO', 'Mavritaniya ugiyası'), ('MXN', 'Meksika pesosu'), ('IMP', 'Men funtu'),
        ('EGP', 'Misir funtu'), ('MDL', 'Moldova leyi'), ('MNT', 'Monqolustan tuqriki'), ('MZN', 'Mozambik metikalı'),
        ('SHP', 'Müqəddəs Yelena funtu'), ('MAD', 'Mərakeş dirhəmi'), ('XAF', 'Mərkəzi Afrika AMİ frankı'),
        ('NAD', 'Namibiya dolları'), ('NPR', 'Nepal rupisi'), ('ANG', 'Niderland Antil adaları quldeni'),
        ('NGN', 'Nigeriya nayrası'), ('NIO', 'Nikaraqua kordobası'), ('NOK', 'Norveç kronu'), ('OMR', 'Oman rialı'),
        ('PKR', 'Pakistan rupisi'), ('PAB', 'Panama balboası'), ('PGK', 'Papua-Yeni Qvineya kinası'),
        ('PYG', 'Paraqvay quaranisi'), ('PLN', 'Polşa zlotısı'), ('GMD', 'Qambiya dalasisi'), ('GHS', 'Qana sedisi'),
        ('GYD', 'Qayana dolları'), ('KZT', 'Qazaxıstan tengəsi'), ('GTQ', 'Qvatemala ketsalı'),
        ('GNF', 'Qvineya frankı'), ('KGS', 'Qırğız somu'), ('XOF', 'Qərbi Afrika AMİ frankı'), ('QAR', 'Qətər rialı'),
        ('RWF', 'Ruanda frankı'), ('RON', 'Rumıniya leyi'), ('RUB', 'Rus rublu'), ('RUB', 'Rusiya rublu'),
        ('WST', 'Samoa talası'), ('STD', 'San-Tome və Prinsipi dobrası'), ('RSD', 'Serbiya dinarı'),
        ('SCR', 'Seyşel rupisi'), ('SGD', 'Sinqapur dolları'), ('SBD', 'Solomon adaları dolları'),
        ('SOS', 'Somali şillinqi'), ('SDG', 'Sudan funtu'), ('SRD', 'Surinam dolları'), ('SYP', 'Suriya funtu'),
        ('SLL', 'Syerra-Leone leonesi'), ('SAR', 'Səudiyyə Ərəbistanı rialı'), ('TJS', 'Tacikistan somonisi'),
        ('THB', 'Tailand bahtı'), ('TZS', 'Tanzaniya şillinqi'), ('TOP', 'Tonqa paanqası'),
        ('TTD', 'Trinidad və Tobaqo dolları'), ('TND', 'Tunis dinarı'), ('TVD', 'Tuvalu dolları'),
        ('TRY', 'Türk lirəsi'), ('TMT', 'Türkmənistan manatı'), ('UAH', 'Ukrayna qrivnası'), ('UGX', 'Uqanda şillinqi'),
        ('UYU', 'Uruqvay pesosu'), ('VUV', 'Vanuatu vatusu'), ('VEF', 'Venesuela bolivarı'), ('VND', 'Vyetnam donqu'),
        ('HRK', 'Xorvatiya kunası'), ('JMD', 'Yamayka dolları'), ('JPY', 'Yapon yeni'), ('BYR', 'Yeni Belarus rublu'),
        ('PEN', 'Yeni Peru solu'), ('TWD', 'Yeni Tayvan dolları'), ('NZD', 'Yeni Zelandiya dolları'),
        ('ILS', 'Yeni İsrail şekeli'), ('YER', 'Yəmən rialı'), ('ZMW', 'Zambiya kvaçası'), ('CZK', 'Çex kronu'),
        ('CLP', 'Çili pesosu'), ('CNY', 'Çin yuanı'), ('UZS', 'Özbək somu'), ('IDR', 'İndoneziya rupiası'),
        ('JOD', 'İordaniya dinarı'), ('IRR', 'İran rialı'), ('IQD', 'İraq dinarı'), ('ISK', 'İslandiya kronası'),
        ('SEK', 'İsveç kronu'), ('CHF', 'İsveçrə frankı'), ('KPW', 'Şimali Koreya vonası'), ('LKR', 'Şri-Lanka rupisi'),
        ('XCD', 'Şərqi Karib dolları'), ('AFN', 'Əfqanıstan əfqanisi'), ('DZD', 'Əlcəzair dinarı')

    )

    price_formats = ["#,##", "%#,##", "%##,##", "%.###,##", "%#.###,##"]

    def pricetag(self):
        return (
                self.numerify(self.random_element(self.price_formats))
                + "\N{no-break space}AZN"
        )
