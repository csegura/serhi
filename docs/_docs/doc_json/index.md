---    
title: Formato documentación
subtitle: Formato del archivo json que acompaña a la series
category: main
layout: default
---

Cada cuaderno debe llevar un archivo json con las documetación, con esta documetación se generará la págin web de documentación en este sitio. 

  - ___entidad___{: .blue} abreviatura del conjunto de datos (INE, REE, FOMENTO, BC)
  - ___nombre___{: .blue} nombre largo de la entidad
  - ___descripcion___{: .blue} descripción del conjunto de datos
  - ___fecha_inicio___{: .blue} fecha de inicio de los datos
  - ___fecha_fin___{: .blue} fecha final ó actual para dia actual/mes actual o año actual
  - ___periodicidad___{: .blue} diaria, mensaula, trmestral, anual; esto es importante por que hay una github action que deberia actualizar la serie con esa periodicidad
  - ___ipynb___{: .blue} nombre del archivo principal sin la extensión, el archivo csv se debe generar usando ese mismo nombre
  - ___csv___{: .blue} nombre del archivo csv si es diferente del notebook, o el notebook genera más de un archivo de datos, en cuyo caso deben existir tantos json como archivos de datos
  - ___autor___{: .blue} github account del mantenedor
  - ___enlaces_info___{: .blue} (opcional) array de urls con información relevante
  - ___indicadores___{: .blue} (minimo 1) array con los indicadores, para cada uno

    * ___nombre___{: .blue} nombre del indicador
    * ___descripcion___{: .blue} descripción del indicador
    * ___unidad___{: .blue} tipo de unidad, eur - euros, % - porcentaje, idx - index, idx_t - indice trimestral ... separar con comas si hay más de una
    * ___enlaces_info___{: .blue} (opcional) array de urls con información relevante

## Ejemplo documentación

```json
{
  "entidad": "INE",
  "nombre": "Indices precio vivienda",
  "descripcion": "El Índice de Precios Industriales (IPRI) mide la evolución mensual de los precios de los productos fabricados por la industria y vendidos en el mercado interior en la primera etapa de su comercialización. El IPRI recoge los precios de venta a salida de fábrica obtenidos por los establecimientos industriales en las transacciones que éstos efectúan, excluyendo los gastos de transporte, comercialización, IVA y otros impuestos indirectos facturados. La cobertura del índice se extiende a todos los sectores industriales, excepto la construcción. Por tanto, investiga las industrias extractivas, manufactureras y de suministro de energía eléctrica, gas y agua. Para su obtención se realiza una encuesta continua que recoge todos los meses aproximadamente 28.000 precios de unos 1.500 productos, en una muestra cercana a los 9.000 establecimientos industriales. La información que se recoge son los precios vigentes el día 15 de cada mes.",
  "fecha_inicio": "01/01/2018",
  "fecha_fin": "mes actual",
  "periodicidad": "trismestral",
  "ipynb": "ine_ipv",
  "autor": "csegura",
  "enlaces_info": [    
    "https://www.ine.es/"    
  ],
  "indicadores": [
    {
      "nombre": "General",
      "descripcion": "Indice base 100 en 1995",
      "unidad": "idx_t"
    },
    {
      "nombre": "Vivienda nueva",
      "descripcion": "",
      "unidad": "idx_t"
    },
    {
      "nombre": "Vivienda segunda mani",
      "descripcion": "",
      "unidad": "idx_t"
    }
  ]
}
```


