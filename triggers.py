# Triggers class

class Triggers:

    def get_triggers(self, raid_name):
        if raid_name.lower() == "ubhl" or\
           raid_name.lower() == "ultimate bahamut impossible":
            trigger = """```
If any ally has Target
    Reginleiv
        Multi-hit, random element damage to random allies. Inflicts Strong Armed.
95% Trigger
    Daedalus Wing
        10000 static Wind damage to all allies.
        Gains Uplifted.
85% Trigger
    Deadly Flare
        Multi-hit Fire damage to random allies. Last hit deals massive Fire damage.
        Inflicts Collapsed and Burned.
        Removes all buffs on all allies.
80% Trigger
    Fills all charge diamonds
75% Trigger
    Virtuous Verse
        Earth damage to one ally.
        Switches up to two random frontline allies with backline allies (will not switch the main character).
        Removes all buffs on all allies.
70% Trigger
    The Rage
        Light damage to all allies.
        Gains Purging Light.
        Removes two debuffs from Ultimate Bahamut.
55% Trigger
    Deadly Flare
50% Trigger
    Sirius (Plain Damage)
        4-hit Plain Damage (30% of max HP) to random allies.
        Removes all buffs on all allies.
45% Trigger
    Sirius (multi-element). Charge diamonds do not reset.
40% Trigger
    Sirius (plain damage). Charge diamonds do not reset.
35% Trigger
    Sirius (multi-element). Charge diamonds do not reset.
30% Trigger
    Removes all debuffs on Ultimate Bahamut.
    Removes all buffs on all allies.
28% Trigger
    Fills all charge diamonds.
22% Trigger
    Casts Ultima Blast
        Massive Water damage to all allies.
        Removes all buffs on all allies.
15% Trigger
    Skyfall Ultimus
        999,999 Dark damage to all allies.
        Gains Ruination Ray and Purging Light.
        Inflicts Summonless.
10% Trigger
    Cosmic Collision
        Multi-hit plain damage and multi-element damage to random allies.
        Removes all buffs on all allies.
        Removes all debuffs on Ultimate Bahamut.
        Inflicts Summonless.
5% Trigger
    Deadly Flare (Dark).
        10,000 Dark damage to all allies.
        Gains Ruination Ray.
1% Trigger
    Cosmic Collision.
```"""
            return trigger
