# Assistente de Chat com GPT-3.5 Turbo em Python

<img src="https://imageio.forbes.com/specials-images/imageserve/63efba4dbbec49e8cbed2983/0x0.jpg?format=jpg&width=1200"/>

Este README oferece uma visão geral do código Python que utiliza o modelo GPT-3.5 Turbo da OpenAI para criar um assistente de chat. O código permite que você participe de uma conversa com o assistente, enviando mensagens e recebendo respostas. O assistente continuará a conversa e fornecerá informações relevantes.

## Pré-requisitos
Antes de usar este código, certifique-se de ter o seguinte:

- Uma chave de API da OpenAI: Substitua "Sua api" no código pela sua chave de API da OpenAI. Se você não tiver uma chave de API, poderá obtê-la se inscrevendo nos serviços da OpenAI.
## Início
Configure a sua chave de API da OpenAI:

- Substitua "Sua api" pela sua chave de API real na variável API_KEY.
### Execute o código:

- Execute o script Python em seu ambiente Python preferido.
### Interaja com o assistente:

- O código cria um loop onde você pode inserir mensagens para conversar com o assistente.
- Digite uma mensagem e pressione Enter para enviá-la ao assistente.
- Digite "sair" e pressione Enter para sair do loop de conversa.
- Como o Código Funciona
- Função enviar_msg
- A função enviar_msg é responsável por enviar mensagens ao modelo GPT-3.5 Turbo e receber respostas. Ela aceita dois argumentos:

- msg: A mensagem que você deseja enviar ao assistente.
- ista_msgs (opcional): Uma lista que armazena o histórico da conversa, incluindo mensagens do usuário e do assistente.
### Aqui está como ela funciona:

- Adiciona a mensagem do usuário ao histórico da conversa no formato de um dicionário com a função "user".
- Utiliza a API da OpenAI para gerar uma resposta com base no histórico da conversa.
- Extrai e retorna a resposta do assistente a partir da resposta recebida.
### Loop Principal
O código configura um loop que permite que você tenha uma conversa de ida e volta com o assistente. O loop faz o seguinte:

- Aceita a entrada do usuário como uma mensagem e a envia para a função enviar_msg.
- Se você digitar "sair", o loop é encerrado e a conversa termina.
- Caso contrário, a resposta do assistente é acrescentada ao histórico da conversa, e o loop continua.

## Observação
O modelo gpt-3.5-turbo é utilizado para conversas baseadas em chat.
Você pode estender e modificar este código para criar aplicativos mais complexos e interativos com o modelo GPT-3.5 Turbo da OpenAI.
