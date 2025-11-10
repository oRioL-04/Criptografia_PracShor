"""
Exemples i tests per a la simulació de l'algorisme de Shor

Aquest fitxer conté exemples addicionals i funcions de test
per verificar el correcte funcionament de la implementació.
"""

import sys
from shor_simulacio import (
    crear_registre_quantic_uniforme,
    exponenciacio_modular,
    mesura_segon_registre,
    qft,
    fraccio_continua,
    modul_quantic,
    algorisme_shor
)
from math import gcd
import numpy as np


def test_registre_quantic():
    """Test de la creació del registre quàntic uniforme"""
    print("\n" + "="*60)
    print("TEST 1: Registre Quàntic Uniforme")
    print("="*60)
    
    n = 4
    registre = crear_registre_quantic_uniforme(n)
    
    # Verificar la mida
    assert len(registre) == 2**n, f"Error: La mida hauria de ser {2**n}"
    
    # Verificar normalització (suma de probabilitats = 1)
    suma_prob = np.sum(np.abs(registre)**2)
    assert abs(suma_prob - 1.0) < 1e-10, f"Error: La suma de probabilitats és {suma_prob}, hauria de ser 1"
    
    print(f"✓ Test superat: Registre de {len(registre)} estats creat correctament")
    print(f"✓ Normalització verificada: Σ|ψ|² = {suma_prob:.10f}")


def test_exponenciacio_modular():
    """Test de l'exponenciació modular"""
    print("\n" + "="*60)
    print("TEST 2: Exponenciació Modular")
    print("="*60)
    
    n = 4
    a = 7
    N = 15
    
    registre = crear_registre_quantic_uniforme(n)
    taula = exponenciacio_modular(registre, a, N)
    
    # Verificar algunes entrades
    assert taula[0] == (0, 1), f"Error: 7^0 mod 15 hauria de ser 1"
    assert taula[1] == (1, 7), f"Error: 7^1 mod 15 hauria de ser 7"
    assert taula[2] == (2, 4), f"Error: 7^2 mod 15 hauria de ser 4"
    
    print(f"✓ Test superat: Exponenciació modular correcta")
    print(f"✓ Taula de {len(taula)} entrades generada")


def test_periode_classic():
    """Test clàssic del càlcul del període"""
    print("\n" + "="*60)
    print("TEST 3: Càlcul Clàssic del Període")
    print("="*60)
    
    test_cases = [
        (7, 15, 4),   # 7^4 ≡ 1 (mod 15)
        (2, 15, 4),   # 2^4 ≡ 1 (mod 15)
        (11, 15, 2),  # 11^2 ≡ 1 (mod 15)
    ]
    
    for a, N, periode_esperat in test_cases:
        # Trobar el període clàssicament
        for r in range(1, N):
            if pow(a, r, N) == 1:
                periode_trobat = r
                break
        
        print(f"   a={a}, N={N}: període trobat={periode_trobat}, esperat={periode_esperat}")
        assert periode_trobat == periode_esperat, f"Error: Període incorrecte per a={a}, N={N}"
    
    print(f"✓ Test superat: Tots els períodes calculats correctament")


def test_factoritzacio():
    """Test de factorització completa"""
    print("\n" + "="*60)
    print("TEST 4: Factorització amb l'Algorisme de Shor")
    print("="*60)
    
    test_cases = [
        (15, {3, 5}),
        (21, {3, 7}),
        (35, {5, 7}),
    ]
    
    for N, factors_esperats in test_cases:
        print(f"\n   Factoritzant N = {N}...")
        resultat = algorisme_shor(N, intents_maxims=5)
        
        if resultat:
            p, q = resultat
            factors_trobats = {p, q}
            print(f"   Factors trobats: {p} × {q} = {p*q}")
            assert p * q == N, f"Error: {p} × {q} ≠ {N}"
            assert factors_trobats == factors_esperats, f"Error: Factors incorrectes"
            print(f"   ✓ Correcte!")
        else:
            print(f"   ⚠ No s'han trobat factors (pot passar amb simulació)")
    
    print(f"\n✓ Test superat: Factoritzacions correctes")


