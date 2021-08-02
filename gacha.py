import random
FIRE = "fire"
WATER = "water"
EARTH = "earth"
WIND = "wind"
LIGHT = "light"
DARK = "dark"



ssr_list = [["Thunder Dirk Jove", "Agielba", FIRE],
            ["Gottfried", "Aglovale", WATER],
            ["Hauteclaire", "Albert", LIGHT],
            ["Greatsword Andalius", "Aletheia", EARTH],
            ["Magma Gauntlet", "Aliza", FIRE],
            ["Dainsleif", "Altair", WATER],
            ["Dragon Slayer", "Amira", LIGHT],
            ["Daemon's Spine", "Anne", WATER],
            ["Forbidden Inferno", "Anthuria", FIRE],
            ["Way Flyer", "Aoidos", FIRE],
            ["Cords of Heaven Lillah", "Arriet", WIND],
            ["Gargantua", "Arulumaya", EARTH],
            ["Sacred Lance", "Athena", FIRE],
            ["Ancient Bandages", "Ayer", EARTH],
            ["Shadow Viperlance", "Azazel", DARK],
            ["Spymur's Clause", "Baal", EARTH],
            ["Symbol of Justice", "Baotorda", LIGHT],
            ["Gram", "Beatrix", DARK],
            ["Ouroboros", "Cagliostro", EARTH],
            ["Black Ouroboros", "Cagliostro", DARK],
            ["Turpin Spear", "Carmelina", WIND],
            ["Arsene", "Catherine", EARTH],
            ["Coco & Mimi", "Cerberus", DARK],
            ["Claíomh Solais", "Charlotta", WATER],
            ["Claidheamh Soluis", "Charlotta", LIGHT],
            ["Phantom Thief Blade", "Chat Noir", WATER],
            ["Mobius Strip", "Clarisse", FIRE],
            ["Fusion Mobius", "Clarisse", LIGHT],
            ["Metal Destroyer", "Colossus", FIRE],
            ["White Hawk", "Cucouroux", WATER],
            ["Neko Punch Pro", "Dante and Freiheit", EARTH],
            ["Spectral Cleaver", "Danua", LIGHT],
            ["Kerykeion", "De La Fille", LIGHT],
            ["Thyrsus", "De La Fille", EARTH],
            ["Gothic Cutlery", "Dorothy and Claudia", LIGHT],
            ["Red Sphere", "Drang", FIRE],
            ["Stratomizer", "Eustace", EARTH],
            ["Ishtar", "Eustace", DARK],
            ["Heroic Bow", "Feena", WIND],
            ["Ethereal Lasher", "Ferry", LIGHT],
            ["Skyrend Spear", "Forte", DARK],
            ["Arachne", "Freezie", DARK],
            ["Windflash", "Gawain", WIND],
            ["Brahma Gauntlet", "Ghandagoza", FIRE],
            ["Draco Claw", "Grea", FIRE],
            ["Soul Eater", "Hallesena", EARTH],
            ["Luin", "Heles", FIRE],
            ["Deirdre's Symbol", "Heles", WIND],
            ["Great Spear", "Herja", EARTH],
            ["Mystic Spray Gun", "Illnott", FIRE],
            ["Gandiva", "Ilsa", EARTH],
            ["Takeminakata", "Ilsa", LIGHT],
            ["Nagelring", "Izmir", WATER],
            ["Caladbolg", "Jeanne d'Arc", LIGHT],
            ["Disparia", "Jeanne d'Arc", DARK],
            ["Soshu Masamune", "Jin", EARTH],
            ["Capulet's Oath", "Juliet", LIGHT],
            ["Vagabond", "Kolulu", DARK],
            ["Wing of the Pure", "Korwa", WIND],
            ["Juzumaru", "Kou", DARK],
            ["Rainbow Hand", "Ladiva", EARTH],
            ["Ukonvasara", "Lady Grey", DARK],
            ["Metal Hand", "Lady Katapillar and Vira", WATER],
            ["Hoarfrost Blade Persius", "Lancelot", WATER],
            ["Heiliges Schwert", "Lancelot", WIND],
            ["Feendrache Pennant", "Lancelot and Vane", FIRE],
            ["Commander's Sidearm", "Lecia", WATER],
            ["Far Away", "Lennah", WIND],
            ["Levin Shooter", "Levin Sisters", LIGHT],
            ["Melodic Sphere", "Lilele", WATER],
            ["Ice Crystal Staff", "Lily", WATER],
            ["Alabaster Zenith", "Lucius", DARK],
            ["Ruling Pen", "Lunalu", DARK],
            ["Froststar Staff", "Macula Marius", DARK],
            ["Illusion Scepter", "Magisa", FIRE],
            ["Gridarvor", "Marquiares", DARK],
            ["Euripides", "Medusa", EARTH],
            ["Split End", "Melissabelle", WIND],
            ["Vassago", "Melleau", EARTH],
            ["Aetherial Bow", "Metera", WIND],
            ["Roseate Aetherial Bow", "Metera", FIRE],
            ["Acid Bolt Shooter", "Milleore and Sahli Lao", WATER],
            ["Trí Bandia", "Morrigna", WIND],
            ["Venustas", "Narmaya", DARK],
            ["Mettle", "Nemone", EARTH],
            ["Pilum", "Nezahualpilli", WIND],
            ["Gigante Slicer", "Nicholas", DARK],
            ["Lohengrin", "Percival", FIRE],
            ["Walthari", "Percival", LIGHT],
            ["Heaven's Cloud", "Petra", WIND],
            ["Predator Claw", "Predator", DARK],
            ["Gae Derg", "Razia", EARTH],
            ["Railgun", "Robomi", LIGHT],
            ["Montague's Oath", "Romeo", WATER],
            ["Twin Helix", "Rosamia", LIGHT],
            ["Sandcastle Song-Lume", "Sara", EARTH],
            ["Eon", "Sara", LIGHT],
            ["Sealed Claustrum", "Sarunan", LIGHT],
            ["Kalaurops", "Sarunan", DARK],
            ["Sikinnis", "Satyr", FIRE],
            ["Deirdre's Claws", "Scathacha", WIND],
            ["Cythara Anglica", "Selfira", WIND],
            ["Galactic Impact", "Sen", WIND],
            ["Hrotti", "Seruel", LIGHT],
            ["Iridescent Bow", "Shitori", LIGHT],
            ["Teiwaz", "Shura", WATER],
            ["Ascalon", "Siegfried", EARTH],
            ["Black Dragon's Maw", "Siegfried", FIRE],
            ["Vlisragna", "Silva", WATER],
            ["Full Metal Recoil", "Silva", LIGHT],
            ["Scarlet Vane", "Societte", WATER],
            ["Blushing Blossom Pin", "Societte", FIRE],
            ["Cardinal Spear", "Societte", WIND],
            ["Ocean Harp", "Sophia", LIGHT],
            ["Wyrmtiger Claw", "Soriz", EARTH],
            ["Golden Dragon", "Stan and Aliza", WIND],
            ["Proelium", "Sturm", WATER],
            ["Hand Axe", "Tabina", FIRE],
            ["Gandring", "Tanya", DARK],
            ["Tanzanite Blade", "Therese", FIRE],
            ["Tiamat Bolt Prime", "Tiamat", WIND],
            ["Two-by-Four", "Tsubasa", FIRE],
            ["Blossom Axe", "Vane", WATER],
            ["Azoth", "Vania", DARK],
            ["Plushie Pal", "Vania and Malinda", WATER],
            ["Mistilteinn", "Vaseraga", DARK],
            ["Wurtzite Scythe", "Vaseraga", EARTH],
            ["Bloody Scar", "Veight", DARK],
            ["Lyst Sin", "Vira", DARK],
            ["Another Sky", "Vira", WIND],
            ["Master Key", "Wulf and Renie", DARK],
            ["Bella Aeterna", "Yggdrasil", EARTH],
            ["Meteora", "Yngwie", WATER],
            ["Fudo-Kuniyuki", "Yodarha", WATER],
            ["True Tiger's Bane", "Yodarha", WIND],
            ["Scarlet Crest Axe", "Yuel", FIRE],
            ["Izayoi", "Yuel", WATER],
            ["Yyrkoon", "Yuisis", WIND],
            ["Gangsta Knife", "Yuisis", FIRE],
            ["Returner Staff", "Yurius", WIND],
            ["Starblaze Rings", "Zahlhamelina", FIRE],
            ["Brionac", "Zeta", FIRE],
            ["Sunspot Spear", "Zeta", DARK],
            ["Ruler of Fate", "Zooey", LIGHT],
            ["Tiny Logger's Axe", "Abby", FIRE],
            ["Ophelia", "Juliet (Water)", WATER],
            ["Brand New Melody", "Diantha (Earth)", EARTH],
            ["Disturbance Signum", "Florence", WIND],
            ["Tabarzin", "Gawain (Light)", LIGHT],
            ["Innocent Doll", "Mireille and Risette", EARTH],
            ["Aurora Bow", "Sutera", WIND],
            ["Barbell", "Fiorito", EARTH],
            ["Hope-Filled Knuckles", "Feather", LIGHT],
            ["Whitefrost Glacier", "Filene", WATER],
            ["Gigante Bisector", "Nicholas (Light)", LIGHT],
            ["Woodland Prayer", "Mishra", LIGHT],
            ["Miming's Baselard", "Zehek", DARK],
            ["Heart of a Songbird", "Lamretta", EARTH],
            ["Raijodo", "Nectar", WIND],
            ["Grynoth Demiclone", "Vaseraga (Fire)", FIRE],
            ["Arvess Demiclone", "Zeta (Water)", WATER],
            ["Bravery", "Farrah and Juri", LIGHT],
            ["Plasma Slicer", "Isaac", WATER],
            ["Embrasque Demiclone", "Beatrix (Earth)", EARTH],
            ["Bonsai Blade", "Shion", FIRE],
            ["Flamelance: Accendo", "Nezha", WIND],
            ["Schwarz Lightning", "Albert (Dark)", DARK],
            ["Reveiller", "Troue", WATER],
            ["Lancet", "Tikoh", LIGHT],
            ["Charming Broom", "Ms. Miranda", FIRE],
            ["Destiny Knuckles", "Sho", WIND],
            ["Merveilleux", "Lennah (Earth)", EARTH],
            ]

