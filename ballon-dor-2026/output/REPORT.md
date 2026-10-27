# Ballon d'Or 2026: juror-by-juror prediction

**Model pick: Harry Kane** (1114 projected points, 80% win probability). Podium: Harry Kane 1114, Ousmane Dembélé 862, Khvicha Kvaratskhelia 791. 17 contenders modelled by name.

Voting closed on 28 September 2026. The award is presented on 26 October 2026.

## Rules applied

- Each of the 100 jurors ranks 10 players: 15, 12, 10, 8, 7, 5, 4, 3, 2, 1 points. The highest total wins.
- Jurors weigh three criteria: (1) Individual Performance, Decisiveness & Impressive Character, the highest-weighted; (2) Team Success, judged by how essential the player was to each trophy; (3) Class & Fair Play, an ethical filter.
- Award window: August to July, so 2026 covers the 2025/26 club season and the 2026 World Cup.

## What is real and what is modelled

- **Real:** every 2024 and 2025 points total, first-place count and regional split, plus the individual ballots listed as *verified* or *partial* (France 2024; Spain, Ghana and South Africa 2025; first places for England, Germany, Italy, Portugal, Netherlands, Brazil, Spain, Scotland, Slovenia, Ecuador; Finland and El Salvador leaving Vinícius off in 2024). The 2025/26 stats and trophies behind every 2026 score are sourced at the bottom.
- **Rebuilt:** every other juror's 2024/2025 positions. France Football published the full sheet, but it could not be fetched from this environment, so `reconstruct.py` rebuilds the most likely set of ballots that reproduces every published number exactly. That includes the totals of every 2026 contender who received votes in those years. Treat a *reconstructed* row as a model estimate, not as that journalist's actual vote.
- **Judgment:** the P (individual) and F (fair play) scores and the 'how essential' trophy factors. Each is written out below and can be edited in `data/criteria.json`.
- **Roster:** the 100 jurors are the list you supplied. Some seats did not match the person who actually voted (Portugal 2024, Ecuador 2024, El Salvador 2024, Spain 2025). Gabon, Honduras and Bolivia appear twice. For 2024 (99 ballots) the second Gabon seat gets no ballot. See `data/jurors.csv`.

## 2024: how the jury scored the top 3

Winner: **Rodri**. Jury: 99 ballots. First places are published counts. Points by confederation and by juror come from the rebuilt ballots, which add up exactly to the published totals.

| Player | Total points | First places | Avg per ballot | Avg UEFA | Avg CONMEBOL | Avg CONCACAF | Avg CAF | Avg AFC | Avg OFC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Rodri** (winner) | 1170 | 49 | 11.8 | 13.6 | 8.2 | 10.8 | 10.4 | 12.2 | 15.0 |
| Vinícius Júnior | 1129 | 35 | 11.4 | 10.6 | 13.5 | 11.2 | 12.8 | 11.0 | 5.0 |
| Jude Bellingham | 917 | 5 | 9.3 | 10.2 | 7.7 | 9.2 | 9.7 | 7.4 | 12.0 |

Ballot sources: 1 verified, 13 partly verified (e.g. only the 1st place is published), 85 rebuilt by the model.

<details><summary>All 100 jurors: points given to Rodri, Vinícius, Bellingham in 2024</summary>

