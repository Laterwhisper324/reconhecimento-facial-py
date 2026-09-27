# Projeto de visão computacional

Coleção de experimentos independentes em Python com OpenCV, MediaPipe e Pygame. Os exemplos usam webcam e imagens locais para testar captura, desenho, detecção por cor, comparação de imagens e rastreamento de mãos.

## Rastreamento de mãos

O script `reconhecimento de objetos/reconhecimentoDeMãos.py` usa o MediaPipe Tasks (`HandLandmarker`) para rastrear até duas mãos pela webcam. Ele:

- espelha a imagem da webcam e desenha os 21 pontos e as conexões de cada mão;
- mostra se o indicador está levantado e em qual lado da linha vertical central está a mão;
- reconhece o gesto em que o dedo médio está levantado enquanto indicador, anelar e mínimo estão abaixados;
- ao detectar o início desse gesto, toca `fart.mp3` e sorteia uma imagem entre `middle_finger_dog.jpg`, `cat_middle_finger.jpg`, `skull_middle_finger.jpg` e `horse_middle_finger.jpg`;
- mostra a imagem sorteada ao lado do vídeo enquanto o gesto continuar. Para sortear e tocar novamente, abaixe o dedo médio e levante-o outra vez.

A detecção dos dedos usa comparações simples entre landmarks e funciona melhor com a mão aproximadamente ereta e voltada para a câmera. O polegar não faz parte da verificação de dedos abaixados na implementação atual.

Na primeira execução, o script baixa o arquivo `hand_landmarker.task` para a pasta `reconhecimento de objetos`; as próximas execuções reutilizam esse modelo local. É necessária conexão com a internet apenas para esse primeiro download.

### Dependências e execução

Instale as bibliotecas usadas pelo rastreador:

```powershell
python -m pip install mediapipe==1.0.1 opencv-python numpy pygame
```

Execute a partir da pasta que contém o áudio `fart.mp3`:

```powershell
Set-Location "reconhecimento de objetos"
python reconhecimentoDeMãos.py
```

Pressione `q` na janela do vídeo para encerrar.

## Outros exemplos

- `camera.py` — captura e exibe quadros da webcam. A função `capture()` está incompleta e não libera a câmera nem fecha a janela ao sair; o arquivo também não chama a função diretamente.
- `4-cameras-test.py` — cria uma visualização em quatro quadrantes usando uma webcam: conversão para LAB, imagem original e cópia girada em 180 graus. Apesar do nome, usa apenas uma câmera.
- `controles-de-imagens.py` — abre e mostra uma imagem de exemplo em `reconhecimento de objetos/ottq2x812v7b1.jpg`.
- `manipulação-de-formas.py` — permite desenhar formas e texto sobre a imagem da webcam.
- `reconhecimento-de-cores.py` — converte o vídeo para HSV, cria máscaras para vermelho e azul e exibe as regiões detectadas.
- `reconhecimento de objetos/reconhecimentoDeFrames.py` — compara um frame e um template usando métodos de template matching do OpenCV.

Os scripts são exemplos separados, não uma aplicação integrada. Os exemplos de webcam usam a câmera de índice `0`. O executável `dist/controles-de-imagens.exe` também está no repositório.
