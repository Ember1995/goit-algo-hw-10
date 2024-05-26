import pulp

model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Змінні
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість Лимонаду
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')  # Кількість Фруктового соку

# Цільова функція (максимізація)
model += lemonade + fruit_juice, "Total Production"

# Обмеження
model += 2 * lemonade + 1 * fruit_juice <= 100  # Вода
model += 1 * lemonade <= 50  # Цукор
model += 1 * lemonade <= 30  # Лимонний сік
model += 2 * fruit_juice <= 40  # Фруктове пюре

# Розв'язання
model.solve()

# Вивід
print("Максимально можлива кількість продуктів 'Лимонад':", lemonade.varValue)
print("Максимально можлива кількість продуктів 'Фруктовий сік':", fruit_juice.varValue)