| # | Country | Juror (your roster) | Rodri pos | Vinícius pos | Bellingham pos | Rodri pts | Vinícius pts | Bellingham pts | Their 1st place | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Spain | José Félix Díaz | 4 | 1 | 2 | 8 | 15 | 12 | Vinícius Júnior | partial |
| 2 | Argentina | Enrique Wolff | – | 1 | 2 | 0 | 15 | 12 | Vinícius Júnior | reconstructed |
| 3 | France | Vincent Garcia | 2 | 1 | 3 | 12 | 15 | 10 | Vinícius Júnior | verified |
| 4 | England | Henry Winter | 1 | 3 | 2 | 15 | 10 | 12 | Rodri | partial |
| 5 | Brazil | Cleber Machado | – | 1 | 8 | 0 | 15 | 3 | Vinícius Júnior | partial |
| 6 | Morocco | Mustapha Badri | 1 | 3 | 8 | 15 | 10 | 3 | Rodri | reconstructed |
| 7 | Portugal | Joaquim Rita | 1 | 3 | 2 | 15 | 10 | 12 | Rodri | partial |
| 8 | Belgium | Christophe Franken | 2 | 1 | 3 | 12 | 15 | 10 | Vinícius Júnior | reconstructed |
| 9 | Netherlands | Frans van den Nieuwenhof | 1 | 3 | 5 | 15 | 10 | 7 | Rodri | partial |
| 10 | Mexico | Salvador Aguilera | 1 | 2 | 5 | 15 | 12 | 7 | Rodri | reconstructed |
| 11 | Colombia | Paché Andrade | 9 | 2 | 3 | 2 | 12 | 10 | Lautaro Martínez | reconstructed |
| 12 | Germany | Karlheinz Wild | 1 | 2 | 4 | 15 | 12 | 8 | Rodri | partial |
| 13 | Croatia | Zdravko Reić | 3 | 1 | 2 | 10 | 15 | 12 | Vinícius Júnior | reconstructed |
| 14 | Switzerland | Christophe Cerf | 4 | 2 | 5 | 8 | 12 | 7 | Toni Kroos | reconstructed |
| 15 | Italy | Paolo Condò | 1 | 3 | 6 | 15 | 10 | 5 | Rodri | partial |
| 16 | USA | Paul Kennedy | 2 | 1 | 3 | 12 | 15 | 10 | Vinícius Júnior | reconstructed |
| 17 | Japan | Shuichi Tamura | 2 | 1 | 3 | 12 | 15 | 10 | Vinícius Júnior | reconstructed |
| 18 | Senegal | Salif Diallo | 4 | 3 | – | 8 | 10 | 0 | Lautaro Martínez | reconstructed |
| 19 | Norway | Lars Tjærnås | 1 | 2 | 3 | 15 | 12 | 10 | Rodri | reconstructed |
| 20 | Uruguay | Ricardo Piñeyrúa | 2 | 1 | 4 | 12 | 15 | 8 | Vinícius Júnior | reconstructed |
| 21 | Denmark | Troels Bager Thøgersen | 2 | 1 | 5 | 12 | 15 | 7 | Vinícius Júnior | reconstructed |
| 22 | Iran | Siamak Rahmani | 1 | 5 | 2 | 15 | 7 | 12 | Rodri | reconstructed |
| 23 | Austria | Walter Kowatsch-Schwarz | 1 | 4 | 2 | 15 | 8 | 12 | Rodri | reconstructed |
| 24 | Egypt | Inas Mazhar | 3 | 1 | 2 | 10 | 15 | 12 | Vinícius Júnior | reconstructed |
| 25 | Ecuador | Tito Rosales Cox | 6 | 2 | 7 | 5 | 12 | 4 | Toni Kroos | partial |
| 26 | Nigeria | Samm Audu | 1 | 3 | 2 | 15 | 10 | 12 | Rodri | reconstructed |
| 27 | Türkiye | Fatih Doğan | 1 | 5 | 2 | 15 | 7 | 12 | Rodri | reconstructed |
| 28 | Australia | David Davutovic | 5 | 1 | 4 | 7 | 15 | 8 | Vinícius Júnior | reconstructed |
| 29 | Algeria | Yazid Ouahib | 1 | 3 | 4 | 15 | 10 | 8 | Rodri | reconstructed |
| 30 | Canada | John Molinaro | 3 | 1 | 2 | 10 | 15 | 12 | Vinícius Júnior | reconstructed |
| 31 | Ivory Coast | Adam Khalil | 2 | 1 | 3 | 12 | 15 | 10 | Vinícius Júnior | reconstructed |
| 32 | South Korea | Sungmo Lee | 1 | 8 | 2 | 15 | 3 | 12 | Rodri | reconstructed |
| 33 | Ukraine | Igor Linnyk | 1 | 2 | 3 | 15 | 12 | 10 | Rodri | reconstructed |
| 34 | Paraguay | Gabriel Cazenave | 2 | 1 | 3 | 12 | 15 | 10 | Vinícius Júnior | reconstructed |
| 35 | Russia | Konstantin Klechev | 1 | 4 | 2 | 15 | 8 | 12 | Rodri | reconstructed |
| 36 | Poland | Maciej Iwański | 1 | 3 | 2 | 15 | 10 | 12 | Rodri | reconstructed |
| 37 | Sweden | Olof Lundh | 1 | 3 | 2 | 15 | 10 | 12 | Rodri | reconstructed |
| 38 | Wales | Paul Abbandonato | 1 | 2 | 4 | 15 | 12 | 8 | Rodri | reconstructed |
| 39 | Hungary | György Szöllősi | 1 | 2 | 3 | 15 | 12 | 10 | Rodri | reconstructed |
| 40 | Serbia | Vladimir Novak | 1 | 3 | 2 | 15 | 10 | 12 | Rodri | reconstructed |
| 41 | DR Congo | Jenovic Mbowa | 2 | 1 | 4 | 12 | 15 | 8 | Vinícius Júnior | reconstructed |
| 42 | Scotland | John Greechan | 3 | 2 | 1 | 10 | 12 | 15 | Jude Bellingham | partial |
| 43 | Cameroon | Emmanuel Gustave Samnick | 5 | 1 | 3 | 7 | 15 | 10 | Vinícius Júnior | reconstructed |
| 44 | Panama | Campo Elías Estrada | 1 | 2 | 4 | 15 | 12 | 8 | Rodri | reconstructed |
| 45 | Slovakia | Marcel Merčiak | 1 | 3 | 4 | 15 | 10 | 8 | Rodri | reconstructed |
| 46 | Greece | Manos Staramopoulos | 1 | 3 | 4 | 15 | 10 | 8 | Rodri | reconstructed |
| 47 | Venezuela | Francisco Blavia | 2 | 1 | 7 | 12 | 15 | 4 | Vinícius Júnior | reconstructed |
| 48 | Czechia | Stanislav Hrabě | 1 | 3 | 2 | 15 | 10 | 12 | Rodri | reconstructed |
| 49 | Chile | Danilo Díaz | 2 | 1 | 7 | 12 | 15 | 4 | Vinícius Júnior | reconstructed |
| 50 | Peru | Roberto Castro | 1 | 5 | 2 | 15 | 7 | 12 | Rodri | reconstructed |
| 51 | Costa Rica | Rodrigo Calvo | 7 | 1 | 5 | 4 | 15 | 7 | Vinícius Júnior | reconstructed |
| 52 | Romania | Emanuel Roșu | 4 | 9 | 2 | 8 | 2 | 12 | Erling Haaland | reconstructed |
| 53 | Qatar | Majed Al-Khelaifi | 1 | 5 | 3 | 15 | 7 | 10 | Rodri | reconstructed |
| 54 | Tunisia | Tarek Gharbi | 2 | 1 | 5 | 12 | 15 | 7 | Vinícius Júnior | reconstructed |
| 55 | Finland | Juha Kanerva | 1 | – | 2 | 15 | 0 | 12 | Rodri | partial |
| 56 | Republic of Ireland | Philip Quinn | 3 | 1 | 2 | 10 | 15 | 12 | Vinícius Júnior | reconstructed |
| 57 | Bosnia & Herzegovina | Bakir Tiro | 2 | 4 | 3 | 12 | 8 | 10 | Erling Haaland | reconstructed |
| 58 | Ghana | Michael Oti Adjei | 2 | 3 | 1 | 12 | 10 | 15 | Jude Bellingham | partial |
| 59 | Jamaica | Sean Williams | 4 | 2 | 5 | 8 | 12 | 7 | Dani Carvajal | reconstructed |
| 60 | Iceland | Víðir Sigurðsson | 1 | 2 | 3 | 15 | 12 | 10 | Rodri | reconstructed |
| 61 | Albania | Besnik Dizdari | 2 | 1 | 6 | 12 | 15 | 5 | Vinícius Júnior | reconstructed |
| 62 | North Macedonia | Miko Zahariev | 1 | 2 | 5 | 15 | 12 | 7 | Rodri | reconstructed |
| 63 | South Africa | Mark Gleeson | 2 | 3 | 1 | 12 | 10 | 15 | Jude Bellingham | reconstructed |
| 64 | Iraq | Ali Nouri | 1 | 9 | 2 | 15 | 2 | 12 | Rodri | reconstructed |
| 65 | UAE | Mohammed Al-Joker | 1 | 2 | 10 | 15 | 12 | 1 | Rodri | reconstructed |
| 66 | Cabo Verde | Pedro Clovis | 3 | 1 | 4 | 10 | 15 | 8 | Vinícius Júnior | reconstructed |
| 67 | Montenegro | Danilo Mitrović | 1 | – | 2 | 15 | 0 | 12 | Rodri | reconstructed |
| 68 | Honduras | Gerson Gómez | – | 1 | 3 | 0 | 15 | 10 | Vinícius Júnior | reconstructed |
| 69 | Georgia | Otar Giorgadze | 1 | 2 | 3 | 15 | 12 | 10 | Rodri | reconstructed |
| 70 | Bolivia | Carlos Enrique Rivera | 4 | 2 | 3 | 8 | 12 | 10 | Dani Carvajal | reconstructed |
| 71 | Guinea | Amadou Diouldé Diallo | 1 | 3 | 2 | 15 | 10 | 12 | Rodri | reconstructed |
| 72 | Mali | Souleymane Bobo Tounkara | 4 | 1 | 7 | 8 | 15 | 4 | Vinícius Júnior | reconstructed |
| 73 | Gabon | James Golden Pincent | 6 | 1 | 2 | 5 | 15 | 12 | Vinícius Júnior | reconstructed |
| 74 | New Zealand | Michael Burgess | 1 | 6 | 2 | 15 | 5 | 12 | Rodri | reconstructed |
| 75 | Uzbekistan | Grigoriy Rtveladze | 1 | 2 | – | 15 | 12 | 0 | Rodri | reconstructed |
| 76 | Jordan | Tayseer Al-Amiri | 2 | 1 | – | 12 | 15 | 0 | Vinícius Júnior | reconstructed |
| 77 | Oman | Jaber Al-Ajmi | 2 | 5 | 6 | 12 | 7 | 5 | Dani Carvajal | reconstructed |
| 78 | El Salvador | Claudio Martínez | 4 | – | 3 | 8 | 0 | 10 | Dani Carvajal | partial |
| 79 | Bahrain | Abdullah Ashoor | – | 1 | 5 | 0 | 15 | 7 | Vinícius Júnior | reconstructed |
| 80 | Curaçao | Kenley Basilio | 1 | 8 | 2 | 15 | 3 | 12 | Rodri | reconstructed |
| 81 | Syria | Lutfi Al-Awan | 1 | 2 | 3 | 15 | 12 | 10 | Rodri | reconstructed |
| 82 | Zambia | Desmond Katongo | 1 | 2 | 3 | 15 | 12 | 10 | Rodri | reconstructed |
| 83 | Uganda | Fred Mwambu | 5 | 2 | 1 | 7 | 12 | 15 | Jude Bellingham | reconstructed |
| 84 | Haiti | Raymond Jean-Louis | 2 | 1 | 8 | 12 | 15 | 3 | Vinícius Júnior | reconstructed |
| 85 | Benin | Hugues Zinsou Zounon | 5 | 1 | 2 | 7 | 15 | 12 | Vinícius Júnior | reconstructed |
| 86 | Luxembourg | Christophe Nadin | 1 | 2 | 3 | 15 | 12 | 10 | Rodri | reconstructed |
| 87 | Armenia | Suren Baghdasaryan | 1 | 2 | – | 15 | 12 | 0 | Rodri | reconstructed |
| 88 | Palestine | Bassam Abu Arra | 3 | 1 | 4 | 10 | 15 | 8 | Vinícius Júnior | reconstructed |
| 89 | Kyrgyzstan | Kuban Atahanov | 1 | 2 | 3 | 15 | 12 | 10 | Rodri | reconstructed |
| 90 | Belarus | Sergey Nikolaev | 1 | 3 | 2 | 15 | 10 | 12 | Rodri | reconstructed |
| 91 | Northern Ireland | Jackie Fullerton | 1 | 4 | 2 | 15 | 8 | 12 | Rodri | reconstructed |
| 92 | Israel | Elad Zeevi | 1 | 3 | 2 | 15 | 10 | 12 | Rodri | reconstructed |
| 93 | China | Luo Ming | 5 | 1 | 3 | 7 | 15 | 10 | Vinícius Júnior | reconstructed |
| 94 | Gabon | Charles Mve | – | – | – | – | – | – | – | no ballot |
| 95 | Slovenia | Andrej Stare | 3 | 2 | 1 | 10 | 12 | 15 | Jude Bellingham | partial |
| 96 | Honduras | Kelvin Coello | 1 | 3 | 2 | 15 | 10 | 12 | Rodri | reconstructed |
| 97 | Trinidad & Tobago | Lasana Liburd | 1 | 3 | 2 | 15 | 10 | 12 | Rodri | reconstructed |
| 98 | Bolivia | Juan Pastén | 2 | 1 | 4 | 12 | 15 | 8 | Vinícius Júnior | reconstructed |
| 99 | Mauritania | Lassana Camara | – | 1 | 2 | 0 | 15 | 12 | Vinícius Júnior | reconstructed |
| 100 | Lebanon | Ibrahim Al-Wazan | 1 | 2 | 7 | 15 | 12 | 4 | Rodri | reconstructed |

</details>

## 2025: how the jury scored the top 3

Winner: **Ousmane Dembélé**. Jury: 100 ballots. First places are published counts. Points by confederation and by juror come from the rebuilt ballots, which add up exactly to the published totals.

| Player | Total points | First places | Avg per ballot | Avg UEFA | Avg CONMEBOL | Avg CONCACAF | Avg CAF | Avg AFC | Avg OFC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Ousmane Dembélé** (winner) | 1380 | 73 | 13.8 | 14.1 | 12.3 | 12.8 | 14.2 | 14.5 | 15.0 |
| Lamine Yamal | 1059 | 11 | 10.6 | 9.9 | 12.8 | 12.7 | 9.9 | 10.0 | 12.0 |
| Vitinha | 703 | 6 | 7.0 | 7.0 | 10.1 | 7.0 | 6.9 | 5.1 | 7.0 |

Ballot sources: 3 verified, 2 partly verified (e.g. only the 1st place is published), 95 rebuilt by the model.

<details><summary>All 100 jurors: points given to Dembélé, Yamal, Vitinha in 2025</summary>