flashfest_list = [["Mirror-Blade Shard", "Alexiel", EARTH],
                  ["Blutgang", "Black Knight", DARK],
                  ["Blue Sphere", "Drang (Grand)", WATER],
                  ["Galilei's Insight", "Europa", WATER],
                  ["Vortex of the Void", "Grimnir", WIND],
                  ["Bab-el-Mandeb", "Helel ben Shalem", DARK],
                  ["Sacred Standard", "Jeanne d'Arc (Grand)", LIGHT],
                  ["Eden", "Lucio", LIGHT],
                  ["Kerak", "Mugen", FIRE],
                  ["Fallen Sword", "Olivia", DARK],
                  ["Parazonium", "Orchid", DARK],
                  ["Purifying Thunderbolt", "Shiva", FIRE],
                  ["Ixaba", "Sturm (Grand)", FIRE],
                  ["Certificus", "Vira (Grand)", LIGHT],
                  ["Cute Ribbon", "Zooey (Grand)", DARK],
                  ["Cerastes", "Golden Knight", EARTH],
                  ["World Ender", "Sandalphon", EARTH],
                  ["Radiant Rinne", "Nehan", LIGHT]
                  ]

legfest_list = [["Ichigo Hitofuri", "Cain", EARTH],
                ["AK-4A", "Eugen", EARTH],
                ["Unheil", "Ferry (Grand)", DARK],
                ["Gambanteinn", "Io (Grand)", LIGHT],
                ["Murgleis", "Katalina (Grand)", WATER],
                ["Reunion", "Lecia (Grand)", WIND],
                ["Sky Ace", "Monika (Grand)", WIND],
                ["Ivory Ark", "Noa", LIGHT],
                ["Taisai Spirit Bow", "Pholia", WATER],
                ["Benedia", "Rackam", FIRE],
                ["Sunya", "Rei", DARK],
                ["Fist of Destruction", "Reinhardtzar", FIRE],
                ["Love Eternal", "Rosetta (Grand)", WIND],
                ["Yahata's Naginata", "Leona (Grand)", EARTH],
                ["Ouroboros Prime", "Cagliostro (Grand)", LIGHT],
                ["Evanescence", "Narmaya (Grand)", WIND],
                ["Atlantis", "Poseidon", WATER]
                ]

