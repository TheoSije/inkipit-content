# Audit du corpus — phase 0 (septembre 2026)

Nettoyage fait par `tools/phase0_cleanup.py` (relisible, une ligne par décision).
**Aucun texte d'incipit n'a été écrit ou reformulé** : le script choisit seulement entre
des entrées déjà présentes, sépare les champs et pose des drapeaux.

Limite : l'audit a été fait sans accès réseau à Wikisource / Gallica / Gutenberg.
Les jugements « n'est pas l'incipit » viennent de la comparaison entre doublons (deux
phrases différentes pour le même livre, l'une étant le début connu) ; tout le reste est
marqué **à vérifier contre une source**, pas corrigé.

## Résultat

| | Avant | Après |
|---|---|---|
| Entrées | 393 | 366 après doublons → **304** après vérification |
| Avec photo d'auteur | 199 | 210 |
| Sourcées (`source`) | 0 | 0 |
| Avec drapeau `flag` (à vérifier) | — | 71 → 9 après vérification |

## Nouveaux champs

- `title`, `author_name`, `year` : saisis séparément dans l'admin. `author`
  (« Titre — Auteur, Année ») est **recomposé** à chaque enregistrement, parce que
  c'est le seul champ que lisent l'app iOS (`Incipit.swift`) et le site.
- `source` : `{url, edition, isbn, translator}` — d'où la phrase a été copiée. `null` = non sourcé.
- `verified` : `true` seulement si le texte a été vérifié mot pour mot dans la source.
- `flag` : note « à vérifier » (vider une fois réglé).
- `completeWrongs` (camelCase) supprimé : doublon mort, l'app ne lit que `complete_wrongs`.


## Doublons supprimés (27)

| Gardé | Supprimé | Raison |
|---|---|---|
| Rue des Boutiques Obscures — Patrick Modiano | « C'est un garçon sans histoire. » | 141 « C'est un garçon sans histoire. » n'est pas l'incipit ; 1978 = parution (Goncourt 1978) |
| Zazie dans le métro — Raymond Queneau | « Il faisait un froid de canard ce jour-là. » | 105 « Il faisait un froid de canard… » n'est pas l'incipit |
| Tristes Tropiques — Claude Lévi-Strauss | « Je hais les voyages et les explorateurs » | même phrase ; 344 a la ponctuation et les accents |
| Mémoires d'Hadrien — Marguerite Yourcenar | « Je ne sais pas pourquoi j'écris. » | 104 « Je ne sais pas pourquoi j'écris. » n'est pas l'incipit ; parution 1951 |
| L'Ordre du jour — Éric Vuillard | « En ce mois de février 1933, vingt-quatre maîtres de l'indust… » | 89 est une paraphrase ; parution 2017 (Goncourt 2017) |
| Madame Bovary — Gustave Flaubert | « Nous étions à l'étude, quand le Proviseur entra, suivi d'un … » | même phrase, 268 plus complète |
| Le Grand Meaulnes — Alain-Fournier | « Il arriva chez nous un dimanche de novembre 18.., quelques j… » | même phrase ; « 189… » est la leçon du texte |
| Je m'en vais — Jean Echenoz | « Je m'en vais. » | 137 « Je m'en vais. » tronqué ; parution 1999 (Goncourt 1999) |
| Et si c'était vrai… — Marc Levy | « Il y a des moments où tout bascule. » | 152 « Il y a des moments où tout bascule. » n'est pas l'incipit ; parution 2000 |
| L'Écume des jours — Boris Vian | « Je suis un monstre. » | 106 « Je suis un monstre. » n'est pas l'incipit |
| Anna Karénine — Léon Tolstoï | « Toutes les familles heureuses se ressemblent, mais chaque fa… » | deux traductions ; on garde 27, traduction à sourcer |
| Bonjour tristesse — Françoise Sagan | « Sur ce sentiment inconnu dont l'ennui, la douceur m'obsèdent… » | même phrase |
| Les Faux-Monnayeurs — André Gide | « Le ciel était d'un bleu si pur… » | 103 « Le ciel était d'un bleu si pur… » n'est pas l'incipit |
| Les Trois Mousquetaires — Alexandre Dumas | « Vers la fin de novembre 1625, le jeune d'Artagnan quitta le … » | 99 « Vers la fin de novembre 1625… » n'est pas l'incipit |
| Jean-Christophe — Romain Rolland | « Je ne suis pas un héros. » | 110 « Je ne suis pas un héros. » n'est pas l'incipit |
| Molloy — Samuel Beckett | « Je suis dans la chambre de ma mère. C'est moi qui y vis main… » | même phrase, 93 plus complète ; parution 1951 |
| L'Ombre du vent — Carlos Ruiz Zafón | « Je suis tombé amoureux d'une ombre. » | 131 « Je suis tombé amoureux d'une ombre. » n'est pas l'incipit |
| La Condition humaine — André Malraux | « Tchen tenterait-il de lever la moustiquaire ? Frapperait-il … » | même phrase, 204 plus complète |
| La Place — Annie Ernaux | « J'ai passé les épreuves pratiques du CAPES à Annecy, les 3 e… » | 88 (CAPES à Annecy) n'est pas l'incipit |
| La Chartreuse de Parme — Stendhal | « Le 15 mai 1796, le général Bonaparte fit son entrée dans Mil… » | même phrase, 260 plus complète |
| Cent ans de solitude  — Gabriel García Márquez | « Bien des années plus tard, face au peloton d'exécution, le c… » / « Bien des années plus tard, face au peloton d'exécution, le c… » | trois variantes ; 352 = traduction Durand, la plus répandue |
| La Gloire de mon père — Marcel Pagnol | « Je suis né dans la ville d'Aubagne, sous le Garlaban couronn… » | même phrase |
| Notre-Dame de Paris — Victor Hugo | « Il y avait aujourd'hui trois cent quarante-huit ans six mois… » | 10 « Il y avait aujourd'hui » : le texte dit « Il y a aujourd'hui » |
| Le Procès — Franz Kafka | « Quelqu'un avait dû calomnier Josef K., car, un matin, sans a… » | deux traductions ; on garde celle de Vialatte, traduction à sourcer |
| Nana — Émile Zola | « À neuf heures du soir, la salle des Variétés était encore vi… » | 94 tronque « du théâtre des Variétés » |
| L'Étranger — Albert Camus | « Aujourd'hui, maman est morte. Ou peut-être hier, je ne sais … » | même phrase, 0 plus complète |

## Descriptions retirées (autre livre / autre sujet)

- La Peste — Albert Camus, 1947 — description de L'Étranger
- Notre-Dame de Paris — Victor Hugo, 1831 — article sur la cathédrale (EN)
- 1984 — George Orwell, 1949 — article sur l'année 1984 (EN)
- Le Mur — Jean-Paul Sartre, 1939 — description de Huis clos
- Cendrillon — Charles Perrault, 1697 — article générique sur le conte (EN)
- Elle s'appelait Sarah — Tatiana de Rosnay, 2007 — article sur le film (EN)
- Eldorado — Laurent Gaudé, 2006 — article sur la cité mythique (EN)
- Je vais bien, ne t'en fais pas — Olivier Adam, 2000 — article sur le film (EN)
- Des hommes — Laurent Mauvignier, 2009 — article sur le film (EN)
- Home — Toni Morrison, 2012 — article sur la notion de foyer (EN)
- Uranus — Marcel Aymé, 1948 — article sur la planète (EN)

À re-remplir via l'admin (bouton Enrichir), en vérifiant le résultat.

## Incipits à vérifier (drapeau `flag`)

Lot principal : entrées ajoutées ensemble (index 98–174 du fichier d'origine), phrases courtes et génériques. Sur les 12 entrées de ce lot qui avaient un doublon, **11 n'étaient pas le vrai début du livre** (la 12ᵉ, *Le Quatrième mur*, reste non tranchée) — le reste du lot est donc très probablement dans le même cas. Le lot précédent (index 75–97) en contenait aussi deux (*La Place*, *L'Ordre du jour*) : il n'est pas marqué en bloc, mais n'est pas vérifié non plus.

**Décision à prendre** : les retirer de la publication d'ici à ce qu'ils soient sourcés, ou les garder en attendant. (L'app n'a pas de champ « masqué » : les garder = ils restent visibles.)

| Livre | Texte actuel | Note |
|---|---|---|
| L'Amant — Marguerite Duras, 1984 | Un jour, j'étais âgée déjà, dans le hall d'un lieu public, un homme es… | description en anglais |
| Paul Clifford — Edward Bulwer-Lytton, 1830 | C'était une nuit sombre et orageuse. | description en anglais |
| Catch-22 — Joseph Heller, 1961 | Ce fut le coup de foudre. | description en anglais |
| Les Détectives sauvages — Roberto Bolaño, 1998 | On m'a cordialement invité à rejoindre les réalistes viscéraux. | formulation à vérifier contre la traduction |
| L'Amour aux temps du choléra — Gabriel García Márquez, 1985 | Il était inévitable : l'odeur des amandes amères lui rappelait toujour… | « Il était inévitable » : formulation à vérifier contre la traduction |
| Aurélien — Louis Aragon, 1944 | La première fois qu'Aurélien vit Bérénice, il la trouva franchement la… | description en anglais |
| Le Hussard sur le toit — Jean Giono, 1951 | Les cloches sonnèrent, et la mer monta. | début du livre probablement pas celui-ci |
| Histoire de France — Jules Michelet, 1833 | Je veux peindre la France. | début du livre probablement pas celui-ci |
| Le Rivage des Syrtes — Julien Gracq, 1951 | Il pleuvait sur Nantes ce jour-là. | début du livre probablement pas celui-ci |
| Journal du voleur — Jean Genet, 1949 | Je suis resté longtemps sans parler. | début du livre probablement pas celui-ci |
| Le Mur — Jean-Paul Sartre, 1939 | J'ai vu la guerre de près. | début du livre probablement pas celui-ci |
| Belle du Seigneur — Albert Cohen, 1968 | Il faisait déjà chaud. | début du livre probablement pas celui-ci |
| Les Contemplations — Victor Hugo, 1856 | Demain, dès l'aube, à l'heure où blanchit la campagne… | début du livre probablement pas celui-ci · « Demain, dès l'aube » est un poème du livre IV, pas l'ouverture du recueil |
| Cendrillon — Charles Perrault, 1697 | Il était une fois une femme qui avait une fille jolie et agréable. | début du livre probablement pas celui-ci |
| Portrait de l'artiste en jeune homme — James Joyce, 1916 | Je suis né à Dublin. | début du livre probablement pas celui-ci |
| Contes — Jacob et Wilhelm Grimm, 1812 | Il était une fois un roi et une reine… | début du livre probablement pas celui-ci |
| Une fin de roman — Julian Barnes, 2011 | Je ne suis pas sûr de savoir comment raconter cette histoire. | début du livre probablement pas celui-ci |
| Carrie — Stephen King, 1974 | Je me rappelle très bien le jour où tout a commencé. | début du livre probablement pas celui-ci |
| Requiem for a Dream — Hubert Selby Jr., 1978 | C'est l'histoire d'un type qui tombe d'un immeuble. | début du livre probablement pas celui-ci |
| Moon Palace — Paul Auster, 1989 | J'ai toujours voulu être quelqu'un d'autre. | début du livre probablement pas celui-ci |
| Pastorale américaine — Philip Roth, 1997 | Je suis né dans une petite ville. | début du livre probablement pas celui-ci |
| L'Inconnu du Nord-Express — Patricia Highsmith, 1950 | J'ai rencontré cet homme dans un train. | début du livre probablement pas celui-ci |
| La Vie est ailleurs — Milan Kundera, 1973 | La vie est ailleurs. | début du livre probablement pas celui-ci |
| Une histoire d'amour et de ténèbres — Amos Oz, 2002 | J'ai commencé ce livre pour me sauver. | début du livre probablement pas celui-ci |
| Istanbul — Orhan Pamuk, 2003 | Je me souviens de tout. | début du livre probablement pas celui-ci |
| Si par une nuit d'hiver un voyageur — Italo Calvino, 1979 | Quelqu'un raconte cette histoire. | début du livre probablement pas celui-ci |
| La Femme gauchère — Peter Handke, 1976 | Je n'ai rien à dire. | début du livre probablement pas celui-ci |
| Kafka sur le rivage — Haruki Murakami, 2002 | Il y avait un silence. | début du livre probablement pas celui-ci |
| Les Cerfs-volants de Kaboul — Khaled Hosseini, 2003 | Je suis né dans un pays en guerre. | début du livre probablement pas celui-ci |
| Montedidio — Erri De Luca, 2001 | Je voulais comprendre le monde. | début du livre probablement pas celui-ci |
| La Poursuite du bonheur — Douglas Kennedy, 2001 | C'était une journée ordinaire. | début du livre probablement pas celui-ci |
| La Maison du sommeil — Jonathan Coe, 1997 | Tout a commencé par une erreur. | début du livre probablement pas celui-ci |
| W ou le souvenir d'enfance — Georges Perec, 1975 | Je n'ai pas de souvenirs d'enfance. | début du livre probablement pas celui-ci |
| Le Pays des autres — Leïla Slimani, 2020 | Je suis née deux fois. | début du livre probablement pas celui-ci |
| Qui a tué mon père — Édouard Louis, 2018 | Mon père est mort deux fois. | début du livre probablement pas celui-ci |
| Rien ne s'oppose à la nuit — Delphine de Vigan, 2011 | Ma mère ne m'a jamais donné la main. | début du livre probablement pas celui-ci |
| Rosie Carpe — Marie NDiaye, 2001 | Je vis dans une maison qui n'est pas la mienne. | début du livre probablement pas celui-ci |
| Zone — Mathias Énard, 2008 | Je n'ai jamais su comment commencer. | début du livre probablement pas celui-ci |
| La Salle de bain — Jean-Philippe Toussaint, 1985 | Il y a longtemps que je me suis couché tard. | début du livre probablement pas celui-ci |
| L'Amour dure trois ans — Frédéric Beigbeder, 1997 | Je n'ai jamais su parler aux femmes. | début du livre probablement pas celui-ci |
| Saga — Tonino Benacquista, 1997 | Il y a des jours où tout commence mal. | début du livre probablement pas celui-ci |
| C'est une chose étrange à la fin que le monde — Jean d'Ormesson, 2010 | Le monde commence sans moi et finit sans moi. | début du livre probablement pas celui-ci |
| L'Usage du monde — Nicolas Bouvier, 1963 | Je suis parti un matin de bonne heure. | début du livre probablement pas celui-ci |
| Ensemble, c'est tout — Anna Gavalda, 2004 | La première fois que je l'ai vue, j'ai su. | début du livre probablement pas celui-ci |
| Et après… — Guillaume Musso, 2004 | Je n'ai jamais cru aux histoires d'amour. | début du livre probablement pas celui-ci |
| Elle s'appelait Sarah — Tatiana de Rosnay, 2007 | C'est arrivé sans prévenir. | début du livre probablement pas celui-ci |
| Eldorado — Laurent Gaudé, 2006 | Je suis parti sans me retourner. | début du livre probablement pas celui-ci |
| La Délicatesse — David Foenkinos, 2009 | Je ne voulais pas venir. | début du livre probablement pas celui-ci |
| Un aller simple — Didier Van Cauwelaert, 1994 | Je suis entré dans cette histoire malgré moi. | début du livre probablement pas celui-ci |
| Désert — J. M. G. Le Clézio, 1980 | Il y avait une fois un homme qui n'avait rien. | début du livre probablement pas celui-ci |
| Naissance d'un pont — Maylis de Kerangal, 2010 | Je suis revenu pour comprendre. | début du livre probablement pas celui-ci |
| La Vérité sur l'affaire Harry Quebert — Joël Dicker, 2012 | Je ne savais pas encore que ma vie allait changer. | début du livre probablement pas celui-ci |
| Le Quatrième mur — Sorj Chalandon, 2013 | J'ai appris très tôt à me taire. | début du livre probablement pas celui-ci · doublon non tranché avec 210 — aucune des deux versions n'est sourcée |
| La Première gorgée de bière — Philippe Delerm, 1997 | Je regarde les gens passer. | début du livre probablement pas celui-ci |
| Je vais bien, ne t'en fais pas — Olivier Adam, 2000 | Je suis né sans histoire. | début du livre probablement pas celui-ci |
| S'adapter — Clara Dupont-Monod, 2021 | Il n'y avait personne pour m'attendre. | début du livre probablement pas celui-ci |
| L'Inceste — Christine Angot, 1999 | J'écris parce que je n'ai rien d'autre. | début du livre probablement pas celui-ci |
| Garçon manqué — Nina Bouraoui, 2000 | Je voulais disparaître. | début du livre probablement pas celui-ci |
| Dans les forêts de Sibérie — Sylvain Tesson, 2011 | Je suis resté longtemps à regarder la mer. | début du livre probablement pas celui-ci |
| Kiffe kiffe demain — Faïza Guène, 2004 | Je n'ai jamais su où était ma place. | début du livre probablement pas celui-ci |
| Shérazade — Leïla Sebbar, 1982 | J'ai grandi entre deux mondes. | début du livre probablement pas celui-ci |
| Le Testament français — Andreï Makine, 1995 | Je suis parti pour ne plus revenir. | début du livre probablement pas celui-ci |
| L'Hiver aux trousses — Cédric Gras, 2015 | Il faisait encore nuit quand je suis parti. | début du livre probablement pas celui-ci |
| Le Village de l'Allemand — Boualem Sansal, 2008 | Je suis né dans une ville qui n'existe plus. | début du livre probablement pas celui-ci |
| La Clé de Smyrne — Tatiana Salem Levy, 2007 | Je n'ai jamais oublié ce jour-là. | début du livre probablement pas celui-ci |
| Les Hirondelles de Kaboul — Yasmina Khadra, 2002 | Je suis resté longtemps dans le silence. | début du livre probablement pas celui-ci |
| Dans ces bras-là — Camille Laurens, 2000 | Il y a des histoires qu'on ne raconte pas. | début du livre probablement pas celui-ci · bio en anglais |
| Des hommes — Laurent Mauvignier, 2009 | Tout commence par une absence. | début du livre probablement pas celui-ci |
| Le Quatrième Mur — Sorj Chalandon, 2013 | Je suis tombé. Je me suis relevé. | doublon non tranché avec 159 — aucune des deux versions n'est sourcée |
| Les Contemplations — Victor Hugo, 1856 | Aujourd'hui, 4 septembre 1856. | incipit du recueil à vérifier (doublon avec 111) |
| Je m'en vais — Jean Echenoz, 1999 | Je m'en vais, dit Ferrer, je te quitte. | apostrophe manquante corrigée (« Je men » → « Je m'en ») |

## Autres constats (pas traités en phase 0)

- **123 couvertures** pointent vers `covers.openlibrary.org/b/title/…`. *Correction (après vérification
  dans un vrai navigateur)* : ce type d'adresse n'est pas documenté par Open Library mais **s'affiche
  le plus souvent correctement** — il n'est donc pas « cassé ». Il reste fragile (recherche par titre :
  peut tomber sur une autre édition ou un autre livre au titre proche). Le panneau « 🖼 Images » de
  l'admin ne liste par défaut que les couvertures réellement cassées, testées dans le navigateur.
- Les bios / descriptions du lot ajouté en dernier (Balzac, Zola… index ~237–391) sont rédigées sans
  source citée : à garder, mais pas considérées comme « sourcées ».
- Traductions probablement encore sous droits (Kafka/Vialatte, García Márquez/Durand…) : à sourcer
  avec le nom du traducteur.
- Photos d'auteur hébergées chez des tiers (babelio, radiofrance, lesechos…) : fragiles, à remplacer
  par Wikimedia Commons en phase « photos ».

## Vérification des suspects (phase 0b)

Les 66 incipits suspects ont été cherchés un par un sur le web (phrase exacte + auteur) : pages d'éditeurs, extraits numériques, fiches pédagogiques, sites d'incipits. Script : `tools/phase0b_verif.py`, détail : `tools/verif_suspects.tsv`.

- **FAUX (25)** : une source montre un autre début → retirés
- **INTROUVABLE (37)** : cités nulle part comme début du livre → retirés
- **FORMULATION (2)** : bon début, mots inexacts → gardés, note avec le lien pour recopier la phrase exacte
- **PARTIEL (2)** : phrase authentique mais pas (entièrement) au début → gardés, note

**Aucune phrase du lot n'a été confirmée comme vrai début de livre.** Les entrées retirées sont sauvegardées dans `tools/retires.json` (restauration possible).

La colonne « vrai début selon source » du TSV est un indice pour retrouver la page, pas un texte à coller : pour ré-ajouter un de ces livres, recopier la phrase depuis la source et la noter dans le champ `source`.

| Livre | Statut | Indice | Source |
|---|---|---|---|
| Les Détectives sauvages | FORMULATION | J'ai été cordialement invité à faire partie du réalisme viscéral. | https://excerpts.numilog.com/books/9782823613131.pdf |
| L'Amour aux temps du choléra | FORMULATION | C'était inévitable : l'odeur des amandes amères lui rappelait le destin des amours contrariées. | http://la-marquise-sortit-a-cinq-heures.over-blog.com/2014/12/c-etait-inevitable-gabriel-garcia-marquez-l-amour-au-temps-du-cholera-incipit.html |
| Le Hussard sur le toit | INTROUVABLE |  | https://www.ebooksgratuits.com/html/giono_[le_cycle_du_hussard_3]_le_hussard_sur_le_toit.html |
| Histoire de France | FAUX | (la phrase est d'Agrippa d'Aubigné, Les Tragiques) | https://www.bacdefrancais.net/lestragiques.php |
| Le Rivage des Syrtes | INTROUVABLE |  |  |
| Journal du voleur | FAUX | Le vêtement des forçats est rayé rose et blanc. | https://www.rodoni.ch/B5/genet-voleur.pdf |
| Le Mur | INTROUVABLE |  |  |
| Belle du Seigneur | FAUX | Descendu de cheval, il allait le long des noisetiers et des églantiers… | https://media.electre-ng.com/extraits/extrait-id/638410a917a297c95c7f9855baf6ac27318c67b21395def2362dff02c7c36a9a.pdf |
| Les Contemplations (Aujourd'hui, 4 septembre 1856) | INTROUVABLE |  | https://www.gutenberg.org/ebooks/29844 |
| Cendrillon | FAUX | Il était une fois un gentilhomme qui épousa, en secondes noces, une femme la plus hautaine et la plus fière qu'on eût jamais vue. | https://fr.wikisource.org/wiki/Contes_de_Perrault_(%C3%A9d._1902)/Cendrillon_ou_la_petite_Pantoufle_de_verre |
| Portrait de l'artiste en jeune homme | INTROUVABLE |  |  |
| Une fin de roman | INTROUVABLE |  |  |
| Carrie | INTROUVABLE |  |  |
| Requiem for a Dream | FAUX | (la phrase vient du film La Haine) | https://www.dicocitations.com/citation_internaute_ajout/4163.php |
| Moon Palace | FAUX | C'était l'été où l'homme a pour la première fois posé le pied sur la Lune. | https://www.incipitmania.com/aut-a/auster-paul/moon-palace-paul-auster/ |
| Pastorale américaine | INTROUVABLE |  |  |
| L'Inconnu du Nord-Express | INTROUVABLE |  |  |
| Une histoire d'amour et de ténèbres | INTROUVABLE |  |  |
| Si par une nuit d'hiver un voyageur | FAUX | (le livre s'ouvre sur « Tu vas commencer le nouveau roman d'Italo Calvino… » — à copier depuis la source) | https://www.bacfrancais.com/commentaire/calvino-nuit-hiver-voyageur-incipit/ |
| Les Cerfs-volants de Kaboul | FAUX | Je suis devenu ce que je suis aujourd'hui à l'âge de douze ans, par un jour glacial et nuageux de l'hiver 1975. | https://booknode.com/les_cerfs-volants_de_kaboul_0993/extraits |
| La Salle de bain | FAUX | Lorsque j'ai commencé à passer mes après-midi dans la salle de bain, je ne comptais pas m'y installer ; … | https://books.google.com/books/about/La_Salle_de_bain.html?id=codSCwAAQBAJ |
| Rien ne s'oppose à la nuit | FAUX | Ma mère était bleue, d'un bleu pâle mêlé de cendres, … | https://www.furet.com/media/pdf/feuilletage/9/7/8/2/2/5/3/1/9782253164265.pdf |
| Qui a tué mon père | INTROUVABLE |  |  |
| Le Pays des autres | FAUX | La première fois que Mathilde visita la ferme, elle pensa : « C'est trop loin. » | https://booknode.com/le_pays_des_autres_tome_1_03166833/extraits |
| Istanbul | INTROUVABLE |  |  |
| La Femme gauchère | INTROUVABLE |  |  |
| Kafka sur le rivage | FAUX | (le roman s'ouvre sur un dialogue avec « le garçon nommé Corbeau ») |  |
| Montedidio | INTROUVABLE |  | https://www.incipitmania.com/aut-d/de-luca-erri/montedidio-erri-de-luca/ |
| La Poursuite du bonheur | FAUX | Le premier, le tout premier souvenir de lui est un regard. | https://booknode.com/la_poursuite_du_bonheur_03439/extraits |
| La Maison du sommeil | INTROUVABLE |  |  |
| W ou le souvenir d'enfance | PARTIEL | phrase authentique, mais c'est le début du chapitre II (partie autobiographique), pas du livre | http://anneprof.unblog.fr/2017/12/31/texte-6-w-ou-le-souvenir-denfance-perec-chapitre-2-incipit-du-souvenir/ |
| Rosie Carpe | INTROUVABLE |  | https://www.leseditionsdeminuit.fr/livre-Rosie_Carpe-1734-1-1-0-1.html |
| Zone | INTROUVABLE |  | https://grandeursrvitude.wordpress.com/2016/02/28/la-longue-phrase-incipit-de-mathias-enard-277-mots/ |
| L'Amour dure trois ans | INTROUVABLE |  |  |
| Saga | INTROUVABLE |  |  |
| C'est une chose étrange à la fin que le monde | INTROUVABLE |  |  |
| L'Usage du monde | INTROUVABLE |  |  |
| Ensemble, c'est tout | FAUX | Non, Paulette Lestafier n'était pas folle du tout. | https://actualitte.com/livres/324051/extraits/ensemble-c-est-tout-anna-gavalda-9782290356135 |
| Et après… | INTROUVABLE |  |  |
| Elle s'appelait Sarah | INTROUVABLE |  |  |
| Eldorado | FAUX |  | https://www.devoir-de-philosophie.com/litterature/la-1-eldorado-laurent-gaude-incipit |
| La Délicatesse | FAUX | Nathalie était plutôt discrète (une sorte de féminité suisse). | https://excerpts.numilog.com/books/9782072767548.pdf |
| Un aller simple | FAUX | J'ai commencé dans la vie comme enfant trouvé par erreur. | https://archive.org/details/unallersimplerom00cauw |
| Désert | FAUX | Ils sont apparus, comme dans un rêve, au sommet de la dune, à demi cachés par la brume de sable que leurs pieds soulevaient. | http://blog.ac-versailles.fr/lettresdarts/public/QUATRE_ELEMENTS/Desert1.pdf |
| Naissance d'un pont | INTROUVABLE |  |  |
| La Vérité sur l'affaire Harry Quebert | INTROUVABLE |  |  |
| Le Quatrième mur (« J'ai appris très tôt à me taire. ») | FAUX | Je suis tombé. (première phrase — voir 184) | https://fr.wikipedia.org/wiki/Le_Quatri%C3%A8me_Mur_(roman) |
| Le Quatrième Mur (« Je suis tombé. Je me suis relevé. ») | PARTIEL | 1re phrase « Je suis tombé. » confirmée ; la suite est à vérifier dans le livre | https://lecturesanalytiquessite.wordpress.com/2017/06/27/le-quatrieme-mur-chapitre-1/ |
| La Première gorgée de bière | INTROUVABLE |  |  |
| Je vais bien, ne t'en fais pas | INTROUVABLE |  |  |
| S'adapter | FAUX | Un jour, dans une famille, est né un enfant inadapté. | https://ifsuede.com/wp-content/uploads/2023/03/Sadapter-Clara-Dupont-Monod-.pdf |
| L'Inceste | INTROUVABLE |  |  |
| Garçon manqué | INTROUVABLE |  |  |
| Dans les forêts de Sibérie | FAUX | Je m'étais promis avant mes quarante ans de vivre en ermite au fond des bois. | https://www.gallimard.fr/catalogue/dans-les-forets-de-siberie/9782070129256 |
| Kiffe kiffe demain | FAUX | C'est lundi et comme tous les lundis, je suis allée chez Mme Burlaud. | https://booknode.com/kiffe_kiffe_demain_048981/extraits |
| Shérazade | INTROUVABLE |  |  |
| Le Testament français | INTROUVABLE |  |  |
| L'Hiver aux trousses | INTROUVABLE |  |  |
| Le Village de l'Allemand | INTROUVABLE |  | https://excerpts.numilog.com/books/9782070396993.pdf |
| La Clé de Smyrne | INTROUVABLE |  |  |
| Les Hirondelles de Kaboul | INTROUVABLE |  |  |
| Dans ces bras-là | INTROUVABLE |  |  |
| Des hommes | INTROUVABLE | (le roman commence au milieu d'une phrase, sans majuscule) | https://laurent-mauvignier.net/des-hommes-laurent-mauvignier-roman.html |
| Les Contemplations (« Demain, dès l'aube… ») | FAUX | (poème du livre IV, pas l'ouverture du recueil) | https://en.wikipedia.org/wiki/Demain_d%C3%A8s_l%27aube |
| Contes (Grimm) | FAUX | (formule générique, ne correspond à aucun conte précis) |  |
| La Vie est ailleurs | FAUX | Quand la mère du poète se demandait où le poète avait été conçu, … | https://excerpts.numilog.com/books/9782070368341.pdf |
