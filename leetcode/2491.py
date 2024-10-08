# 2491 Divide Players Into Teams of Equal Skill
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/ - Medium


class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        # if skill is sorted, then does lowest have to be paired with largest?
        # let a < b < c < d, then if we think it's possible for a + c == b + d
        # it's not possible because if c < d then => a > b which is => <=
        # so biggest has to be paired with smallest

        if len(skill) <= 2:
            # if there's 2 players just return their chem
            return skill[0] * skill[1]

        skill.sort()
        teams = []

        i = 0
        while i < len(skill):
            first = skill[i]
            last = skill.pop()
            teams.append((first + last, first * last))  # total skill and chem

            i += 1

        # check if all skills are equal
        first_skill = teams[0][0]
        total_chem = teams[0][1]
        for skill_sum, chem in teams[1:]:
            if skill_sum != first_skill:
                return -1
            total_chem += chem

        return total_chem