zodiac_list = [["Dormius", "Andira", WIND],
               ["Ramulus", "Anila", FIRE],
               ["Porculius", "Kumbhira", LIGHT],
               ["Gallinarius", "Mahira", EARTH],
               ["Canisius", "Vajra", WATER],
               ["Rodentius", "Vikala", DARK],
               ["Bovinius", "Catura", WIND]
               ]

valentine_list = [["Silphium", "Clarisse (Valentine)", DARK],
                  ["Lupercalia", "Grimnir (Valentine)", WIND],
                  ["Medusiana Staff", "Medusa (Valentine)", EARTH],
                  ["Sword on the Cob", "Melissabelle (Valentine)", LIGHT],
                  ["Deirdre's Heart", "Scathacha (Valentine)", FIRE],
                  ["Lovely Ace", "Monika (Valentine)", EARTH],
                  ["Wales' Finest", "Aglovale (Valentine)", LIGHT]
                  ]

summer_list = [["Nibelung Glas", "Alexiel (Summer)", EARTH],
               ["Forbidden Memories", "Anthuria (Summer)", DARK],
               ["Delta Quartz", "Beatrix (Summer)", FIRE],
               ["Only for a Cutie", "Cagliostro (Summer)", WATER],
               ["Mikazuki", "Dauna (Summer)", DARK],
               ["Diamond Edge", "De La Fille (Summer)", LIGHT],
               ["Tlepilli", "Diantha (Summer)", WATER],
               ["Crystal Bellflowers", "Europa (Summer)", WATER],
               ["Draco Horn", "Grea (Summer)", WATER],
               ["Sharp Letter", "Halluel and Malluel", LIGHT],
               ["Crystal Luin", "Heles (Summer)", LIGHT],
               ["Arjunan Bow", "Ilsa (Summer)", FIRE],
               ["Sunflower Wand", "Io (Summer)", FIRE],
               ["Frostbite", "Izmir (Summer)", WATER],
               ["Orleans Standard", "Jeanne d'Arc (Summer)", WIND],
               ["Midnight Radiance", "Jessica (Summer)", EARTH],
               ["Bell of Happy Endings", "Korwa (Summer)", WIND],
               ["Conifer", "Naoise (Summer)", LIGHT],
               ["Raikiri", "Narmaya (Summer)", WATER],
               ["Antwerp", "Percival (Summer)", FIRE],
               ["Thorny Rose", "Rosetta (Summer)", EARTH],
               ["Ain Soph", "Sandalphon (Summer)", WATER],
               ["Sinensis", "Siegfried (Summer)", WIND],
               ["Tropical Fairy", "Teena (Summer)", FIRE],
               ["Deep Desire", "Vira (Summer)", EARTH],
               ["Crimson Sapphire", "Yuel (Summer)", WIND],
               ["Cletine", "Zeta (Summer)", LIGHT],
               ["Much Ado", "Kolulu (Summer)", WATER],
               ["Dayspring", "Lucio (Summer)", WATER],
               ["Summer Genesis", "Amira (Summer)", DARK],
               ["Eight Point of the Flock", "Anila (Summer)", WIND],
               ["Official's Jitte", "Rosamia (Summer)", LIGHT],
               ["Surviving Lightning", "Albert (Summer)", WIND],
               ["Beach-Camouflage Vlisragna", "Silva (Summer)", EARTH],
               ["My Little Mim", "Mimlemel (Summer)", FIRE],
               ["Twelfth Vertex of the Passel", "Kumbhira (Summer)", FIRE],
               ["Ninth Head of the Cartload", "Andira (Summer)", WATER],
               ["Auriculata Bow", "Izmir (Yukata)", FIRE],
               ["C'est la Vie", "Yngwie (Yukata)", WIND],
               ["Ravening Harpoon", "Siegfried (Summer)", WATER],
               ["Bubble Sketcher", "Illnot (Summer)", EARTH],
               ["Aetherial Marine", "Metera (Summer)", EARTH],
               ["Ursula Glove", "Meg (Summer)", DARK]
               ]

