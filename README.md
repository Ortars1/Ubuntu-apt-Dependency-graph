# Ubuntu-apt-Dependency-graph
Зависимости определяются по имени пакета **ОС Ubuntu (apt)**. Для описания 
графа зависимостей используется представление Mermaid. Визуализатор должен 
выводить результат в виде сообщения об успешном выполнении и сохранять граф 
в файле формата **png**. 
Ключами командной строки задаются: 

• Путь к программе для визуализации графов. 

• Имя анализируемого пакета. 

• Путь к файлу с изображением графа зависимостей. 

• URL-адрес репозитория.

**ЗАПУСК**

Перед запуском необходимо установить дополнительные библиотеки для работы программы: **pip3 install networkx matplotlib requests**

Программа выполняется под Ubuntu, проверка работы программы проводилась с помощью WSL.

Перейдите в папку с помощью cd и запустите dependency_visualizer.py с переданными аргументами: **python3 dependency_visualizer.py --package-name bash --output-file ~/workspace/Visualizer/deps.png --repository-url http://archive.ubuntu.com/ubuntu**
Для запусков тестов: **python3 -m unittest test_dependency_visualizer.py** 
