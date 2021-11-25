alha = []
yes = []
try:
    '''Ввод количества критериев'''
    koeff = int(input("Введите колличество критериев пожалуйсто: "))
    '''Создание матрицы с единичной диагональю и ввод значений под диагональю матрицы'''
    matrex = [[0 for a in range(koeff)] for o in range(koeff)]
    for a in range(koeff):
        for o in range(koeff):
            if a == o:
                matrex[a][o] = 1
            elif a - o > -1:
                matrex[a][o] = int(
                    input('Введите данные попарного сравнения критериев ' + str(o + 1) + " и " + str(a + 1)
                          + " : "))
                if (matrex[a][o] < 1 or matrex[a][o] > 9):
                    quit("Ошибка! Шкала сравнения включает в себя числа от 1 до 9! Перезапустите программу!")
                matrex[o][a] = matrex[a][o]

    count = 1
    gif = 0
    gaf = 1
    yes_summ = 0
    for m in range(koeff):
        for p in range(koeff):
            if p < gaf:
                count = count * matrex[gif][p]
            else:
                count = count * (1 / matrex[gif][p])
                '''Заполнение над диагональю матрицы зеркально числами'''
        alha.append(count)
        '''Произведения всех чисел одной строки'''
        yes.append(pow(alha[m], 1 / koeff))
        '''Корни произведений всех чисел одной строки'''
        yes_summ += yes[m]
        '''Сумма корней произведений всех чисел одной строки'''
        count = 1
        gif += 1
        gaf += 1
    for p in range(koeff):
        '''Вывод весовых коэффициентов для всех критериев'''
        print("Весовой коэффициент для " + str(p + 1) + "-го критерия: " + str(round((yes[p] / yes_summ), 2)))
except ValueError:
    quit("Ошибка! Перезапустите программу!")
