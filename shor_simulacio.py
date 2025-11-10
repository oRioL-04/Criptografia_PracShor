"""
Pràctica: Simulació de l'algorisme de Shor
Assignatura: Seguretat d'Aplicacions i Comunicacions
Universitat de Lleida

Implementació pas a pas de l'algorisme de Shor per factoritzar N = p · q
"""

import numpy as np
from math import gcd, log2, ceil
from fractions import Fraction


def crear_registre_quantic_uniforme(n):
    """
    1. Creació d'un registre quàntic uniforme
    Crea un registre quàntic de mida 2^n amb amplituds uniformes.
    
    Args:
        n: nombre de qubits
    
    Returns:
        array amb amplituds uniformes (superposició uniforme)
    """
    mida = 2**n
    amplitud = 1 / np.sqrt(mida)
    registre = np.full(mida, amplitud, dtype=complex)
    
    print(f"\n1. Registre quàntic uniforme creat:")
    print(f"   - Nombre de qubits: {n}")
    print(f"   - Mida del registre: {mida}")
    print(f"   - Amplitud de cada estat: {amplitud:.4f}")
    
    return registre


def exponenciacio_modular(registre1, a, N):
    """
    2. Entrellaçament: Exponenciació modular
    Simula l'operació quàntica que transforma |x⟩ → |x, a^x mod N⟩
    
    Args:
        registre1: registre quàntic inicial
        a: base per l'exponenciació
        N: mòdul
    
    Returns:
        taula amb parelles (x, a^x mod N)
    """
    mida = len(registre1)
    taula = []
    
    for x in range(mida):
        valor_mod = pow(a, x, N)  # Calcula a^x mod N eficientment
        taula.append((x, valor_mod))
    
    print(f"\n2. Exponenciació modular aplicada:")
    print(f"   - Funció: f(x) = {a}^x mod {N}")
    print(f"   - Primeres 10 entrades de la taula:")
    for i, (x, fx) in enumerate(taula[:10]):
        print(f"     |{x}⟩ → |{x}, {fx}⟩")
    
    return taula


def mesura_segon_registre(taula, registre1):
    """
    3. Mesura del segon registre
    Simula la mesura del segon registre i la reducció del primer.
    
    Args:
        taula: taula amb parelles (x, f(x))
        registre1: amplituds del primer registre
    
    Returns:
        valor mesurat i estats compatibles del primer registre
    """
    # Simulem la mesura: triem aleatòriament un valor del segon registre
    # basat en les probabilitats (amplituds al quadrat)
    probabilitats = np.abs(registre1)**2
    x_mesurat = np.random.choice(len(registre1), p=probabilitats)
    valor_mesurat = taula[x_mesurat][1]
    
    # Trobem tots els estats del primer registre compatibles amb el valor mesurat
    estats_compatibles = [x for x, fx in taula if fx == valor_mesurat]
    
    print(f"\n3. Mesura del segon registre:")
    print(f"   - Valor mesurat: {valor_mesurat}")
    print(f"   - Estats del primer registre compatibles: {estats_compatibles[:10]}" + 
          (f"... (total: {len(estats_compatibles)})" if len(estats_compatibles) > 10 else ""))
    
    # Normalitzem el primer registre només amb els estats compatibles
    nou_registre = np.zeros(len(registre1), dtype=complex)
    for x in estats_compatibles:
        nou_registre[x] = registre1[x]
    
    # Normalització
    norma = np.sqrt(np.sum(np.abs(nou_registre)**2))
    if norma > 0:
        nou_registre = nou_registre / norma
    
    return valor_mesurat, estats_compatibles, nou_registre


