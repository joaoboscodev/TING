from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    lines = txt_importer(path_file)

    if lines is not None:
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }

    if result in instance.queue:
        return None

    instance.enqueue(result)
    print(result)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