halloween_list = [["Ouroboros Treat", "Cagliostro (Halloween)", DARK],
                  ["Jack-O'-Brand", "Charlotta (Halloween)", LIGHT],
                  ["Snack Pole", "Danua (Halloween)", FIRE],
                  ["Nightmare Mobilizer", "Eustace (Halloween)", EARTH],
                  ["Spirit Seeker", "Hallessena (Halloween)", LIGHT],
                  ["Distant Requiem", "Lady Grey (Halloween)", DARK],
                  ["Enchanted Broomstick", "Zeta and Vaseraga (Halloween)", EARTH],
                  ["Trick Serpent", "Azazel (Halloween)", FIRE],
                  ["Midnight Rose", "Rosetta (Halloween)", WATER]
                  ]

xmas_list = [["Stardust Holly Rod", "Arulumaya (Holiday)", WATER],
             ["Snowy Mobius Strip", "Clarisse (Holiday)", EARTH],
             ["Holy Night Scepter", "Magisa (Holiday)", EARTH],
             ["Jolly Starcracker", "Mary (Holiday)", LIGHT],
             ["Ray Gun", "Meteon (Holiday)", WIND],
             ["Pinkie Needle", "Metera (Holiday)", LIGHT],
             ["Blade of Purification", "Narmaya (Holiday)", EARTH],
             ["Rosen Maiden", "Rosetta (Holiday)", DARK],
             ["Brand of Binding Oath", "Seruel (Holiday)", WIND],
             ["Tropical Winter", "Nemone (Holiday)", FIRE],
             ["Snowbane", "Mirin (Holiday)", WATER],
             ["Saintly Crystal", "Lily (Holiday)", LIGHT]
             ]

