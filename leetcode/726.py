# 726 Number of Atoms


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [[]]
        i = 0

        def parse_atom():
            """
            Parse an atom like H2 or Mg
            given i is at the start of the atom.

            Appends it to the last list on the stack
            """
            nonlocal i
            start = i
            i += 1
            while i < len(formula) and formula[i].islower():
                i += 1
            atom = formula[start:i]
            count = 0
            while i < len(formula) and formula[i].isdigit():
                count = count * 10 + int(formula[i])
                i += 1
            count = count if count else 1

            stack[-1].append((atom, count))

        def parse_group():
            """
            Parse a group like (OH)2 or (Mg)3
            Assumes i is at the start of the group symbol '('.
            Directly mutates the last list on the stack
            """
            nonlocal i
            i += 1
            stack.append([])
            while i < len(formula) and formula[i] != ")":
                if formula[i] == "(":
                    parse_group()
                else:
                    parse_atom()

            i += 1
            count = 0
            while i < len(formula) and formula[i].isdigit():
                count = count * 10 + int(formula[i])
                i += 1
            count = count if count else 1

            for atom, atom_count in stack.pop():
                stack[-1].append((atom, atom_count * count))

        while i < len(formula):
            if formula[i] == "(":
                parse_group()
            else:
                parse_atom()

        ans = {}
        for atom, count in stack[0]:
            ans[atom] = ans.get(atom, 0) + count

        # sort the atoms alphabetically
        atoms = sorted(ans.keys())
        return "".join(f"{atom}{ans[atom] if ans[atom] > 1 else ''}" for atom in atoms)
