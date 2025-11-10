# Explicació Teòrica de l'Algorisme de Shor

## Context Teòric

L'algorisme de Shor és un dels resultats més importants de la computació quàntica. Permet factoritzar un enter N en temps polinòmic utilitzant les propietats de la superposició i de la transformada de Fourier quàntica.

## Conceptes Bàsics de Computació Quàntica

### Qubits
Un qubit és la unitat bàsica d'informació quàntica. A diferència d'un bit clàssic (0 o 1), un qubit pot estar en superposició:

```
|ψ⟩ = α|0⟩ + β|1⟩
```

On α i β són nombres complexos tals que |α|² + |β|² = 1

### Superposició
Un sistema quàntic pot estar en múltiples estats simultàniament fins que es mesura. Per exemple, un registre de n qubits pot representar 2^n estats alhora.

### Entrellaçament (Entanglement)
Dos o més qubits poden estar correlacionats de manera que l'estat d'un depèn de l'estat de l'altre, independentment de la distància.

### Mesura
Quan mesurem un sistema quàntic, aquest "col·lapsa" a un dels seus estats possibles amb una probabilitat determinada per les amplituds.

## L'Algorisme de Shor: Pas a Pas

### Objectiu
Factoritzar un enter compost N = p · q en els seus factors primers p i q.

### Idea Central
El nucli de l'algorisme consisteix en trobar el període r de la funció:

```
f(x) = a^x mod N
```

on a és un enter coprimer amb N (gcd(a, N) = 1).

### Per què el període ajuda a factoritzar?

Si trobem r tal que:
```
a^r ≡ 1 (mod N)
```

I r és parell, llavors:
```
a^r - 1 ≡ 0 (mod N)
(a^(r/2))² - 1 ≡ 0 (mod N)
(a^(r/2) - 1)(a^(r/2) + 1) ≡ 0 (mod N)
```

Això significa que N divideix el producte (a^(r/2) - 1)(a^(r/2) + 1).

Si a^(r/2) ≢ -1 (mod N), llavors ni (a^(r/2) - 1) ni (a^(r/2) + 1) són divisibles per N, però el seu producte sí que ho és.

Per tant, és probable que:
- p = gcd(a^(r/2) - 1, N)
- q = gcd(a^(r/2) + 1, N)

siguin factors no trivials de N.

## Parts de l'Algorisme

### Part 1: Preparació Clàssica

1. **Escollir a aleatòriament** amb 2 ≤ a < N
2. **Calcular gcd(a, N)**
   - Si gcd(a, N) ≠ 1, hem trobat un factor!
   - Altrament, continuar

### Part 2: Mòdul Quàntic (Càlcul del Període)

#### Pas 1: Crear Registre Quàntic Uniforme
Preparar dos registres quàntics:
- Primer registre: n qubits en superposició uniforme
- Segon registre: inicialitzat a |0⟩

```
|ψ₀⟩ = 1/√(2^n) Σ(x=0 to 2^n-1) |x⟩|0⟩
```

#### Pas 2: Exponenciació Modular (Entrellaçament)
Aplicar la transformació:
```
|x⟩|0⟩ → |x⟩|a^x mod N⟩
```

Aquest pas crea entrellaçament entre els dos registres:
```
|ψ₁⟩ = 1/√(2^n) Σ(x=0 to 2^n-1) |x⟩|a^x mod N⟩
```

#### Pas 3: Mesura del Segon Registre
Mesurem el segon registre i obtenim un valor k = a^y mod N per algun y.

El primer registre col·lapsa als estats compatibles: y, y+r, y+2r, y+3r, ...

```
|ψ₂⟩ = 1/√M Σ(j=0 to M-1) |y + jr⟩
```

On M és el nombre d'estats compatibles.

#### Pas 4: Transformada de Fourier Quàntica (QFT)
La QFT transforma el registre per fer visible la periodicitat:

```
QFT|x⟩ = 1/√(2^n) Σ(k=0 to 2^n-1) e^(2πikx/2^n)|k⟩
```

Després de la QFT, els estats amb fases múltiples de 2^n/r tenen amplituds grans.

#### Pas 5: Mesura i Extracció del Període
Mesurem el primer registre i obtenim un valor m.

La probabilitat de mesurar m és alta si:
```
m ≈ k · 2^n / r
```

Per algun enter k < r.

Utilitzant **fraccions continues**, aproximem m/2^n per trobar k/r, i d'aquí obtenim r.

### Part 3: Càlcul Clàssic dels Factors

1. **Verificar que r és parell**
   - Si r és senar, tornar a començar

2. **Verificar que a^(r/2) ≢ -1 (mod N)**
   - Si a^(r/2) ≡ -1 (mod N), tornar a començar

