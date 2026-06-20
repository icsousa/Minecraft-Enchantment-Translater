# **`⛏️✨ Minecraft Enchantment Translator`** 

Um script em Python que traduz frases normais para o **Standard Galactic Alphabet (SGA)**, a linguagem clássica utilizada na Mesa de Encantamentos do Minecraft.

## 🌟 Funcionalidades

* **Suporte para Português:** Remove automaticamente acentos e cedilhas através da normalização do texto (ex: `Maçã Mágica` é lido e convertido sem erros).
* **Mapeamento Unicode:** Utiliza os caracteres Unicode correspondentes para desenhar os símbolos exatos do jogo.
* **Geração de Ficheiros:** Guarda automaticamente o resultado final num ficheiro `traducao.txt` com a codificação correta (`UTF-8`).

## 🚀 Como Utilizar

1. Certifica-te de que tens o **Python 3** instalado no teu sistema. Não são necessárias bibliotecas externas, pois o script utiliza apenas ferramentas nativas do Python (`unicodedata`).
2. Clona este repositório para a tua máquina:
```bash
   git clone [https://github.com/icsousa/Minecraft-Enchantment-Translater.git](https://github.com/icsousa/Minecraft-Enchantment-Translater.git)
   ```
3. Navega até à pasta do projeto e executa o script:
```bash
   python main.py
   ```
   *(Nota: substitui `main.py` pelo nome exato do teu ficheiro Python, se for diferente).*
   
4. Escreve a frase pretendida no terminal.
   
5. Abre o ficheiro `traducao.txt` que foi gerado na mesma pasta para veres o resultado!

## ⚠️ Notas Importantes de Visualização

* O Alfabeto Galáctico (SGA) apenas suporta letras de **A a Z**. Números e sinais de pontuação (como `!`, `?`, `,`) não são convertidos e mantêm o seu formato original na tradução final.
* Se os caracteres aparecerem como **quadrados (□)** no Bloco de Notas (Notepad) do Windows, isso significa que a fonte padrão não suporta estes símbolos Unicode. Experimenta abrir o ficheiro `.txt` no **Visual Studio Code**, **Notepad++**, ou arrastar o ficheiro para o teu navegador web.

## 👨‍💻 Autor

Desenvolvido por **Ivo Costa Sousa**.