def qft(registre):
    """
    4. Aplicació de la QFT (Transformada de Fourier Quàntica)
    Simula la QFT mitjançant una FFT estàndard.
    
    Args:
        registre: registre quàntic
    
    Returns:
        registre després d'aplicar la QFT
    """
    print(f"\n4. Aplicant la Transformada de Fourier Quàntica (QFT)...")
    
    # La QFT és equivalent a la FFT normalitzada
    registre_qft = np.fft.fft(registre) / np.sqrt(len(registre))
    
    # Trobem els pics més prominents
    probabilitats = np.abs(registre_qft)**2
    pics = np.argsort(probabilitats)[-5:][::-1]
    
    print(f"   - Pics més prominents després de la QFT:")
    for pic in pics:
        print(f"     Estat |{pic}⟩: probabilitat = {probabilitats[pic]:.4f}")
    
    return registre_qft


def fraccio_continua(fase, m):
    """
    5. Càlcul del període mitjançant fraccions continues
    Aproxima fase/2^m utilitzant fraccions continues per trobar el període r.
    
    Args:
        fase: fase mesurada després de la QFT
        m: nombre de qubits
    
    Returns:
        període r aproximat
    """
    # Convertim fase/2^m a una fracció
    x = fase / (2**m)
    
    print(f"\n5. Càlcul del període amb fraccions continues:")
    print(f"   - Fase mesurada: {fase}")
    print(f"   - x = fase/2^m = {fase}/{2**m} = {x:.6f}")
    
    # Utilitzem Fraction per trobar una aproximació amb fraccions continues
    frac = Fraction(fase, 2**m).limit_denominator(1000)
    
    print(f"   - Fracció aproximada: {frac.numerator}/{frac.denominator}")
    print(f"   - Període r candidat: {frac.denominator}")
    
    return frac.denominator


def modul_quantic(a, N, n_qubits=None):
    """
    Mòdul quàntic complet que calcula el període r
    tal que a^r ≡ 1 (mod N)
    
    Args:
        a: base per l'exponenciació
        N: mòdul
        n_qubits: nombre de qubits (si None, es calcula automàticament)
    
    Returns:
        període r
    """
    if n_qubits is None:
        n_qubits = ceil(2 * log2(N))
    
    print(f"\n{'='*60}")
    print(f"MÒDUL QUÀNTIC: Cercant període r per a = {a}, N = {N}")
    print(f"{'='*60}")
    
    # Pas 1: Crear registre quàntic uniforme
    registre = crear_registre_quantic_uniforme(n_qubits)
    
    # Pas 2: Exponenciació modular (entrellaçament)
    taula = exponenciacio_modular(registre, a, N)
    
    # Pas 3: Mesura del segon registre
    valor_mesurat, estats_compatibles, registre_reduit = mesura_segon_registre(taula, registre)
    
    # Pas 4: Aplicar QFT
    registre_qft = qft(registre_reduit)
    
    # Mesura després de la QFT
    probabilitats = np.abs(registre_qft)**2
    fase_mesurada = np.random.choice(len(registre_qft), p=probabilitats)
    
    # Pas 5: Càlcul del període amb fraccions continues
    r = fraccio_continua(fase_mesurada, n_qubits)
    
    # Verificar el període
    if pow(a, r, N) == 1:
        print(f"\n   ✓ Període verificat: {a}^{r} ≡ 1 (mod {N})")
    else:
        print(f"\n   ⚠ Període no verificat, caldrà reintentar")
    
    return r


