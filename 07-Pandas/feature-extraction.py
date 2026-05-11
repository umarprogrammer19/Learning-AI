import pandas as pd

# Loading The Anime Data
df = pd.read_csv(r"anime.csv")

# 0      1  Fullmetal Alchemist: BrotherhoodTV (64 eps)Apr...   9.10
# 1      2  Steins;GateTV (24 eps)Apr 2011 - Sep 20112,473...   9.07
# 2      3  Bleach: Sennen Kessen-henTV (13 eps)Oct 2022 -...   9.06
# 3      4  Gintama°TV (51 eps)Apr 2015 - Mar 2016605,113 ...   9.06
# 4      5  Shingeki no Kyojin Season 3 Part 2TV (10 eps)A...   9.05
# 5      6  Gintama'TV (51 eps)Apr 2011 - Mar 2012534,105 ...   9.04
# 6      7  Gintama: The FinalMovie (1 eps)Jan 2021 - Jan ...   9.04
# 7      8  Hunter x Hunter TV (148 eps)Oct 2011 - Sep 201...   9.04
# 8      9  Kaguya-sama wa Kokurasetai: Ultra RomanticTV (...   9.04
# 9     10  Gintama': EnchousenTV (13 eps)Oct 2012 - Mar 2...   9.03
# 10    11  Shingeki no Kyojin: The Final Season - Kankets...   9.03
# 11    12  Ginga Eiyuu DensetsuOVA (110 eps)Jan 1988 - Ma...   9.02
# 12    13  Bleach: Sennen Kessen-hen - Ketsubetsu-tanTV (...   8.99
# 13    14  Fruits Basket: The FinalTV (13 eps)Apr 2021 - ...   8.99
# 14    15  Gintama.TV (12 eps)Jan 2017 - Mar 2017302,232 ...   8.98
# 15    16  GintamaTV (201 eps)Apr 2006 - Mar 20101,034,41...   8.94
# 16    17  Koe no KatachiMovie (1 eps)Sep 2016 - Sep 2016...   8.94
# 17    18  3-gatsu no Lion 2nd SeasonTV (22 eps)Oct 2017 ...   8.93
# 18    19  Clannad: After StoryTV (24 eps)Oct 2008 - Mar ...   8.93
# 19    20  Code Geass: Hangyaku no Lelouch R2TV (25 eps)A...   8.91
# 20    21  Gintama Movie 2: Kanketsu-hen - Yorozuya yo Ei...   8.91
# 21    22  Violet Evergarden MovieMovie (1 eps)Sep 2020 -...   8.89
# 22    23  Owarimonogatari 2nd SeasonTV (7 eps)Aug 2017 -...   8.88
# 23    24  Gintama.: Shirogane no Tamashii-hen - Kouhan-s...   8.88
# 24    25  MonsterTV (74 eps)Apr 2004 - Sep 20051,041,081...   8.87
# 25    26  Kimi no Na wa.Movie (1 eps)Aug 2016 - Aug 2016...   8.84
# 26    27  Kaguya-sama wa Kokurasetai: First Kiss wa Owar...   8.84
# 27    28  Bocchi the Rock!TV (12 eps)Oct 2022 - Dec 2022...   8.83
# 28    29  The First Slam DunkMovie (1 eps)Dec 2022 - Dec...   8.83
# 29    30  Vinland Saga Season 2TV (24 eps)Jan 2023 - Jun...   8.82
# 30    31  Jujutsu Kaisen 2nd SeasonTV (23 eps)Jul 2023 -...   8.82
# 31    32  Gintama.: Shirogane no Tamashii-henTV (12 eps)...   8.81
# 32    33  Kingdom 3rd SeasonTV (26 eps)Apr 2020 - Oct 20...   8.81
# 33    34  Mob Psycho 100 IITV (13 eps)Jan 2019 - Apr 201...   8.80
# 34    35  Shingeki no Kyojin: The Final SeasonTV (16 eps...   8.80
# 35    36  Kimetsu no Yaiba: Yuukaku-henTV (11 eps)Dec 20...   8.79
# 36    37  Kizumonogatari III: Reiketsu-henMovie (1 eps)J...   8.79
# 37    38  "Oshi no Ko"TV (11 eps)Apr 2023 - Jun 2023645,...   8.79
# 38    39  Haikyuu!! Karasuno Koukou vs. Shiratorizawa Ga...   8.78
# 39    40  Sen to Chihiro no KamikakushiMovie (1 eps)Jul ...   8.78
# 40    41  Monogatari Series: Second SeasonTV (26 eps)Jul...   8.77
# 41    42  Shingeki no Kyojin: The Final Season Part 2TV ...   8.77
# 42    43  Hajime no IppoTV (75 eps)Oct 2000 - Mar 200255...   8.76
# 43    44  Cowboy BebopTV (26 eps)Apr 1998 - Apr 19991,79...   8.75
# 44    45  Kingdom 4th SeasonTV (26 eps)Apr 2022 - Oct 20...   8.75
# 45    46  Vinland SagaTV (24 eps)Jul 2019 - Dec 20191,40...   8.74
# 46    47  Mushishi Zoku Shou 2nd SeasonTV (10 eps)Oct 20...   8.73
# 47    48  Shouwa Genroku Rakugo Shinjuu: Sukeroku Futata...   8.72
# 48    49  Mob Psycho 100 IIITV (12 eps)Oct 2022 - Dec 20...   8.71
# 49    50  Rurouni Kenshin: Meiji Kenkaku Romantan - Tsui...   8.71


# Make a New Column For Episode count
def extract_episodes(txt):
    check = False
    data = ""
    for i in txt:
        if i == ")":
            check = False
            return data
        if check == True:
            data = data + i
        if i == "(":
            check = True


df["Episodes"] = df["Title"].apply(extract_episodes).str.replace(" eps", "").astype(int)
