# ÍNDEX DEL PROJECTE

## Pràctica: Simulació de l'Algorisme de Shor
**Universitat de Lleida - Seguretat d'Aplicacions i Comunicacions**

---

## 📁 Estructura del Projecte

```
Practica_Simulacio_Shor/
│
├── 📄 PracticaShor.pdf                  # Enunciat original de la pràctica
│
├── 🐍 ARXIUS PYTHON (Codi Font)
│   ├── shor_simulacio.py                # ⭐ PRINCIPAL - Implementació completa
│   ├── exemples_tests.py                # Tests i verificació
│   ├── visualitzacio.py                 # Visualitzacions i anàlisi
│   └── demo.py                          # Demostració ràpida
│
├── 📚 DOCUMENTACIÓ
│   ├── README.md                        # Guia general del projecte
│   ├── TEORIA.md                        # Explicació teòrica detallada
│   ├── RESUM.md                         # Resum executiu
│   ├── INSTRUCCIONS.md                  # Instruccions d'execució
│   └── INDEX.md                         # Aquest document
│
├── 📊 VISUALITZACIONS (generats automàticament)
│   ├── funcio_modular_a7_N15.png        # Gràfic de f(x) = 7^x mod 15
│   ├── funcio_modular_a2_N15.png        # Gràfic de f(x) = 2^x mod 15
│   ├── funcio_modular_a11_N21.png       # Gràfic de f(x) = 11^x mod 21
│   └── funcio_modular_a13_N35.png       # Gràfic de f(x) = 13^x mod 35
│
├── ⚙️ CONFIGURACIÓ
│   ├── requirements.txt                 # Dependències de Python
│   └── venv/                            # Entorn virtual (no cal lliurar)
│
└── 🗑️ ALTRES
    └── __pycache__/                     # Cache de Python (no cal lliurar)
```

---

## 📄 Descripció Detallada dels Arxius

### 🐍 Arxius Python

#### `shor_simulacio.py` ⭐ (PRINCIPAL)
**Descripció:** Implementació completa de l'algorisme de Shor  
**Línies de codi:** ~290  
**Funcions principals:**
- `crear_registre_quantic_uniforme(n)` - Pas 1 del mòdul quàntic
- `exponenciacio_modular(registre, a, N)` - Pas 2 del mòdul quàntic
- `mesura_segon_registre(taula, registre)` - Pas 3 del mòdul quàntic
- `qft(registre)` - Pas 4: Transformada de Fourier Quàntica
- `fraccio_continua(fase, m)` - Pas 5: Extracció del període
- `modul_quantic(a, N)` - Mòdul quàntic complet
- `algorisme_shor(N)` - Algorisme complet amb part clàssica

**Com executar:**
```bash
python shor_simulacio.py
```

---

#### `exemples_tests.py`
**Descripció:** Tests unitaris i exemples d'ús  
**Línies de codi:** ~250  
**Tests inclosos:**
- Test de registre quàntic uniforme
- Test d'exponenciació modular
- Test de càlcul clàssic del període
- Test de factorització completa
- Exemple detallat pas a pas (N=15)
- Factorització de múltiples números

**Com executar:**
```bash
python exemples_tests.py
```

**Sortida esperada:**
```
✓ Tots els tests han estat superats
```

---

#### `visualitzacio.py`
**Descripció:** Eines de visualització i anàlisi  
**Línies de codi:** ~280  
**Funcions principals:**
- `visualitzar_registre()` - Gràfics d'amplituds i probabilitats
- `visualitzar_funcio_modular()` - Gràfics de periodicitat
- `analisi_periode()` - Anàlisi de períodes per diferents 'a'
- `taula_exponenciacio_modular()` - Taules detallades
- `comparar_metodes_factoritzacio()` - Comparació Trial Division vs Shor
- `tutorial_interactiu()` - Tutorial pas a pas

**Com executar:**
```bash
python visualitzacio.py
```

**Genera:** Gràfics PNG de funcions modulars

---

#### `demo.py`
**Descripció:** Demostració ràpida i senzilla  
**Línies de codi:** ~40  
**Números factoritzats:** 15, 21, 35

**Com executar:**
```bash
python demo.py
```

**Temps d'execució:** 10-30 segons

---

### 📚 Documentació

#### `README.md`
**Contingut:**
- Descripció general del projecte
- Objectius de la pràctica
- Estructura del codi
- Instruccions d'instal·lació
- Guia d'ús
- Exemples de sortida
- Explicació dels conceptes implementats
- Referències bibliogràfiques

**Longitud:** ~250 línies

---

#### `TEORIA.md`
**Contingut:**
- Context teòric de l'algorisme de Shor
- Conceptes de computació quàntica (qubits, superposició, entrellaçament)
- Explicació matemàtica detallada
- Exemple numèric complet (N=15)
- Complexitat algorítmica
- Implicacions per la criptografia
- Fraccions continues
- Limitacions de la simulació
- Glossari de termes
- Referències acadèmiques

**Longitud:** ~400 línies

---

#### `RESUM.md`
**Contingut:**
- Resum executiu del projecte
- Llista de fitxers i descripció
- Instruccions d'execució ràpida
- Taula de resultats obtinguts
- Estructura del codi (diagrama)
- Conceptes clau implementats
- Tests realitzats
- Compliment dels objectius
- Extensions possibles
- Conclusió

**Longitud:** ~200 línies

---

