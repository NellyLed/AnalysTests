Задача:написать программу,вычисляющую распределение предложений по числу слов и выводящую все предложения в зависимости от аргументов
запуска.Код должен работать на ОС Windows и UNIX-подобной системе.
Решение:считывается текст из файла "Метель" с помощью функции read().Она возвращает все строки файла в виде списка.   
Программа определяет новое предложение по признакам:
1) Первое слово начинается с большой буквы.
2) В начале стоит не только слово, но и некоторые знаки препинания.
3) Предложение заканчивается точкой, вопросительным знаком, восклицательным знаком или
многоточием.
4) Те же знаки препинания «.», «?», «!». «...» встречаются и в середине предложения
В переменную string записывается содержимое файла по циклу.
Специальный набор команд разделяет соседние предложения с помощью символов (в переменную pattern записывается образ разделения текста
через такие символы, как знаки препинания и наподобие(^, \ и т.д.)). Цикл обходит всю переменную string, в результате на экран
 выводится номер предложения через квадратные скобки, а после само предложение,которое записывается в массив sent[0].В этом цикле
переменная s считает предложения без знаков препинания.Символы образуются из слов, на которые делится исходное предложение с
помощью функции split.После идет подсчет предложений с одинаковым количеством слов
