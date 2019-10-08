# Projeto final de EE881
## Modulação digital FSK
Até agora, nós vimos apenas modulações digitais em amplitude. Para o projeto nós vamos utilizar outra estratégia de modulação, onde a informação está contida na frequência da portadora. Para o modem acustico, essa estratégia é eficiente, pois como vimos em transmissões analógicas, modulações em frequência apresentam uma imunidade ao ruído muito superior a transmissões em amplitude. 
A modulação FSK (*frequency-shift keying*) consiste em uma modulação em banda passante onde a informação é enviada por meio de mudanças discretas na frequência de uma portadora. O modo mais simples de gerar esse tipo de modulação é "chavear" a frequência da portadora entre dois valores conforme o bit a ser transmitido é zero ou um. Essa portadora então é multiplicada pelo pulso de transmissão adotado e enviada. 
Esta modulação normalmente é adotada em transmissões na banda de RF, no entanto ela permite utilizarmos frequências baixas para a portadora com uma perda tolerável de eficiência. Essa capacidade faz com que seja possível uma transmissão digital por canais normalmente utilizados para transmitir voz (telefone, rádio-difusão, alto-falantes, etc) e fornece um protocolo versátil de comunicação onde não há possibilidade de se transmitir por ondas de rádio ou fibra óptica. 

## 