#### `INSTRUCCIONS.md`
**Contingut:**
- Guia pas a pas d'instal·lació
- Instruccions d'execució detallades
- Resultats esperats
- Com modificar el codi
- Checklist de funcionalitats
- Solució de problemes comuns
- Verificació final abans de lliurar
- Format de lliurament
- Rúbrica d'autoevaluació

**Longitud:** ~250 línies

---

#### `INDEX.md` (aquest document)
**Contingut:**
- Índex complet del projecte
- Descripció de cada arxiu
- Mapa de navegació
- Guia ràpida de referència

---

### ⚙️ Configuració

#### `requirements.txt`
**Contingut:**
```
numpy>=1.24.0
qiskit>=0.45.0
matplotlib>=3.7.0
jupyter>=1.0.0
ipykernel>=6.25.0
```

**Instal·lació:**
```bash
pip install -r requirements.txt
```

---

## 🗺️ Mapa de Navegació

### Per començar ràpidament:
1. Llegir `INSTRUCCIONS.md`
2. Executar `python demo.py`

### Per entendre la teoria:
1. Llegir `TEORIA.md`
2. Revisar exemples a `exemples_tests.py`

### Per modificar el codi:
1. Obrir `shor_simulacio.py`
2. Consultar comentaris en el codi
3. Provar amb `python demo.py`

### Per veure visualitzacions:
1. Executar `python visualitzacio.py`
2. Obrir els PNG generats

### Per verificar el funcionament:
1. Executar `python exemples_tests.py`
2. Comprovar que tots els tests passen

---

## 📊 Estadístiques del Projecte

| Mètrica | Valor |
|---------|-------|
| Arxius Python | 4 |
| Línies de codi total | ~860 |
| Arxius de documentació | 5 |
| Línies de documentació | ~1100 |
| Funcions implementades | 15+ |
| Tests implementats | 7+ |
| Números factoritzats amb èxit | 10+ |
| Gràfics generats | 4+ |

---

## ✅ Checklist de Completitud

### Implementació
- [x] Pas 1: Registre quàntic uniforme
- [x] Pas 2: Exponenciació modular
- [x] Pas 3: Mesura del segon registre
- [x] Pas 4: Transformada de Fourier Quàntica
- [x] Pas 5: Fraccions continues
- [x] Mòdul quàntic complet
- [x] Part clàssica de l'algorisme
- [x] Verificacions i comprovacions

### Documentació
- [x] README general
- [x] Explicació teòrica
- [x] Instruccions d'ús
- [x] Resum executiu
- [x] Comentaris en el codi
- [x] Índex del projecte

### Tests i Verificació
- [x] Tests unitaris
- [x] Tests d'integració
- [x] Exemples d'ús
- [x] Verificació de resultats
- [x] Demo ràpida

### Extras
- [x] Visualitzacions
- [x] Anàlisi comparativa
- [x] Tutorial interactiu
- [x] Solució de problemes
- [x] Rúbrica d'avaluació

---

## 🎯 Guia de Lectura Recomanada

### Per a Comprensió Ràpida (15 minuts)
1. `RESUM.md` - Resum executiu
2. `demo.py` - Executar demostració
3. `INSTRUCCIONS.md` - Secció "Resultats Esperats"

### Per a Comprensió Completa (1 hora)
1. `TEORIA.md` - Llegir la teoria
2. `README.md` - Llegir la documentació
3. `shor_simulacio.py` - Revisar el codi
4. `exemples_tests.py` - Executar i revisar tests

### Per a Modificació i Experimentació (2 hores)
1. Tot l'anterior
2. `visualitzacio.py` - Experimentar amb visualitzacions
3. Modificar paràmetres i provar nous números
4. Generar gràfics personalitzats

---

## 🔗 Referències Creuades

### Si vols saber sobre...

**Teoria de l'algorisme:**
- Veure: `TEORIA.md`, secció "Context Teòric"
- Codi: `shor_simulacio.py`, comentaris de les funcions

**Com funciona la QFT:**
- Veure: `TEORIA.md`, secció "Transformada de Fourier Quàntica"
- Codi: `shor_simulacio.py`, funció `qft()`

**Fraccions continues:**
- Veure: `TEORIA.md`, secció "Fraccions Continues"
- Codi: `shor_simulacio.py`, funció `fraccio_continua()`

**Exemples pràctics:**
- Veure: `RESUM.md`, secció "Resultats Obtinguts"
- Executar: `demo.py` o `exemples_tests.py`

**Visualitzacions:**
- Veure: Gràfics PNG generats
- Executar: `visualitzacio.py`
- Codi: Funcions `visualitzar_*`

**Solució d'errors:**
- Veure: `INSTRUCCIONS.md`, secció "Solució de Problemes"

---

## 📞 On Trobar Ajuda

| Problema | On Buscar |
|----------|-----------|
| Conceptes teòrics | `TEORIA.md` |
| Instal·lació | `INSTRUCCIONS.md` |
| Ús del codi | `README.md` |
| Errors | `INSTRUCCIONS.md` → "Solució de Problemes" |
| Exemples | `exemples_tests.py` |
| Modificació | Comentaris en `shor_simulacio.py` |

---

## 🎓 Conclusió

Aquest projecte conté una implementació completa, documentada i verificada de l'algorisme de Shor segons les especificacions de la pràctica.

**Tot està llest per ser executat, provat i lliurat.**

---

**Document generat:** Novembre 2025  
**Última actualització:** Novembre 2025  
**Estat del projecte:** ✅ COMPLET
