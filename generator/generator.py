class Generator:
    def generate(self, rows: int) -> list[list[int]]:
        """ The generator code should go here """
        if rows == 0:
            return []
        elif rows == 1:
            return [[1]]
        else:
            new_row = [1]
            result = self.generate(rows-1)
            last_row = result[-1]
            for i in range(len(last_row)-1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row += [1]
            result.append(new_row)
        return result