| # | Country | Juror (your roster) | Dembélé pos | Yamal pos | Vitinha pos | Dembélé pts | Yamal pts | Vitinha pts | Their 1st place | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Spain | José Félix Díaz | 3 | 1 | 2 | 10 | 15 | 12 | Lamine Yamal | verified |
| 2 | Argentina | Enrique Wolff | 2 | 1 | 4 | 12 | 15 | 8 | Lamine Yamal | reconstructed |
| 3 | France | Vincent Garcia | 1 | 4 | 6 | 15 | 8 | 5 | Ousmane Dembélé | reconstructed |
| 4 | England | Henry Winter | 1 | 2 | 8 | 15 | 12 | 3 | Ousmane Dembélé | reconstructed |
| 5 | Brazil | Cleber Machado | 1 | 3 | 6 | 15 | 10 | 5 | Ousmane Dembélé | reconstructed |
| 6 | Morocco | Mustapha Badri | 1 | 3 | 4 | 15 | 10 | 8 | Ousmane Dembélé | reconstructed |
| 7 | Portugal | Joaquim Rita | 1 | 4 | 2 | 15 | 8 | 12 | Ousmane Dembélé | reconstructed |
| 8 | Belgium | Christophe Franken | 1 | 6 | 5 | 15 | 5 | 7 | Ousmane Dembélé | reconstructed |
| 9 | Netherlands | Frans van den Nieuwenhof | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 10 | Mexico | Salvador Aguilera | 2 | 1 | 3 | 12 | 15 | 10 | Lamine Yamal | reconstructed |
| 11 | Colombia | Paché Andrade | 2 | 1 | 3 | 12 | 15 | 10 | Lamine Yamal | reconstructed |
| 12 | Germany | Karlheinz Wild | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 13 | Croatia | Zdravko Reić | 1 | 2 | 4 | 15 | 12 | 8 | Ousmane Dembélé | reconstructed |
| 14 | Switzerland | Christophe Cerf | 1 | 2 | 5 | 15 | 12 | 7 | Ousmane Dembélé | reconstructed |
| 15 | Italy | Paolo Condò | 1 | 5 | 4 | 15 | 7 | 8 | Ousmane Dembélé | reconstructed |
| 16 | USA | Paul Kennedy | 1 | 2 | 5 | 15 | 12 | 7 | Ousmane Dembélé | reconstructed |
| 17 | Japan | Shuichi Tamura | 1 | 7 | – | 15 | 4 | 0 | Ousmane Dembélé | reconstructed |
| 18 | Senegal | Salif Diallo | 1 | 3 | – | 15 | 10 | 0 | Ousmane Dembélé | reconstructed |
| 19 | Norway | Lars Tjærnås | 3 | 2 | 4 | 10 | 12 | 8 | Mohamed Salah | reconstructed |
| 20 | Uruguay | Ricardo Piñeyrúa | 2 | 4 | 1 | 12 | 8 | 15 | Vitinha | reconstructed |
| 21 | Denmark | Troels Bager Thøgersen | 1 | 2 | 5 | 15 | 12 | 7 | Ousmane Dembélé | reconstructed |
| 22 | Iran | Siamak Rahmani | 1 | 3 | 2 | 15 | 10 | 12 | Ousmane Dembélé | reconstructed |
| 23 | Austria | Walter Kowatsch-Schwarz | 1 | 4 | 3 | 15 | 8 | 10 | Ousmane Dembélé | reconstructed |
| 24 | Egypt | Inas Mazhar | 1 | 4 | – | 15 | 8 | 0 | Ousmane Dembélé | reconstructed |
| 25 | Ecuador | Tito Rosales Cox | 2 | 1 | 3 | 12 | 15 | 10 | Lamine Yamal | reconstructed |
| 26 | Nigeria | Samm Audu | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 27 | Türkiye | Fatih Doğan | 1 | 5 | 7 | 15 | 7 | 4 | Ousmane Dembélé | reconstructed |
| 28 | Australia | David Davutovic | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 29 | Algeria | Yazid Ouahib | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 30 | Canada | John Molinaro | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 31 | Ivory Coast | Adam Khalil | 1 | 3 | 2 | 15 | 10 | 12 | Ousmane Dembélé | reconstructed |
| 32 | South Korea | Sungmo Lee | 2 | 1 | – | 12 | 15 | 0 | Lamine Yamal | reconstructed |
| 33 | Ukraine | Igor Linnyk | 1 | 2 | 5 | 15 | 12 | 7 | Ousmane Dembélé | reconstructed |
| 34 | Paraguay | Gabriel Cazenave | 2 | 1 | 3 | 12 | 15 | 10 | Lamine Yamal | reconstructed |
| 35 | Russia | Konstantin Klechev | 1 | 2 | 9 | 15 | 12 | 2 | Ousmane Dembélé | reconstructed |
| 36 | Poland | Maciej Iwański | 3 | 4 | 5 | 10 | 8 | 7 | Kylian Mbappé | reconstructed |
| 37 | Sweden | Olof Lundh | 1 | 5 | 7 | 15 | 7 | 4 | Ousmane Dembélé | reconstructed |
| 38 | Wales | Paul Abbandonato | 1 | 2 | – | 15 | 12 | 0 | Ousmane Dembélé | reconstructed |
| 39 | Hungary | György Szöllősi | 2 | 3 | 1 | 12 | 10 | 15 | Vitinha | reconstructed |
| 40 | Serbia | Vladimir Novak | 3 | 2 | 1 | 10 | 12 | 15 | Vitinha | reconstructed |
| 41 | DR Congo | Jenovic Mbowa | 2 | 3 | 5 | 12 | 10 | 7 | Achraf Hakimi | reconstructed |
| 42 | Scotland | John Greechan | 3 | 2 | 5 | 10 | 12 | 7 | Scott McTominay | partial |
| 43 | Cameroon | Emmanuel Gustave Samnick | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 44 | Panama | Campo Elías Estrada | 2 | 1 | 5 | 12 | 15 | 7 | Lamine Yamal | reconstructed |
| 45 | Slovakia | Marcel Merčiak | 1 | 2 | – | 15 | 12 | 0 | Ousmane Dembélé | reconstructed |
| 46 | Greece | Manos Staramopoulos | 1 | 3 | – | 15 | 10 | 0 | Ousmane Dembélé | reconstructed |
| 47 | Venezuela | Francisco Blavia | 3 | 1 | 4 | 10 | 15 | 8 | Lamine Yamal | reconstructed |
| 48 | Czechia | Stanislav Hrabě | 1 | 2 | 6 | 15 | 12 | 5 | Ousmane Dembélé | reconstructed |
| 49 | Chile | Danilo Díaz | 3 | 2 | 1 | 10 | 12 | 15 | Vitinha | reconstructed |
| 50 | Peru | Roberto Castro | 1 | 2 | 5 | 15 | 12 | 7 | Ousmane Dembélé | reconstructed |
| 51 | Costa Rica | Rodrigo Calvo | 2 | 1 | 4 | 12 | 15 | 8 | Lamine Yamal | reconstructed |
| 52 | Romania | Emanuel Roșu | 1 | 2 | 5 | 15 | 12 | 7 | Ousmane Dembélé | reconstructed |
| 53 | Qatar | Majed Al-Khelaifi | 1 | 2 | 7 | 15 | 12 | 4 | Ousmane Dembélé | reconstructed |
| 54 | Tunisia | Tarek Gharbi | 1 | 6 | 5 | 15 | 5 | 7 | Ousmane Dembélé | reconstructed |
| 55 | Finland | Juha Kanerva | 1 | 2 | 6 | 15 | 12 | 5 | Ousmane Dembélé | reconstructed |
| 56 | Republic of Ireland | Philip Quinn | 1 | 2 | 4 | 15 | 12 | 8 | Ousmane Dembélé | reconstructed |
| 57 | Bosnia & Herzegovina | Bakir Tiro | 1 | 2 | 5 | 15 | 12 | 7 | Ousmane Dembélé | reconstructed |
| 58 | Ghana | Michael Oti Adjei | 1 | 2 | 6 | 15 | 12 | 5 | Ousmane Dembélé | verified |
| 59 | Jamaica | Sean Williams | 3 | 2 | 4 | 10 | 12 | 8 | Mohamed Salah | reconstructed |
| 60 | Iceland | Víðir Sigurðsson | 3 | 2 | 6 | 10 | 12 | 5 | Achraf Hakimi | reconstructed |
| 61 | Albania | Besnik Dizdari | 1 | 7 | 3 | 15 | 4 | 10 | Ousmane Dembélé | reconstructed |
| 62 | North Macedonia | Miko Zahariev | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 63 | South Africa | Mark Gleeson | 2 | 3 | 4 | 12 | 10 | 8 | Mohamed Salah | verified |
| 64 | Iraq | Ali Nouri | 1 | 5 | – | 15 | 7 | 0 | Ousmane Dembélé | reconstructed |
| 65 | UAE | Mohammed Al-Joker | 1 | 3 | 5 | 15 | 10 | 7 | Ousmane Dembélé | reconstructed |
| 66 | Cabo Verde | Pedro Clovis | 1 | 4 | 10 | 15 | 8 | 1 | Ousmane Dembélé | reconstructed |
| 67 | Montenegro | Danilo Mitrović | 1 | 4 | 7 | 15 | 8 | 4 | Ousmane Dembélé | reconstructed |
| 68 | Honduras | Gerson Gómez | 6 | 2 | – | 5 | 12 | 0 | Achraf Hakimi | reconstructed |
| 69 | Georgia | Otar Giorgadze | 3 | 5 | 4 | 10 | 7 | 8 | Khvicha Kvaratskhelia | partial |
| 70 | Bolivia | Carlos Enrique Rivera | 1 | 2 | 4 | 15 | 12 | 8 | Ousmane Dembélé | reconstructed |
| 71 | Guinea | Amadou Diouldé Diallo | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 72 | Mali | Souleymane Bobo Tounkara | 1 | 2 | 5 | 15 | 12 | 7 | Ousmane Dembélé | reconstructed |
| 73 | Gabon | James Golden Pincent | 1 | 2 | 6 | 15 | 12 | 5 | Ousmane Dembélé | reconstructed |
| 74 | New Zealand | Michael Burgess | 1 | 2 | 5 | 15 | 12 | 7 | Ousmane Dembélé | reconstructed |
| 75 | Uzbekistan | Grigoriy Rtveladze | 1 | 2 | 6 | 15 | 12 | 5 | Ousmane Dembélé | reconstructed |
| 76 | Jordan | Tayseer Al-Amiri | 1 | 2 | – | 15 | 12 | 0 | Ousmane Dembélé | reconstructed |
| 77 | Oman | Jaber Al-Ajmi | 1 | 4 | 3 | 15 | 8 | 10 | Ousmane Dembélé | reconstructed |
| 78 | El Salvador | Claudio Martínez | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 79 | Bahrain | Abdullah Ashoor | 1 | 3 | 8 | 15 | 10 | 3 | Ousmane Dembélé | reconstructed |
| 80 | Curaçao | Kenley Basilio | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 81 | Syria | Lutfi Al-Awan | 1 | 3 | 8 | 15 | 10 | 3 | Ousmane Dembélé | reconstructed |
| 82 | Zambia | Desmond Katongo | 1 | 3 | – | 15 | 10 | 0 | Ousmane Dembélé | reconstructed |
| 83 | Uganda | Fred Mwambu | 1 | 4 | 6 | 15 | 8 | 5 | Ousmane Dembélé | reconstructed |
| 84 | Haiti | Raymond Jean-Louis | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 85 | Benin | Hugues Zinsou Zounon | 1 | 3 | 4 | 15 | 10 | 8 | Ousmane Dembélé | reconstructed |
| 86 | Luxembourg | Christophe Nadin | 1 | – | 9 | 15 | 0 | 2 | Ousmane Dembélé | reconstructed |
| 87 | Armenia | Suren Baghdasaryan | 1 | 6 | 5 | 15 | 5 | 7 | Ousmane Dembélé | reconstructed |
| 88 | Palestine | Bassam Abu Arra | 3 | 7 | 2 | 10 | 4 | 12 | Mohamed Salah | reconstructed |
| 89 | Kyrgyzstan | Kuban Atahanov | 1 | 2 | – | 15 | 12 | 0 | Ousmane Dembélé | reconstructed |
| 90 | Belarus | Sergey Nikolaev | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 91 | Northern Ireland | Jackie Fullerton | 1 | 3 | 4 | 15 | 10 | 8 | Ousmane Dembélé | reconstructed |
| 92 | Israel | Elad Zeevi | 1 | 2 | 5 | 15 | 12 | 7 | Ousmane Dembélé | reconstructed |
| 93 | China | Luo Ming | 1 | 2 | 4 | 15 | 12 | 8 | Ousmane Dembélé | reconstructed |
| 94 | Gabon | Charles Mve | 1 | 2 | 3 | 15 | 12 | 10 | Ousmane Dembélé | reconstructed |
| 95 | Slovenia | Andrej Stare | 1 | 6 | 3 | 15 | 5 | 10 | Ousmane Dembélé | reconstructed |
| 96 | Honduras | Kelvin Coello | 2 | 1 | 7 | 12 | 15 | 4 | Lamine Yamal | reconstructed |
| 97 | Trinidad & Tobago | Lasana Liburd | 1 | 4 | – | 15 | 8 | 0 | Ousmane Dembélé | reconstructed |
| 98 | Bolivia | Juan Pastén | 3 | 2 | 1 | 10 | 12 | 15 | Vitinha | reconstructed |
| 99 | Mauritania | Lassana Camara | 7 | 8 | 1 | 4 | 3 | 15 | Vitinha | reconstructed |
| 100 | Lebanon | Ibrahim Al-Wazan | 1 | 3 | 4 | 15 | 10 | 8 | Ousmane Dembélé | reconstructed |