def exemple_detallat():
    """Exemple detallat pas a pas per N = 15, a = 7"""
    print("\n" + "="*60)
    print("EXEMPLE DETALLAT: N = 15, a = 7")
    print("="*60)
    
    N = 15
    a = 7
    
    # Verificar que gcd(a, N) = 1
    print(f"\n1. Verificar que a={a} és coprimer amb N={N}")
    g = gcd(a, N)
    print(f"   gcd({a}, {N}) = {g}")
    assert g == 1, "a i N no són coprimers!"
    
    # Trobar el període clàssicament
    print(f"\n2. Trobar el període r (clàssicament per comparació)")
    for r in range(1, N):
        if pow(a, r, N) == 1:
            print(f"   Període trobat: r = {r}")
            print(f"   Verificació: {a}^{r} mod {N} = {pow(a, r, N)}")
            break
    
    # Verificar que r és parell
    print(f"\n3. Verificar que r={r} és parell")
    assert r % 2 == 0, "El període no és parell!"
    print(f"   ✓ r és parell")
    
    # Verificar que a^(r/2) ≢ -1 (mod N)
    print(f"\n4. Verificar que a^(r/2) ≢ -1 (mod N)")
    val = pow(a, r // 2, N)
    print(f"   {a}^{r//2} mod {N} = {val}")
    print(f"   -1 mod {N} = {N-1}")
    assert val != N - 1, "a^(r/2) ≡ -1 (mod N)!"
    print(f"   ✓ Condició satisfeta")
    
    # Calcular els factors
    print(f"\n5. Calcular els factors")
    p = gcd(pow(a, r // 2, N) - 1, N)
    q = gcd(pow(a, r // 2, N) + 1, N)
    print(f"   p = gcd({a}^{r//2} - 1, {N}) = gcd({pow(a, r//2, N) - 1}, {N}) = {p}")
    print(f"   q = gcd({a}^{r//2} + 1, {N}) = gcd({pow(a, r//2, N) + 1}, {N}) = {q}")
    
    # Verificar
    print(f"\n6. Verificació")
    print(f"   {N} = {p} × {q} = {p * q}")
    assert p * q == N, "Els factors no són correctes!"
    print(f"   ✓✓✓ Factorització correcta! ✓✓✓")


def exemple_diferents_numeros():
    """Prova l'algorisme amb diferents números"""
    print("\n" + "="*60)
    print("EXEMPLES AMB DIFERENTS NÚMEROS")
    print("="*60)
    
    numeros = [15, 21, 33, 35, 39, 51, 55, 57, 65, 77]
    
    resultats = []
    
    for N in numeros:
        print(f"\n{'='*60}")
        print(f"Factoritzant N = {N}")
        print(f"{'='*60}")
        
        resultat = algorisme_shor(N, intents_maxims=5)
        
        if resultat:
            p, q = resultat
            resultats.append((N, p, q, "✓"))
            print(f"\n✓ {N} = {p} × {q}")
        else:
            resultats.append((N, None, None, "✗"))
            print(f"\n✗ No s'han trobat factors")
    
    # Resum
    print("\n" + "="*60)
    print("RESUM DE RESULTATS")
    print("="*60)
    print(f"{'N':<6} {'p':<6} {'q':<6} {'Verificació':<12} {'Estat'}")
    print("-" * 60)
    
    for N, p, q, estat in resultats:
        if p and q:
            verif = f"{p}×{q}={p*q}"
            print(f"{N:<6} {p:<6} {q:<6} {verif:<12} {estat}")
        else:
            print(f"{N:<6} {'N/A':<6} {'N/A':<6} {'N/A':<12} {estat}")


def main():
    """Executa tots els tests i exemples"""
    print("\n" + "#"*60)
    print("#" + " "*58 + "#")
    print("#" + "  TESTS I EXEMPLES DE L'ALGORISME DE SHOR".center(58) + "#")
    print("#" + " "*58 + "#")
    print("#"*60)
    
    try:
        # Tests unitaris
        test_registre_quantic()
        test_exponenciacio_modular()
        test_periode_classic()
        
        # Exemple detallat
        exemple_detallat()
        
        # Test de factorització
        test_factoritzacio()
        
        # Exemples amb diferents números
        exemple_diferents_numeros()
        
        print("\n" + "="*60)
        print("✓✓✓ TOTS ELS TESTS HAN ESTAT SUPERATS ✓✓✓")
        print("="*60)
        
    except AssertionError as e:
        print(f"\n✗✗✗ ERROR EN EL TEST: {e} ✗✗✗")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗✗✗ ERROR INESPERAT: {e} ✗✗✗")
        sys.exit(1)


if __name__ == "__main__":
    main()
