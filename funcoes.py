def import_users(caminho="users.txt"):
    try:
        with open(caminho, "r") as f:
            return [linha.strip() for linha in f if linha.strip()]
    except FileNotFoundError:
        return []


def c_tar(caminho="tar.txt"):
    tar = []
    try:
        with open(caminho, "r") as f:
            for linha in f:
                part = linha.strip().split("|")
                if len(part) >= 3:
                    tar.append({
                        "usuario": part[0],
                        "descricao": part[1],
                        "prioridade": part[2]
                    })
    except FileNotFoundError:
        pass
    return tar


def fil_tar_p_user(tar, user):
    return [t for t in tar if t["usuario"] == user]