</details>

## Criteria scores fed to the model

P = Individual Performance, Decisiveness & Impressive Character. T = Team Success (trophy value × how essential the player was, capped at 100). F = Class & Fair Play. All on 0–100.

| Year | Player | P | T | F | Basis |
|---|---|---:|---:|---:|---|
| 2024 | Rodri | 87 | 66.6 | 92 | Midfield engine of City's long unbeaten run; Euro 2024 Player of the Tournament; huge tactical influence, modest goal output for a winner. Silverware: Premier League ×0.9; Euro 2024 ×1.0; UEFA Super Cup ×0.85; Club World Cup 2023 ×1.0; UCL quarter-final ×0.85. No notable disciplinary issues. |
| 2024 | Vinícius Júnior | 92 | 61.1 | 72 | 24 goals, 11 assists; scored in the UCL final; UCL Player of the Season. Silverware: Champions League ×1.0; LaLiga ×0.85; Supercopa (hat-trick in final) ×1.0; Copa América quarter-final ×0.7. Several dissent bookings and on-pitch flashpoints across the season. |
| 2024 | Jude Bellingham | 87 | 67.0 | 78 | 23 goals, 13 assists in debut Madrid season; strong autumn, faded in spring; Euro bicycle-kick rescue vs Slovakia. Silverware: Champions League ×0.85; LaLiga (Madrid's top league scorer) ×1.0; Supercopa ×0.85; Euro 2024 runner-up ×0.85. Red card after the final whistle at Valencia (March 2024), two-match ban. |
| 2025 | Ousmane Dembélé | 94 | 74.6 | 90 | About 35 goals and 16 assists; decisive in PSG's Champions League knockout run. Silverware: Champions League ×1.0; Ligue 1 ×1.0; Coupe de France ×0.85; Trophée des Champions (scored winner) ×1.0; Club World Cup runner-up ×0.85; Nations League semi-final ×0.7. No notable disciplinary issues. |
| 2025 | Lamine Yamal | 93 | 42.9 | 90 | About 18 goals and 25 assists at 17; standout in Barcelona's UCL semi-final run. Silverware: LaLiga ×1.0; Copa del Rey ×0.85; Supercopa ×0.85; UCL semi-final ×1.0; Nations League runner-up ×0.85. No notable disciplinary issues. |
| 2025 | Vitinha | 78 | 70.5 | 92 | Elite control midfielder for PSG and Portugal; low goal/assist output. Silverware: Champions League ×0.85; Ligue 1 ×0.85; Coupe de France ×0.85; Trophée des Champions ×0.85; Nations League ×0.85; Club World Cup runner-up ×0.85. No notable disciplinary issues. |
| 2026 | Harry Kane | 96 | 51.0 | 94 | 61 goals in 51 Bayern games (36 Bundesliga, 14 UCL, 10 DFB-Pokal) and 73 in 65 including England; European Golden Shoe; Bundesliga top scorer for a 3rd straight season; DFB-Pokal final hat-trick; 6 goals and 1 assist at the World Cup. Silverware: Bundesliga ×1.0; DFB-Pokal (hat-trick in final) ×1.0; DFL-Supercup ×1.0; UCL semi-final (lost to PSG) ×1.0; World Cup 3rd place (benched for the play-off) ×0.9. England captain; no red cards found in the window. |
| 2026 | Lamine Yamal | 86 | 66.2 | 92 | 24 goals; LaLiga 16 goals + 11 assists (league's top assister, LaLiga Player of the Season); hamstring injury cost the final 6 club games; World Cup: 8 games, 1 goal, 0 assists, most dribbles completed. Silverware: World Cup winner ×0.85; LaLiga (Player of the Season, missed final 6 games) ×0.95; Supercopa ×1.0; UCL quarter-final ×1.0. No red cards in the window. |
| 2026 | Kylian Mbappé | 92 | 11.0 | 92 | 42 goals in 44 Real Madrid games; Pichichi (25) and UCL top scorer (15); World Cup Golden Boot (10 goals, 4 assists) and Bronze Ball. About 52 goals in the window, but knee problems and no knockout-stage wins when it mattered. Silverware: UCL quarter-final (lost to Bayern) ×1.0; World Cup 4th place (Golden Boot) ×1.0. No red cards found in the window. |
| 2026 | Lionel Messi | 90 | 28.0 | 92 | World Cup: 8 goals, 4 assists, Silver Ball and Silver Boot at 39, Argentina to the final; MLS Cup MVP with a record 15 playoff goal contributions; about 32 goals and 25 assists for Inter Miami in the window (MLS level, not a top-5 league). Silverware: MLS Cup (MVP of the final) ×1.0; World Cup runner-up (Silver Ball) ×1.0. No notable disciplinary issues identified. |
| 2026 | Khvicha Kvaratskhelia | 86 | 66.9 | 92 | UCL Player of the Season: 10 goals, 6 assists, scored or assisted in 7 straight knockout games (a record); 19 goals and 11 assists in all competitions; Georgia did not qualify for the World Cup. Silverware: Champions League (Player of the Season) ×1.0; Ligue 1 ×0.85; UEFA Super Cup ×0.85; Intercontinental Cup ×0.85; Trophée des Champions ×0.85. No notable disciplinary issues identified. |
| 2026 | Rodri | 84 | 55.5 | 92 | World Cup Golden Ball as Spain's captain (six clean-sheet wins, including the final); modest club season back from injury (about 33 games, a handful of goals and assists). Silverware: World Cup winner (Golden Ball) ×1.0; FA Cup ×0.7; League Cup ×0.7; UCL last 16 ×0.7. No notable disciplinary issues identified. |
| 2026 | Bruno Fernandes | 84 | 2.0 | 92 | Premier League Player of the Season; 21 league assists (a Premier League record) plus 8 goals for a Manchester United side without a trophy. Silverware: World Cup last 16 ×1.0. No notable disciplinary issues identified. |
| 2026 | Declan Rice | 78 | 40.2 | 92 | Midfield engine of Arsenal's first league title in 22 years (4 goals, 5 assists in the league); captained England to 3rd and scored after 2 minutes in the bronze match. Silverware: Premier League ×0.9; UCL runner-up ×0.85; World Cup 3rd place ×0.85. No notable disciplinary issues identified. |
| 2026 | Erling Haaland | 89 | 18.1 | 92 | 38 goals and 8 assists in 52 City games, Premier League Golden Boot (27); 7 World Cup goals in his first 4 games including both goals that knocked out Brazil. Silverware: FA Cup ×0.85; League Cup ×0.85; UCL last 16 ×1.0; World Cup quarter-final ×1.0. No notable disciplinary issues identified. |
| 2026 | Jude Bellingham | 82 | 13.4 | 92 | Weak club season (8 goals, 5 assists in 40 games) but 7 World Cup goals, the most by an England player at any major tournament. Silverware: UCL quarter-final ×0.85; World Cup 3rd place (England's top scorer) ×1.0. No notable disciplinary issues identified. |
| 2026 | Lautaro Martínez | 82 | 43.3 | 92 | Serie A top scorer (17) and Inter's striker of the season; 3 goals and 1 assist at the World Cup, including the stoppage-time semi-final winner against England; did not play in the final. Silverware: Serie A (top scorer) ×1.0; Coppa Italia ×0.85; UCL knockout play-off ×1.0; World Cup runner-up ×0.75. No notable disciplinary issues identified. |
| 2026 | Luis Díaz | 85 | 37.7 | 92 | 24 goals and 17 assists in his first Bayern season (15 goals + 13 assists in the Bundesliga); Colombia out on penalties in the last 16. Silverware: Bundesliga ×0.85; DFB-Pokal ×0.85; DFL-Supercup ×0.85; UCL semi-final ×0.85; World Cup last 16 ×1.0. No notable disciplinary issues identified. |
| 2026 | Michael Olise | 86 | 43.9 | 92 | Bundesliga Player of the Season and assist leader (15 goals, 19 assists); more than 20 goals and 25 assists in all competitions, Europe's top provider. Silverware: Bundesliga (Player of the Season) ×1.0; DFB-Pokal ×0.85; DFL-Supercup ×0.85; UCL semi-final ×0.85; World Cup 4th place (individual output not verified) ×0.7. No notable disciplinary issues identified. |
| 2026 | Nuno Mendes | 76 | 62.9 | 92 | Elite left-back: 4 goals and 5 assists in 20 Ligue 1 games, 2 goals and 2 assists in the Champions League; scored in the Intercontinental Cup shootout. Silverware: Champions League ×0.85; Ligue 1 ×0.85; UEFA Super Cup ×0.85; Intercontinental Cup ×0.85; Trophée des Champions ×0.85; World Cup last 16 ×0.85. No notable disciplinary issues identified. |
| 2026 | Ousmane Dembélé | 87 | 68.2 | 92 | 26 goals and 14 assists in 50 PSG games (8 goals in the UCL) after an injury-hit start; 6 goals and 2 assists at the World Cup, including a first-half hat-trick against Norway. Silverware: Champions League ×0.85; Ligue 1 ×0.85; UEFA Super Cup ×0.85; Intercontinental Cup ×0.85; Trophée des Champions ×0.85; World Cup 4th place ×1.0. No notable disciplinary issues identified. |
| 2026 | Vinícius Júnior | 83 | 5.4 | 86 | 22 goals and 10 assists in 53 Madrid games; scored in all three World Cup group games (4 goals, 1 assist) before Brazil fell to Norway in the last 16. Silverware: UCL quarter-final ×0.85; World Cup last 16 ×1.0. Public outburst after being substituted in the October 2025 Clásico (later apologised). |
| 2026 | Vitinha | 79 | 68.6 | 92 | Player of the Match in the Champions League final (141 of 150 passes completed); 1 goal and 7 assists in Ligue 1; Portugal out in the last 16. Silverware: Champions League (final Player of the Match) ×1.0; Ligue 1 ×0.85; UEFA Super Cup ×0.85; Intercontinental Cup ×0.85; Trophée des Champions ×0.85; World Cup last 16 ×0.85. No notable disciplinary issues identified. |

## Backtest: does the model reproduce 2024 and 2025?

Fitted on both years: wP = 0.7, wT = 0.2, wF = 0.1, juror noise σ = 5.0, field gap = 6.0 (grid search; wP ≥ wT enforced).

| Year | Player | Actual pts | Model pts | Actual 1st places | Model 1st places |
|---|---|---:|---:|---:|---:|
| 2024 | Rodri | 1170 | 1136 | 49 | 32.4 |
| 2024 | Vinícius Júnior | 1129 | 1147 | 35 | 34.0 |
| 2024 | Jude Bellingham | 917 | 1052 | 5 | 23.0 |
| 2025 | Ousmane Dembélé | 1380 | 1392 | 73 | 74.3 |
| 2025 | Lamine Yamal | 1059 | 997 | 11 | 13.3 |
| 2025 | Vitinha | 703 | 663 | 6 | 2.2 |

The model picks Dembélé in 100% of simulated 2025 juries. It picks Rodri in 40% of simulated 2024 juries, and in the rest Vinícius edges it, which matches how close 2024 really was (41 points). It overrates Bellingham's 2024 first-place pull.

## 2026 prediction: all 17 contenders

**Predicted winner: Harry Kane**, then Ousmane Dembélé and Khvicha Kvaratskhelia.

| # | Player | P | T | F | Projected points | 90% range | Expected 1st places | Predicted-ballot points | Win probability | Bookmakers, 29 Sep |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Harry Kane | 96 | 51 | 94 | **1114** | 1048–1177 | 38.7 | 1438 | 80% | 5/4 (~44%) |
| 2 | Ousmane Dembélé | 87 | 68 | 92 | **862** | 790–935 | 17.7 | 1111 | 11% | – |
| 3 | Khvicha Kvaratskhelia | 86 | 67 | 92 | **791** | 718–866 | 14.5 | 986 | 5% | – |
| 4 | Lamine Yamal | 86 | 66 | 92 | **761** | 688–833 | 13.0 | 928 | 4% | 2/1 (~33%) |
| 5 | Rodri | 84 | 56 | 92 | **464** | 396–533 | 3.6 | 561 | 0% | – |
| 6 | Michael Olise | 86 | 44 | 92 | **389** | 324–454 | 2.6 | 423 | 0% | – |
| 7 | Lionel Messi | 90 | 28 | 92 | **378** | 315–445 | 2.3 | 403 | 0% | – |
| 8 | Vitinha | 79 | 69 | 92 | **376** | 314–440 | 2.4 | 385 | 0% | – |
| 9 | Luis Díaz | 85 | 38 | 92 | **259** | 204–317 | 1.1 | 119 | 0% | – |
| 10 | Kylian Mbappé | 92 | 11 | 92 | **257** | 203–314 | 1.1 | 126 | 0% | 14/1 (~7%) |
| 11 | Erling Haaland | 89 | 18 | 92 | **227** | 176–281 | 0.9 | 103 | 0% | – |
| 12 | Lautaro Martínez | 82 | 43 | 92 | **205** | 157–256 | 0.8 | 56 | 0% | – |
| 13 | Nuno Mendes | 76 | 63 | 92 | **183** | 137–231 | 0.6 | 40 | 0% | – |
| 14 | Declan Rice | 78 | 40 | 92 | **85** | 53–120 | 0.2 | 14 | 0% | – |
| 15 | Jude Bellingham | 82 | 13 | 92 | **37** | 17–59 | 0.0 | 3 | 0% | – |
| 16 | Bruno Fernandes | 84 | 2 | 92 | **22** | 7–40 | 0.0 | 0 | 0% | – |
| 17 | Vinícius Júnior | 83 | 5 | 86 | **21** | 7–39 | 0.0 | 4 | 0% | – |

- *Projected points* average 5,000 simulated juries. *Predicted-ballot points* score every juror's single most likely ballot, which exaggerates the leader's margin. *Win probability* also varies the criteria weights and every P/T score, not just juror-to-juror noise.
- The other 13 shortlisted players you didn't list are modelled as a generic remainder. They are calibrated to take about 4% of all points (271 here), the share places 18–30 took in 2025. They also take about 0.4 first places.

### Why the model lands here

- Fitted weights (backtest on 2024–25): Individual Performance **0.70**, Team Success **0.20**, Fair Play **0.10**.
- **Kane** has the highest individual score (P 96) by a distance. He scored 73 goals, won the Golden Shoe and the German double, and reached a Champions League semi-final and a World Cup semi-final.
- **Dembélé, Kvaratskhelia and Yamal are a three-way race for 2nd**, spread over about 101 points. The PSG pair have five trophies each (including the Champions League) on top of strong individual seasons. Yamal has the World Cup, but he scored once there and missed the end of the club season.
- **Mbappé drops to #10.** His individual score (P 92) is #2 of 17. He won three scoring titles and the World Cup Bronze Ball. But with no trophy (T 11), 16 named rivals with silverware push him down most ballots. The bookmakers rate him far higher (3rd favourite).
- **Rodri** (World Cup Golden Ball) lands #5 and **Messi** (Silver Ball, MLS Cup) #7. Outside the top four, Rodri takes the most first places (about 4).

### Who leads at each weighting

Leader as the weight on Individual Performance changes (Team Success = 0.90 − wP): wP 0.45–0.58: **Ousmane Dembélé**; wP 0.59–0.75: **Harry Kane**.

| wP | wT | 1st | 2nd | 3rd |
|---:|---:|---|---|---|
| 0.45 | 0.45 | Ousmane Dembélé (1067) | Khvicha Kvaratskhelia (1006) | Lamine Yamal (964) |
| 0.50 | 0.40 | Ousmane Dembélé (1045) | Khvicha Kvaratskhelia (984) | Lamine Yamal (943) |
| 0.55 | 0.35 | Ousmane Dembélé (1017) | Khvicha Kvaratskhelia (956) | Harry Kane (955) |
| 0.60 | 0.30 | Harry Kane (1020) | Ousmane Dembélé (980) | Khvicha Kvaratskhelia (917) |
| 0.65 | 0.25 | Harry Kane (1075) | Ousmane Dembélé (929) | Khvicha Kvaratskhelia (864) |
| 0.70 | 0.20 | Harry Kane (1120) | Ousmane Dembélé (860) | Khvicha Kvaratskhelia (792) |
| 0.75 | 0.15 | Harry Kane (1147) | Ousmane Dembélé (764) | Khvicha Kvaratskhelia (695) |

### Sensitivity

| Scenario | 1st | 2nd | 3rd |
|---|---|---|---|
| Baseline (fitted weights) | Harry Kane (1114) | Ousmane Dembélé (862) | Khvicha Kvaratskhelia (791) |
| Silverware-heavy jury (wP = wT = 0.45) | Ousmane Dembélé (1067) | Khvicha Kvaratskhelia (1006) | Lamine Yamal (967) |
| Output-heavy jury (wP + 0.05) | Harry Kane (1143) | Ousmane Dembélé (765) | Khvicha Kvaratskhelia (696) |
| Yamal rated Spain's World Cup standout (essential 1.0) | Harry Kane (1101) | Lamine Yamal (862) | Ousmane Dembélé (848) |
| No juror history (merit + blocs only) | Harry Kane (1122) | Ousmane Dembélé (873) | Khvicha Kvaratskhelia (808) |

### Projected points per ballot by confederation (top 6)

| Confederation | Jurors | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | Olise |
|---|---:|---:|---:|---:|---:|---:|---:|
| UEFA | 40 | 11.1 | 8.6 | 8.6 | 7.2 | 4.8 | 4.0 |
| CONMEBOL | 11 | 10.7 | 7.3 | 6.7 | 9.4 | 4.5 | 3.3 |
| CONCACAF | 12 | 10.9 | 7.9 | 7.0 | 9.2 | 4.9 | 3.6 |
| CAF | 20 | 11.4 | 9.6 | 7.7 | 6.8 | 4.2 | 4.2 |
| AFC | 16 | 11.3 | 8.7 | 8.1 | 7.4 | 4.6 | 3.9 |
| OFC | 1 | 12.8 | 8.9 | 7.1 | 7.0 | 5.7 | 3.4 |

<details><summary>All 100 jurors: predicted 2026 ballot</summary>

*1st–5th* is each juror's single most likely ballot (positions 6–10 are in `output/prediction_2026_ballots.csv`). *P(1st)* is the chance that juror puts the player 1st, across 5,000 simulated juries. Expected points for every juror and all 17 players are in `output/prediction_2026_expected_points.csv`.

| # | Country | Juror | 1st (15) | 2nd (12) | 3rd (10) | 4th (8) | 5th (7) | P(1st) Kane | P(1st) Dembélé | P(1st) Kvaratskhelia | P(1st) Yamal |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|
| 1 | Spain | José Félix Díaz | Yamal | Kane | Rodri | Kvaratskhelia | Dembélé | 18% | 3% | 4% | 63% |
| 2 | Argentina | Enrique Wolff | Kane | Yamal | Messi | Lautaro | Dembélé | 35% | 6% | 6% | 21% |
| 3 | France | Vincent Garcia | Dembélé | Kane | Mbappé | Olise | Kvaratskhelia | 18% | 54% | 5% | 4% |
| 4 | England | Henry Winter | Kane | Dembélé | Yamal | Kvaratskhelia | Rodri | 89% | 4% | 2% | 2% |
| 5 | Brazil | Cleber Machado | Kane | Dembélé | Kvaratskhelia | Yamal | Messi | 38% | 20% | 10% | 10% |
| 6 | Morocco | Mustapha Badri | Dembélé | Kane | Kvaratskhelia | Yamal | Rodri | 27% | 36% | 13% | 8% |
| 7 | Portugal | Joaquim Rita | Kane | Vitinha | Dembélé | N. Mendes | Kvaratskhelia | 32% | 14% | 6% | 4% |
| 8 | Belgium | Christophe Franken | Kane | Dembélé | Kvaratskhelia | Yamal | Olise | 36% | 31% | 12% | 8% |
| 9 | Netherlands | Frans van den Nieuwenhof | Kane | Dembélé | Yamal | Kvaratskhelia | Rodri | 42% | 20% | 10% | 13% |
| 10 | Mexico | Salvador Aguilera | Yamal | Kane | Dembélé | Kvaratskhelia | Rodri | 28% | 11% | 9% | 36% |
| 11 | Colombia | Paché Andrade | Kane | Yamal | Díaz | Dembélé | Kvaratskhelia | 31% | 10% | 8% | 22% |
| 12 | Germany | Karlheinz Wild | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 61% | 13% | 8% | 7% |
| 13 | Croatia | Zdravko Reić | Kane | Kvaratskhelia | Dembélé | Yamal | Rodri | 31% | 17% | 30% | 11% |
| 14 | Switzerland | Christophe Cerf | Kane | Kvaratskhelia | Dembélé | Yamal | Olise | 29% | 26% | 25% | 8% |
| 15 | Italy | Paolo Condò | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 42% | 22% | 11% | 8% |
| 16 | USA | Paul Kennedy | Kane | Dembélé | Yamal | Kvaratskhelia | Rodri | 48% | 17% | 9% | 13% |
| 17 | Japan | Shuichi Tamura | Kvaratskhelia | Kane | Dembélé | Yamal | Rodri | 31% | 17% | 32% | 5% |
| 18 | Senegal | Salif Diallo | Kane | Dembélé | Kvaratskhelia | Yamal | Olise | 35% | 29% | 12% | 9% |
| 19 | Norway | Lars Tjærnås | Kane | Kvaratskhelia | Yamal | Haaland | Dembélé | 42% | 8% | 15% | 12% |
| 20 | Uruguay | Ricardo Piñeyrúa | Kane | Yamal | Dembélé | Kvaratskhelia | Rodri | 30% | 12% | 11% | 26% |
| 21 | Denmark | Troels Bager Thøgersen | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 37% | 19% | 16% | 13% |
| 22 | Iran | Siamak Rahmani | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 35% | 21% | 17% | 10% |
| 23 | Austria | Walter Kowatsch-Schwarz | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 42% | 20% | 12% | 10% |
| 24 | Egypt | Inas Mazhar | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 39% | 23% | 12% | 9% |
| 25 | Ecuador | Tito Rosales Cox | Kane | Yamal | Dembélé | Kvaratskhelia | Messi | 36% | 11% | 8% | 31% |
| 26 | Nigeria | Samm Audu | Kane | Dembélé | Yamal | Kvaratskhelia | Rodri | 59% | 15% | 7% | 8% |
| 27 | Türkiye | Fatih Doğan | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 54% | 17% | 14% | 6% |
| 28 | Australia | David Davutovic | Kane | Yamal | Dembélé | Kvaratskhelia | Messi | 74% | 8% | 4% | 9% |
| 29 | Algeria | Yazid Ouahib | Dembélé | Kvaratskhelia | Kane | Yamal | Vitinha | 25% | 31% | 24% | 7% |
| 30 | Canada | John Molinaro | Kane | Dembélé | Yamal | Kvaratskhelia | Rodri | 48% | 16% | 9% | 13% |
| 31 | Ivory Coast | Adam Khalil | Kane | Dembélé | Kvaratskhelia | Yamal | Vitinha | 37% | 31% | 10% | 7% |
| 32 | South Korea | Sungmo Lee | Kane | Kvaratskhelia | Yamal | Dembélé | Rodri | 39% | 11% | 22% | 14% |
| 33 | Ukraine | Igor Linnyk | Kane | Dembélé | Kvaratskhelia | Olise | Yamal | 32% | 19% | 17% | 10% |
| 34 | Paraguay | Gabriel Cazenave | Kane | Yamal | Dembélé | Kvaratskhelia | Rodri | 32% | 12% | 10% | 25% |
| 35 | Russia | Konstantin Klechev | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 48% | 16% | 14% | 10% |
| 36 | Poland | Maciej Iwański | Kane | Kvaratskhelia | Dembélé | Yamal | Rodri | 37% | 12% | 20% | 12% |
| 37 | Sweden | Olof Lundh | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 47% | 17% | 15% | 9% |
| 38 | Wales | Paul Abbandonato | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 45% | 18% | 10% | 9% |
| 39 | Hungary | György Szöllősi | Kane | Kvaratskhelia | Dembélé | Yamal | Vitinha | 32% | 15% | 19% | 14% |
| 40 | Serbia | Vladimir Novak | Kane | Kvaratskhelia | Yamal | Dembélé | Vitinha | 33% | 11% | 27% | 11% |
| 41 | DR Congo | Jenovic Mbowa | Kane | Dembélé | Kvaratskhelia | Yamal | Olise | 37% | 23% | 15% | 9% |
| 42 | Scotland | John Greechan | Kane | Yamal | Kvaratskhelia | Dembélé | Rice | 46% | 8% | 10% | 12% |
| 43 | Cameroon | Emmanuel Gustave Samnick | Kane | Dembélé | Kvaratskhelia | Yamal | Olise | 52% | 22% | 9% | 6% |
| 44 | Panama | Campo Elías Estrada | Kane | Yamal | Dembélé | Kvaratskhelia | Rodri | 32% | 10% | 9% | 29% |
| 45 | Slovakia | Marcel Merčiak | Kane | Kvaratskhelia | Dembélé | Yamal | Rodri | 36% | 13% | 33% | 8% |
| 46 | Greece | Manos Staramopoulos | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 33% | 19% | 18% | 15% |
| 47 | Venezuela | Francisco Blavia | Kane | Yamal | Kvaratskhelia | Dembélé | Rodri | 34% | 9% | 9% | 28% |
| 48 | Czechia | Stanislav Hrabě | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 43% | 17% | 16% | 12% |
| 49 | Chile | Danilo Díaz | Kane | Yamal | Kvaratskhelia | Dembélé | Rodri | 37% | 8% | 9% | 28% |
| 50 | Peru | Roberto Castro | Yamal | Kane | Dembélé | Kvaratskhelia | Rodri | 29% | 16% | 9% | 29% |
| 51 | Costa Rica | Rodrigo Calvo | Yamal | Kane | Dembélé | Kvaratskhelia | Messi | 31% | 9% | 8% | 36% |
| 52 | Romania | Emanuel Roșu | Kane | Kvaratskhelia | Dembélé | Yamal | Haaland | 28% | 18% | 28% | 12% |
| 53 | Qatar | Majed Al-Khelaifi | Kane | Dembélé | Yamal | Kvaratskhelia | Rodri | 42% | 20% | 11% | 12% |
| 54 | Tunisia | Tarek Gharbi | Dembélé | Kane | Kvaratskhelia | Yamal | Olise | 29% | 34% | 13% | 6% |
| 55 | Finland | Juha Kanerva | Kvaratskhelia | Kane | Dembélé | Yamal | Rodri | 30% | 16% | 32% | 11% |
| 56 | Republic of Ireland | Philip Quinn | Kane | Dembélé | Yamal | Kvaratskhelia | Rodri | 53% | 15% | 7% | 10% |
| 57 | Bosnia & Herzegovina | Bakir Tiro | Kane | Kvaratskhelia | Dembélé | Yamal | Haaland | 31% | 18% | 24% | 10% |
| 58 | Ghana | Michael Oti Adjei | Kane | Dembélé | Yamal | Kvaratskhelia | Rodri | 45% | 18% | 9% | 12% |
| 59 | Jamaica | Sean Williams | Kane | Yamal | Kvaratskhelia | Dembélé | Messi | 50% | 8% | 10% | 17% |
| 60 | Iceland | Víðir Sigurðsson | Kane | Olise | Kvaratskhelia | Yamal | Dembélé | 35% | 7% | 13% | 10% |
| 61 | Albania | Besnik Dizdari | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 34% | 23% | 19% | 6% |
| 62 | North Macedonia | Miko Zahariev | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 34% | 20% | 17% | 12% |
| 63 | South Africa | Mark Gleeson | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 57% | 11% | 10% | 8% |
| 64 | Iraq | Ali Nouri | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 42% | 21% | 12% | 9% |
| 65 | UAE | Mohammed Al-Joker | Kane | Dembélé | Yamal | Kvaratskhelia | Rodri | 35% | 22% | 13% | 13% |
| 66 | Cabo Verde | Pedro Clovis | Kane | Dembélé | Kvaratskhelia | Yamal | N. Mendes | 63% | 13% | 7% | 5% |
| 67 | Montenegro | Danilo Mitrović | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 34% | 21% | 19% | 9% |
| 68 | Honduras | Gerson Gómez | Kane | Yamal | Kvaratskhelia | Messi | Mbappé | 39% | 3% | 9% | 26% |
| 69 | Georgia | Otar Giorgadze | Kvaratskhelia | Kane | Dembélé | Yamal | Rodri | 12% | 2% | 81% | 2% |
| 70 | Bolivia | Carlos Enrique Rivera | Kane | Yamal | Dembélé | Kvaratskhelia | Messi | 33% | 18% | 10% | 20% |
| 71 | Guinea | Amadou Diouldé Diallo | Dembélé | Kane | Kvaratskhelia | Yamal | Vitinha | 23% | 32% | 20% | 12% |
| 72 | Mali | Souleymane Bobo Tounkara | Dembélé | Kane | Yamal | Kvaratskhelia | Olise | 29% | 29% | 11% | 14% |
| 73 | Gabon | James Golden Pincent | Kane | Dembélé | Kvaratskhelia | Yamal | Mbappé | 49% | 25% | 9% | 6% |
| 74 | New Zealand | Michael Burgess | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 57% | 15% | 8% | 8% |
| 75 | Uzbekistan | Grigoriy Rtveladze | Kane | Dembélé | Kvaratskhelia | Yamal | Olise | 32% | 20% | 16% | 11% |
| 76 | Jordan | Tayseer Al-Amiri | Kane | Dembélé | Yamal | Kvaratskhelia | Rodri | 40% | 16% | 15% | 16% |
| 77 | Oman | Jaber Al-Ajmi | Kane | Dembélé | Kvaratskhelia | Yamal | Vitinha | 48% | 20% | 11% | 9% |
| 78 | El Salvador | Claudio Martínez | Yamal | Kane | Dembélé | Kvaratskhelia | Rodri | 25% | 17% | 8% | 36% |
| 79 | Bahrain | Abdullah Ashoor | Kane | Dembélé | Kvaratskhelia | Yamal | Messi | 40% | 20% | 11% | 10% |
| 80 | Curaçao | Kenley Basilio | Kane | Dembélé | Yamal | Kvaratskhelia | Rodri | 34% | 23% | 13% | 13% |
| 81 | Syria | Lutfi Al-Awan | Kane | Dembélé | Yamal | Kvaratskhelia | Rodri | 35% | 21% | 11% | 16% |
| 82 | Zambia | Desmond Katongo | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 69% | 11% | 6% | 4% |
| 83 | Uganda | Fred Mwambu | Kane | Dembélé | Kvaratskhelia | Yamal | Messi | 57% | 16% | 10% | 6% |
| 84 | Haiti | Raymond Jean-Louis | Dembélé | Kane | Yamal | Kvaratskhelia | Vitinha | 27% | 32% | 12% | 12% |
| 85 | Benin | Hugues Zinsou Zounon | Dembélé | Kane | Kvaratskhelia | Yamal | Olise | 32% | 33% | 15% | 7% |
| 86 | Luxembourg | Christophe Nadin | Kane | Dembélé | Kvaratskhelia | Yamal | Olise | 39% | 31% | 13% | 5% |
| 87 | Armenia | Suren Baghdasaryan | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 34% | 21% | 19% | 9% |
| 88 | Palestine | Bassam Abu Arra | Kane | Kvaratskhelia | Dembélé | Yamal | Vitinha | 52% | 11% | 13% | 8% |
| 89 | Kyrgyzstan | Kuban Atahanov | Kvaratskhelia | Kane | Dembélé | Yamal | Rodri | 29% | 16% | 31% | 13% |
| 90 | Belarus | Sergey Nikolaev | Kvaratskhelia | Kane | Dembélé | Yamal | Rodri | 28% | 18% | 33% | 9% |
| 91 | Northern Ireland | Jackie Fullerton | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 51% | 17% | 11% | 9% |
| 92 | Israel | Elad Zeevi | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 33% | 20% | 19% | 14% |
| 93 | China | Luo Ming | Kane | Dembélé | Kvaratskhelia | Yamal | Haaland | 41% | 17% | 15% | 12% |
| 94 | Gabon | Charles Mve | Kane | Dembélé | Yamal | Kvaratskhelia | Vitinha | 32% | 30% | 10% | 16% |
| 95 | Slovenia | Andrej Stare | Kvaratskhelia | Kane | Dembélé | Yamal | Vitinha | 31% | 17% | 34% | 5% |
| 96 | Honduras | Kelvin Coello | Yamal | Kane | Dembélé | Kvaratskhelia | Rodri | 30% | 11% | 9% | 30% |
| 97 | Trinidad & Tobago | Lasana Liburd | Kane | Dembélé | Yamal | Kvaratskhelia | Rodri | 44% | 19% | 10% | 10% |
| 98 | Bolivia | Juan Pastén | Kane | Yamal | Kvaratskhelia | Dembélé | Rodri | 43% | 8% | 9% | 21% |
| 99 | Mauritania | Lassana Camara | Kane | Kvaratskhelia | Dembélé | Vitinha | Yamal | 38% | 10% | 19% | 7% |
| 100 | Lebanon | Ibrahim Al-Wazan | Kane | Dembélé | Kvaratskhelia | Yamal | Rodri | 45% | 20% | 11% | 9% |

</details>

## How each juror's 2026 ballot is modelled

Utility for juror *j* and contender *c* = wP_j·P + wT_j·T + 0.10·F + bloc affinity + juror history + noise. Each juror's ballot is the top 10 by utility.

- **Bloc affinity:** +5 for the juror's own national players; +1.5 when the juror's media language matches the player's nationality; +1.0 when it matches the league he plays in.
- **Juror history:** +1.0 per standard deviation of the points that juror gave the same player in the rebuilt 2024–25 ballots. Players who received no votes in those years (Messi, Bruno, Díaz) get no history term.
- **Output vs silverware lean:** jurors who put Vinícius above Rodri (2024) and Yamal above Vitinha (2025) get a slightly higher personal wP (±0.05 per unit of lean).
- **Unlisted nominees:** 5 generic slots stand in for the other 13 shortlisted players. Their level is set so they take 4% of all points.

## Reproduce

```
cd ballon-dor-2026/src
python3 reconstruct.py   # rebuild 2024/2025 ballots -> output/ballots_*.csv
python3 predict.py       # backtest + 2026 simulation -> output/prediction_2026_*.csv, summary.json
python3 report.py        # this report
```

Pure Python 3 standard library, fixed random seeds. Edit `data/criteria.json` to test your own scores, or add or remove 2026 contenders there.

## Sources

- [2024 points totals (90min)](https://www.90min.com/ballon-dor-2024-full-points-totals-revealed)
- [2024 voting breakdown, first places by country (GOAL)](https://www.goal.com/en-us/lists/full-2024-ballon-dor-voting-breakdown-reveals-rodri-margin-victory-over-vinicius-jr-controversial-contest/blt0e0bff7ed05adce4)
- [2024 France juror's ballot (GOAL France)](https://www.goal.com/fr/listes/ballon-d-or-2024-le-vote-surprenant-de-la-france-et-les-points-detailles-des-joueurs/bltdcb101478c4b27e8)
- [2024 every journalist's vote (GiveMeSport)](https://www.givemesport.com/journalist-votes-2024-ballon-dor-rodri-vinicius-bellingham/)
- [2024 African jurors' first places (allAfrica)](https://fr.allafrica.com/stories/202411090289.html)
- [2024 Ghana juror, Rodri ahead of Vinícius](https://turn.liquiddesign.co.uk/sports/football/270826-michael-oti-adjei-how-ghanaian-journalist-voted-2024-ballon-d-rodri-vini)
- [2024 jurors who left Vinícius out (Finland, El Salvador, Namibia)](https://element.liquiddesign.co.uk/sports/football/270842-finnish-journalist-resigns-ballon-d-jury-mistake-voting-vinicius-junior)
- [2025 points totals (World Soccer Talk)](https://worldsoccertalk.com/news/2025-ballon-dor-voting-results-revealed-how-close-were-ousmane-dembele-and-lamine-yamal-how-many-points-did-mohamed-salah-and-kylian-mbappe-receive/)
- [2025 positions 11-30 (Foot Africa)](https://foot-africa.com/en/news/ballon-dor-2025-full-voting-breakdown-revealed-895881/)
- [2025 first-place counts (Sports Illustrated)](https://www.si.com/soccer/2025-ballon-dor-voting-breakdown-revealed)
- [2025 how each country voted (Tribuna)](https://tribuna.com/en/blogs/how-each-country-voted-for-in-2025-ballon-dor-revealed/)
- [2025 country votes incl. Georgia/Scotland (Sportaran)](https://sportaran.com/en/post/kak-golosovali-strany-za-zolotoj-myach-2025-raskryty-rezultaty-ballon-dor/)
- [2025 Spain juror's top 3 (SPORTbible)](https://www.sportbible.com/football/football-news/ballon-dor-ousmane-dembele-lamine-yamal-psg-barcelona-716363-20250923)
- [2025 Ghana juror's ballot (Flashscore)](https://www.flashscore.com/news/soccer-champions-league-how-ghana-s-journalist-voted-in-the-2025-ballon-d-or-awards/QPbVqrCk)
- [2025 South Africa juror's ballot (Sportsclub)](https://www.sportsclub.co.za/?p=224719)
- [Kane 2025/26 numbers (Bundesliga.com)](https://www.bundesliga.com/en/bundesliga/news/harry-kane-2025-26-numbers-england-bauern-munich-goals-records-messi-38301)
- [Bayern win the 2026 DFB-Pokal final (FC Bayern)](https://fcbayern.com/en/matches/profis/dfb-pokal/2025-2026/fc-bayern-muenchen-vfb-stuttgart-23-05-2026/report)
- [Bayern out to PSG in the UCL semi-final (Bundesliga.com)](https://www.bundesliga.com/en/bundesliga/news/bayern-munich-manuel-neuer-killer-instinct-champions-league-final-psg-37259)
- [Yamal, LaLiga 2025/26 Player of the Season (FC Barcelona)](https://www.fcbarcelona.com/en/football/first-team/news/4514485/lamine-yamal-202526-laliga-player-of-the-season)
- [Yamal out for the rest of the club season (AP)](https://www.clickorlando.com/sports/2026/04/23/yamal-to-miss-rest-of-barcelona-season-but-be-fit-for-world-cup-with-spain/)
- [Barcelona out to Atlético in the UCL quarter-final (theScore)](https://thescore.com/news/3523183)
- [Mbappé wins the 2025/26 Pichichi (Real Madrid)](https://www.realmadrid.com/en-US/news/football/first-team/latest-news/mbappe-gana-el-trofeo-pichichi-2025-26-23-05-2026)
- [Mbappé 2025/26 UCL top scorer (Real Madrid)](https://www.realmadrid.com/en-US/news/football/first-team/latest-news/mbappe-recibe-el-premio-al-maximo-goleador-de-la-champions-league-2025-26-08-09-2026)
- [Real Madrid out to Bayern in the UCL quarter-final (GOAL)](https://www.goal.com/en-sg/lists/jude-bellingham-speaks-out-real-madrid-controversial-champions-league-exit/bltf4ec2b542d3ca9be)
- [World Cup final: Spain 1-0 Argentina; Rodri Golden Ball; Mbappé Golden Boot (TSN)](https://www.tsn.ca/soccer/fifa-world-cup/article/frances-mbappe-wins-2026-fifa-world-cup-golden-boot/)
- [France out to Spain in the World Cup semi-final (Yahoo Sports)](https://sports.yahoo.com/articles/france-eliminated-world-cup-heartbreaking-205427061.html)
- [England beat France 6-4 for World Cup 3rd place (Euronews)](https://euronews.com/2026/07/19/england-beat-france-6-4-in-world-cup-third-place-thriller)
- [2026 UCL final: PSG beat Arsenal on penalties (Wikipedia)](https://en.wikipedia.org/wiki/2026_UEFA_Champions_League_final)
- [Ballon d'Or 2026 odds, 29 Sep 2026 (Oddschecker)](https://www.oddschecker.com/insight/football/20260929-ballon-dor-2026-odds-harry-kane-favourite-ahead-of-lamine-yamal)
- [Arsenal crowned 2025/26 Premier League champions (Arsenal)](https://www.arsenal.com/news/arsenal-crowned-202526-premier-league-champions)
- [Man City win the 2026 FA Cup (The FA)](https://www.thefa.com/news/2026/may/16/emirates-fa-cup-final-chelsea-v-manchester-city-report-20261605)
- [Man City exit the UCL in the last 16 (Premier League)](https://www.premierleague.com/en/news/4250621)
- [Inter out of the UCL to Bodø/Glimt (Inter)](https://www.inter.it/en/news/inter-bodo-glimt-champions-league-2025-2026)
- [Lautaro, Serie A 2025/26 top scorer (Inter)](https://www.inter.it/en/news/lautaro-martinez-top-scorer-serie-a-2025-26)
- [World Cup knockout results (FIFA)](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/knockout-stage-match-schedule-bracket)
- [Portugal out to Spain in the World Cup last 16 (NBC)](https://www.nbcdfw.com/world-cup/spain-portugal-score-cristiano-ronaldo/4045474/)
- [Colombia out to Switzerland in the World Cup last 16 (FC Bayern)](https://fcbayern.com/en/news/2026/07/luis-diaz-colombia-miss-out-on-world-cup-quarter-finals)
- [Rodri wins the World Cup Golden Ball (FIFA)](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/rodri-earns-adidas-golden-ball)
- [Messi: Silver Ball and Silver Boot (LatestLY)](https://www.latestly.com/sports/football/lionel-messi-wins-silver-ball-and-silver-boot-at-fifa-world-cup-2026-awards-7523924.html)
- [Messi named MLS Cup 2025 MVP (MLS)](https://www.mlssoccer.com/news/inter-miami-s-lionel-messi-named-mls-cup-2025-mvp-pres-by-audi)
- [Kvaratskhelia, 2025/26 UCL Player of the Season (UEFA)](https://www.uefa.com/uefachampionsleague/news/02a5-20c1d7bf915e-f9e703cf0108-1000--khvicha-kvaratskhelia-named-2025-26-uefa-champions-league-/)
- [Why Kvaratskhelia missed the World Cup (World Soccer Talk)](https://worldsoccertalk.com/world-cup/why-khvicha-kvaratskhelia-is-not-playing-in-the-2026-world-cup)
- [Vitinha, 2026 UCL final Player of the Match (UEFA)](https://www.uefa.com/uefachampionsleague/news/02a5-20c0324a93c4-a269d65f5aeb-1000--vitinha-named-official-2026-uefa-champions-league-final-play/)
- [PSG win the 2025 UEFA Super Cup (beIN)](https://www.beinsports.com/en-us/soccer/uefa-super-cup/articles/psg-pulls-off-historic-comeback-against-tottenham-to-win-the-uefa-super-cup-2025-08-13)
- [PSG win the 2025 Intercontinental Cup (FIFA)](https://www.fifa.com/en/tournaments/mens/intercontinentalcup/2025/articles/paris-saint-germain-flamengo-match-report)
- [PSG win the 2026 Trophée des Champions (PSG)](https://www.psg.fr/en/content/match-report-paris-saint-germain-olympique-de-marseille-trophee-des-champions-kuwait-city-2025)
- [Dembélé 2026 World Cup hat-trick vs Norway (Al Jazeera)](https://www.aljazeera.com/sports/2026/6/26/dembele-scores-hat-trick-as-france-beat-norway-4-1-at-world-cup-2026)
- [Haaland scores twice to knock out Brazil (Al Jazeera)](https://www.aljazeera.com/sports/2026/7/5/haaland-scores-twice-as-norway-stun-brazil-2-1-in-world-cup-2026-last-16)
- [Bellingham's England major-tournament goal record (England Football)](https://www.englandfootball.com/articles/2026/Jul/18/jude-bellingham-major-tournament-record-scorer-england-20261807)
- [Declan Rice captains England in the bronze match (England Football)](https://www.englandfootball.com/articles/2026/Jul/19/declan-rice-france-england-captaincy-stats-20261907)
- [Bruno Fernandes breaks the Premier League assist record (beIN)](https://www.beinsports.com/en-us/soccer/premier-league/articles/bruno-fernandes-breaks-historic-premier-league-assist-record-2026-05-24)
- [Luis Díaz 2025/26: 24 goals, 17 assists (Sofascore)](https://www.sofascore.com/news/elite-output-little-noise-luis-diazs-bayern-season-in-numbers)
- [Olise, Bundesliga 2025/26 Player of the Season (Bundesliga.com)](https://www.bundesliga.com/en/bundesliga/news/player-of-the-month-2025-26-vote-winners-ea-sports-olise-34233)
- [Ballon d'Or 2026 30-man shortlist (Yen)](https://yen.com.gh/sports/football/311547-ballon-d-2026-full-list-30-man-nominees-lamine-yamal-mbappe-head-head/)
