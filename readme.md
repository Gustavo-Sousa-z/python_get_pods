
---

# kubernetes-get-images.py

Um utilitário de linha de comando para listar **pods e suas imagens Docker** em um cluster Kubernetes. O script suporta listagem global (todos os namespaces) ou filtragem por namespace específico.

## 📋 Descrição

Este script em Python utiliza a API oficial do Kubernetes para recuperar informações de pods e imagens associadas, exibindo os dados em uma tabela colorida e legível no terminal.

---

## 🚀 Requisitos

- Python 3.6+
- Acesso a um cluster Kubernetes via `kubeconfig`
- Permissões suficientes para listar pods nos namespaces desejados

---

## 🧰 Instalação

Clone este repositório ou copie o script diretamente, e instale as dependências:

```bash

pip install -r requirements.txt

```

---

## ⚙️ Uso

```bash
python kubernetes-get-images.py [-n NAMESPACE]
```

### Argumentos:

| Argumento           | Descrição                                                                                     |
| ------------------- | --------------------------------------------------------------------------------------------- |
| `-n`, `--namespace` | (Opcional) Filtra os pods por um namespace específico. Se omitido, busca todos os namespaces. |

---

## 🖼️ Exemplo de Saída

```text
╔═════════════════════╦═════════════════════════════════════════════╦══════════════╗
║ Nomes dos Pods      ║ Imagens                                     ║ Namespace    ║
╠═════════════════════╬═════════════════════════════════════════════╬══════════════╣
║ my-pod-123          ║ nginx:latest                                ║ default      ║
║ backend-app-456     ║ myapp/backend:v1.2                          ║ production   ║
╚═════════════════════╩═════════════════════════════════════════════╩══════════════╝
```

---

## 🧪 Exemplo de Execução

Listar **todos os pods de todos os namespaces**:

```bash
python kubernetes-get-images.py
```

Listar **somente os pods do namespace `dev`**:

```bash
python kubernetes-get-images.py -n dev
```

---

## 📦 Estrutura do Código

* **Funções principais**:

  * `get_pods_all_namespaces()`: Retorna todos os pods do cluster.
  * `get_pods_namespace(namespace)`: Retorna os pods de um namespace específico.
  * `get_images_pod(pod)`: Extrai a(s) imagem(ns) de um pod.
  * `create_table(pod, images, table)`: Adiciona uma linha à tabela com dados do pod.

---

## 📌 Notas

* O script usa `colorama` para destacar visualmente os dados na saída.
* A biblioteca `tabulate` é usada para formatação elegante da tabela no terminal.

---
