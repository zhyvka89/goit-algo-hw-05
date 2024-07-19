
import timeit

from _boyer_moore import boyer_moore_search
from _kmp import kmp_search
from _rabin_karp import rabin_karp_search


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def main():
  
  file1_path = 'C:\\Users\\Comp100\\Downloads\\стаття 11.txt'
  file2_path = 'C:\\Users\\Comp100\\Downloads\\стаття 22.txt'

  text1 = read_file(file1_path)
  text2 = read_file(file2_path)

  real_pattern_text1 = "Пошук стрибками, цей алгоритм від двійкового пошуку відрізняється рухом виключно вперед"
  real_pattern_text2 = "Для прискорення пошуку окремих елементів у розгорнутому списку після заповнення блоку можна відсортувати його елементи"
  fake_pattern = "Чоловік попросив жінку зав’язати вороні ноги хусточкою ноги, а в хусточці були гроші"

  # Вимірюємо час для алгоритмів стаття 11
  boyer_moore_time_text1_real = timeit.timeit(lambda: boyer_moore_search(text1, real_pattern_text1), number=100)
  boyer_moore_time_text1_fake = timeit.timeit(lambda: boyer_moore_search(text1, fake_pattern), number=100)

  kmp_time_text1_real = timeit.timeit(lambda: kmp_search(text1, real_pattern_text1), number=100)
  kmp_time_text1_fake = timeit.timeit(lambda: kmp_search(text1, fake_pattern), number=100)

  rabin_karp_time_text1_real = timeit.timeit(lambda: rabin_karp_search(text1, real_pattern_text1), number=100)
  rabin_karp_time_text1_fake = timeit.timeit(lambda: rabin_karp_search(text1, fake_pattern), number=100)

  print("Час виконання на статті 11:")
  print(f"Боєра-Мура (існуючий підрядок): {boyer_moore_time_text1_real} сек")
  print(f"Боєра-Мура (вигаданий підрядок): {boyer_moore_time_text1_fake} сек\n")
  print(f"Кнута-Морріса-Пратта (існуючий підрядок): {kmp_time_text1_real} сек")
  print(f"Кнута-Морріса-Пратта (вигаданий підрядок): {kmp_time_text1_fake} сек\n")
  print(f"Рабіна-Карпа (існуючий підрядок): {rabin_karp_time_text1_real} сек")
  print(f"Рабіна-Карпа (вигаданий підрядок): {rabin_karp_time_text1_fake} сек\n")

  # Вимірюємо час для алгоритмів стаття 22
  boyer_moore_time_text2_real = timeit.timeit(lambda: boyer_moore_search(text2, real_pattern_text2), number=100)
  boyer_moore_time_text2_fake = timeit.timeit(lambda: boyer_moore_search(text2, fake_pattern), number=100)

  kmp_time_text2_real = timeit.timeit(lambda: kmp_search(text2, real_pattern_text2), number=100)
  kmp_time_text2_fake = timeit.timeit(lambda: kmp_search(text2, fake_pattern), number=100)

  rabin_karp_time_text2_real = timeit.timeit(lambda: rabin_karp_search(text2, real_pattern_text2), number=100)
  rabin_karp_time_text2_fake = timeit.timeit(lambda: rabin_karp_search(text2, fake_pattern), number=100)

  print("Час виконання на статті 22:")
  print(f"Боєра-Мура (існуючий підрядок): {boyer_moore_time_text2_real} сек")
  print(f"Боєра-Мура (вигаданий підрядок): {boyer_moore_time_text2_fake} сек\n")
  print(f"Кнута-Морріса-Пратта (існуючий підрядок): {kmp_time_text2_real} сек")
  print(f"Кнута-Морріса-Пратта (вигаданий підрядок): {kmp_time_text2_fake} сек\n")
  print(f"Рабіна-Карпа (існуючий підрядок): {rabin_karp_time_text2_real} сек")
  print(f"Рабіна-Карпа (вигаданий підрядок): {rabin_karp_time_text2_fake} сек\n")


if __name__ == "__main__":
  main()


"""
На основі наданих даних про час виконання алгоритмів для пошуку підрядків можна зробити наступні висновки:

1. Боєра-Мура:
   - Час виконання для існуючого підрядка на статті 11: 0.00625 сек, на статті 22: 0.00695 сек.
   - Час виконання для вигаданого підрядка на статті 11: 0.00709 сек, на статті 22: 0.00923 сек.
   - Загальною тенденцією є стабільна швидкість виконання, що свідчить про консистентність алгоритму незалежно від тексту.

2. Кнута-Морріса-Пратта (kmp):
   - Час виконання для існуючого підрядка на статті 11: 0.14686 сек, на статті 22: 0.21453 сек.
   - Час виконання для вигаданого підрядка на статті 11: 0.14650 сек, на статті 22: 0.21002 сек.
   - Зауважимо, що KMP показує значні коливання в часі виконання в залежності від тексту, що може бути пов'язано з його внутрішніми механізмами знаходження підрядка.

3. Рабіна-Карпа:
   - Час виконання для існуючого підрядка на статті 11: 0.33794 сек, на статті 22: 0.49686 сек.
   - Час виконання для вигаданого підрядка на статті 11: 0.34632 сек, на статті 22: 0.48490 сек.
   - Rabin-Karp показує найбільший час виконання серед усіх трьох алгоритмів, що свідчить про його меншу ефективність порівняно з Boyer-Moore і KMP.

Загальний висновок:
Алгоритми Боєра-Мура і Кнута-Морріса-Пратта виявляються швидшими в більшості випадків порівняно з алгоритмом Рабіна-Карпа.
Серед Боєра-Мура і Кнута-Морріса-Пратта, Боєр-Мур показує більш стабільну швидкість виконання незалежно від конкретного тексту.
Кнут-Морріс-Пратт, хоча і може бути дуже швидким у деяких випадках, виявляється менш консистентним у своїй швидкості порівняно з Боєр-Муром.

"""