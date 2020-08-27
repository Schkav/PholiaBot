from bisect import bisect

BOX_OPENED = [1, 4, 45, 80]  # bracket of boxes
TOTAL = [800, 1200, 1000, 2500, 2500]  # total number of items in each brackets
TOKENS_PER_DRAW = [2, 2, 2, 4, 6]  # tokens per draw in each brackets
TOKENS_REQUIRED = [1600, 8800, 90800, 440800]  # cumulative total tokens required for each box bracket


class GwBox:

    def calculate_box(self, tokens):
        """
        Calculate number of GW boxes
        you can open with input tokens
        """
        # Split tokens bracket according to TOKENS_REQUIRED
        # i.e if tokens < 1600, i = 0; if tokens < 8800, i = 1
        i = bisect(TOKENS_REQUIRED, tokens)
        if not i:  # if i = 0
            return 0, tokens
        box_rate = TOTAL[i] * TOKENS_PER_DRAW[i]  # get rate of tokens required per box based on bracket
        tokens_bracket = TOKENS_REQUIRED[i - 1]  # get total tokens required for current bracket level
        tokens_left = tokens - tokens_bracket  # get leftover tokens from current tokens - tokens_bracket
        box_in_bracket = tokens_left // box_rate  # get number of boxes from leftover tokens in current bracket
        box_count = BOX_OPENED[i - 1] + box_in_bracket  # count total number of boxes
        result = [box_count, tokens_left % box_rate]  # get box count and leftover tokens from calculate box_in_bracket
        return result


