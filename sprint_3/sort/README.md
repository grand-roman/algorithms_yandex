# A. Пузырек

Чтобы выбрать самый лучший алгоритм для решения задачи, Гоша взялся изучать разные сортировки. На очереди - сортировка пузырьком.
Алгоритм следующий (сортируем по возрастанию):
На каждом шаге проходим по массиву поочередно сравниваем пары соседних элементов. Если элемент на позиции i больше элемента на позиции i+1, меняем их местами. После первой итерации самый большой элемент окажется в конце массива.
Проходим по массиву, выполняя указанные действия n - 1 раз, или до тех пор, пока на очередной итерации не окажется, что обмены больше не нужны, то есть массив уже отсортирован.
Помогите Гоше написать код алгоритма.

# B. Сортировка вставками

Теперь Гоша взялся за сортировку вставками.
Алгоритм следующий: На i-том шаге мы делаем так, чтобы первые i элементов массива шли в возрастающем порядке.
1) На первом шаге ничего делать не нужно — один элемент и так "отсортирован".
2) На втором шаге нужно сделать так, чтобы два первых элемента были верно отсортированы. То есть если второй элемент оказался меньше первого, их нужно поменять местами.
3) На i-том шаге мы знаем, что первые i-1 элементов уже отсортированы. Ищем, куда нужно вставить i-ый элемент.
Для этого, начиная с позиции j = i - 1, сравниваем текущий элемент с элементом на позиции j. Пока j+1-й элемент больше j-ого и j > 0, меняем элементы местами и уменьшаем счётчик j на 1. Таким образом, стоявший на позиции i элемент будет перемещаться к своей правильной позиции.

# C. Эффективная быстрая сортировка

Рита захотела оптимизировать алгоритм быстрой сортировки. Алгоритму не должно требоваться O(n) дополнительной памяти. А у вас получится?

# D. Тараканьи бега

Сегодня 31 апреля, и в Удотинске по традиции проводятся тараканьи бега. Забеги разделены на две категории. Если таракан участвовал в забеге одной из категорий, он не может принимать участие в забегах другой категории. Но встречаются нарушители! Помогите судьям их выявить и восстановить справедливость.
Есть два списка со стартовыми номерами тараканов. Нужно вывести номера, которые встречаются и в первом, и во втором списке. Квадратичный алгоритм не подойдет для этой задачи. Тараканы разбегутся, пока алгоритм закончит работу.
Формат ввода

В первой строке записано число n - длина первого списка. Во второй строке - число m - длина второго списка. Оба числа не превосходят 10000 В следующих двух строках через пробел могут быть записаны два списка соответствующей длины, состоящие из чисел, не превосходящих 10000.
Формат вывода

Нужно в строку вывести стартовые номера тараканов в порядке, в котором они встречались в первом списке.

Пример 1

Ввод
3
5
4 9 5
9 4 9 8 4
Вывод
4 9

Пример 2

Ввод
3
8
7 8 10
9 7 5 3 6 6 4 1
Вывод
7

### Примечания

Нужно выводить только уникальные стартовые номера.


# E. Бессовестные тараканы

На этот раз нужно определить стартовые номера тараканов с учетом того, в скольких именно забегах первой и второй категории одновременно они участвовали. То есть, если таракан со стартовым номером 1 участвовал в двух забегах первой категории, и в трех забегах второй категории, то номер 1 в ответе должен встречаться два раза.
Формат ввода

В первой строке записано число n - длина первого списка. Во второй строке - число m - длина второго списка. Оба числа не превосходят 10000 В следующих двух строках через пробел записаны два списка соответствующей длины, состоящие из чисел, не превосходящих 10000.
Формат вывода

Нужно в строку вывести стартовые номера тараканов с учетом того, как они записаны в первом списке.

Пример 1

Ввод
5
7
4 9 5 2 2
9 4 9 8 4 2 2
Вывод
4 9 2 2

# F. Сортировка по четности

Кондратий издал новый закон. Во всех списках четные числа должны стоять на четных позициях, а нечетные числа - на нечетных. Уже существующие списки придется пересортировать. В списках, которые вам достанутся, одинаковое количество четных и нечетных элементов. Нужно отсортировать его в соответствии с новым законом. Исходный порядок внутри групп четных и нечетных элементов менять нельзя.


# G. Периметр треугольника

Перед сном Рита решила поиграть в игру на телефоне. Дан массив целых чисел, в котором каждый элемент обозначает длину стороны треугольника. Нужно определить максимально возможный периметр треугольника, составленного из сторон с длинами из заданного массива. Помогите Рите скорее закончить игру и пойти спать.
Напомним, что из трёх отрезков с длинами a ≤ b ≤ c можно составить треугольник, если выполнено неравенство треугольника: c < a + b
Разберём пример: длины сторон равны 6, 3, 3, 2.
Допустим, что в качестве наибольшей стороны можно выбрать 6. Тогда максимальная сумма двух других сторон, исходя из нашего набора, равна 6, так как остались только 3, 3, 2. Неравенство треугольника не может выполняться.
Оставшиеся три отрезка уже образуют треугольник со сторонами 3, 3, 2. Неравенство выполняется: 3 < 3 + 2.
Во втором примере подойдут стороны 8, 7, 5. Проверим неравенство: 8 < 7 + 5 = 12. В данном случае нам повезло: эти три элемента уже наибольшие в массиве, поэтому другие комбинации можно не рассматривать.
Формат ввода

В первой строке записано n — целое число, не превосходящее 10000. Во второй строке записаны n неотрицательных целых чисел, каждое из которых не превосходит 10000.
Формат вывода

