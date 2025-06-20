#! usr/bin/env python
import argparse

from kubernetes import client, config
from kubernetes.client.models.v1_pod import V1Pod
from tabulate import tabulate
from colorama import Fore, Style

config.load_kube_config()
codev1 = client.CoreV1Api()
appv1 = client.AppsV1Api()
parser = argparse.ArgumentParser(
    description='Pegar todas as pods/imagens em todos os namespaces',
    prog='kubernetes-get-images.py'
)
parser.add_argument(
    '-n', '--namespace', help='Filtrar pods/imagens a partir de uma namespace'
)


TABLE_HEADERS = [
    f'{Fore.RED}{Style.BRIGHT}Nomes dos Pods{Style.RESET_ALL}',
    f'{Fore.GREEN}{Style.BRIGHT}Imagens{Style.RESET_ALL}',
    f'{Fore.BLUE}{Style.BRIGHT}Namespace{Style.RESET_ALL}'
]
FMT = 'double_grid'


def get_pods_all_namespaces() -> list:
    return codev1.list_pod_for_all_namespaces().items


def get_pods_namespace(namespace: str) -> list:
    return codev1.list_namespaced_pod(namespace).items

def get_images_pod(pod: V1Pod) -> list:
    return [ container.image for container in pod.spec.containers ]


def create_table (pod: V1Pod, images: list, table: list) -> list:
    return table.append([
        Fore.RED + pod.metadata.name + Style.RESET_ALL,
        Fore.GREEN + ', '.join(images) + Style.RESET_ALL,
        Fore.BLUE + pod.metadata.namespace + Style.RESET_ALL
        ] 
    )


def main():
    args = parser.parse_args()
    table = []
    if args.namespace == None:
        pod = get_pods_all_namespaces()
    else:
        pod = get_pods_namespace(args.namespace)
    for p in pod:
        images = get_images_pod(p)
        create_table(p, images, table)
    print(tabulate(table, headers=TABLE_HEADERS, tablefmt=FMT))

if __name__ == "__main__":
    main()
