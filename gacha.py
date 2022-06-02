import csv
import random


with open('perm_chara_list.csv') as csv_file:  # Open csv file
    perm_reader = csv.reader(csv_file)  # Read csv file
    next(perm_reader, None)  # Skip first line
    ssr_list = list(perm_reader)  # Convert read csv into list type

with open('flash_chara_list.csv') as csv_file:
    flash_reader = csv.reader(csv_file)
    next(flash_reader, None)
    flashfest_list = list(flash_reader)

with open('leg_chara_list.csv') as csv_file:
    leg_reader = csv.reader(csv_file)
    next(leg_reader, None)
    legfest_list = list(leg_reader)

with open('zodiac_list.csv') as csv_file:
    zodiac_reader = csv.reader(csv_file)
    next(zodiac_reader, None)
    zodiac_list = list(zodiac_reader)

with open('valentine_list.csv') as csv_file:
    valentine_reader = csv.reader(csv_file)
    next(valentine_reader, None)
    valentine_list = list(valentine_reader)

with open('summer_chara_list.csv') as csv_file:
    summer_reader = csv.reader(csv_file)
    next(summer_reader, None)
    summer_list = list(summer_reader)

with open('halloween_chara_list.csv') as csv_file:
    halloween_reader = csv.reader(csv_file)
    next(halloween_reader, None)
    halloween_list = list(halloween_reader)

with open('xmas_chara_list.csv') as csv_file:
    xmas_reader = csv.reader(csv_file)
    next(xmas_reader, None)
    xmas_list = list(xmas_reader)

with open('sr_list.csv') as csv_file:
    sr_reader = csv.reader(csv_file)
    next(sr_reader, None)
    sr_list = []
    for row in sr_reader:
        sr_list.append(row[0])

with open('r_list.csv') as csv_file:
    r_reader = csv.reader(csv_file)
    next(r_reader, None)
    r_list = []
    for row in r_reader:
        r_list.append(row[0])


with open('perm_summon_list.csv') as csv_file:
    perm_summon_reader = csv.reader(csv_file)
    next(perm_summon_reader, None)
    ssr_summon_list = list(perm_summon_reader)

# Limited summons are listed in double as the rollspark command use the second value of list
with open('summer_summon_list.csv') as csv_file:
    summer_summon_reader = csv.reader(csv_file)
    next(summer_summon_reader, None)
    summer_summon_list = list(summer_summon_reader)

with open('xmas_summon_list.csv') as csv_file:
    xmas_summon_reader = csv.reader(csv_file)
    next(xmas_summon_reader, None)
    xmas_summon_list = list(xmas_summon_reader)


# Rates
LIMITED_RATE_UP = 0.015
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
                return random.choice(self.ssr_perm_pool)
            elif random.random() < SR_RATE:
                return random.choice(self.sr_pool)
            else:
                return random.choice(self.r_pool)

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

    def get_spark(self):
        """
        Do get_ten 30x and return ssr list
        """
        self.draw_results = []
        self.draw_result = []
        for i in range(30):
            self.draw_results.append(self.get_ten())  # Result is a list of list
        # Convert list of list into a single list
        self.draw_result = [item for sublist in self.draw_results for item in sublist]
        '''
        for sublist in self.draw_results:
            for item in sublist:
                self.draw_result.append(item)
        '''
        # Filter item in list by SSR only
        ssr_result = [ssr for ssr in self.draw_result if ssr in self.ssr_perm_pool or ssr in self.limited_pool]
        return ssr_result