sr_list = ["SR character",
           "SR summon",
           "SR dupe",
           "SR dupe",
           "SR dupe"]

r_list = ["R character",
          "R summon",
          "R dupe",
          "R dupe",
          "R dupe",
          "R dupe",
          "R dupe",
          "R dupe",
          "R dupe",
          "R dupe"]

ssr_summon_list = [["Adramelech", LIGHT],
                   ["Anat, for Love and War", WIND],
                   ["Ankusha", EARTH],
                   ["Anubis", DARK],
                   ["Aphrodite", LIGHT],
                   ["Apollo", LIGHT],
                   ["Athena", FIRE],
                   ["Baal", EARTH],
                   ["Bonito", WATER],
                   ["Ca Ong", WATER],
                   ["Cerberus, Hellhound Trifecta", DARK],
                   ["Charybdis", WATER],
                   ["Cybele", EARTH],
                   ["Dark Angel Olivia", DARK],
                   ["Demonbream", WIND],
                   ["Dogu", EARTH],
                   ["Freyr", WIND],
                   ["Garuda", WIND],
                   ["Garula, Shining Hawk", WIND],
                   ["Gilgamesh", EARTH],
                   ["Gorilla", EARTH],
                   ["Grani", WATER],
                   ["Hamsa", WIND],
                   ["Hector", LIGHT],
                   ["Heimdallr", LIGHT],
                   ["Lich", DARK],
                   ["Macula Marius", WATER],
                   ["Magus, Triad of Wisdom", LIGHT],
                   ["Marduk, Battlefield Reaper", EARTH],
                   ["Medusa", EARTH],
                   ["Morrigna", WIND],
                   ["Nacht", DARK],
                   ["Neptune", WATER],
                   ["Nezha", WIND],
                   ["Nyarlathotep", DARK],
                   ["Oceanus", WATER],
                   ["Odin", LIGHT],
                   ["Owlcat", WIND],
                   ["Poseidon, the Tide Father", WATER],
                   ["Princess Long Ji", WATER],
                   ["Prometheus", FIRE],
                   ["Quetzalcoatl", WIND],
                   ["Red Hare", FIRE],
                   ["Rose Queen", WIND],
                   ["Satan", DARK],
                   ["Satyr", FIRE],
                   ["Setekh", WIND],
                   ["Sethlans", FIRE],
                   ["Siren", WIND],
                   ["Snow White", WATER],
                   ["Surtr", FIRE],
                   ["Sylph, Flutterspirit of Purity", FIRE],
                   ["Tezcatlipoca", EARTH],
                   ["Thor", LIGHT],
                   ["Tsukuyomi", DARK],
                   ["Twin Elements", FIRE],
                   ["Typhon", DARK],
                   ["Vortex Dragon", LIGHT],
                   ["Zaoshen", FIRE],
                   ["Mammoth", EARTH],
                   ["Zirnitra", DARK],
                   ["Tsuchinoko", EARTH]
                   ["Wilnas", FIRE],
                   ["Galleon", EARTH],

                   ["Agni", FIRE],
                   ["Bahamut", DARK],
                   ["Belial", DARK],
                   ["Europa", WATER],
                   ["Gabriel", WATER],
                   ["Godsworn Alexiel", EARTH],
                   ["Grand Order", LIGHT],
                   ["Grimnir", WIND],
                   ["Hades", DARK],
                   ["Halluel and Malluel", LIGHT],
                   ["Kaguya", WATER],
                   ["Lucifer", " light"],
                   ["Metatron", LIGHT],
                   ["Michael", FIRE],
                   ["Raphael", WIND],
                   ["Sariel", DARK],
                   ["Shiva", FIRE],
                   ["Titan", EARTH],
                   ["Uriel", EARTH],
                   ["Varuna", WATER],
                   ["Zepyhrus", WIND],
                   ["Zeus", LIGHT],
                   ]

