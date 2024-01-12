def exists_word(word, instance):
    result = []

    for file in instance.queue:
        if any(word in line.lower() for line in file["linhas_do_arquivo"]):
            occurrences = [
                {"linha": num}
                for num, line in enumerate(file["linhas_do_arquivo"], 1)
                if word in line.lower()
            ]

            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return result


def search_by_word(word, instance):
    result = []

    for file in instance.queue:
        occurrences = [
            {
                "linha": num,
                "conteudo": line.strip()
            }
            for num, line in enumerate(file["linhas_do_arquivo"], 1)
            if word in line.lower()
        ]

        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return result