Нужно вывести наибольший периметр треугольника, который возможно составить из сторон с заданными длинами.

Пример 1

Ввод
4
6 3 3 2
Вывод
8

Пример 2

Ввод
6
5 3 7 2 8 3
Вывод
20


# H. Клумбы

Евлампия захотела, чтобы у нее под окном были клумбы с одуванчиками. Для работ по подготовке земельного участка под клумбы было нанято n садовников. 
Каждый из садовников обрабатывал какой-то участок земли. Процесс был организован не очень хорошо, иногда один и тот же участок, или часть участка мог быть обработан сразу несколькими садовниками. Обработанный участок любого размера становился клумбой. В клумбе не могло быть необработанных промежутков. 
Нужно определить границы получившихся клумб.
Формат ввода

В первой строке задано количество садовников - n. Число садовников не превосходит 1000 В следующих n строках через пробел записаны координаты участков в формате: 
start end Оба числа целые, неотрицательные, и не превосходят 1000. start не может быть больше, чем end
Формат вывода

Нужно вывести в отдельной строке координаты каждой из получившихся клумб.
Данные должны выводится в отсортированном порядке.

Пример 1

Ввод
5
7 8
7 8
2 2
2 3
6 10
Вывод
2 3
6 10

Пример 2

Ввод
5
2 3
5 5
2 2
3 4
3 4
Вывод
2 4
5 5


# I. Гардероб

Евлампия решила оставить у себя в гардеробе вещи только трех цветов: розового, желтого, и малинового. Она захотела отсортировать одежду по цветам. Сначала должны идти вещи розового цвета, далее - желтого, и в конце - малинового. Помогите Евлампии навести порядок в гардеробе.

# J. Относительная сортировка

Кондратий ввел новый метод сортировки - Относительная сортировка.
Идея метода следующая. С помощью образца - массива уникальных чисел, задается порядок. В соответствии с этим порядком и должны сортироваться числа. 
Но метод еще требует доработки. Пока не известно, как сортировать числа, которые не входят в образец. Так что такие числа нужно выводить в конце в соответствии со стандартной сортировкой.

Ввод
10
2 4 3 5 6 0 9 8 7 7
6
2 4 3 5 6 0
Вывод
2 4 3 5 6 0 7 7 8 9


# K. Частичная сортировка

После того, как Гоша узнал про сортировку слиянием и быструю сортировку, он решил придумать свой метод сортировки, который предполагал бы разделение данных на части.
Назвал он свою сортировку Частичной. 
Этим методом можно отсортировать n уникальных чисел a1, a2, … , an, находящихся в диапазоне от 0 до n - 1. 
Алгоритм сортировки состоит из трёх шагов:
Разбить исходную последовательность на k блоков B1, …, Bk. Блоки могут иметь разные размеры. Если размер блока i равен si, то B1 ={ a1, …, as1 }, B2 = { as1 + 1, … , as1 + s2 } и так далее.
Отсортировать каждый из блоков.
Объединить блоки — записать сначала отсортированный блок B1, потом B2, … , Bk
Частичная сортировка лучше обычной в том случае, если в первом пункте у нас получится разбить последовательность на большое число блоков. Однако далеко не каждое такое разбиение подходит. Определите максимальное число блоков, на которое можно разбить исходную последовательность, чтобы сортировка отработала корректно.
Рассмотрим пример: a = [3, 2, 0, 1, 4, 6, 5].
Минимальный размер первого блока B1 равен 4. Если взять лишь первые два элемента, то отсортированная последовательность будет начинаться с двойки, что неправильно. Если взять первые три элемента, то последовательность будет начинаться с нуля, но после него сразу же пойдёт двойка. Первые четыре элемента уже гарантируют корректный префикс после объединения блоков. Четвёрку можно взять как самостоятельный блок из одного элемента. Последние два элемента надо объединить в третий блок. Таким образом:
B1 = { 3, 2, 0, 1 } 
B2 = { 4 } 
B3 = { 6, 5 } 
В данном примере ответ равен 3. Максимальное число блоков равно трём.

Пример 1

Ввод
4
0 1 3 2
Вывод
3

Пример 2

Ввод
8
3 6 7 4 1 5 0 2
Вывод
1

Пример 3

Ввод
5
1 0 2 3 4
Вывод
4


# M. Самое длинное подслово

Евлампия стала подозревать, что Кондратий отец пытается читать её сообщения и письма. 
Она приказала разработать новую систему шифрования. Дано зашифрованное слово и список слов. Для того, чтобы узнать, какое слово зашифровано, нужно в списке найти самое длинное слово, которое является подсловом (подпоследовательностью) зашифрованного слова. Если таких слов более одного, нужно вывести лексикографически минимальное из них.

Пример 1

Ввод
abpcplea
4
ale
apple
monkey
plea
Вывод
apple

Пример 2

Ввод
abpcplea
3
a
b
c
Вывод
a



# N. Техника скорочтения

Евлампия решила научится технике скорочтения, чтобы успевать читать все выпуски любимых журналов. 
Она узнала, что в основе многих техник, позволяющий быстро читать, лежит идея просматривать текст по диагонали. 
Евлампия решила, что если будет чаще иметь дело с данными, которые упорядочены по диагонали, быстрее освоит технику скорочтения.
В своем дневнике она хранит зашифрованные в виде числовых матриц записи. Нужно отсортировать матрицы по диагонали.

Пример 1

Ввод	
3
4
3 3 1 1
2 2 1 2
1 1 1 2
Вывод
1 1 1 1
1 2 2 2
1 2 3 3

Пример 2

Ввод
3
2
10 6
5 0
8 10
Вывод
0 6
5 10
8 10