3. **Calcular els factors**
   ```
   p = gcd(a^(r/2) - 1, N)
   q = gcd(a^(r/2) + 1, N)
   ```

4. **Verificar**
   - Si p > 1 i q > 1 i p·q = N, èxit!
   - Altrament, tornar a començar

## Exemple Numèric: Factoritzar N = 15

### Pas 1: Escollir a
Suposem a = 7. Comprovem: gcd(7, 15) = 1 ✓

### Pas 2: Trobar el període r
Calculem 7^x mod 15:
- 7¹ mod 15 = 7
- 7² mod 15 = 4
- 7³ mod 15 = 13
- 7⁴ mod 15 = 1 ← Període r = 4

### Pas 3: Verificacions
- r = 4 és parell ✓
- 7^(4/2) mod 15 = 7² mod 15 = 4 ≠ 14 ✓

### Pas 4: Calcular factors
```
p = gcd(7² - 1, 15) = gcd(48, 15) = 3
q = gcd(7² + 1, 15) = gcd(50, 15) = 5
```

### Verificació
15 = 3 × 5 ✓

## Complexitat

### Algorisme Clàssic (Trial Division)
- Complexitat: O(√N)
- Per N amb d dígits: O(10^(d/2))
- **Exponencial** en el nombre de dígits

### Algorisme de Shor
- Complexitat: O((log N)³)
- Per N amb d dígits: O(d³)
- **Polinòmica** en el nombre de dígits

### Exemple Pràctic
Per factoritzar un número de 2048 bits (usats en RSA):
- **Clàssic:** ~10^308 operacions (impossible!)
- **Shor:** ~10^12 operacions (factible en ordinador quàntic)

## Implicacions per la Criptografia

### RSA
El sistema criptogràfic RSA es basa en la dificultat de factoritzar números grans.

L'algorisme de Shor pot trencar RSA en temps polinòmic amb un ordinador quàntic suficientment gran.

### Estat Actual (2025)
- Els ordinadors quàntics actuals són massa petits
- Es poden factoritzar números petits (fins a ~100-200 bits)
- RSA amb claus de 2048-4096 bits encara és segur
- Però s'està investigant criptografia post-quàntica

## Fraccions Continues

Les fraccions continues són clau per extreure el període de la fase mesurada.

### Exemple
Si mesurem m = 192 després de la QFT amb n = 8 qubits:

```
m/2^n = 192/256 = 0.75
```

Expressem 0.75 com a fracció continua:
```
0.75 = 3/4
```

El denominador 4 és el nostre període candidat r.

### Algoritme de Fraccions Continues

Per convertir un decimal x en fracció:
1. Prendre la part entera: a₀ = ⌊x⌋
2. Si x - a₀ ≈ 0, acabar
3. Altrament, x ← 1/(x - a₀) i repetir

Per 0.75:
- a₀ = 0, x = 1/0.75 = 4/3
- a₁ = 1, x = 1/(4/3 - 1) = 3
- a₂ = 3, acabar
- Fracció: [0; 1, 3] = 0 + 1/(1 + 1/3) = 3/4

## Limitacions de la Simulació

La nostra simulació és **clàssica** i per tant:

1. **No mostra avantatge quàntic real**
   - La complexitat segueix sent exponencial
   - Un ordinador quàntic real seria polinòmica

2. **Mida limitada**
   - Només podem simular registres petits (~10-15 qubits)
   - Un ordinador quàntic podria usar centenars de qubits

3. **Aleatorietat simulada**
   - Usem números pseudoaleatoris
   - Els ordinadors quàntics tenen aleatorietat real

4. **No hi ha decoherència**
   - Els qubits reals es degraden amb el temps
   - La simulació no té aquest problema

## Referències

1. **Shor, P. W. (1997)**
   "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer"
   SIAM Journal on Computing, 26(5), 1484-1509

2. **Nielsen, M. A., & Chuang, I. L. (2010)**
   "Quantum Computation and Quantum Information"
   Cambridge University Press

3. **Ekert, A., & Jozsa, R. (1996)**
   "Quantum computation and Shor's factoring algorithm"
   Reviews of Modern Physics, 68(3), 733

4. **Qiskit Documentation**
   https://qiskit.org/textbook/ch-algorithms/shor.html

## Glossari

- **Qubit:** Bit quàntic, unitat bàsica d'informació quàntica
- **Superposició:** Estat quàntic que és combinació lineal de diversos estats base
- **Entrellaçament:** Correlació quàntica entre qubits
- **QFT:** Quantum Fourier Transform (Transformada de Fourier Quàntica)
- **Període:** Valor r tal que a^r ≡ 1 (mod N)
- **gcd:** Greatest Common Divisor (Màxim Comú Divisor)
- **Fraccions continues:** Representació d'un número com a suma de fraccions imbricades
