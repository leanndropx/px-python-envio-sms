# Este repositório contém: 



1. Uma aplicação web para envio de SMS desenvolvida em Python com Flask, Twilio, requests e Beautiful Soup. 
2. O usuário informa o código de rastreamento do objeto e o telefone que irá receber o SMS, em seguida a aplicação em Python automatiza o acesso a página de rastreamento dos correios, pesquisando as informações de status da encomenda e enviando o SMS para o telefone informado.




#  Este repositório tem como finalidade:



2. Mostrar um pouco dos meus conhecimentos em flask e hands-on com diferentes bibliotecas Python, neste caso, twilio, requests e Beautiful Soup que foram as bibliotecas utilizadas na aplicação.   
3. contribuir com a comunidade compartilhando conhecimento prático, e também me abrir para aprendizados e contribuições.
3. Servir como meu material de apoio para relembrar conceitos, sintaxes, bibliotecas e funções de todos os recursos que foram usados para construir este projeto.



# Neste repositório foram usadas as bibliotecas:



1. twilio - biblioteca que configura e aciona todo o envio de SMS - foram usados os módulos rest e Client
2. flask - com os módulos Flask, render_template e request 
3. requests
4. BS4 - módulo Beautiful Soup





# Para melhor explorá-lo, como principal sugestão, siga os passos abaixo:




1. Clone o repositório para o seu ambiente de desenvolvimento

2. Abra o terminal, caminhe até a pasta clonada do projeto. 

3. Na linha de comando, digite **pip3 install requests --users** para instalar a biblioteca Requests

4. Na linha de comando, digite **pip3 install flask --users** para instalar a biblioteca flask, que contém os módulos Flask, render_template e request que serão utilizados nesta aplicação.

5. Na linha de comando, digite **pip3 install twilio --users** para instalar a biblioteca twilio, que é responsável por estruturar todas as configurações para envio do SMS. 

6. Na linha de comando, digite **pip3 install bs4 --users** para instalar a biblioteca bs4, que contém o módulo Beautiful Soup que será usado nesta aplicação.

   

Após a instalação de todas as bibliotecas necessárias, vamos executar:



7. Na linha de comando, ainda dentro da pasta do projeto, digite **python3 main.py**

8. Pronto, o código será executado e.o framework flask iniciará um servidor local:

- Copie o endereço http do servidor que aparecerá em seu terminal
- Abra seu navegador e cole o endereço para acessar a aplicação. 
- No primeiro campo, insira o código de rastreamento do objeto que gostaria de verificar
- No segundo campo, insira o número de telefone que irá receber o SMS, seguindo as orientações de formato do número, como o exemplo 11991912222, sendo que os dois primeiros números (11) se refere ao código de área e o restante o número do telefone.
- Marque a opção "Aceito receber o status via SMS"
- Cique em "Solicitar Status"
- O SMS será enviado o número de telefone informado com o status da aplicação. Veja bem, caso o código de rastreamento informado seja inválido, a mensagem enviada será "Não existe código de rastreio para este objeto"



## **Como foram organizados os conteúdos** e por que:



O sistema é composto por 2 arquivos:

1. **main.py**: aqui está localizado o código principal, onde são importadas as bibliotecas utilizadas no programa - requests, flask, twilio e Beautiful Soup - e onde foram estruturadas as linhas de código para cada página HTML da aplicação.
2. **funcoes.py:** aqui estão localizadas as funções criadas para serem usadas no código principal (main.py). 
3. **templates (diretório)**: este diretório é requisito do modo de trabalho com o framework flask, dentro dele estão localizadas as páginas HTML que serão renderizadas na aplicação. Para este projeto, são duas:
   - Index.html: página inicial, abre assim que o endereço da aplicação é acessado. 
   - enviado.html: esta página é retornada quando o envio de SMS é concluído. 
