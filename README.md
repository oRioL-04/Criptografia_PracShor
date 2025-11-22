# Pràctica: Simulació de l'Algorisme de Shor

**Assignatura:** Seguretat d'Aplicacions i Comunicacions  
**Grau:** Enginyeria Informàtica  
**Universitat:** Universitat de Lleida

## Objectius

- ✅ Comprendre els conceptes bàsics de la computació quàntica aplicats a la factorització
- ✅ Implementar una simulació pas a pas de l'algorisme de Shor
- ✅ Entendre la relació entre la transformada de Fourier quàntica (QFT) i el càlcul del període d'una funció modular
- ✅ Aplicar la part clàssica de l'algorisme per obtenir els factors d'un enter compost N = p · q

## Descripció

Aquest projecte implementa una simulació completa de l'algorisme de Shor per factoritzar enters compostos utilitzant conceptes de computació quàntica.

L'algorisme de Shor és capaç de factoritzar un enter N en temps polinòmic utilitzant:
- **Superposició quàntica**
- **Transformada de Fourier Quàntica (QFT)**
- **Càlcul del període** d'una funció modular f(x) = a^x mod N

## Estructura del Codi

El programa està organitzat en les següents funcions, seguint l'estructura descrita a la pràctica:

### 1. Part Clàssica

#### `algorisme_shor(N, intents_maxims=10)`
Funció principal que implementa el diagrama de flux de l'algorisme:
- Escull un valor `a` amb gcd(a, N) = 1
- Crida al mòdul quàntic per obtenir el període r
- Verifica si r és parell i si a^(r/2) ≢ -1 (mod N)
- Calcula els factors: p = gcd(a^(r/2) - 1, N) i q = gcd(a^(r/2) + 1, N)

### 2. Mòdul Quàntic

#### `modul_quantic(a, N, n_qubits=None)`
Simula el mòdul quàntic que calcula el període r tal que a^r ≡ 1 (mod N)

Implementa els 5 passos següents:

#### **Pas 1:** `crear_registre_quantic_uniforme(n)`
- Crea un registre quàntic de mida 2^n
- Inicialitza amb amplituds uniformes (superposició uniforme)
- Cada estat té amplitud 1/√(2^n)

#### **Pas 2:** `exponenciacio_modular(registre1, a, N)`
- Simula l'entrellaçament quàntic
- Transforma |x⟩ → |x, a^x mod N⟩
- Crea una taula amb totes les parelles (x, f(x))

#### **Pas 3:** `mesura_segon_registre(taula, registre1)`
- Simula la mesura del segon registre
- Troba els estats compatibles del primer registre
- Redueix i normalitza el primer registre

#### **Pas 4:** `qft(registre)`
- Aplica la Transformada de Fourier Quàntica
- Utilitza la FFT (Fast Fourier Transform) estàndard normalitzada
- Identifica els pics de probabilitat més prominents

#### **Pas 5:** `fraccio_continua(fase, m)`
- Utilitza fraccions continues per aproximar fase/2^m
- Troba el període r com a denominador de la fracció
- Verifica que a^r ≡ 1 (mod N)

## Instal·lació

### Requisits
- Python 3.8 o superior
- pip (gestor de paquets de Python)

### Instal·lació de dependències

```bash
# Crear entorn virtual (opcional però recomanat)
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate  # En Windows

# Instal·lar les llibreries necessàries
pip install numpy qiskit matplotlib
```

## Ús

### Execució bàsica

```bash
python shor_simulacio.py
```

### Exemple de sortida

```
============================================================
SIMULACIÓ DE L'ALGORISME DE SHOR
Pràctica: Seguretat d'Aplicacions i Comunicacions
Universitat de Lleida
============================================================

Exemple 1: Factorització de N = 15

############################################################
ALGORISME DE SHOR: Factoritzant N = 15
############################################################

************************************************************
Intent #1
************************************************************

Part clàssica:
   - a escollit aleatòriament: 12
   - gcd(a, N) = gcd(12, 15) = 3

✓ Factor trobat per gcd: 3

============================================================
RESULTAT FINAL
============================================================
N = 15
Factors: p = 3, q = 5
Verificació: 3 × 5 = 15
```

## Modificació del Codi

Per factoritzar altres números, modifica la funció `main()`:

```python
def main():
    # Escull el número a factoritzar
    N = 35  # Exemple: 35 = 5 × 7
    
    resultat = algorisme_shor(N)
    
    if resultat:
        p, q = resultat
        print(f"Factors de {N}: {p} × {q}")
```

## Conceptes Clau Implementats

### Computació Quàntica
- **Superposició:** Els registres quàntics poden estar en múltiples estats simultàniament
- **Entrellaçament:** La correlació entre dos registres quàntics
- **Mesura:** Col·lapsa el sistema quàntic a un estat definit

### Transformada de Fourier Quàntica (QFT)
- Equivalent quàntic de la FFT clàssica
- Permet detectar periodicitats en funcions modulars
- Clau per trobar el període r de f(x) = a^x mod N

### Fraccions Continues
- Mètode per aproximar nombres reals amb fraccions racionals
- Permet extreure el període r de la fase mesurada després de la QFT
- Aproximació: k/2^m ≈ k'/r on r és el període buscat


## Llibreries Utilitzades

- **numpy:** Càlculs numèrics i arrays
- **qiskit:** Framework de computació quàntica (IBM)
- **matplotlib:** Visualització

## Referències

1. Shor, P. W. (1997). "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer"
2. Nielsen, M. A., & Chuang, I. L. (2010). "Quantum Computation and Quantum Information"
3. Qiskit Documentation: https://qiskit.org/

