# Telegram Bot de Pesquisa Google

Este é um simples bot de Telegram que permite aos usuários pesquisar no Google diretamente da plataforma Telegram. O bot utiliza a biblioteca `googlesearch-python` para realizar as pesquisas no Google e a API do Telegram para interagir com os usuários.

## Pré-requisitos

Antes de começar a usar este bot, você precisará de algumas coisas:

1. **Token do Bot do Telegram**: Para interagir com a API do Telegram, você deve obter um token para o seu bot. Você pode criar um bot e obter um token seguindo as instruções na [Documentação do BotFather](https://core.telegram.org/bots#botfather).

2. **Python**: Certifique-se de ter o Python instalado em seu sistema. Você pode baixar o Python em [python.org](https://www.python.org/downloads/).

3. **Bibliotecas Python**: Este projeto utiliza duas bibliotecas externas que não fazem parte da biblioteca padrão do Python: `requests` e `googlesearch-python`. Você pode instalá-las usando o `pip`:

   ```bash
   pip install requests googlesearch-python
   ```

## Configuração

Após obter o token do bot, substitua a variável `TOKEN` no código pelo seu próprio token:

```python
TOKEN = 'SEU_TOKEN_AQUI'
```

## Uso

Para usar o bot, siga as etapas abaixo:

1. Execute o arquivo Python (`telegram_google_bot.py`) em seu ambiente Python.

2. Abra o Telegram e procure pelo nome de usuário do seu bot.

3. Inicie a conversa com o bot enviando o comando `/start`. Ele responderá com uma mensagem de boas-vindas.

4. Digite qualquer termo de pesquisa que você deseja no chat. O bot executará uma pesquisa no Google com o termo e enviará os resultados de volta para você.

5. Para desativar o bot, você pode enviar o comando `/stop`. O bot responderá e não processará mais pesquisas até que seja reativado com `/start`.

## Funcionalidades

O bot possui as seguintes funcionalidades:

- `/start`: Inicia a conversa com o bot e exibe uma mensagem de boas-vindas.

- `/stop`: Desativa o bot e interrompe o processamento de pesquisas até que seja reativado com `/start`.

- Pesquisa Google: Qualquer mensagem de texto enviada para o bot (exceto `/start` e `/stop`) será tratada como um termo de pesquisa. O bot realizará uma pesquisa no Google com o termo e enviará os resultados de volta para o usuário.

## Personalização

Você pode personalizar este bot adicionando funcionalidades adicionais, como armazenamento de histórico de pesquisa, formatação melhorada de resultados ou suporte a comandos personalizados.

## Observações

- Este bot tem como base um loop que busca atualizações do Telegram a cada 10 segundos. Portanto, é importante manter o programa em execução para que o bot funcione de maneira contínua.

- Tenha em mente que este é um exemplo simples de bot e pode ser estendido e aprimorado de várias maneiras, dependendo das suas necessidades.
