# mtnport - monitor port


\_Permite monitorizar un o varios puertos y crear en un csv donde se ubicara el reporte.
\_Los campos que tendra el csv son
'uid','pid','pcpu','pmem','command','rss','port','datetime'

## Comenzando 🚀

```
git clone https://github.com/R-Livise/mntport.git
```

Mira **Despliege** para conocer como desplegar el proyecto.

### Pre-requisitos 📋

El proyecto fue creado en python 3.

Si solo quieres hacer pruebas crea un entorno virtual

```bash
virtualenv --python=python3 env

```

## Despliegue 📦

Antes de usar algun comando , crea 2 carpetas en la raiz.

```bash
mkdir reports
mkdir data

```

Para instarlo ubicate ene el proyecto y escribe el siguiente comando:


```bash
pip install .

```

Luego de intalarlo.

Tienes 2 opciones :

Añadir puertos :
```bash
mntport monitor add-port

```
Monitorear los puertos añadidos :
```bash
mntport monitor start

```

## Construido con 🛠️

- [VSCode](https://code.visualstudio.com/) - Editor de codigo.
- [Click](https://palletsprojects.com/p/click/) - Paquete de python para hacer aplicacion de consola.

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

- **Rafael Livise** - _Trabajo Inicial_ - [R-Livise](https://github.com/R-Livise)

## Licencia 📄

Este proyecto está bajo la Licencia (MIT).

⌨️ con ❤️ por [R-Livise](https://github.com/R-Livise) 😊
