import argparse
import subprocess
import networkx as nx
import matplotlib.pyplot as plt
import requests

def get_package_dependencies(package_name):
    """Функция для получения зависимостей пакета через WSL."""
    print(f"Получаем зависимости для пакета: {package_name}")
    try:
        output = subprocess.check_output(['sh', '-c', f'apt-cache depends {package_name}'], universal_newlines=True)
        dependencies = []
        for line in output.split('\n'):
            if line.strip().startswith('Depends:'):
                dependencies.append(line.split(':')[1].strip())
        return dependencies
    except subprocess.CalledProcessError as e:
        print(e.output)
        return []

def build_dependency_graph(package_name, graph=None, visited=None):
    """Функция для построения графа зависимостей."""
    print(f"Строим граф для пакета: {package_name}")
    if graph is None:
        graph = nx.DiGraph()
    if visited is None:
        visited = set()

    if package_name in visited:
        return graph

    visited.add(package_name)
    dependencies = get_package_dependencies(package_name)
    for dependency in dependencies:
        graph.add_edge(package_name, dependency)
        build_dependency_graph(dependency, graph, visited)

    return graph

def save_graph(graph, output_path):
    """Функция для сохранения графа в PNG файл."""
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(12, 12))
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=3000, edge_color='#BBBBBB', font_size=10, font_weight='bold')
    plt.savefig(output_path)
    plt.close()

def main():
    parser = argparse.ArgumentParser(description='Визуализатор графа зависимостей пакетов Ubuntu.')
    parser.add_argument('--package-name', required=True, help='Имя анализируемого пакета.')
    parser.add_argument('--output-file', required=True, help='Путь к файлу с изображением графа зависимостей.')
    parser.add_argument('--repository-url', required=True, help='URL-адрес репозитория.')

    args = parser.parse_args()

    # Проверка URL репозитория
    try:
        response = requests.get(args.repository_url)
        if response.status_code != 200:
            print("Невозможно подключиться к репозиторию.")
            return
    except requests.RequestException as e:
        print(f"Ошибка при подключении к репозиторию: {e}")
        return

    graph = build_dependency_graph(args.package_name)
    save_graph(graph, args.output_file)

    print("Граф зависимостей успешно создан и сохранён в файл:", args.output_file)

if __name__ == '__main__':
    main()
