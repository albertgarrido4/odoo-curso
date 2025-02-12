# 🏫 Módulo: Curso

Este repositorio contiene un módulo de Odoo llamado **Curso**, cuyo objetivo es servir como ejemplo (o punto de partida) para desarrollos personalizados dentro de la plataforma Odoo.

---

## 📁 Estructura de Carpetas

- **`__init__.py`**  

  📌 Indica a Python que esta carpeta es un módulo. Aquí puedes importar tus submódulos (por ejemplo, `models`, `controllers`, etc.).

- **`__manifest__.py`**  

  📌 Archivo de metadatos del módulo (nombre, resumen, versión, autor, dependencias, etc.).  

  - Aquí defines las dependencias de otros módulos que tu módulo necesita para funcionar.

- **`models/`**  

  📌 Carpeta donde se definen los modelos de datos (clases Python) que representan la lógica de negocio (por ejemplo, modelos que extiendan `res.partner`).

- **`controllers/`**  

  📌 Carpeta donde defines tus controladores web (endpoints) si tu módulo ofrece servicios, páginas web personalizadas, etc.

- **`security/`** *(opcional)*  

  📌 Contiene los archivos de reglas de acceso, grupos de usuarios y permisos (`ir.model.access.csv`, archivos `.xml` para roles, etc.).

- **`views/`**  

  📌 Carpeta con las vistas XML (formularios, listas, acciones, menús, etc.). Aquí defines cómo se mostrarán tus modelos en la interfaz de Odoo.

- **`data/`** *(opcional)*  

  📌 Archivos XML/CSV con datos iniciales (registros predeterminados, configuraciones básicas, etc.).

- **`static/`** *(opcional)*  

  📌 Recursos estáticos (imágenes, CSS, JS) utilizados por tu módulo.

---

## ⚙️ Requisitos Previos

- Tener una instancia de Odoo (versión 12, 18, etc., según el caso) en funcionamiento.  

- Acceso a la carpeta de `addons` donde se copiará o se encuentra este módulo.

---

## 🚀 Instalación

1\. Copia o clona la carpeta `Curso` (o el nombre de tu módulo) dentro de la ruta de `addons` de tu instancia de Odoo.  

   - Por ejemplo:

     ```

     C:\Program Files\Odoo 18.0.20250115\server\odoo\addons\Curso

     ```

2\. Asegúrate de que el usuario de Odoo tenga los permisos adecuados sobre la carpeta y sus archivos.  

3\. Reinicia tu servidor de Odoo (o el servicio de Windows, en caso de que esté instalado así).  

4\. Inicia sesión en Odoo como administrador y ve a **Aplicaciones / Apps**.  

5\. Haz clic en **Actualizar lista de aplicaciones** (o en "Actualizar" si estás en modo desarrollador).  

6\. Busca el módulo llamado **Curso** y haz clic en **Instalar**.

---

## 🧭 Uso

- Una vez instalado, si el módulo define nuevos menús, podrás encontrarlos en la interfaz principal de Odoo.  

- En caso de que extienda modelos existentes (por ejemplo, `res.partner`), verás los campos añadidos al formulario de Clientes o al menú correspondiente.

---

## 🧩 Personalización

- Ajusta el archivo `__manifest__.py` para reflejar tu información (versión, autor, licencia, dependencias de otros módulos, etc.).  

- Agrega o modifica modelos en `models/` según tu lógica de negocio.  

- Agrega vistas en `views/` para mostrar tus datos en formularios, vistas listas, kanban, etc.

---


## 📮 Soporte y Contacto

- **Autor**: Albert Garrido  

---

> Este **README.md** sirve como guía general y puede ser ampliado en el futuro.
