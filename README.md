# 1. Cifrario di Cesare
Si sostituisce ogni lettera con la lettera che si trova un certo numero di posizioni dopo nell'alfabeto.

- Il numero di posizioni è la chiave che consente di ricostruire la stringa originale.

- Un cifrario di Cesare ha per chiave un valore numerico.

Questo cifrario è facilmente attaccabile con un attacco bruteforce.

# 2. Cifrario di Vigenère
Si combina una chiave di lunghezza arbitraria con il testo in chiaro.

- Si somma la posizione della lettera del testo in chiaro a quella della chiave. Il risultato determina la posizione della lettera da riportare.