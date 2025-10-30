# Poetry

## Definicion 

Es una herramienta para la gention de dependencias y empaquetados en python, permite declarar las bibliotecas de tu proyecto y se encarga de instalarlas y actualizarlas.

## ¿Como usar?

Primero debemos instalar Poetry y luego utilizar los comandos en la terminal para gestionar proyectos y depencias 
#### - Comandos basicos 
 Para crear un nuevo proyecto:
 
 `poetry new nombre-del-proyecto`

 Agregar depencias:
 
 `poetry add nombre-de-la-libreria`
 
 `pyproject.toml`
 
 `poetry.lock`

 Instalar dependencias:

 `poetry install`

 Actualizar dependencias:

 `poetry update`

 Compilar el proyecto:
 
 Esto crea los archivos del paquete en una carpeta.
 
 `poetry build` 

 Ejecutar comandos dentro un entorno virtual: 

 `poetry run <comando>`

Ver la informacion del entorno virtual:

`poetry env info`

## ¿Por que usar poetry?

1. Almacenas la version de cada depencia de otras, esto facilita las complilacion repetitivas.

2. Utiliza un solucionador de depencias para resolver automaticamente conflictos entre paquetes.

3. Control de versiones.

4. Puede definir y ejecutar scripts desde la configuracion de poetry

## ¿Cuando usar Poetry?

Para los proyectos grandes que vayas a realizar:

- Proyecos compartidos o de largo plazo

- Proyectos de dependencia o empaquetar.
  
