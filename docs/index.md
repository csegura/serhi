---
title: Series Históricas de Datos
category: main
---s

Hola!!

La idea de este repositorio es generar series de datos uniformes a partir de datos que ya están disponibles públicamente. 

### ¿como? 

Cada vez que tengo que hacer alguna exploración de datos uso un notebook de python, que es lo más cómodo. Así que esto funciona con notebooks. 

Se crea el notebook, que decarga los datos, los procesa y los guarda en el formato común para las series [Formato Series]({{ site.baseurl }}{% link _docs/doc_series/index.md %}) el archivo resultante debe ser un csv. 

Para documentar las series descargadas y que formarán parte del conjunto se crea un archivo json, este archivo servirá también para generar la documentación correspondiente en este sitio [Formato Documentación]({{ site.baseurl }}{% link _docs/doc_json/index.md %}) 

## Contribuir 

¿A que estas esperando? MD x Twitter

## Por hacer

#### Octubre 2022

- [ ] Actualizar las series automáticamente 
    - [x] acción manual
    - [ ] temporizador / github actions
    - [ ] day / week / month runners
- [x] Página con el estado de las últimas actualizaciones
- [ ] API REST para consulta
    - [ ] url/set/from_date/to_date    
- [x] Documentación
    - [x] (entity).json 
