import unicodedata

# 1. Dicionário de conversão (Alfabeto Galáctico)
alfabeto_galatico = {
    'a': 'ᔑ', 
    'b': 'ʖ', 
    'c': 'ᓵ', 
    'd': '↸', 
    'e': 'ᒷ', 
    'f': '⎓', 
    'g': '⊣', 
    'h': '⍑', 
    'i': '╎', 
    'j': '⋮', 
    'k': 'ꖌ', 
    'l': 'ꖎ', 
    'm': 'ᒲ', 
    'n': 'リ', 
    'o': '𝙹', 
    'p': '!¡', 
    'q': 'ᑑ', 
    'r': '∷', 
    's': 'ᓭ', 
    't': 'ℸ',
    'u': '⚍',
    'v': '⍊',
    'w': '∴',
    'x': '̇/',
    'y': 'ǁ',
    'z': '⨅'
}

def limpar_texto(texto):
    """Remove acentos e cedilhas e converte para minúsculas."""
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_limpo = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return texto_limpo.lower()

def traduzir_para_minecraft(frase):
    """Limpa a frase e aplica os caracteres galácticos."""
    frase_limpa = limpar_texto(frase)
    frase_traduzida = ""
    for letra in frase_limpa:
        frase_traduzida += alfabeto_galatico.get(letra, letra)
    return frase_traduzida

if __name__ == "__main__":
    frase_original = input()
    
    resultado = traduzir_para_minecraft(frase_original)
    
    nome_ficheiro = "traducao.txt"
    
    with open(nome_ficheiro, "w", encoding="utf-8") as ficheiro:
        ficheiro.write(f"{resultado}\n")
    
    print(f"\n ➡ '{nome_ficheiro}'")