summer_summon_list = [["Macula Marius (Summer)", WATER],
                      ["Rose Queen (Summer)", WIND],
                      ["Satyr (Summer)", FIRE],
                      ["Yggdrasil (Summer)", EARTH],
                      ["Athena (Summer)", FIRE],
                      ["Freyr (Summer)", EARTH],
                      ["Kaguya (Summer)", LIGHT],
                      ["Tiamat (Summer), WIND"]
                      ]

xmas_summon_list = [["Sariel (Holiday)", DARK]
                    ]

# Rates
LIMITED_RATE_UP = 0.025
SSR_RATE = 0.03
SR_RATE = 0.15
R_RATE = 0.82


class Gacha:

    def __init__(self):
        self.ssr_chara_pool = ssr_list
        self.sr_pool = sr_list
        self.r_pool = r_list
        self.draw_result = {}
        self.draw_message = []
        self.ssr_rate = SSR_RATE
        self.limited_pool = []
        self.ssr_perm_pool = ssr_list + ssr_summon_list
        self.ssr_summon_pool = ssr_summon_list + summer_summon_list + xmas_summon_list

    def set_pool(self, pools):
        """
        Set the gacha pool according to banners pools inputted
        And set the SSR rate according to banner pools inputted
        """
        self.ssr_rate = SSR_RATE
        self.limited_pool = []
        for pool in pools:
            # iterate through each banner to add to the total pool
            if pool.lower() == "valentine" or \
                    pool.lower() == "val":
                self.limited_pool += valentine_list
            elif pool.lower() == "summer" or \
                    pool.lower() == "sum":
                self.limited_pool = self.limited_pool + summer_list + summer_summon_list
            elif pool.lower() == "xmas" or \
                    pool.lower() == "christmas" or \
                    pool.lower() == "holiday":
                self.limited_pool = self.limited_pool + xmas_list + xmas_summon_list
            elif pool.lower() == "halloween" or \
                    pool.lower() == "hal":
                self.limited_pool += halloween_list
            elif pool.lower() == "leg" or \
                    pool.lower() == "legfes" or \
                    pool.lower() == "legfest":
                self.limited_pool = self.limited_pool + legfest_list + zodiac_list
                self.ssr_rate = SSR_RATE * 2
            elif pool.lower() == "flash" or \
                    pool.lower() == "flashfest" or \
                    pool.lower() == "flashfes":
                self.limited_pool = self.limited_pool + flashfest_list
                self.ssr_rate = SSR_RATE * 2
            elif pool.lower() == "all":
                self.limited_pool = self.limited_pool + flashfest_list + legfest_list + zodiac_list + \
                                summer_list + summer_summon_list + xmas_list + halloween_list + xmas_summon_list
                self.ssr_rate = SSR_RATE * 2
            elif pool.lower() == "mukku":
                self.ssr_rate = SSR_RATE * 5
            elif pool.lower() == "100" or \
                 pool.lower() == "100%":
                self.ssr_rate = 1
            else:
                self.ssr_perm_pool = self.ssr_perm_pool

    def get_single(self):
        """
        Do a single roll
        If there is limited banner, rate up for limited banner will be applied
        """
        if self.limited_pool:
            if random.random() < LIMITED_RATE_UP:
                return random.choice(list(self.limited_pool))
            elif random.random() < (self.ssr_rate - LIMITED_RATE_UP):
                return random.choice(list(self.ssr_perm_pool))
            elif random.random() < SR_RATE:
                return random.choice(list(self.sr_pool))
            else:
                return random.choice(list(self.r_pool))
        else:
            if random.random() < self.ssr_rate:
                return random.choice(list(self.ssr_perm_pool))
            elif random.random() < SR_RATE:
                return random.choice(list(self.sr_pool))
            else:
                return random.choice(list(self.r_pool))

    def get_last_draw(self):
        """
        Last draw of a 10 roll with SR and up
        """
        if self.limited_pool:
            if random.random() < LIMITED_RATE_UP:
                return random.choice(list(self.limited_pool))
            elif random.random() < (self.ssr_rate - LIMITED_RATE_UP):
                return random.choice(list(self.ssr_perm_pool))
            else:
                return random.choice(list(self.sr_pool))
        else:
            if random.random() < self.ssr_rate:
                return random.choice(list(self.ssr_perm_pool))
            else:
                return random.choice(list(self.sr_pool))

    def get_ten(self):
        """
        Do single draw 9x + 1x last draw and add them to draw_result
        Then return draw_result
        """
        self.draw_result = []
        count = 1
        for i in range(10):
            if count == 10:
                self.draw_result.append(self.get_last_draw())
            else:
                self.draw_result.append(self.get_single())
                count += 1
        return self.draw_result
