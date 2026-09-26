# Projeto de visão computacional

Pequenos experimentos em Python com OpenCV. O projeto reúne exemplos de captura de webcam, manipulação de imagem e detecção simples por cor e por comparação de modelos.

## Versão atual

O repositório não define número de versão nem possui tags de release. O estado registrado no Git é a branch `reconhecimentoDeFrames.py`, commit `002e88d` (`remoção de arquivo`). Portanto, esta é uma versão experimental, sem release numerada.

## Arquivos de código

- `camera.py` — inicia uma captura da câmera e exibe os quadros. A função `capture()` está incompleta: não libera a câmera nem fecha a janela ao sair.
- `4-cameras-test.py` — captura uma webcam e monta uma visualização em quatro quadrantes: imagem convertida para LAB, imagem original e uma cópia girada em 180 graus. Apesar do nome, usa apenas uma câmera.
- `controles-de-imagens.py` — abre e mostra uma imagem de exemplo (`reconhecimento de objetos/ottq2x812v7b1.jpg`).
- `manipulação-de-formas.py` — permite escolher na webcam entre desenhar linhas, retângulo, círculo ou texto.
- `reconhecimento-de-cores.py` — converte o vídeo para HSV, cria máscaras para vermelho e azul e exibe as regiões detectadas.
- `reconhecimento de objetos/teste.py` — compara `cadeira2.png` com `mesa.jpg` usando vários métodos de template matching do OpenCV e marca a localização encontrada.

As imagens usadas pelo exemplo de comparação estão na pasta `reconhecimento de objetos`. Execute esse script com essa pasta como diretório de trabalho para que os caminhos relativos (`mesa.jpg` e `cadeira2.png`) sejam encontrados.

## Requisitos e execução

É necessário Python com `opencv-python` e `numpy` instalados, além de uma webcam para os exemplos de vídeo.

```powershell
python -m pip install opencv-python numpy
python reconcilement-de-cores.py
```

Para executar outro exemplo, substitua o nome do script. Para `reconhecimentoDeFrames.py`, entre primeiro na pasta de imagens:

```powershell
Set-Location "reconcilement de objetos"
python teste.py
```

Nas janelas de webcam, pressione `q` para sair. O arquivo `dist/controles-de-imagens.exe` é um executável já presente no projeto; não há informação no repositório sobre como foi empacotado ou sobre sua versão.

## Observações

Os scripts são exemplos independentes, não uma aplicação integrada. Os scripts de webcam assumem que a câmera de índice `0` está disponível. `camera.py` não contém chamada direta à função `capture()`, então executá-lo isoladamente não inicia a captura. O script de comparação de objetos imprime/localiza apenas o resultado do último método percorrido.
