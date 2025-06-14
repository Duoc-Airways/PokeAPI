---
title: Changelog
layout: default
permalink: /changelog/
---

# 📜 Changelog - PokeAPI

Todas las modificaciones importantes a este proyecto se documentarán aquí.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [v1.0.0] - 2025-06-13

### 🎉 Features

- Publicación inicial de la documentación en GitHub Pages.
- Implementación de navegación con navbar (Inicio, Equipo, Tecnologías, Documentación API, Changelog).
- Mejora de diseño visual con `custom.css`.
- Estructura completa del sitio con páginas `team.md`, `tech.md`, `api.md`.

### 🐛 Fixes

- Corrección de la URL en la página de inicio (`index.md`).
- Corrección de la página 404 personalizada.

---

## [v0.3.0] - 2025-06-10

### 🎉 Features

- Implementación del `Dockerfile` para contenerización de la API.
- Integración de GitHub Actions para CI/CD básico.

### 🐛 Fixes

- Corrección de errores en la integración entre frontend y backend.
- Ajustes en el manejo de CORS en la API.

---

## [v0.2.0] - 2025-06-05

### 🎉 Features

- Implementación inicial de roles en la API (Admin, User).
- Desarrollo del FrontEnd PokeAPI con React.

---

## [v0.1.0] - 2025-05-30

### 🎉 Features

- Setup inicial del proyecto.
- Creación de la API REST con los endpoints:
  - `GET /pokemon`
  - `GET /pokemon/:id`
  - `GET /evolution/:id`
- Primeras pruebas funcionales del backend.
