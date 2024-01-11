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
    if not instance:
        print("Não há elementos")
        return

    removed_file = instance.dequeue()

    if removed_file:
        print(
            f"Arquivo {removed_file['nome_do_arquivo']} "
            f"removido com sucesso"
        )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
