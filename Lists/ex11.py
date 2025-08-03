# Dois vetores com 10 elementos cada;
# Terceiro vetor com 20 elementos que são fruto da intercalação dos vetores anteriores;

vector1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vector2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

"""vector3 = vector1.copy()
vector3.extend(vector2)
print(vector3)"""

# Intercalar 3 vetores de 10 elementos cada

vector4 = vector1.copy()
vector4.extend(vector1)
vector4.extend(vector2)
vector4.sort()
print(vector4)