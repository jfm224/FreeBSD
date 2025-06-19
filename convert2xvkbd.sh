#!/bin/sh
# Converts hunspell .dic to xvkbd word list
# Identifique o arquivo com file -i pt_BR.dic
iconv -f ISO-8859-1 -t UTF-8 pt_BR.dic > pt_BR-utf8.txt
# limpezinha no dicionario
cat pt_BR-utf8.txt |cut -f 1 -d '/' > pt_BR-clean.txt
# organiza por comprimento da palavra
awk '{ print length, $0 }' pt_BR-clean.txt | sort -n | cut -d' ' -f2- > xvkbd.words 
# Tudo certo? Vamos ver:
wc -l xvkbd.words
# Contar o número de linhas no arquivo sorted_words.txt
line_count=$(wc -l < xvkbd.words)

# Verificar se o número de linhas é diferente de 0
if [ "$line_count" -ne 0 ]; then
    # Salvar o conteúdo em ~/.xvkbd.words
    cp xvkbd.words ~/.xvkbd.words
    echo "Palavras salvas em ~/.xvkbd.words"
else
    echo "O arquivo xvkbd.words está vazio."
fi
