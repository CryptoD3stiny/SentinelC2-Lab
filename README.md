# SentinelC2-Lab
# 🛡️ SentinelC2 Lab

**Automated C2 Simulation, Beacon Detection & Honeypot Framework**

SentinelC2 es un laboratorio de ciberseguridad desarrollado en Python que simula comunicación tipo Command & Control (C2), detecta patrones de beaconing y registra intentos de acceso mediante un honeypot TCP.

El proyecto está diseñado con un enfoque **defensivo**, orientado a analistas SOC, Blue Team y estudiantes de ciberseguridad.

---

## 🎯 Objetivos del Proyecto

- Simular comportamiento de malware de forma **segura y controlada**
- Detectar beaconing mediante análisis de frecuencia
- Registrar intentos de conexión sospechosos
- Automatizar la ejecución completa del laboratorio
- Generar un **reporte final unificado**, sin interacción manual

---

## 🧠 Componentes

### 1️⃣ C2 Simulator
Simula tráfico periódico tipo beacon (heartbeat) entre un cliente y un servidor C2 local.

### 2️⃣ Beacon Detector
Analiza logs y detecta comportamiento anómalo basado en número de conexiones repetitivas.

### 3️⃣ TCP Honeypot
Escucha en un puerto configurable y registra intentos de conexión entrantes.

### 4️⃣ Automated Orchestrator
Un script central (`auto_lab.py`) que:
- Lanza todos los servicios
- Simula actividad maliciosa
- Detiene el entorno
- Genera un reporte final

---

## 📁 Estructura del Proyecto

