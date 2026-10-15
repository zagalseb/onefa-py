# onefa-py

Cargadores de datos de la ONEFA (Liga Mayor) para Python.
Los datos viven en [`onefa-data`](https://github.com/zagalseb/onefa-data).

## Instalar

```bash
pip install git+https://github.com/zagalseb/onefa-py
```

En Colab, en la primera celda:

```python
!pip install -q git+https://github.com/zagalseb/onefa-py
```

## Usar

```python
from onefa import load_onefa_teams

teams = load_onefa_teams()
teams[["id", "nombre_corto", "abreviatura", "color_primario"]].head()
```

## Funciones

| Funcion | Devuelve |
|---|---|
| `load_onefa_teams()` | DataFrame con los equipos (una fila por equipo) |

Las siguientes (calendario, rosters, jugadas) se agregan con el mismo patron.

## Actualizar a la ultima version

```bash
pip install --upgrade --force-reinstall git+https://github.com/zagalseb/onefa-py
```

Los datos se leen de GitHub cada vez que corres la funcion, asi que un cambio en `onefa-data` aparece sin reinstalar el paquete (GitHub puede tardar unos minutos en refrescar su cache).
