# Torre de Control

App de menú que concentra el acceso a todas tus herramientas (Walmart, C&A,
Santory/ZOY, Liverpool) en una sola pantalla, con un botón "Abrir" por cada una.

## Desplegarla (mismo flujo que tus otras apps)

1. Crea un repo nuevo en GitHub (`naga690512-ops`), por ejemplo `torre-control`.
2. Sube `app.py` y `requirements.txt` a la raíz del repo.
3. En share.streamlit.io → "New app" → selecciona el repo → `app.py` como
   archivo principal → Deploy.
4. Te da una URL pública, igual que tus otras apps.

## Para tener acceso de un toque en el iPhone

1. Abre la URL de esta app en Safari (no en la app de Claude).
2. Toca el ícono de Compartir → "Agregar a pantalla de inicio".
3. Te queda un ícono en tu pantalla que abre directo este menú — de ahí,
   un toque más abre cada app.

## Pendiente

Faltan 3 ligas por completar en `app.py` (quedaron con `"url": ""`):
- Packing List Surtido (Santory/ZOY)
- Carta de Acceso CEDIS (Liverpool)
- Carta de Recolección de Equipo (Liverpool)

Mándame esas 3 ligas y te dejo el archivo actualizado.
