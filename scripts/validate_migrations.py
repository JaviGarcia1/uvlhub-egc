import os
import re


def validate_migrations():
    base_dir = "migrations/versions"
    files = [f for f in os.listdir(base_dir) if f.endswith(".py")]

    revision_map = {}
    no_revise_files = []

    for file in files:
        path = os.path.join(base_dir, file)
        with open(path, "r") as f:
            content = f.read()

        # Extraer revision
        revision = re.search(r"revision\s*=\s*'([\w\d]+)'", content)
        if not revision:
            raise ValueError(f"Archivo {file} no contiene 'revision'")

        revision_id = revision.group(1)

        # Extraer down_revision, permitiendo tuplas o None
        revises = re.search(r"down_revision\s*=\s*'([\w\d, ]*)'", content)
        if revises:
            down_revision_str = revises.group(1).strip()
            print(f"Procesando archivo: {file} - down_revision_str: {down_revision_str}")  # Depuración

            # Si no hay 'down_revision' o está vacío, debe ser None
            if down_revision_str:
                # Convertir en una tupla
                down_revision = tuple(down_revision_str.replace(" ", "").split(','))
                print(f"down_revision (tupla): {down_revision}")  # Depuración
            else:
                down_revision = None
        else:
            down_revision = None

        revision_map[revision_id] = down_revision

        if down_revision is None:
            no_revise_files.append(file)

    # Validar que solo un archivo no tiene "down_revision"
    if len(no_revise_files) != 1:
        raise ValueError(f"Debe haber exactamente un archivo sin down_revision. Encontrados: {no_revise_files}")

    # Validar que las revisiones estén conectadas en una cadena continua
    visited = set()
    current = list(revision_map.keys())[0]  # Iniciar desde el primer archivo

    while current:
        if current in visited:
            raise ValueError("Se ha detectado un bucle en las referencias de revisiones.")
        visited.add(current)

        # Obtener el siguiente archivo de la cadena de migraciones
        next_revision = revision_map.get(current)

        # Depuración: mostrar el valor actual y la referencia siguiente
        print(f"Procesando revisión: {current} -> next_revision: {next_revision}")

        # Si next_revision es una tupla, tomamos la primera revisión
        if isinstance(next_revision, tuple):
            current = next_revision[0]  # Solo tomamos la primera revisión como referencia
        else:
            current = next_revision

    # Verificar que todas las revisiones están conectadas
    if len(visited) != len(revision_map):
        raise ValueError("Las revisiones no forman una cadena continua.")

    print("Validación completada con éxito.")


if __name__ == "__main__":
    validate_migrations()
