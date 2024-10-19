from fake_math import divide as fake_divide
from true_math import divide as true_divide

result_fake = fake_divide(10, 0)
result_true = true_divide(10, 0)

print("Результат fake_math:", result_fake)
print("Результат true_math:", result_true)
#