def algorisme_shor(N, intents_maxims=10):
    """
    Algoritme complet de Shor per factoritzar N.
    
    Args:
        N: enter a factoritzar (N = p · q)
        intents_maxims: nombre màxim d'intents
    
    Returns:
        tuple (p, q) amb els factors de N, o None si no es troben
    """
    print(f"\n{'#'*60}")
    print(f"ALGORISME DE SHOR: Factoritzant N = {N}")
    print(f"{'#'*60}")
    
    # Comprovacions inicials
    if N % 2 == 0:
        print(f"\n✓ N és parell! Factors trivials: 2 i {N//2}")
        return (2, N//2)
    
    for intent in range(intents_maxims):
        print(f"\n\n{'*'*60}")
        print(f"Intent #{intent + 1}")
        print(f"{'*'*60}")
        
        # Pas 1: Escollir a amb gcd(a, N) = 1
        a = np.random.randint(2, N)
        factor_comun = gcd(a, N)
        
        print(f"\nPart clàssica:")
        print(f"   - a escollit aleatòriament: {a}")
        print(f"   - gcd(a, N) = gcd({a}, {N}) = {factor_comun}")
        
        if factor_comun != 1:
            print(f"\n✓ Factor trobat per gcd: {factor_comun}")
            return (factor_comun, N // factor_comun)
        
        # Pas 2: Mòdul quàntic (cerca del període r)
        try:
            r = modul_quantic(a, N)
            
            # Pas 3: Verificar si r és útil
            print(f"\n{'='*60}")
            print(f"VERIFICACIÓ DEL PERÍODE")
            print(f"{'='*60}")
            print(f"   - Període r trobat: {r}")
            
            # Comprovar si r és parell
            if r % 2 != 0:
                print(f"   ✗ r és senar, no es pot utilitzar. Reintentant...")
                continue
            
            print(f"   ✓ r és parell")
            
            # Comprovar si a^(r/2) ≡ -1 (mod N)
            valor = pow(a, r // 2, N)
            print(f"   - a^(r/2) mod N = {a}^{r//2} mod {N} = {valor}")
            
            if valor == N - 1:
                print(f"   ✗ a^(r/2) ≡ -1 (mod N), no es pot utilitzar. Reintentant...")
                continue
            
            print(f"   ✓ a^(r/2) ≢ -1 (mod N)")
            
            # Pas 4: Calcular els factors
            print(f"\nCàlcul dels factors:")
            p = gcd(pow(a, r // 2, N) - 1, N)
            q = gcd(pow(a, r // 2, N) + 1, N)
            
            print(f"   - p = gcd(a^(r/2) - 1, N) = gcd({pow(a, r//2, N)} - 1, {N}) = {p}")
            print(f"   - q = gcd(a^(r/2) + 1, N) = gcd({pow(a, r//2, N)} + 1, {N}) = {q}")
            
            # Verificar els factors
            if p > 1 and q > 1 and p * q == N:
                print(f"\n{'='*60}")
                print(f"✓✓✓ FACTORS TROBATS! ✓✓✓")
                print(f"{'='*60}")
                print(f"   N = {N} = {p} × {q}")
                print(f"   Verificació: {p} × {q} = {p * q}")
                return (p, q)
            else:
                print(f"   ✗ Factors no vàlids. Reintentant...")
                
        except Exception as e:
            print(f"   ✗ Error durant l'execució: {e}. Reintentant...")
            continue
    
    print(f"\n✗ No s'han pogut trobar factors després de {intents_maxims} intents")
    return None


def main():
    """
    Funció principal que executa la simulació de l'algorisme de Shor.
    """
    print("\n" + "="*60)
    print("SIMULACIÓ DE L'ALGORISME DE SHOR")
    print("Pràctica: Seguretat d'Aplicacions i Comunicacions")
    print("Universitat de Lleida")
    print("="*60)
    
    # Exemple 1: Factoritzar N = 15 (cas clàssic de l'algorisme de Shor)
    N = 15
    print(f"\n\nExemple 1: Factorització de N = {N}")
    resultat = algorisme_shor(N)
    
    if resultat:
        p, q = resultat
        print(f"\n{'='*60}")
        print(f"RESULTAT FINAL")
        print(f"{'='*60}")
        print(f"N = {N}")
        print(f"Factors: p = {p}, q = {q}")
        print(f"Verificació: {p} × {q} = {p * q}")
    
    # Exemple 2: Un altre número
    print("\n\n" + "="*80)
    N = 21
    print(f"\n\nExemple 2: Factorització de N = {N}")
    resultat = algorisme_shor(N)
    
    if resultat:
        p, q = resultat
        print(f"\n{'='*60}")
        print(f"RESULTAT FINAL")
        print(f"{'='*60}")
        print(f"N = {N}")
        print(f"Factors: p = {p}, q = {q}")
        print(f"Verificació: {p} × {q} = {p * q}")


if __name__ == "__main__":
    main()
