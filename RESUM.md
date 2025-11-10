# RESUM DE LA PRÀCTICA

## Implementació de l'Algorisme de Shor

**Assignatura:** Seguretat d'Aplicacions i Comunicacions  
**Universitat:** Universitat de Lleida

---

## Fitxers Inclosos

### 1. `shor_simulacio.py` (Principal)
Implementació completa de l'algorisme de Shor seguint l'estructura del PDF de la pràctica:

- **Funcions del mòdul quàntic:**
  - `crear_registre_quantic_uniforme(n)` - Pas 1: Registre quàntic uniforme
  - `exponenciacio_modular(registre, a, N)` - Pas 2: Entrellaçament
  - `mesura_segon_registre(taula, registre)` - Pas 3: Mesura i col·lapse
  - `qft(registre)` - Pas 4: Transformada de Fourier Quàntica
  - `fraccio_continua(fase, m)` - Pas 5: Extracció del període

- **Funcions de l'algorisme complet:**
  - `modul_quantic(a, N)` - Simulació completa del mòdul quàntic
  - `algorisme_shor(N)` - Algorisme complet amb part clàssica i quàntica

### 2. `exemples_tests.py`
Tests unitaris i exemples d'ús:
- Tests de cada component individual
- Exemple detallat pas a pas per N=15
- Factorització de múltiples números
- Verificació de correctesa

### 3. `visualitzacio.py`
Eines de visualització i anàlisi:
- Gràfics de funcions modulars
- Anàlisi de períodes
- Comparació de mètodes de factorització
- Tutorial interactiu

### 4. Documentació
- `README.md` - Documentació general del projecte
- `TEORIA.md` - Explicació teòrica detallada
- `requirements.txt` - Dependències de Python

---

## Execució Ràpida

### Instal·lació
```bash
# Crear entorn virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac

# Instal·lar dependències
pip install -r requirements.txt
```

### Ús Bàsic
```bash
# Executar la simulació principal
python shor_simulacio.py

# Executar tots els tests
python exemples_tests.py

# Generar visualitzacions
python visualitzacio.py
```

---

## Resultats Obtinguts

### Exemples de Factorització

| N  | Factors | Temps (aprox.) | Intents |
|----|---------|----------------|---------|
| 15 | 3 × 5   | < 1s          | 1-2     |
| 21 | 3 × 7   | < 1s          | 1-3     |
| 33 | 3 × 11  | < 2s          | 1-4     |
| 35 | 5 × 7   | < 2s          | 1-4     |

*Nota: Els temps i intents varien degut a la naturalesa probabilística de l'algorisme.*

---

## Estructura del Codi

L'implementació segueix exactament l'estructura descrita a la pràctica:

```
┌─────────────────────────────────────────────┐
│         ALGORISME DE SHOR                   │
└─────────────────────────────────────────────┘
                    │
    ┌───────────────┴───────────────┐
    │                               │
┌───▼─────────────┐      ┌──────────▼─────────┐
│  PART CLÀSSICA  │      │   MÒDUL QUÀNTIC    │
│                 │      │                    │
│ • Escollir a    │      │ 1. Registre        │
│ • Verificar gcd │      │ 2. Exponenciació   │
│ • Comprovar r   │      │ 3. Mesura          │
│ • Calcular gcd  │◄─────┤ 4. QFT             │
│                 │  r   │ 5. Fraccions       │
└─────────────────┘      └────────────────────┘
        │
        ▼
┌─────────────────┐
│    FACTORS      │
│    p × q = N    │
└─────────────────┘
```

---

## Conceptes Clau Implementats

### Computació Quàntica
✓ **Superposició**: Registres quàntics amb múltiples estats simultanis  
✓ **Entrellaçament**: Correlació entre dos registres quàntics  
✓ **Mesura**: Col·lapse del sistema quàntic a un estat definit  

### Transformada de Fourier Quàntica
✓ Implementada utilitzant FFT normalitzada  
✓ Permet detectar periodicitats en funcions modulars  
✓ Clau per trobar el període r de f(x) = aˣ mod N  

### Fraccions Continues
✓ Aproximació de fase/2ⁿ → k/r  
✓ Extracció del període r del denominador  
✓ Utilitzant `Fraction.limit_denominator()`  

---

## Verificació i Tests

### Tests Implementats
1. ✓ Test de creació de registre quàntic uniforme
2. ✓ Test d'exponenciació modular
3. ✓ Test de càlcul clàssic del període
4. ✓ Test de factorització completa

### Exemples Verificats
- ✓ N = 15 → Factors: 3 × 5
- ✓ N = 21 → Factors: 3 × 7
- ✓ N = 35 → Factors: 5 × 7
- ✓ N = 33 → Factors: 3 × 11

Tots els tests passen correctament i les factoritzacions són vàlides.

---

## Llibreries Utilitzades

| Llibreria | Versió | Ús |
|-----------|--------|-----|
| numpy | ≥1.24 | Càlculs numèrics, FFT |
| qiskit | ≥0.45 | Framework de computació quàntica |
| matplotlib | ≥3.7 | Visualització de dades |

---

## Limitacions i Notes

### Limitacions de la Simulació
⚠️ **Simulació clàssica**: Aquest codi simula un algorisme quàntic utilitzant mètodes clàssics.

- La complexitat temporal és **exponencial** en la simulació
- Un ordinador quàntic real seria **polinòmica**
- Només podem simular registres petits (~10-15 qubits)
- Un ordinador quàntic podria usar centenars de qubits

### Naturalesa Probabilística
L'algorisme de Shor és probabilístic:
- Pot requerir múltiples intents
- Cada intent té una probabilitat de trobar factors
- El codi reintenta automàticament fins a trobar-los

---

## Compliment dels Objectius

### ✓ Objectius Assolits

1. ✅ **Comprendre conceptes de computació quàntica**: Implementació completa de superposició, entrellaçament i mesura

2. ✅ **Implementar simulació pas a pas**: Cada pas del PDF està implementat com a funció independent

3. ✅ **Entendre QFT i càlcul del període**: QFT implementada amb FFT i fraccions continues per extreure r

4. ✅ **Aplicar part clàssica**: Diagrama de flux del PDF implementat exactament

---

## Extensions Possibles

### Millores Implementades
- ✓ Visualització de funcions modulars
- ✓ Anàlisi comparativa de mètodes
- ✓ Tests exhaustius
- ✓ Documentació completa

### Millores Futures
- [ ] Implementació amb circuits quàntics reals (IBM Quantum)
- [ ] Optimització per a números més grans
- [ ] Interfície gràfica interactiva
- [ ] Comparació de rendiment amb altres algorismes

---

## Referències i Recursos

### Bibliografia
1. Shor, P. W. (1997). "Polynomial-Time Algorithms for Prime Factorization"
2. Nielsen & Chuang (2010). "Quantum Computation and Quantum Information"
3. Qiskit Documentation: https://qiskit.org/

### Recursos Adicionals
- IBM Quantum Experience: https://quantum-computing.ibm.com/
- Qiskit Textbook: https://qiskit.org/textbook/
- Microsoft Quantum: https://azure.microsoft.com/en-us/products/quantum/

---

## Contacte i Suport

**Pràctica realitzada per:**  
Assignatura de Seguretat d'Aplicacions i Comunicacions  
Universitat de Lleida

**Data:** Novembre 2025

---

## Llicència

Aquest codi s'ha desenvolupat amb finalitats educatives per a la pràctica de l'assignatura.

---

## Conclusió

Aquesta implementació proporciona una simulació completa i funcional de l'algorisme de Shor, seguint fidelment l'estructura i requisits especificats al PDF de la pràctica. El codi inclou:

- ✓ Totes les funcions requerides
- ✓ Documentació exhaustiva
- ✓ Tests i verificacions
- ✓ Exemples d'ús
- ✓ Visualitzacions
- ✓ Explicacions teòriques

El projecte està llest per ser executat, provat i presentat.
